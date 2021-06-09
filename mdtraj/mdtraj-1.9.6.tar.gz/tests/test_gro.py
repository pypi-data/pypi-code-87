##############################################################################
# MDTraj: A Python Library for Loading, Saving, and Manipulating
#         Molecular Dynamics Trajectories.
# Copyright 2012-2017 Stanford University and the Authors
#
# Authors: Robert T. McGibbon
# Contributors: Matthew Harrigan
#
# MDTraj is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with MDTraj. If not, see <http://www.gnu.org/licenses/>.
##############################################################################


import tempfile, os
import mdtraj as md
from mdtraj.formats import GroTrajectoryFile
from mdtraj.testing import eq

fd, temp = tempfile.mkstemp(suffix='.gro')
os.close(fd)


def teardown_module(module):
    """remove the temporary file created by tests in this file
    this gets automatically called by pytest"""
    os.unlink(temp)


def test_read_write(get_fn):
    for t in [md.load(get_fn('4waters.pdb')),  # no unit cell
              md.load(get_fn('native2.pdb')),  # unitcell
              md.load(get_fn('frame0.pdb'))]:  # multiframe
        with GroTrajectoryFile(temp, 'w') as f:
            f.write(t.xyz, t.topology, unitcell_vectors=t.unitcell_vectors)

        with GroTrajectoryFile(temp) as f:
            xyz, time, unitcell = f.read()
            top = f.topology

        eq(xyz, t.xyz, decimal=3)
        eq(list(top.atoms), list(t.top.atoms))
        if t.unitcell_vectors is not None:
            eq(unitcell, t.unitcell_vectors)


def test_read_write_precision(get_fn):
    import random
    for t in [md.load(get_fn('4waters.pdb')),  # no unit cell
              md.load(get_fn('native2.pdb')),  # unitcell
              md.load(get_fn('frame0.pdb'))]:  # multiframe
        with GroTrajectoryFile(temp, 'w') as f:
            f.write(t.xyz, t.topology, unitcell_vectors=t.unitcell_vectors,
                    precision=random.randint(4, 10))

        with GroTrajectoryFile(temp) as f:
            xyz, time, unitcell = f.read()
            top = f.topology

        eq(xyz, t.xyz, decimal=3)
        eq(list(top.atoms), list(t.top.atoms))
        if t.unitcell_vectors is not None:
            eq(unitcell, t.unitcell_vectors)

    # Test out the automatic saver and loader with different precisions
    t = md.load(get_fn('native2.pdb'))
    t.save(temp, precision=5)
    eq(t.xyz, md.load(temp).xyz, decimal=3)


def test_no_whitespace_gro(get_fn):
    t = md.load(get_fn('v_error.gro'))
    eq(t.xyz.shape, (1, 1, 3))
    eq(t.n_atoms, 1)


def test_load(get_fn):
    for tref in [md.load(get_fn('4waters.pdb')),  # no unit cell
                 md.load(get_fn('native2.pdb'))]:  # unit cell
        with GroTrajectoryFile(temp, 'w') as f:
            f.write(tref.xyz, tref.topology, unitcell_vectors=tref.unitcell_vectors)

        t = md.load(temp)
        eq(t.xyz, tref.xyz, decimal=3)
        eq(list(t.top.atoms), list(tref.top.atoms))
        eq(t.unitcell_vectors, tref.unitcell_vectors)

    #if there are 2 residues with same renum but different resname
    t = md.load(get_fn('two_residues_same_resnum.gro'))
    eq(t.n_residues, 2)


def test_against_gmx(get_fn, tmpdir):
    t1 = md.load(get_fn('frame0.pdb'))

    # generated by converting frame0.pdb to gro with g_trajconv
    t2 = md.load(get_fn('frame0.gro'))

    fn = "{}/temp.gro".format(tmpdir)
    t1.save(fn)
    t3 = md.load(fn)

    eq(t1.xyz, t2.xyz)
    eq(t1.xyz, t3.xyz)
    eq(t1.time, t2.time)
    eq(t1.time, t3.time)
    eq(t1.unitcell_vectors, t2.unitcell_vectors)
    eq(t1.unitcell_vectors, t3.unitcell_vectors)
