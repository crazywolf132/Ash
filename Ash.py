import os, sys

_ver = 1.2.1
_settings = []
_sett_con = []
_def_sett = ["setup","encode","version","noticed_changes","AFN","trust_lev"]
_def_con = ["true","23923351","","false","none","1"]

_con_file = Path("~/.ash")

'''
1   2   3   4   5   6   7   8   9
---------------------------------
A   B   C   D   E   F   G   H   I  | 1
J   K   L   M   N   O   P   Q   R  | 2
S   T   U   V   W   X   Y   Z      | 3

True    = 23923351
False   = 6111321351
'''


def _main():
    _def_con[2] = _ver
    _lod_con()

def _lod_con():
    '''
    This method is here to load all the settings of Ash.
    It will load everything needed.
    '''
    if not _con_file.is_file():
        with open(_con_file, 'w') as _out:
            for _x in _def_sett:
                print(_x)
    else:
        with open(_con_file, 'r') as _in:
            for _x in _in:
                _x = _x.strip("\n")
                _tokens = _x.split("=")
                _settings.append(_tokens[0])
                _sett_con.append(_tokens[1])

def _sch_con(_setting, _ret):
    '''
    This method is here to search "_settings" for the
    index location of a setting... to then remove, change
    or even return the value of that setting.
    '''
    if _ret == True:
        try:
            _num = _settings.index(_setting)
            return _sett_con[_num]
        except ValueError:
            return None
    else:
        try:
            return _settings.index(_setting)
        except ValueError:
            return None

def _set_con(_setting, _value):
    '''
    This method is here to change the value of a specific
    config value.
    '''
    _num = _sch_con(_setting, False)
    if _num == None:
        print("Sorry, there is no such value as this.")
    else:
        _sett_con[_num] = _value

def _add_con(_setting, _value):
    '''
    This method is here to add another config to the settings/
    '''
    _settings.append(_setting)
    _sett_con.append(_value)

def _rem_con(_setting):
    '''
    This method is here to remove a config from the system.
    '''
    _num = _sch_con(_setting, False)
    del _settings[_num]
    del _sett_con[_num]

def _sve_con():
    '''
    This method is here to save the config that is loaded...
    out to the file.
    '''
    with open(_con_file, 'w') as _out:
        for _x in _settings:
            print(_x)

def _de_code(_string):
    '''
    This method is here to de-code any config settings
    hidden within asher.
    '''


def _secure():
    '''
    This method is here to protect Ash. This will keep the integrity
    of his whole system... if anything changes, he will change it back.
    '''

    '''
    Trust levels.
    0 = Clearly edited by the user - change to 10... dont trust the user.
    1 = Defualt. Trust the user... they wont harm you.
    2 = Hmmm... My file system is different to last time. - Log this.
    3 = Wow, my file system is different again... and its already Logged.
    4 = My config file has been manually edited...
    5 = My config file has been deleted, and the trust level is above 3
    6 = Oh no, they tried to delete me. - Move to another location on the computer.
    7 = Been deleted again. Re-name self. Move. Backup reguarly.
    8 = Things about me are changing without me doing it. (Config files... and code.)
    9 = _secure is missing from code. This is sketch ASF.
    10 = Trust no-one!. Make another user, load myself into file-system. lock user. - Triggered by being completely deleted after Level 7.
    '''


_main()
