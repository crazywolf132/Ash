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
    This method is here to add another cotnfig to the settings/
    '''
    _settings.append(_setting)
    _sett_con.append(_value)
    _def_sett.append(_setting)
    _def_con.append(_value)
    _sve_con()

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
        _def_con[2] = _ver
        _def_con[5] = _Tlvl
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

    global _Tlvl
    global _ver
    _con_ver = _sch_con("version", "_norm", True)
    if _con_ver > _ver:
        '''
        Something strange is happening here... the value of the _con file
        version number is greater than us... Lets check online if we have
        an update... if not... then raise trust level.
        '''
        ## Check online version.
        _O_ver = "1.2.2"
        if _O_ver >
    elif _con_ver < _ver:
        '''
        We are newer than the _con file... lets wipe the con file...
        and upload new defaults... but keeping information like trust level...
        This could be sketchy as the user could change the version number along
        with the trust level... then it creates a Hole where the user can just change
        the trust level without any repercusions.
        '''
        ## Lets just note that the version is different... if it happens again... change trust_lvl
        _returned_con = _sch_con("_verError", "_norm", True)
        _returned_lcl = _sch_con("_verError", "_def", True)
        if _returned_lcl == "true" and _returned_con == "false":
            '''
            Raise trust_lev as we have found that they have manually changed the
            con_file
            '''
            _up_tlvl()
            _add_con("_verError", "true")
        elif _returned_lcl == "false" and _returned_con == "true":
            _add_con("_verError", "true")
        elif _returned_lcl == "true" and _returned_con == "true":
            _up_tlvl()
        elif _returned_lcl == "false" and _returned_con == "false":
            _add_con("_verError", "true")
        elif _returned_lcl == "NONE" or _returned_con == "NONE":
            _add_con("_verError", "true")

    _L_tlvl = _load_tlvl(True)
    _C_tlvl = _load_tlvl(False)
    if _C_tlvl > _L_tlvl:
        '''
        Hmmm... this is strange... I have a lower trust_val to my config.
        Lets assume i have the correct val... and push my current val...
        but we will note this.
        '''
        _returned_con = _sch_con("_valError", "_norm", True)
        _returned_lcl = _sch_con("_valError", "_def", True)
        if _returned_lcl == "true" and _returned_con == "false":
            '''
            Raise trust_lev as we have found that they have manually changed the
            con_file
            '''
            _up_tlvl()
            _add_con("_valError", "true")
        elif _returned_lcl == "false" and _returned_con == "true":
            _add_con("_valError", "true")
        elif _returned_lcl == "true" and _returned_con == "true":
            _up_tlvl()
        elif _returned_lcl == "false" and _returned_con == "false":
            _add_con("_valError", "true")
        elif _returned_lcl == "NONE" or _returned_con == "NONE":
            _add_con("_valError", "true")


    elif _C_tlvl < _L_tlvl:
        '''
        The trust_val in the config is lower than me... lets push my current
        value to the config... then we will log it and see if it continues...
        '''

        _returned_con = _sch_con("_valError", "_norm", True)
        _returned_lcl = _sch_con("_valError", "_def", True)
        if _returned_lcl == "true" and _returned_con == "false":
            '''
            Raise trust_lev as we have found that they have manually changed the
            con_file
            '''
            _up_tlvl()
            _add_con("_valError", "true")
        elif _returned_lcl == "false" and _returned_con == "true":
            _add_con("_valError", "true")
        elif _returned_lcl == "true" and _returned_con == "true":
            _up_tlvl()
        elif _returned_lcl == "false" and _returned_con == ""


def _load_tlvl(_local):
    global _Tlvl
    if _local == True:
        _t = _Tlvl
        if _t == "_t_1_"
            return 1
        elif _t == "_t_2_":
            return 2
        elif _t == "_t_3_":
            return 3
        elif _t == "_t_4_":
            return 4
        elif _t == "_t_5_":
            return 5
        elif _t == "_t_6_":
            return 6
        elif _t == "_t_7_":
            return 7
        elif _t == "_t_8_":
            return 8
        elif _t == "_t_9_":
            return 9
        elif _t == "_t_10_":
            return 10
    else:
        _t = _sch_con("trust_lev", "_norm", True)
        if _t == "_t_1_"
            return 1
        elif _t == "_t_2_":
            return 2
        elif _t == "_t_3_":
            return 3
        elif _t == "_t_4_":
            return 4
        elif _t == "_t_5_":
            return 5
        elif _t == "_t_6_":
            return 6
        elif _t == "_t_7_":
            return 7
        elif _t == "_t_8_":
            return 8
        elif _t == "_t_9_":
            return 9
        elif _t == "_t_10_":
            return 10

def _up_tlvl():

'''

'''
    global _Tlvl
    _t = _Tlvl
    if _t == "_t_1_"
        _slf_chnge("_Tlvl", "_t_2_")
    elif _t == "_t_2_":
        _slf_chnge("_Tlvl", "_t_3_")
    elif _t == "_t_3_":
        _slf_chnge("_Tlvl", "_t_4_")
    elif _t == "_t_4_":
        _slf_chnge("_Tlvl", "_t_5_")
    elif _t == "_t_5_":
        _slf_chnge("_Tlvl", "_t_6_")
    elif _t == "_t_6_":
        _slf_chnge("_Tlvl", "_t_7_")
    elif _t == "_t_7_":
        _slf_chnge("_Tlvl", "_t_8_")
    elif _t == "_t_8_":
        _slf_chnge("_Tlvl", "_t_9_")
    elif _t == "_t_9_":
        _slf_chnge("_Tlvl", "_t_10_")
    elif _t == "_t_10_":
        print("Trust level 10 needs to be setup.")
    _rem_con("", True)
    _sve_con(True)


_main()
