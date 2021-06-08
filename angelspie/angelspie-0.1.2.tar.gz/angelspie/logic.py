import inspect
import logging
import os
import re
import time

import gi
gi.require_version('Wnck', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')

from gi.repository import Wnck, Gtk, Keybinder, Gdk
from .autogenerated import IfWindow, WnckWindowActions, GdkWindowActions
try:
    from .xtest import press, click
except ModuleNotFoundError:
    press, click = None, None

scr = Wnck.Screen.get_default()
gdk_screen = Gdk.Screen.get_default()
kb = Keybinder
bindings = []
bound = []
logger = logging.getLogger()


class Match:
    def __init__(self, cfg):
        if not cfg:
            cfg = {'true': cfg}
        elif not isinstance(cfg, dict):
            cfg = {'eq': cfg}
        for k in cfg:
            if not hasattr(self, k):
                vals = ', '.join(f for f in self.__class__.__dict__ if not f.startswith('_'))
                logger.error(f'Wrong condition {k}. Possible values: {vals}')
        self.cfg = cfg
    def __call__(self, val):
        for k, v in self.cfg.items():
            if not getattr(self, k)(v, val):
                return False
        return True
    def true(self, val, s):
        ''' is true'''
        return bool(s)
    def contains(self, val, s):
        ''' contains substring '''
        s = str(s)
        return val in s
    def eq(self, val, k):
        ''' equals  '''
        val = type(k)(val)
        return k == val
    def re(self, val, k):
        ''' regexp '''
        return bool(re.search(val, str(k)))
    def icontains(self, val, s):
        ''' contains substring, ignore case '''
        return val.lower() in str(s).lower()
    def ieq(self, val, k):
        ''' equals, ignore case '''
        return str(k).lower() == val.lower()
    def ire(self, val, k):
        ''' regexp, ignore case '''
        return bool(re.search(val, str(k), re.IGNORECASE))


class If(IfWindow):

    def __init__(self, cfg, then):
        self.then = then
        self.event = cfg.pop('event', 'active_window_changed')
        if 'key' in cfg:
            key = cfg.pop('key')
            bindings.append((self, key, then))
            self.event = 'key_pressed'
        self.conditions = []
        for k, v in cfg.items():
            if k in ('sh', 'py'):
                self.conditions.append((getattr(self, k), v))
            elif hasattr(self, k):
                self.conditions.append((Match(v), getattr(self, k)))
            else:
                self.conditions.append((Match(v), self._custom(k)))

    def _cb(self, event, *args):
        if event == self.event and self():
            self.then()

    def __call__(self):
        for k, v in self.conditions:
            v = v() if callable(v) else v
            try:
                if not k(v):
                    return False
            except Exception as e:
                logger.exception(e)
        return True

    @staticmethod
    def sh(cmd):
        ''' If shell comannd has exitcode 0 '''
        return not os.system(cmd)
    @staticmethod
    def py(cmd):
        ''' Eval python code '''
        return eval(cmd)

    def _custom(self, key):
        ''' run chain of methods like scr.get_active_window.get_application.get_name '''
        obj_map = {'scr': lambda: scr, 'gdk_scr': Gdk.Screen.get_default, 'win': scr.get_active_window,
                   'ws': scr.get_active_workspace, 'gdk_win': lambda: Gdk.Screen.get_default().get_active_window()}
        keys = key.split('.')
        def cb():
            obj = obj_map[keys[0]]()
            for key in keys[1:]:
                obj = getattr(obj, key)()
            return str(obj)
        return cb

    @classmethod
    def _vars(cls):
        return {k: getattr(cls, k)() for k, _ in inspect.getmembers(cls) if not k.startswith('_') and k not in ('sh', 'py')}


class Then(WnckWindowActions, GdkWindowActions):
    def __init__(self, cfg):
        for k in cfg:
            if not hasattr(self, k):
                vals = ', '.join(f for f, _ in inspect.getmembers(self) if not f.startswith('_'))
                logger.error(f'Wrong action {k}. Possible values: {vals}')
        self.cfg = cfg

    def __call__(self):
        for k, v in self.cfg.items():
            getattr(self, k)(v)

    def sh(self, cmd):
        ''' Run shell command '''
        os.system(cmd)

    def echo(self, s):
        ''' Print to stdout '''
        print(s.format(**If._vars()))

    def debug(self, s):
        ''' Information about current window, etc '''
        print(repr(If._vars()))

    def py(self, s):
        ''' Run python code '''
        eval(s)

    def sleep(self, s):
        ''' Sleep'''
        time.sleep(float(s))

    def press(self, key):
        ''' Emulate keypress '''
        if press is None:
            logger.error('Press function requires python-xlib library')
            return
        press(key)

    def click(self, button):
        ''' Emulate mouse click '''
        if click is None:
            logger.error('Click function requires python-xlib library')
            return
        click(int(button))


def rebind(*args):
    while bound:
        kb.unbind(bound.pop())
    for condition, key, then in bindings:
        if condition():
            bound.append(key)
            kb.bind(key, lambda key: then())
