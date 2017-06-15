import os, sys

_settings = []
_sett_con = []

def _main():


def _load_con():
    '''
    This method is here to load all the settings of Ash.
    It will load everything needed.
    '''
    with open("~/.ash", 'r') as _in:
        for _x in _in:
            _x = _x.strip("\n")
            _tokens = _x.split("=")
            _settings.append(_tokens[0])
            _sett_con.append(_tokens[1])

def _sch_con(_setting, _ret):
    if _ret == True:
        try:
            _num = _settings.index(_setting)
            return _sett_con[_num]
        except ValueError:
            return None
    else:
        try:
            _num = _settings.index(_setting)
            return _num
        except ValueError:
            return NONE

def _set_con(_setting, _value):

def _add_con(_setting, _value):

def _rem_con(_setting):

def _secure():
    '''
    This method is here to protect Ash. This will keep the integrity
    of his whole system... if anything changes, he will change it back.
    '''


_main()
