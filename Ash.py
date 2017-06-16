import os, sys

_ver = "1.2.1"
_Tlvl = "_t_1_"
_settings = []
_sett_con = []
_def_sett = ["setup","encode","version","noticed_changes","AFN","trust_lev","code"]
_def_con = ["true","23923351","","false","none","","1"]

_con_file = "ash"

'''
1   2   3   4   5   6   7   8   9
---------------------------------
A   B   C   D   E   F   G   H   I  | 1
J   K   L   M   N   O   P   Q   R  | 2
S   T   U   V   W   X   Y   Z      | 3

True    = 23923351
False   = 6111321351

use "code" to change the value of the numbers ^^^
- only use this after config has been edited...
'''


def _main():
    _def_con[2] = _ver
    _def_con[5] = _Tlvl
    _lod_con()
    while True:
        _in = raw_input("> ")
        _proccess(_in)

def _proccess(_input):
    _tokens = _input.split(" ")
    for _x in _settings:
        _pos = _sch_con(_x, "_norm", True)
        print("{0}={1}".format(_x, _pos))


def _lod_con():
    '''
    This method is here to load all the settings of Ash.
    It will load everything needed.
    '''
    if not os.path.isfile(_con_file):
        _results = []
        _len = len(_def_sett)
        _int = 0
        while _int < _len:
            _results.append("{0}={1}\n".format(_def_sett[_int], _def_con[_int]))
            _int += 1
        with open(_con_file, 'w') as _out:
            for _x in _results:
                _out.write(_x)

    else:
        with open(_con_file, 'r') as _in:
            for _x in _in:
                _x = _x.strip("\n")
                _tokens = _x.split("=")
                _settings.append(_tokens[0])
                _sett_con.append(_tokens[1])
        _con_chck()

def _con_chck():
    global _ver
    _con_ver = _sch_con("version", "_norm", True)
    if _con_ver > _ver:
        '''
        Something strange is happening here... the value of the _con file
        version number is greater than us... Lets check online if we have
        an update... if not... then raise trust level.
        '''
        _slf_chnge("_Tlvl", "_t_2_")
        _rem_con("", True)

    elif _con_ver < _ver:
        '''
        We are newer than the _con file... lets wipe the con file...
        and upload new defaults... but keeping information like trust level.
        '''
        _tlvl = _sch_con("trust_lev", "_norm", True)
        _pos = _sch_con("trust_lev", "_def", False)

        exit()

def _sch_con(_setting, _cons, _ret):
    '''
    This method is here to search "_settings" for the
    index location of a setting... to then remove, change
    or even return the value of that setting.
    '''
    if _ret == True:
        if _cons == "_def":
            try:
                _num = _def_sett.index(_setting)
                return _def_con[_num]
            except ValueError:
                return None
        else:
            try:
                _num = _settings.index(_setting)
                return _sett_con[_num]
            except ValueError:
                return None
    else:
        if _cons == "_def":
            try:
                return _def_sett.index(_setting)
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
    _num = _sch_con(_setting, "_norm", False)
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

def _rem_con(_setting, _all):
    global _settings
    global _sett_con
    '''
    This method is here to remove a config from the system.
    '''
    if _all == True:
         os.remove(_con_file)
    else:
        _num = _sch_con(_setting, "_norm" , False)
        del _settings[_num]
        del _sett_con[_num]

def _sve_con(_def):
    '''
    This method is here to save the config that is loaded...
    out to the file.
    '''
    if _def == True:
        _results = []
        _len = len(_def_sett)
        _int = 0
        while _int < _len:
            _results.append("{0}={1}\n".format(_def_sett[_int], _def_con[_int]))
            _int += 1
        with open(_con_file, 'w') as _out:
            for _x in _results:
                _out.write(_x)
    else:
        _results = []
        _len = len(_def_sett)
        _int = 0
        while _int < _len:
            _results.append("{0}={1}\n".format(_settings[_int], _sett_con[_int]))
            _int += 1
        with open(_con_file, 'w') as _out:
            for _x in _results:
                _out.write(_x)

def _de_code(_string):
    '''
    This method is here to de-code any config settings
    hidden within asher.
    '''
    print("Need to finish _de_code()")


def _slf_chnge(_string, _new):
    _results = ""
    with open("Ash.py", 'r') as _in:
        for _x in _in:
            if _x.startswith(_string):
                _x = _x.strip("\n")
                _tokens = _x.split(" = ")
                _results = _tokens[1][1:-1]

    with open("Ash.py") as f:
        newText=f.read().replace(_results, _new)

    with open("Ash.py", "w") as f:
        f.write(newText)

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

    _trust_num = _sch_con("trust_lev", "_norm", False)
    _trust_val = _sch_con("trust_lev", "_norm", True)
    print("need to finish _secure()")




_main()
