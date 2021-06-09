# -*- coding: utf-8 -*-

"""
Module et_micc2.project
=======================

An OO interface to *micc* projects.

"""
import os, sys, site, subprocess
import sysconfig
import shutil
import json
from pathlib import Path
from operator import xor
import requests
from types import SimpleNamespace
from importlib import import_module

import click
import semantic_version

import et_micc2.config
import et_micc2.utils
import et_micc2.expand
import et_micc2.logger
import pkg_resources


__FILE__ = Path(__file__).resolve()


def micc_version():
    return et_micc2.__version__


def on_vsc_cluster():
    """test if we are running on one of the VSC clusters"""
    try:
        os.environ['VSC_HOME']
        os.environ['VSC_INSTITUTE_CLUSTER']
    except:
        return False
    else:
        return True


def is_os_tool(path_to_exe):
    """test if path_to_exe was installed as part of the OS."""
    return path_to_exe.startswith('/usr/bin')

class PkgInfo:
    mock = [] # list of module names to pretend missing. This is just for testing purposes.

    def __init__(self, pkg_name):
        if pkg_name in PkgInfo.mock:
            print(f'Mock: pretending module `{pkg_name}` is missing.')
            self.which = ''
        else:
            try:
                self.pkg_dist_info = pkg_resources.get_distribution(pkg_name)
            except pkg_resources.DistributionNotFound:
                self.which = ''
            else:
                self.which = self.pkg_dist_info.location

    def is_available(self):
        """Return True if the tool is available, False otherwise."""
        return bool(self.which)

    def version(self):
        """Return the version string of the tool, or an empty string if the tool is not available."""
        return self.pkg_dist_info.version if self.which else ''


__pybind11_required_version__ = '2.6.2'


class ToolInfo:
    mock = [] # list of executable names to pretend missing. This is just fortesting purposes.

    def __init__(self, exe, accept_cluster_os_tools=False):
        """Check if tool 'exe' is available.

        :param str exe: name of an executable
        :param bool accept_cluster_os_tools: accept cluster operating system tools


        :return: SimpleNamespace(which,version), where which is the location of the tool or an empty
            string if it is not found or not accepted, and version is the version string (if requested)
            as returned be 'exe --version'.
        """
        self.exe = exe
        if exe in ToolInfo.mock:
            print(f'Mock: pretending tool `{exe}` is missing.')
            self.which = ''
        else:
            # completed_which = subprocess.run(['which', exe], capture_output=True, text=True)
            # self.which = completed_which.stdout.strip().replace('\n', ' ')
            self.which = shutil.which(exe)

        if self.which:
            if on_vsc_cluster() and not accept_cluster_os_tools and is_os_tool(self.which):
                self.which = ''

    def is_available(self):
        """Return True if the tool is available, False otherwise."""
        return bool(self.which)

    def version(self):
        """Return the version string of the tool, or an empty string if the tool is not available."""
        if self.which:
            completed_version = subprocess.run([self.exe, '--version'], capture_output=True, text=True)
            self.version = completed_version.stdout.strip().replace('\n\n','\n')#.replace('\n','\n        ')
        else:
            self.version = ''
        return self.version

_exit_missing_component = -1

class Project:
    """
    An OO interface to *micc* projects.

    :param types.SimpleNameSpace options: all options from the ``micc`` CLI.
    """

    def __init__(self, options):
        self.exit_code = 0
        self.logger = None
        self.options = options
        project_path = options.project_path

        if hasattr(options, 'template_parameters'):
            # only needed for expanding templates.
            # Pick up the default parameters
            parameters = self.options.preferences
            parameters.update(options.template_parameters)
            options.template_parameters = parameters

        if et_micc2.utils.is_project_directory(project_path, self):
            # If the project already exists, we can get ourselves a logger;
            self.get_logger()
        else:
            # Not a project directory, only create and setup subcommands can work,
            # (but setup does not construct a Project object)
            if not self.options.invoked_subcommand in ('create',):
                self.error(f'Not a project directory: `{project_path}`')


    def ask_user_to_continue_or_not(self, default=False, stop_message='Exiting.'):
        """Ask the user if he wants to continue or stop a command.

        If the answer is to stop, sets self.exit_code to -1, and prints the stop_message.

        :param bool default: The answer if the user just presses enter.
        :return: True if the user wants to stop, False otherwise.
        """
        if default == True:
            question = 'Continue? [Yes]/No'
        else:
            question = 'Continue? [No]/Yes'
        answer = input(question)

        if not answer:
            answer = default
        else:
            answer = answer.lower()
            answer = True if answer.startswith('y') else False

        if not answer:
            self.error(stop_message, exit_code=_exit_missing_component)


    @property
    def project_path(self):
        return self.options.project_path

    def error(self, msg, exit_code=1, raise_runtimeerror=True):
        """Print an error message,  set this project's exit_code, and optionally raise a
        RuntimeError.
        
        :param str msg: the error message
        :param int exit_code: the exit_code to set
        :param bool raise_runtimeerror: raise RuntimeError if True
        """
        click.secho("[ERROR]\n" + msg, fg='bright_red') 
        self.exit_code = exit_code
        if raise_runtimeerror:
            raise RuntimeError


    def warning(self, msg):
        """Print an warning message :py:obj:`msg` and set the project's :py:obj:`exit_code`."""
        click.secho("[WARNING]\n" + msg, fg='green')


    def create_cmd(self):
        """Create a new project skeleton."""

        # Check for tools needed:
        # . git is required for creating a local repo
        # . gh is required for creating a remote repo
        
        if self.options.project_path.exists() and os.listdir(str(self.options.project_path)):
            self.error(f"Cannot create project in ({self.options.project_path}):\n"
                       f"  Directory must be empty.")

        if not self.options.no_git and not ToolInfo('git').is_available():
            if on_vsc_cluster():
                self.warning('Your current environment has no suitable git command.\n'
                             'Load a cluster module that has git.\n'
                             'If you continue, this project will NOT have a local git repository.'
                            )
            else:
                self.warning('Your current environment has no git command.\n'
                             'To install git: https://git-scm.com/downloads.\n'
                             'If you continue, this project will NOT have a local git repository.'
                            )

            self.ask_user_to_continue_or_not(stop_message='Project not created.')

        if self.options.remote != 'none':
            # Check that we have github username
            github_username = self.options.template_parameters['github_username']
            if not github_username:
                self.error('Micc2 configuration does not have a github username. Creation of remote repo is not possible.\n'
                           'Project is not created.'
                          )
            # Check availability of gh command:
            if not ToolInfo('gh').is_available() and self.options.remote:
                self.warning('The gh command is not available in your environment.\n'
                             'If you continue this project a remote repository will not be created.'
                            )
                self.ask_user_to_continue_or_not(stop_message='Project not created.')


        if not self.options.allow_nesting:
            # Prevent the creation of a project inside another project
            p = self.project_path.parent.resolve()
            while not p.samefile('/'):
                if et_micc2.utils.is_project_directory(p):
                    self.error(f"Cannot create project in ({self.project_path}):\n"
                               f"  Specify '--allow-nesting' to create a et_micc2 project inside another et_micc2 project ({p})."
                               )
                p = p.parent

        # Proceed creating the project
        self.project_path.mkdir(parents=True, exist_ok=True)

        project_name = self.project_path.name
        self.project_name = project_name
        if not self.options.module_name:
            if not et_micc2.utils.verify_project_name(project_name):
                self.error(f"The project name ({project_name}) does not yield a PEP8 compliant module name:\n"
                           f"  The project name must start with char, and contain only chars, digits, hyphens and underscores.\n"
                           f"  Alternatively, provide an explicit module name with the --module-name=<name>."
                           )
            else:
                self.package_name = et_micc2.utils.pep8_module_name(project_name)
        else:
            self.package_name = self.options.module_name

        try:
            relative_project_path = self.project_path.relative_to(Path.cwd())
        except ValueError:
            # project_path was specified relative to cwd using ../
            # use full path instead of relative path
            relative_project_path = self.project_path

        if self.options.publish:
            rv = et_micc2.utils.existsOnPyPI(self.package_name)
            if rv is False:
                pass # the name is not yet in use
            else:
                if rv is True:
                    self.error(
                        f"    The name '{self.package_name}' is already in use on PyPI.\n"
                        f"    The project is not created.\n"
                        f"    You must choose another name if you want to publish your code on PyPI."
                    )
                elif isinstance(rv, requests.exceptions.ConnectionError):
                    self.error(f"    ConnectionError: Check your internect connection.\n"
                               f"    The availability of name '{self.package_name}' on PyPI could not be verified. \n"
                               f"    The project is not created."
                    )
                else: # unknown error
                    self.error(f"    {type(rv)}\n"
                               f"    {str(rv)}\n"
                               f"    The availability of name '{self.package_name}' on PyPI could not be verified. \n"
                               f"    The project is not created."
                               )

        structure, source_file = ('package', f'({relative_project_path}{os.sep}{self.package_name}{os.sep}__init__.py)') \
                                 if self.options.package_structure else \
                                 ('module' , f'({relative_project_path}{os.sep}{self.package_name}.py)')

        self.options.verbosity = max(1, self.options.verbosity)

        # The project directory is created, so we can get ourselves a logger:
        self.get_logger()

        with et_micc2.logger.logtime(self):
            with et_micc2.logger.log(self.logger.info
                                    , f"Creating project directory ({self.project_name}):"
                                    ):
                self.logger.info(f"Python {structure} ({self.package_name}): structure = {source_file}")
                
                # project_name must come before github_repo because the value of github_repo depends on project_name
                template_parameters = et_micc2.config.Config( project_name=self.project_name
                                                               , package_name=self.package_name )
                template_parameters.update(self.options.template_parameters.data)
                self.options.template_parameters = template_parameters
                
                self.options.overwrite = False
                self.exit_code = et_micc2.expand.expand_templates(self.options)
                if self.exit_code:
                    self.logger.critical(f"Exiting ({self.exit_code}) ...")
                    return

                proj_cfg = self.project_path / 'micc2.cfg'
                self.options.template_parameters.save(proj_cfg)

                # add git support if requested
                if self.options.no_git:
                    self.logger.warning(f"Flag `--no-git` specified: project `{project_name}` created without git support.")
                else:
                    with et_micc2.logger.log(self.logger.info, "Creating local git repository"):
                        with et_micc2.utils.in_directory(self.project_path):
                            cmds = [ ['git', 'init', f'--initial-branch={self.options.template_parameters["git_default_branch"]}']
                                   , ['git', 'add', '*']
                                   , ['git', 'add', '.gitignore']
                                   , ['git', 'commit', '-m', '"And so this begun..."']
                                   ]
                            returncode = et_micc2.utils.execute(cmds, self.logger.debug, stop_on_error=True)
                    if not returncode:
                        if self.options.remote:
                            # todo this context manager does not print correctly
                            with et_micc2.logger.log(self.logger.info, f"Creating remote git repository at https://github.com/{github_username}/{self.project_name}"):
                                with et_micc2.utils.in_directory(self.project_path):
                                    pat_file = self.options._cfg_dir / f'{self.options.template_parameters["github_username"]}.pat'
                                    if pat_file.exists():
                                        with open(pat_file) as f:
                                            completed_process = \
                                                subprocess.run( ['gh', 'auth', 'login', '--with-token'], stdin=f, text=True )
                                            et_micc2.utils.log_completed_process(completed_process,self.logger.debug)

                                            cmds = [ ['gh', 'repo', 'create', self.project_name, f'--{self.options.remote}', '-y']
                                                   , ['git', 'push', '-u', 'origin', self.options.template_parameters['git_default_branch']]
                                                   ]
                                            et_micc2.utils.execute(cmds, self.logger.debug, stop_on_error=True)
                                    else:
                                        self.logger.error(f"Unable to access your GitHub account: \n"
                                                          f"    File not found: '{pat_file}'.\n"
                                                          f"Remote repository not created."
                                                         )
                        else:
                            self.logger.warning("Creation of remote GitHub repository not requested.")

                # self.logger.warning(
                #     "Run 'poetry install' in the project directory to create a virtual "
                #     "environment and install its dependencies."
                # )

        if self.options.publish:
            self.logger.info(f"The name '{self.package_name}' is still available on PyPI.")
            self.logger.warning("To claim the name, it is best to publish your project right away\n"
                                "by running 'poetry publish --build'."
            )


    @property
    def version(self):
        """Return the project's version (str)."""
        return self.pyproject_toml['tool']['poetry']['version']


    def require_project_created(self):
        """Raise a runtime error if this project does not have a project directory."""
        if self.logger is None:
            self.error(f'Not a project directory: {self.options.project_path}')


    def module_to_package_cmd(self):
        """Convert a module project (:file:`module.py`) to a package project (:file:`package/__init__.py`)."""
        self.require_project_created()

        # This command does not require any external tools.

        if self.structure == 'package':
            self.warning(f"Project ({self.project_name}) is already a package ({self.package}).")
            return

        self.logger.info(
            f"Converting Python module project {self.project_name} to Python package project."
        )

        # add documentation files for general Python project
        self.options.templates = "package-general-docs"
        self.options.template_parameters = self.options.preferences
        self.options.template_parameters.update(
            {'project_short_description': self.pyproject_toml['tool']['poetry']['description']}
        )
        self.exit_code = et_micc2.expand.expand_templates(self.options)
        if self.exit_code:
            self.logger.critical(
                f"Expand failed during Project.module_to_package_cmd for project ({self.project_name})."
            )
            return

        # move <package_name>.py to <package_name>/__init__.py
        package_path = self.project_path / self.package_name
        package_path.mkdir(exist_ok=True)
        src = self.project_path / (self.package_name + '.py')
        dst = self.project_path / self.package_name / '__init__.py'
        shutil.move(src, dst)


    def info_cmd(self):
        """Output info on the project."""
        self.require_project_created()

        # This command does not require any external tools.

        if self.options.verbosity >= 0:
            self.options.verbosity = 10

        if self.options.verbosity >= 1:
            click.echo("Project " + click.style(str(self.project_name), fg='green')
                       + " located at "
                       + click.style(str(self.project_path), fg='green')
                       + "\n  package: " + click.style(str(self.package_name), fg='green')
                       + "\n  version: " + click.style(self.version, fg='green')
                       )

        if self.options.verbosity >= 2:
            click.echo("  structure: " + click.style(self.src_file, fg='green') + f' (Python {self.structure})')

        if self.options.verbosity >= 3 and self.structure == 'package':
            package_path = self.project_path / self.package_name
            files = []
            files.extend(package_path.glob('**/*.py'))
            files.extend(package_path.glob('**/cpp_*/'))
            files.extend(package_path.glob('**/f90_*'))
            if len(files) > 1:  # __init__.py is always there.
                click.echo("  contents:")
                for f in files:
                    # filters
                    sf = str(f)
                    if '_cmake_build' in sf \
                    or '{' in str(f) \
                    or 'package-' in sf \
                    or 'build_' in sf:
                        continue
                    if f.name == "__init__.py" and f.parent.samefile(package_path):  # ignore the top-level __init__.py
                        continue

                    fg = 'green'
                    extra = ''
                    if f.name.startswith('cli'):
                        kind = "application "
                        fg = 'blue'
                    elif f.name.startswith('cpp_'):
                        kind = "C++ module  "
                        extra = f"{os.sep}{f.name.split('_', 1)[1]}.cpp"
                    elif f.name.startswith('f90_'):
                        kind = "f90 module "
                        extra = f"{os.sep}{f.name.split('_', 1)[1]}.f90"
                    elif f.name == '__init__.py':
                        kind = "package     "
                    else:
                        kind = "module      "
                    click.echo("    " + kind + click.style(str(f.relative_to(package_path)) + extra, fg=fg))


    def version_cmd(self):
        """Bump the version according to :py:obj:`self.options.rule` or show the
        current version if no rule is specified.

        The version is stored in pyproject.toml in the project directory, and in
        :py:obj:`__version__` variable of the top-level package, which is either
        in :file:`<package_name>.py`, :file:`<package_name>/__init__.py`, or in
        :file:`<package_name>/__version__.py`.
        """
        self.require_project_created()

        # This command does not require any external tools.

        self.options.verbosity = max(1, self.options.verbosity)

        if not self.options.rule:
            if self.options.short:
                print(self.version)
            else:
                click.echo("Project " + click.style(f"({self.project_name}) ", fg='green')
                           + "version " + click.style(f"({self.version}) ", fg='green')
                           )
        else:
            r = f"--{self.options.rule}"
            current_semver = semantic_version.Version(self.version)
            if self.options.rule == 'patch':
                new_semver = current_semver.next_patch()
            elif self.options.rule == 'minor':
                new_semver = current_semver.next_minor()
            elif self.options.rule == 'major':
                new_semver = current_semver.next_major()
            else:
                r = f"--rule {self.options.rule}"
                new_semver = semantic_version.Version(self.options.rule)

            # update pyproject.toml
            if not self.options.dry_run:
                self.pyproject_toml['tool']['poetry']['version'] = str(new_semver)
                self.pyproject_toml.save()
                # update __version__
                look_for = f'__version__ = "{current_semver}"'
                replace_with = f'__version__ = "{new_semver}"'
                if self.structure == 'module':
                    # update in <package_name>.py
                    et_micc2.utils.replace_in_file(self.project_path / self.src_file, look_for, replace_with)
                else:
                    # update in <package_name>/__init__.py
                    p = self.project_path / self.package_name / "__version__.py"
                    if p.exists():
                        et_micc2.utils.replace_in_file(p, look_for, replace_with)
                    else:
                        p = self.project_path / self.package_name / '__init__.py'
                        et_micc2.utils.replace_in_file(p, look_for, replace_with)

                self.logger.info(f"({self.project_name})> version ({current_semver}) -> ({new_semver})")
            else:
                click.echo(f"({self.project_name})> micc version {r} --dry-run : "
                           + click.style(f"({current_semver} ", fg='cyan') + "-> "
                           + click.style(f"({new_semver})", fg='cyan')
                           )

    def tag_cmd(self):
        """Create and push a version tag ``v<Major>.<minor>.<patch>`` for the current version."""
        self.require_project_created()

        # Git is required

        git = ToolInfo('git')
        if not git.is_available():
            s = '(or not suitable) ' if on_vsc_cluster() else ''
            self.error(f'The tag command requires git, which is not available {s}in your environment.\n'
                        'Exiting.')

        tag = f"v{self.version}"

        with et_micc2.utils.in_directory(self.project_path):
            self.logger.info(f"Creating git tag {tag} for project {self.project_name}")
            cmd = ['git', 'tag', '-a', tag, '-m', f'"tag version {self.version}"']
            self.logger.debug(f"Running '{' '.join(cmd)}'")
            completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            self.logger.debug(completed_process.stdout.decode('utf-8'))
            if completed_process.stderr:
                self.logger.critical(completed_process.stderr.decode('utf-8'))

            self.logger.debug(f"Pushing tag {tag} for project {self.project_name}")
            cmd = ['git', 'push', 'origin', tag]
            self.logger.debug(f"Running '{' '.join(cmd)}'")
            completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if completed_process.returncode == 0:
                if completed_process.stdout:
                    self.logger.debug(completed_process.stdout.decode('utf-8'))
            else:
                if completed_process.stdout:
                    self.logger.warning(completed_process.stdout.decode('utf-8'))
                if completed_process.stderr:
                    self.logger.warning(completed_process.stderr.decode('utf-8'))
                self.logger.warning(f"Failed '{' '.join(cmd)}'\nRerun the command later (you must be online).")

        self.logger.info('Done.')


    def add_cmd(self):
        """Add some source file to the project.

        This method dispatches to

        * :py:meth:`add_python_cli`,
        * :py:meth:`add_python_module`,
        * :py:meth:`add_f90_module`,
        * :py:meth:`add_cpp_module`
        """
        self.require_project_created()

        if self.structure == 'module':
            self.error(f"Cannot add to a module project ({self.project_name}).\n"
                       f"  Run `micc2 convert-to-package` on this project to convert it to a package project."
                       )

        # set implied flags:
        if self.options.clisub:
            app_implied = f" [implied by --clisub   ({int(self.options.clisub)})]"
            self.options.cli = True
        else:
            app_implied = ""

        if self.options.package:
            py_implied = f" [implied by --package ({int(self.options.package)})]"
            self.options.py = True
        else:
            py_implied = ""

        # Verify that one and only one of app/py/f90/cpp flags has been selected:
        if (not (self.options.cli or self.options.py or self.options.f90 or self.options.cpp)
                or not xor(xor(self.options.cli, self.options.py), xor(self.options.f90, self.options.cpp))):
            # Do not log, as the state of the project is not changed.
            self.error(f"Specify one and only one of \n"
                       f"  --cli ({int(self.options.cli)}){app_implied}\n"
                       f"  --py  ({int(self.options.py )}){py_implied}\n"
                       f"  --f90 ({int(self.options.f90)})\n"
                       f"  --cpp ({int(self.options.cpp)})\n"
                       )

        db_entry = {'options': self.options}

        if self.options.cli:
            # Prepare for adding an app
            app_name = self.options.add_name
            if self.app_exists(app_name):
                self.error(f"Project {self.project_name} has already an app named {app_name}.")

            if not et_micc2.utils.verify_project_name(app_name):
                self.error(f"Not a valid app name ({app_name}_. Valid names:\n"
                           f"  * start with a letter [a-zA-Z]\n"
                           f"  * contain only [a-zA-Z], digits, hyphens, and underscores\n"
                          )

            if self.options.clisub:
                if not self.options.templates:
                    self.options.templates = 'app-sub-commands'
            else:
                if not self.options.templates:
                    self.options.templates = 'app-simple'

            self.add_python_cli(db_entry)

        else:
            # Prepare for adding a sub-module
            module_name = self.options.add_name

            # Verify that the name is not already used:
            if self.module_exists(module_name):
                self.error(f"Project {self.project_name} has already a module named {module_name}.")

            # Verify that the name is valid:
            if (not et_micc2.utils.verify_project_name(module_name)
                    or module_name != et_micc2.utils.pep8_module_name(module_name)):
                self.error(f"Not a valid module name ({module_name}). Valid names:\n"
                           f"  * start with a letter [a-zA-Z]\n"
                           f"  * contain only [a-zA-Z], digits, and underscores\n"
                          )

            if self.options.py:
                # prepare for adding a Python sub-module:
                # self.options.structure = 'package' if self.options.package else 'module'
                if not self.options.templates:
                    self.options.templates = 'module-py'
                self.add_python_module(db_entry)

            else: # add a binary extension module
                # Warn if cmake is not available
                if not ToolInfo('cmake').is_available():
                    self.warning('Building binary extensions requires cmake, which is currently not available in your environment.')

                if self.options.f90:
                    # Warn if f2py is not available
                    if not ToolInfo('f2py').is_available():
                        msg = 'Building Fortran binary extensions requires f2py, which is currently not available in your environment.\n'
                        if on_vsc_cluster():
                            msg += 'To enable f2py:\n'\
                                   '    load a cluster module that has numpy pre-installed.\n'
                        else:
                            msg += 'To enable f2py, install numpy:\n' \
                                   '    If you are using a virtual environment:\n' \
                                   '            (.venv) > pip install numpy\n' \
                                   '    otherwise:\n' \
                                   '            > pip install numpy --user\n'
                        msg += '(You also need a Fortran compiler and a C compiler).'
                        self.warning(msg)

                    # prepare for adding a Fortran sub-module:
                    if not self.options.templates:
                        self.options.templates = 'module-f90'
                    self.add_f90_module(db_entry)

                if self.options.cpp:
                    # Warn if pybind11 is not available or too old
                    pybind11 = PkgInfo('pybind11')
                    if not pybind11.is_available():
                        self.warning('Building C++ binary extensions requires pybind11, which is not available in your environment.\n'
                                     'If you are using a virtual environment, install it as .\n'
                                     '    (.venv) > pip install pybind11\n'
                                     'otherwise,\n'
                                     '    > pip install pybind11 --user\n'
                                     '(You also need a C++ compiler).'
                                     )
                    else:
                        if pybind11.version() < __pybind11_required_version__:
                            self.warning(f'Building C++ binary extensions requires pybind11, which is available in your environment (v{pybind11.version()}).\n'
                                         f'However, you may experience problems because it is older than v{__pybind11_required_version__}.\n'
                                          'Upgrading is recommended.'
                                         )
                    # prepare for adding a C++ sub-module:
                    if not self.options.templates:
                        self.options.templates = 'module-cpp'
                    self.add_cpp_module(db_entry)

        self.deserialize_db()
        self.serialize_db(db_entry)

    
    def add_python_cli(self, db_entry):
        """Add a console script (app, aka CLI) to the package."""
        project_path = self.project_path
        app_name = self.options.add_name
        cli_app_name = 'cli_' + et_micc2.utils.pep8_module_name(app_name)
        w = 'with' if self.options.clisub else 'without'

        with et_micc2.logger.log(self.logger.info,
                                f"Adding CLI {app_name} {w} sub-commands to project {project_path.name}."):
            self.options.template_parameters.update(
                {'app_name': app_name, 'cli_app_name': cli_app_name}
            )

            self.exit_code = et_micc2.expand.expand_templates(self.options)
            if self.exit_code:
                self.logger.critical(
                    f"Expand failed during Project.add_python_cli for project ({self.project_name})."
                )
                return

            package_name = self.options.template_parameters['package_name']
            src_file = os.path.join(project_path.name, package_name, f"cli_{app_name}.py")
            tst_file = os.path.join(project_path.name, 'tests', f"test_cli_{app_name}.py")
            self.logger.info(f"- Python source file {src_file}.")
            self.logger.info(f"- Python test code   {tst_file}.")

            with et_micc2.utils.in_directory(project_path):
                # docs
                # Look if this package has already an 'apps' entry in docs/index.rst
                with open('docs/index.rst', "r") as f:
                    lines = f.readlines()
                has_already_apps = False
                api_line = -1
                for l, line in enumerate(lines):
                    has_already_apps = has_already_apps or line.startswith("   apps")
                    if line.startswith('   api'):
                        api_line = l

                # if not, create it:
                if not has_already_apps:
                    lines.insert(api_line, '   apps\n')
                    with open('docs/index.rst', "w") as f:
                        for line in lines:
                            f.write(line)
                # Create 'APPS.rst' if it does not exist:
                txt = ''
                if not Path('APPS.rst').exists():
                    # create a title
                    title = "Command Line Interfaces (apps)"
                    line = len(title) * '*' + '\n'
                    txt += (line
                            + title + '\n'
                            + line
                            + '\n'
                            )
                # create entry for this apps documentation
                txt2 = (f".. click:: {package_name}.{cli_app_name}:main\n"
                        f"   :prog: {app_name}\n"
                        f"   :show-nested:\n\n"
                        )
                file = 'APPS.rst'
                with open(file, "a") as f:
                    f.write(txt + txt2)
                db_entry[file] = txt2

                # pyproject.toml
                self.add_dependencies({'click': '^7.0.0'})
                self.pyproject_toml['tool']['poetry']['scripts'][app_name] = f"{package_name}:{cli_app_name}.main"
                self.pyproject_toml.save()
                db_entry['pyproject.toml'] = f'{app_name} = "refactoring_dev:cli_{app_name}.main"\n'

                # add 'import <package_name>.cli_<app_name> to __init__.py
                line = f"import {package_name}.cli_{app_name}\n"
                file = project_path / self.package_name / '__init__.py'
                et_micc2.utils.insert_in_file(file, [line], before=True, startswith="__version__")
                db_entry[os.path.join(self.package_name, '__init__.py')] = line

    def add_python_module(self, db_entry):
        """Add a python sub-module or sub-package to this project."""
        project_path = self.project_path
        module_name = self.options.add_name

        if not module_name == et_micc2.utils.pep8_module_name(module_name):
            self.error(f"Not a valid module_name: {module_name}")

        source_file = f"{module_name}{os.sep}__init__.py" if self.options.package else f"{module_name}.py"
        with et_micc2.logger.log(self.logger.info,
                                f"Adding python module {source_file} to project {project_path.name}."
                                ):
            self.options.template_parameters.update({'module_name': module_name})

            # Create the needed folders and files by expanding the templates:
            self.exit_code = et_micc2.expand.expand_templates(self.options)
            if self.exit_code:
                self.logger.critical(
                    f"Expand failed during Project.add_python_module for project ({self.project_name})."
                )
                return

            package_name = self.options.template_parameters['package_name']
            if self.options.package:
                self.module_to_package(project_path / package_name / (module_name + '.py'))

            src_file = os.path.join(project_path.name, package_name, source_file)
            tst_file = os.path.join(project_path.name, 'tests', 'test_' + module_name + '.py')

            self.logger.info(f"- python source in    {src_file}.")
            self.logger.info(f"- Python test code in {tst_file}.")

            with et_micc2.utils.in_directory(project_path):
                # docs
                filename = "API.rst"
                text = f"\n.. automodule:: {package_name}.{module_name}" \
                        "\n   :members:\n\n"
                with open(filename, "a") as f:
                    f.write(text)
                db_entry[filename] = text

            self.add_import_code(db_entry)

    def add_import_code(self, db_entry):
        """Add import statement for this python s in :file:`__init__.py` of the package."""
        module_name = self.options.add_name
        text_to_insert = [ ""
                         , f"import {self.package_name}.{module_name}"
                         ]
        file = os.path.join(self.package_name, '__init__.py')
        et_micc2.utils.insert_in_file(
            self.project_path / file,
            text_to_insert,
            startswith="__version__ = ",
        )
        text = '\n'.join(text_to_insert)
        db_entry[file] = text

    def add_f90_module(self, db_entry):
        """Add a f90 module to this project."""
        project_path = self.project_path
        module_name = self.options.add_name

        with et_micc2.logger.log(self.logger.info,
                                f"Adding f90 module {module_name} to project {project_path.name}."
                                ):
            self.options.template_parameters.update({'module_name': module_name})

            self.exit_code = et_micc2.expand.expand_templates(self.options)
            if self.exit_code:
                self.logger.critical(
                    f"Expand failed during Project.add_f90_module for project ({self.project_name})."
                )

            package_name = self.options.template_parameters['package_name']
            src_file = os.path.join(project_path.name
                                    , package_name
                                    , 'f90_' + module_name
                                    , module_name + '.f90'
                                    )
            cmk_file = os.path.join(project_path.name
                                    , package_name
                                    , 'f90_' + module_name
                                    , 'CMakeLists.txt'
                                    )
            tst_file = os.path.join(project_path.name
                                    , 'tests'
                                    , 'test_f90_' + module_name + '.py'
                                    )

            rst_file = os.path.join(project_path.name
                                    , package_name
                                    , 'f90_' + module_name
                                    , module_name + '.rst'
                                    )
            self.logger.info(f"- Fortran source in       {src_file}.")
            self.logger.info(f"- build settings in       {cmk_file}.")
            self.logger.info(f"- Python test code in     {tst_file}.")
            self.logger.info(f"- module documentation in {rst_file} (restructuredText format).")

            with et_micc2.utils.in_directory(project_path):
                # docs
                filename = "API.rst"
                text = f"\n.. include:: ../{package_name}/f90_{module_name}/{module_name}.rst\n"
                with open(filename, "a") as f:
                    f.write(text)
                db_entry[filename] = text

        self.add_auto_build_code(db_entry)

    def add_auto_build_code(self, db_entry):
        """Add auto build code for binary extension modules in :file:`__init__.py` of the package."""
        module_name = self.options.add_name
        text_to_insert = [
            "",
            "try:",
            f"    import {self.package_name}.{module_name}",
            "except ModuleNotFoundError as e:",
            "    # Try to build this binary extension:",
            "    from pathlib import Path",
            "    import click",
            "    from et_micc2.project import auto_build_binary_extension",
            f"    msg = auto_build_binary_extension(Path(__file__).parent, '{module_name}')",
            "    if not msg:",
            f"        import {self.package_name}.{module_name}",
            "    else:",
            f"        click.secho(msg, fg='bright_red')",
        ]
        file = os.path.join(self.package_name, '__init__.py')
        et_micc2.utils.insert_in_file(
            self.project_path / file,
            text_to_insert,
            startswith="__version__ = ",
        )
        text = '\n'.join(text_to_insert)
        db_entry[file] = text

    def add_cpp_module(self, db_entry):
        """Add a cpp module to this project."""
        project_path = self.project_path
        module_name = self.options.add_name

        with et_micc2.logger.log(self.logger.info,
                                f"Adding cpp module cpp_{module_name} to project {project_path.name}."
                                ):
            self.options.template_parameters.update({'module_name': module_name})

            self.exit_code = et_micc2.expand.expand_templates(self.options)
            if self.exit_code:
                self.logger.critical(
                    f"Expand failed during Project.add_cpp_module for project ({self.project_name})."
                )
                return

            package_name = self.options.template_parameters['package_name']
            src_file = os.path.join(project_path.name
                                    , package_name
                                    , 'cpp_' + module_name
                                    , module_name + '.cpp'
                                    )
            cmk_file = os.path.join(project_path.name
                                    , package_name
                                    , 'cpp_' + module_name
                                    , 'CMakeLists.txt'
                                    )
            tst_file = os.path.join(project_path.name
                                    , 'tests'
                                    , 'test_cpp_' + module_name + '.py'
                                    )

            rst_file = os.path.join(project_path.name
                                    , package_name
                                    , 'cpp_' + module_name
                                    , module_name + '.rst'
                                    )
            self.logger.info(f"- C++ source in           {src_file}.")
            self.logger.info(f"- build settings in       {cmk_file}.")
            self.logger.info(f"- Python test code in     {tst_file}.")
            self.logger.info(f"- module documentation in {rst_file} (restructuredText format).")

            with et_micc2.utils.in_directory(project_path):
                # docs
                with open("API.rst", "a") as f:
                    filename = "API.rst"
                    text = f"\n.. include:: ../{package_name}/cpp_{module_name}/{module_name}.rst\n"
                    with open(filename, "a") as f:
                        f.write(text)
                    db_entry[filename] = text

        self.add_auto_build_code(db_entry)


    def build_cmd(self):
        """Build a binary extension."""
        self.require_project_created()

        # Exit if cmake is not available:
        if not ToolInfo('cmake').is_available():
            msg = 'The build command requires cmake, which is not available in your current environment.\n'
            if on_vsc_cluster():
                msg += 'Load a cluster module that enables cmake.'
            else:
                msg += 'Make sure cmake is installed and on your PATH.'
            self.error(msg)

        project_path = self.options.project_path
        if getattr(self, 'module', False):
            self.warning(
                f"Nothing to do. A module project ({self.project_name}) cannot have binary extension modules."
            )

        build_options = self.options.build_options

        # get extension for binary extensions (depends on OS and python version)
        extension_suffix = get_extension_suffix()

        package_path = self.options.project_path / self.package_name
        dirs = os.listdir(package_path)
        succeeded = []
        failed = []
        for d in dirs:
            if (package_path / d).is_dir():
                build_d = False
                for prefix in ('cpp_','f90_'):
                    if d.startswith(prefix):
                        # d is a directory with a binary extension module
                        if self.options.build_options.module_to_build:
                            # build only one module, check if it is the one specified by module_to_build
                            build_d = d == f'{prefix}{self.options.build_options.module_to_build}' or \
                                      d == self.options.build_options.module_to_build
                        else:
                            # build all binary extension modules
                            build_d = True
                if build_d:
                    module_kind, module_name = d.split('_', 1)
                    if module_kind == 'f90':
                        # Exit if f2py is not available
                        if not ToolInfo('f2py').is_available():
                            msg = 'Building a Fortran binary extension requires f2py, which is not available in your current environment.\n' \
                                  '(F2py is part of the numpy Python package).'
                            if on_vsc_cluster():
                                msg += 'Load a cluster module that has the numpy package pre-installed.'
                            else:
                                msg += 'If you are using a virtual environment, install numpy as:\n' \
                                       '    (.venv) > pip install numpy\n' \
                                       'otherwise,\n' \
                                       '    > pip install numpy --user\n'
                            self.error(msg)

                    elif module_kind == 'cpp':
                        # exit if pybind11 is not available, and warn if too old...
                        pybind11 = PkgInfo('pybind11')
                        if not pybind11.is_available():
                            self.error('Building C++ binary extensions requires pybind11, which is not available in your current environment.\n'
                                       'If you are using a virtual environment, install it as .\n'
                                       '    (.venv) > pip install pybind11\n'
                                       'otherwise,\n'
                                       '    > pip install pybind11 --user\n'
                                       , exit_code=_exit_missing_component
                                       )
                        else:
                            if pybind11.version() < __pybind11_required_version__:
                                self.warning(f'Building C++ binary extensions requires pybind11, which is available in your current environment (v{pybind11.version()}).\n'
                                             f'However, you may experience problems because it is older than v{__pybind11_required_version__}.\n'
                                             'Upgrading is recommended.'
                                             )

                    binary_extension = package_path / (module_name + extension_suffix)
                    self.options.module_srcdir_path = package_path / d
                    self.options.module_kind = module_kind
                    self.options.module_name = module_name
                    self.options.package_path = package_path
                    self.exit_code = build_binary_extension(self.options)

                    if self.exit_code:
                        failed.append(binary_extension)
                    else:
                        succeeded.append(binary_extension)


        build_logger = self.logger
        if succeeded:
            build_logger.info("\n\nBinary extensions built successfully:")
            for binary_extension in succeeded:
                build_logger.info(f"  - {binary_extension}")
        if failed:
            build_logger.error("\nBinary extensions failing to build:")
            for binary_extension in failed:
                build_logger.error(f"  - {binary_extension}")
        if not succeeded and not failed:
            self.warning(
                f"No binary extensions found in package ({self.package_name})."
            )


    def app_exists(self, app_name):
        """Test if there is already an app with name ``app_name`` in this project.

        * :file:`<package_name>/cli_<app_name>.py`

        :param str app_name: app name
        :returns: bool
        """
        return (self.project_path / self.package_name / f"cli_{app_name}.py").is_file()

    def module_exists(self, module_name):
        """Test if there is already a module with name py:obj:`module_name` in this project.

        This can be either a Python module, package, or a binary extension module.

        :param str module_name: module name
        :returns: bool
        """
        return (self.py_module_exists(module_name)
                or self.py_package_exists(module_name)
                or self.cpp_module_exists(module_name)
                or self.f90_module_exists(module_name)
                )

    def py_module_exists(self, module_name):
        """Test if there is already a python module with name :py:obj:`module_name`
        in the project at :file:`project_path`.

        :param str module_name: module name
        :returns: bool
        """
        file = self.project_path / self.package_name / f'{module_name}.py'
        return file.is_file()

    def py_package_exists(self, module_name):
        """Test if there is already a python package with name :py:obj:`module_name`
        in the project at :file:`project_path`.

        :param str module_name: module name
        :returns: bool
        """
        return (self.project_path / self.package_name / module_name / '__init__.py').is_file()

    def f90_module_exists(self, module_name):
        """Test if there is already a f90 module with name py:obj:`module_name` in this project.

        :param str module_name: module name
        :returns: bool
        """
        return (self.project_path / self.package_name / ('f90_' + module_name) / f"{module_name}.f90").is_file()

    def cpp_module_exists(self, module_name):
        """Test if there is already a cpp module with name py:obj:`module_name` in this project.

        :param str module_name: module name
        :returns: bool
        """
        return (self.project_path / self.package_name / ('cpp_' + module_name) / f"{module_name}.cpp").is_file()

    def add_dependencies(self, deps):
        """Add dependencies to the :file:`pyproject.toml` file.

        :param dict deps: (package,version_constraint) pairs.
        """
        tool_poetry_dependencies = self.pyproject_toml['tool']['poetry']['dependencies']
        modified = False
        for pkg, version_constraint in deps.items():
            if pkg in tool_poetry_dependencies:
                # project was already depending on this package
                range1 = et_micc2.utils.version_range(version_constraint)
                range2 = et_micc2.utils.version_range(tool_poetry_dependencies[pkg])
                if range1 == range2:
                    # nothing to do: new and old version specifcation are the same
                    continue
                intersection = et_micc2.utils.intersect(range1, range2)
                if et_micc2.utils.validate_intersection(intersection):
                    range = intersection
                else:
                    range = et_micc2.utils.most_recent(version_constraint, tool_poetry_dependencies[pkg])
                tool_poetry_dependencies[pkg] = et_micc2.utils.version_constraint(range)
                modified = True
            else:
                # an entirely new dependency
                tool_poetry_dependencies[pkg] = version_constraint
                modified = True

        if modified:
            self.pyproject_toml.save()
            # Tell the user how to add the new dependencies
            msg = 'Dependencies added:\n' \
                  'If you are using a virtual environment created with poetry, run:\n' \
                  '    `poetry install` or `poetry update` to install missing dependencies.\n' \
                  'If you are using a virtual environment not created with poetry, run:\n'
            for dep,version in deps.items():
                msg += f'    (.venv) > pip install {dep}\n'
            msg += 'Otherwise, run:\n'
            for dep,version in deps.items():
                msg += f'    > pip install {dep} --user'
            self.logger.warning(msg)


    def module_to_package(self, module_py):
        """Move file :file:`module.py` to :file:`module/__init__.py`.

        :param str|Path module_py: path to module.py
        """
        module_py = Path(module_py).resolve()

        if not module_py.is_file():
            raise FileNotFoundError(module_py)
        src = str(module_py)

        package_name = str(module_py.name).replace('.py', '')
        package = module_py.parent / package_name
        package.mkdir()
        dst = str(package / '__init__.py')
        shutil.move(src, dst)

        et_micc2.logger.log(self.logger.debug,
                           f" . Module {module_py} converted to package {package_name}{os.sep}__init__.py."
                           )


    def get_logger(self, log_file_path=None):
        """"""
        if self.logger:
            return

        if log_file_path:
            log_file_name = log_file_path.name
            log_file_dir = log_file_path.parent
        else:
            log_file_name = f"{self.options.project_path.name}.micc.log"
            log_file_dir = self.options.project_path
            log_file_path = log_file_dir / log_file_name
        self.log_file = log_file_path

        if getattr(self.options, 'clear_log', False):
            if log_file_path.exists():
                log_file_path.unlink()

        # create a new logger object that will write to the log file and to the console
        self.logger = et_micc2.logger.create_logger(log_file_path)

        # set the log level from the verbosity
        self.logger.console_handler.setLevel(et_micc2.logger.verbosity_to_loglevel(self.options.verbosity))

        if self.options.verbosity > 2:
            print(f"Current logfile = {log_file_path}")

        if getattr(self.options, 'clear_log', False):
            self.logger.info(f"The log file was cleared: {log_file_path}")
            self.options.clear_log = False

        self.options.logger = self.logger


    def deserialize_db(self):
        """Read file ``db.json`` into self.db."""

        db_json = self.project_path / 'db.json'
        if db_json.exists():
            with db_json.open('r') as f:
                self.db = json.load(f)
        else:
            self.db = {}

    def serialize_db(self, db_entry=None, verbose=False):
        """Write self.db to file ``db.json``.

        Self.options is a SimpleNamespace object which is not default json serializable.
        This function takes care of that by converting to ``str`` where possible, and
        ignoring objects that do not need serialization, as e.g. self.options.logger.
        """

        if db_entry:
            # produce a json serializable version of db_entry['options']:
            my_options = {}
            for key, val in db_entry['options'].__dict__.items():
                if isinstance(val,(dict, list, tuple, str, int, float, bool)):
                    # default serializable types
                    my_options[key] = val
                    if verbose:
                        print(f"serialize_db: using ({key}:{val})")
                elif isinstance(val, Path):
                    my_options[key] = str(val)
                    if verbose:
                        print(f"serialize_db: using ({key}:str('{val}'))")
                else:
                    if verbose:
                        print(f"serialize_db: ignoring ({key}:{val})")

            db_entry['options'] = my_options

            if not hasattr(self, 'db'):
                # Read db.json into self.db if self.db does not yet exist.
                self.deserialize_db()

            # store the entry in self.db:
            self.db[self.options.add_name] = db_entry

        # finally, serialize self.db
        with et_micc2.utils.in_directory(self.project_path):
            with open('db.json','w') as f:
                json.dump(self.db, f, indent=2)


    def mv_component(self):
        """Rename or Remove a component (sub-module, sub-package, Fortran module, C++ module, app (CLI)."""
        cur_name, new_name = self.options.cur_name, self.options.new_name
        # Look up <cur_name> in the project's database to find out what kind of a component it is:
        self.deserialize_db()
        db_entry = self.db[cur_name] # may raise KeyError

        component_options = db_entry['options']
        if new_name: # rename
            with et_micc2.logger.log(self.logger.info
                                   , f"Package '{self.package_name}' Renaming component {cur_name} -> {new_name}:"
                                   ):
                if self.options.entire_project:
                    self.logger.info(f"Renaming entire project (--entire-project): '{self.project_name}'")
                    self.replace_in_folder(self.project_path, cur_name, new_name)

                elif self.options.entire_package:
                    self.logger.info(f"Renaming entire package (--entire-package): '{self.package_name}'")
                    self.replace_in_folder(self.project_path / self.package_name, cur_name, new_name)

                elif component_options['package']:
                    self.logger.info(f"Renaming Python sub-package: '{cur_name}{os.sep}__init__.py'")
                    self.replace_in_folder(self.project_path / self.package_name / cur_name, cur_name, new_name)
                    self.logger.info(f"Renaming test file: 'tests/test_{cur_name}.py'")
                    self.replace_in_file(self.project_path / 'tests' / f'test_{cur_name}.py', cur_name, new_name)

                elif component_options['py']:
                    self.logger.info(f"Renaming Python sub-module: '{cur_name}.py'")
                    self.replace_in_file(self.project_path / self.package_name / f'{cur_name}.py', cur_name, new_name)
                    self.logger.info(f"Renaming test file: 'tests/test_{cur_name}.py'")
                    self.replace_in_file(self.project_path / 'tests' / f'test_{cur_name}.py', cur_name, new_name)

                elif component_options['f90']:
                    self.logger.info(f"Fortran sub-module: 'f90_{cur_name}{os.sep}{cur_name}.f90'")
                    self.replace_in_folder(self.project_path / self.package_name / f'f90_{cur_name}', cur_name, new_name)
                    self.logger.info(f"Renaming test file: 'tests/test_{cur_name}.py'")
                    self.replace_in_file(self.project_path / 'tests'/ f'test_f90_{cur_name}.py', cur_name, new_name)

                elif component_options['cpp']:
                    self.logger.info(f"C++ sub-module: 'cpp_{cur_name}{os.sep}{cur_name}.cpp'")
                    self.replace_in_folder(self.project_path / self.package_name / f'cpp_{cur_name}', cur_name, new_name)
                    self.logger.info(f"Renaming test file: 'tests/test_{cur_name}.py'")
                    self.replace_in_file(self.project_path / 'tests' / f'test_cpp_{cur_name}.py', cur_name, new_name)

                elif component_options['app'] or component_options['group']:
                    self.logger.info(f"Command line interface (no subcommands): 'cli_{cur_name}.py'")
                    self.replace_in_file(self.project_path / self.package_name / f"cli_{cur_name}.py", cur_name, new_name)
                    self.replace_in_file(self.project_path / 'tests' / f"test_cli_{cur_name}.py", cur_name, new_name)
                    
                for key,val in db_entry.items():
                    if not key=='options':
                        filepath = self.project_path / key
                        new_string = val.replace(cur_name, new_name)
                        self.replace_in_file(filepath, val, new_string, contents_only=True)
                        db_entry[key] = new_string

                # Update the database:
                self.logger.info(f"Updating database entry for : '{cur_name}'")
                self.db[new_name] = db_entry

        else: # remove
            with et_micc2.logger.log(self.logger.info
                                   , f"Package '{self.package_name}' Removing component '{cur_name}'"
                                   ):
                if component_options['package']:
                    self.logger.info(f"Removing Python sub-package: '{cur_name}{os.sep}__init__.py'")
                    self.remove_folder(self.project_path / self.package_name / cur_name)
                    self.logger.info(f"Removing test file: 'tests/test_{cur_name}.py'")
                    self.remove_file(self.project_path / 'tests' / f'test_{cur_name}.py',)

                elif component_options['py']:
                    self.logger.info(f"Removing Python sub-module: '{cur_name}.py'")
                    self.remove_file(self.project_path / self.package_name / f'{cur_name}.py')
                    self.logger.info(f"Removing test file: 'tests/test_{cur_name}.py'")
                    self.remove_file(self.project_path / 'tests' / f'test_{cur_name}.py')

                elif component_options['f90']:
                    self.logger.info(f"Removing Fortran sub-module: 'f90_{cur_name}")
                    self.remove_folder(self.project_path / self.package_name / f'f90_{cur_name}')
                    self.logger.info(f"Removing test file: 'tests/test_f90_{cur_name}.py'")
                    self.remove_file(self.project_path / 'tests' / f'test_f90_{cur_name}.py')

                elif component_options['cpp']:
                    self.logger.info(f"Removing C++ sub-module: 'cpp_{cur_name}")
                    self.remove_folder(self.project_path / self.package_name / f'cpp_{cur_name}')
                    self.logger.info(f"Removing test file: 'tests/test_cpp_{cur_name}.py'")
                    self.remove_file(self.project_path / 'tests' / f'test_cpp_{cur_name}.py')

                elif component_options['cli'] or component_options['clisub']:
                    self.logger.info(f"Removing CLI: 'cli_{cur_name}.py'")
                    self.remove_file(self.project_path / self.package_name / f"cli_{cur_name}.py")
                    self.logger.info(f"Removing test file: 'test_cli_{cur_name}.py'")
                    self.remove_file(self.project_path /  'tests' / f"test_cli_{cur_name}.py")


                for key, val in db_entry.items():
                    if not key == 'options':
                        path = self.project_path / key
                        parent_folder, filename, old_string = path.parent, path.name, val
                        new_string = ''
                        self.replace_in_file(path, old_string, new_string, contents_only=True)

                # Update the database:
                self.logger.info(f"Updating database entry for : '{cur_name}'")

        del self.db[cur_name]
        self.serialize_db()


    def replace_in_folder( self, folderpath, cur_name, new_name ):
        """"""
        cur_dirname = folderpath.name
        new_dirname = cur_dirname.replace(cur_name,new_name)

        with et_micc2.logger.log(self.logger.info, f'Renaming folder "{cur_dirname}" -> "{new_dirname}"'):
            # first rename the folder
            new_folderpath = folderpath.parent / new_dirname
            os.rename(folderpath, new_folderpath)

            # rename subfolder names:
            folder_list = [] # list of tuples with (oldname,newname)
            for root, folders, files in os.walk(str(new_folderpath)):
                _filter(folders) # in place modification of the list of folders to traverse
                for folder in folders:
                    new_folder = folder.replace(cur_name,new_name)
                    folder_list.append((os.path.join(root,folder), os.path.join(root,new_folder)))

            # rename subfolder names:
            for tpl in folder_list:
                old_folder = tpl[0]
                new_folder = tpl[1]
                self.logger.info(f"Renaming folder '{old_folder}'  -> '{new_folder}'")
                os.rename(old_folder, new_folder)

            # rename in files and file contents:
            for root, folders, files in os.walk(str(new_folderpath)):
                for file in files:
                    if file.startswith('.orig.'):
                        continue
                    if file.endswith('.so'):
                        continue
                    if file.endswith('.json'):
                        continue
                    if file.endswith('.lock'):
                        continue
                    self.replace_in_file(Path(root) / file, cur_name, new_name)
                _filter(folders) # in place modification of the list of folders to traverse


    def remove_file(self,path):
        try:
            os.remove(path)
        except FileNotFoundError:
            pass


    def remove_folder(self,path):
        shutil.rmtree(path)


    def replace_in_file(self, filepath, cur_name, new_name, contents_only=False):
        """Replace <cur_name> with <new_name> in the filename and its contents."""

        file = filepath.name

        what = 'Modifying' if contents_only else 'Renaming'
        with et_micc2.logger.log(self.logger.info, f"{what} file {filepath}:"):
            self.logger.info(f'Reading from {filepath}')
            with open(filepath,'r') as f:
                old_contents = f.read()

            self.logger.info(f'Replacing "{cur_name}" with "{new_name}" in file contents.')
            new_contents = old_contents.replace(cur_name, new_name)

            if contents_only:
                new_file = file
            else:
                new_file = file.replace(cur_name,new_name)
                self.logger.info(f'Replacing "{cur_name}" with "{new_name}" in file name -> "{new_file}"')
            new_path = filepath.parent / new_file

            # By first renaming the original file, we avoid problems when the new
            # file name is identical to the old file name (because it is invariant,
            # e.g. __init__.py)
            orig_file = '.orig.'+file
            orig_path = filepath.parent / orig_file
            self.logger.info(f'Keeping original file "{file}" as "{orig_file}".')
            os.rename(filepath, orig_path)

            self.logger.info(f'Writing modified file contents to {new_path}: ')
            with open(new_path,'w') as f:
                f.write(new_contents)

    
    def doc_cmd(self):
        """Build documentation."""
        self.require_project_created()

        if on_vsc_cluster():
            self.error("The cluster is not suited for building documentation. Use a desktop machine instead.")

        # Check needed tools
        if not ToolInfo('make').is_available():
            self.error("The make command is missing in your current environment. You must install it to build documentation.")
        if not PkgInfo('sphinx').is_available():
            self.error("The sphinx package is missing in your current environment.\n"
                       "You must install it to build documentation.")
        if not PkgInfo('sphinx_rtd_theme').is_available():
            self.error("The sphinx_rtd_theme package is missing in your current environment.\n"
                       "You must install it to build documentation.")
        if not PkgInfo('sphinx_click').is_available():
            self.error("The sphinx_click package is missing in your current environment.\n"
                       "You must install it to build documentation.")

        self.exit_code = et_micc2.utils.execute(
            ['make', self.options.what],
            cwd=Path(self.options.project_path) / 'docs',
            logfun=self.logger.info
        )


    # def venv_cmd(self):
    #     """"""
    #     venv_path = self.options.project_path / self.options.venv_name
    #     if venv_path.exists():
    #         self.error(f'A virtual environment with name `{venv_path}` exists already.\n'
    #                    f'Choose another name, or delete it first.')
    # 
    #     if not Path(self.options.python_executable).exists():
    #         self.error(f'The Python executable `{self.options.python_executable}` is not found.')
    # 
    #     cmd = [self.options.python_executable, '-m', 'venv', self.options.venv_name]
    #     if self.options.system_site_packages:
    #         cmd.append('--system-site-packages')
    #     self.exit_code = et_micc2.utils.execute(cmd, cwd=self.options.project_path, logfun=self.logger.info)


def get_extension_suffix():
    """Return the extension suffix, e.g. :file:`.cpython-37m-darwin.so`."""
    return sysconfig.get_config_var('EXT_SUFFIX')


def build_binary_extension(options):
    """Build a binary extension described by *options*.

    :param options:
    :return:
    """
    # get extension for binary extensions (depends on OS and python version)
    extension_suffix = get_extension_suffix()

    build_options = options.build_options

    # Remove so file to avoid "RuntimeError: Symlink loop from ..."
    so_file = options.package_path / (options.module_name + extension_suffix)
    try:
        so_file.unlink()  # missing_ok=True only available from 3.8 on, not in 3.7
    except FileNotFoundError:
        pass

    build_log_file = options.module_srcdir_path / "micc-build.log"
    build_logger = et_micc2.logger.create_logger(build_log_file, filemode='w')
    with et_micc2.logger.log(build_logger.info, f"Building {options.module_kind} module '{options.module_name}':"):
        binary_extension = options.module_name + extension_suffix
        destination = (options.package_path / binary_extension).resolve()

        if options.module_kind in ('cpp', 'f90') and (options.module_srcdir_path / 'CMakeLists.txt').exists():
            output_dir = options.module_srcdir_path / '_cmake_build'
            build_dir = output_dir
            if build_options.clean and output_dir.exists():
                build_logger.info(f"--clean: shutil.removing('{output_dir}').")
                shutil.rmtree(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            with et_micc2.utils.in_directory(output_dir):
                cmake_cmd = ['cmake', '-D', f"PYTHON_EXECUTABLE={sys.executable}"]
                for key,val in options.build_options.cmake.items():
                    cmake_cmd.extend(['-D', f"{key}={val}"])
                if sys.platform == 'win32':
                    cmake_cmd.extend(['-G', 'NMake Makefiles'])
                    make = 'nmake'
                else:
                    make = 'make'

                if options.module_kind == 'cpp':
                    cmake_cmd.extend(['-D', f"pybind11_DIR={path_to_cmake_tools()}"])

                cmake_cmd.append('..')

                cmds = [ cmake_cmd
                       , [make, 'VERBOSE=1']
                       # [make, 'install']
                ]
                # This is a fix for the native Windows case, when using the
                # Intel Python distribution and building a f90 binary extension
                fix = sys.platform == 'win32' and 'intel' in sys.executable and options.module_kind == 'f90'
                if not fix:
                    cmds.append([make, 'install'])

                exit_code = et_micc2.utils.execute(
                    cmds, build_logger.debug, stop_on_error=True, env=os.environ.copy()
                )

                if fix:
                    from glob import glob
                    search = str(options.package_path/f'f90_{options.module_name}/_cmake_build/') \
                             + f'{os.sep}{options.module_name}.*.pyd'
                    # print(search)
                    pyd = glob(search)
                    dst = options.package_path / f'{options.module_name}.pyd'
                    build_logger.info(f'Installing `{pyd[0]}` as {dst}')
                    shutil.copyfile(pyd[0], dst)

                if build_options.cleanup:
                    build_logger.info(f"--cleanup: shutil.removing('{build_dir}').")
                    shutil.rmtree(build_dir)
        else:
            raise RuntimeError("Bad module kind, or no CMakeLists.txt   ")

    return exit_code


def path_to_cmake_tools():
    """Return the path to the folder with the CMake tools.
    
    """
    found = ''
    #look in global site-packages:
    site_packages = site.getsitepackages()
    site_packages.append(site.getusersitepackages())
    print(site_packages)
    for d in site_packages:
        pd = Path(d) / 'pybind11'
        if pd.exists():
            found = pd
            break
    
    if not found:
        raise ModuleNotFoundError('pybind11 not found in {site_packages}')
        
    p = pd / 'share' / 'cmake' / 'pybind11'
    print(f'path_to_cmake_tools={p}')
    return str(p)


def _filter(folders):
    """"In place modification of the list of folders to traverse.

    see https://docs.python.org/3/library/os.html

    ...

    When topdown is True, the caller can modify the dirnames list in-place
    (perhaps using del or slice assignment), and walk() will only recurse
    into the subdirectories whose names remain in dirnames; this can be used
    to prune the search, impose a specific order of visiting, or even to
    inform walk() about directories the caller creates or renames before it
    resumes walk() again. Modifying dirnames when topdown is False has no
    effect on the behavior of the walk, because in bottom-up mode the
    directories in dirnames are generated before dirpath itself is generated.

    ...
    """
    exclude_folders = ['.venv', '.git', '_build', '_cmake_build', '__pycache__']
    folders[:] = [f for f in folders if not f in exclude_folders]

def auto_build_binary_extension(package_path, module_to_build):
    """Set options for building binary extensions, and build
    binary extension *module_to_build* in *package_path*.

    :param Path package_path:
    :param str module_to_build:
    :return: exit_code
    """
    options = SimpleNamespace( package_path  = package_path
                             , verbosity     = 1
                             , module_name   = module_to_build
                             , build_options = SimpleNamespace( module_to_build = module_to_build
                                                              , clean           = True
                                                              , cleanup         = True
                                                              , cmake           = {'CMAKE_BUILD_TYPE': 'RELEASE'}
                                                              )
                             )
    for module_prefix in ["cpp", "f90"]:
        module_srcdir_path = package_path / f"{module_prefix}_{options.module_name}"
        if module_srcdir_path.exists():
            options.module_kind = module_prefix
            options.module_srcdir_path = module_srcdir_path
            options.build_options.build_tool_options = {}
            break
    else:
        raise ValueError(f"No binary extension source directory found for module '{module_to_build}'.")

    exit_code = build_binary_extension(options)

    msg = ("[ERROR]\n"
          F"    Binary extension module '{options.module_name}{get_extension_suffix()}' could not be build.\n"
           "    Any attempt to use it will raise exceptions.\n"
           ) if exit_code else ""
    return msg


# eof
