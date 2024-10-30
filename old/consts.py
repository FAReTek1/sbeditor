# Thanks to scratch wiki:
# https://en.scratch-wiki.info/wiki/Scratch_File_Format
# https://en.scratch-wiki.info/wiki/List_of_Block_Opcodes

def vdir(obj):
    # https://stackoverflow.com/questions/21542753/dir-without-built-in-methods
    return [x for x in dir(obj) if not x.startswith("__")]


def all_of_the(cls: type, *, with_a: str = None):
    if with_a is None:
        return vdir(cls)

    return [getattr(cls, a).get(with_a) for a in vdir(cls)]


ID_DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"£$%^&*()-_+=[]{}:;'@#~,.?<>/\\|`¬¦"
ID_BASE = len(ID_DIGITS)

class Extensions:
    PEN = \
        {"name": "Pen Extension",
         "code": "pen"}
    WEDO2 = \
        {"name": "LEGO Education WeDo 2.0 Extension",
         "code": "wedo2"}
    MUSIC = \
        {"name": "Music Extension",
         "code": "music"}
    MICROBIT = \
        {"name": "micro:bit Extension",
         "code": "microbit"}
    TEXT2SPEECH = \
        {"name": "Text to Speech Extension",
         "code": "text2speech"}
    TRANSLATE = \
        {"name": "Translate Extension",
         "code": "translate"}
    VIDEO_SENSING = \
        {"name": "Video Sensing Extension",
         "code": "videoSensing"}
    EV3 = \
        {"name": "LEGO MINDSTORMS EV3 Extension",
         "code": "ev3"}
    MAKEY_MAKEY = \
        {"name": "Makey Makey Extension",
         "code": "makeymakey"}
    BOOST = \
        {"name": "LEGO BOOST Extension",
         "code": "boost"}
    GDXFOR = \
        {"name": "Go Direct Force & Acceleration Extension",
         "code": "gdxfor"}


class Blocks:
    """
    Class containing all block opcodes and functions for creating JSON data for array-like blocks
    """

    ALL = {"motion": {"movesteps": "motion_movesteps",
                      "turnright": "motion_turnright",
                      "turnleft": "motion_turnleft",
                      "goto": "motion_goto",
                      "gotoxy": "motion_gotoxy",
                      "glideto": "motion_glideto",
                      "glidesecstoxy": "motion_glidesecstoxy",
                      "pointindirection": "motion_pointindirection",
                      "pointtowards": "motion_pointtowards",
                      "changexby": "motion_changexby",
                      "setx": "motion_setx",
                      "changeyby": "motion_changeyby",
                      "sety": "motion_sety",
                      "ifonedgebounce": "motion_ifonedgebounce",
                      "setrotationstyle": "motion_setrotationstyle",
                      "xposition": "motion_xposition",
                      "yposition": "motion_yposition",
                      "direction": "motion_direction",
                      "scroll_right": "motion_scroll_right",
                      "scroll_up": "motion_scroll_up",
                      "align_scene": "motion_align_scene",
                      "xscroll": "motion_xscroll",
                      "yscroll": "motion_yscroll",
                      "goto_menu": "motion_goto_menu",
                      "glideto_menu": "motion_glideto_menu",
                      "pointtowards_menu": "motion_pointtowards_menu"},

           "looks": {"sayforsecs": "looks_sayforsecs",
                     "say": "looks_say",
                     "thinkforsecs": "looks_thinkforsecs",
                     "think": "looks_think",
                     "switchcostumeto": "looks_switchcostumeto",
                     "nextcostume": "looks_nextcostume",
                     "switchbackdropto": "looks_switchbackdropto",
                     "switchbackdroptoandwait": "looks_switchbackdroptoandwait",
                     "nextbackdrop": "looks_nextbackdrop",
                     "changesizeby": "looks_changesizeby",
                     "setsizeto": "looks_setsizeto",
                     "changeeffectby": "looks_changeeffectby",
                     "seteffectto": "looks_seteffectto",
                     "cleargraphiceffects": "looks_cleargraphiceffects",
                     "show": "looks_show",
                     "hide": "looks_hide",
                     "gotofrontback": "looks_gotofrontback",
                     "goforwardbackwardlayers": "looks_goforwardbackwardlayers",
                     "costumenumbername": "looks_costumenumbername",
                     "backdropnumbername": "looks_backdropnumbername",
                     "size": "looks_size",
                     "hideallsprites": "looks_hideallsprites",
                     "setstretchto": "looks_setstretchto",
                     "changestretchby": "looks_changestretchby",
                     "costume": "looks_costume",
                     "backdrops": "looks_backdrops"},

           "sound": {"playuntildone": "sound_playuntildone",
                     "play": "sound_play",
                     "stopallsounds": "sound_stopallsounds",
                     "changeeffectby": "sound_changeeffectby",
                     "seteffectto": "sound_seteffectto",
                     "cleareffects": "sound_cleareffects",
                     "changevolumeby": "sound_changevolumeby",
                     "setvolumeto": "sound_setvolumeto",
                     "volume": "sound_volume",
                     "sounds_menu": "sound_sounds_menu"},

           "event": {"whenflagclicked": "event_whenflagclicked",
                     "whenkeypressed": "event_whenkeypressed",
                     "whenthisspriteclicked": "event_whenthisspriteclicked",
                     "whenstageclicked": "event_whenstageclicked",
                     "whenbackdropswitchesto": "event_whenbackdropswitchesto",
                     "whengreaterthan": "event_whengreaterthan",
                     "whenbroadcastreceived": "event_whenbroadcastreceived",
                     "broadcast": "event_broadcast",
                     "broadcastandwait": "event_broadcastandwait",
                     "whentouchingobject": "event_whentouchingobject",
                     "broadcast_menu": "event_broadcast_menu",
                     "touchingobjectmenu": "event_touchingobjectmenu"},

           "control": {"wait": "control_wait",
                       "forever": "control_forever",
                       "if": "control_if",
                       "if_else": "control_if_else",
                       "wait_until": "control_wait_until",
                       "repeat_until": "control_repeat_until",
                       "stop": "control_stop",
                       "start_as_clone": "control_start_as_clone",
                       "create_clone_of": "control_create_clone_of",
                       "delete_this_clone": "control_delete_this_clone",
                       "for_each": "control_for_each",
                       "while": "control_while",
                       "get_counter": "control_get_counter",
                       "incr_counter": "control_incr_counter",
                       "clear_counter": "control_clear_counter",
                       "all_at_once": "control_all_at_once",
                       "create_clone_of_menu": "control_create_clone_of_menu"},

           "sensing": {"touchingobject": "sensing_touchingobject",
                       "touchingcolor": "sensing_touchingcolor",
                       "coloristouchingcolor": "sensing_coloristouchingcolor",
                       "distanceto": "sensing_distanceto",
                       "askandwait": "sensing_askandwait",
                       "answer": "sensing_answer",
                       "keypressed": "sensing_keypressed",
                       "mousedown": "sensing_mousedown",
                       "mousex": "sensing_mousex",
                       "mousey": "sensing_mousey",
                       "setdragmode": "sensing_setdragmode",
                       "loudness": "sensing_loudness",
                       "timer": "sensing_timer",
                       "resettimer": "sensing_resettimer",
                       "of": "sensing_of",
                       "current": "sensing_current",
                       "dayssince2000": "sensing_dayssince2000",
                       "username": "sensing_username",
                       "loud": "sensing_loud",
                       "userid": "sensing_userid",
                       "touchingobjectmenu": "sensing_touchingobjectmenu",
                       "distancetomenu": "sensing_distancetomenu",
                       "keyoptions": "sensing_keyoptions",
                       "of_object_menu": "sensing_of_object_menu"},

           "operator": {"add": "operator_add",
                        "subtract": "operator_subtract",
                        "multiply": "operator_multiply",
                        "divide": "operator_divide",
                        "random": "operator_random",
                        "gt": "operator_gt",
                        "lt": "operator_lt",
                        "equals": "operator_equals",
                        "and": "operator_and",
                        "or": "operator_or",
                        "not": "operator_not",
                        "join": "operator_join",
                        "letter_of": "operator_letter_of",
                        "length": "operator_length",
                        "contains": "operator_contains",
                        "mod": "operator_mod",
                        "round": "operator_round",
                        "mathop": "operator_mathop"},

           "data": {"variable": "data_variable",
                    "setvariableto": "data_setvariableto",
                    "changevariableby": "data_changevariableby",
                    "showvariable": "data_showvariable",
                    "hidevariable": "data_hidevariable",
                    "listcontents": "data_listcontents",
                    "addtolist": "data_addtolist",
                    "deleteoflist": "data_deleteoflist",
                    "deletealloflist": "data_deletealloflist",
                    "insertatlist": "data_insertatlist",
                    "replaceitemoflist": "data_replaceitemoflist",
                    "itemoflist": "data_itemoflist",
                    "itemnumoflist": "data_itemnumoflist",
                    "lengthoflist": "data_lengthoflist",
                    "listcontainsitem": "data_listcontainsitem",
                    "showlist": "data_showlist",
                    "hidelist": "data_hidelist",
                    "listindexall": "data_listindexall",
                    "listindexrandom": "data_listindexrandom"},

           "procedures": {"definition": "procedures_definition",
                          "call": "procedures_call", # MAKE SURE TO ADD SA DEBUG BLOCKS ASW
                          "declaration": "procedures_declaration",
                          "prototype": "procedures_prototype"},

           "argument": {"reporter_string_number": "argument_reporter_string_number",
                        "reporter_boolean": "argument_reporter_boolean",
                        "editor_boolean": "argument_editor_boolean",
                        "editor_string_number": "argument_editor_string_number"},

           "music": {"playDrumForBeats": "music_playDrumForBeats",
                     "restForBeats": "music_restForBeats",
                     "playNoteForBeats": "music_playNoteForBeats",
                     "setInstrument": "music_setInstrument",
                     "setTempo": "music_setTempo",
                     "changeTempo": "music_changeTempo",
                     "getTempo": "music_getTempo",
                     "midiPlayDrumForBeats": "music_midiPlayDrumForBeats",
                     "midiSetInstrument": "music_midiSetInstrument",
                     "menu_DRUM": "music_menu_DRUM",
                     "menu_INSTRUMENT": "music_menu_INSTRUMENT"},

           "pen": {"clear": "pen_clear",
                   "stamp": "pen_stamp",
                   "penDown": "pen_penDown",
                   "penUp": "pen_penUp",
                   "setPenColorToColor": "pen_setPenColorToColor",
                   "changePenColorParamBy": "pen_changePenColorParamBy",
                   "setPenColorParamTo": "pen_setPenColorParamTo",
                   "changePenSizeBy": "pen_changePenSizeBy",
                   "setPenSizeTo": "pen_setPenSizeTo",
                   "setPenHueToNumber": "pen_setPenHueToNumber",
                   "changePenHueBy": "pen_changePenHueBy",
                   "setPenShadeToNumber": "pen_setPenShadeToNumber",
                   "changePenShadeBy": "pen_changePenShadeBy",
                   "menu_colorParam": "pen_menu_colorParam"},

           "videoSensing": {"whenMotionGreaterThan": "videoSensing_whenMotionGreaterThan",
                            "videoOn": "videoSensing_videoOn",
                            "videoToggle": "videoSensing_videoToggle",
                            "setVideoTransparency": "videoSensing_setVideoTransparency",
                            "menu_ATTRIBUTE": "videoSensing_menu_ATTRIBUTE",
                            "menu_SUBJECT": "videoSensing_menu_SUBJECT",
                            "menu_VIDEO_STATE": "videoSensing_menu_VIDEO_STATE"},

           "text2speech": {"speakAndWait": "text2speech_speakAndWait",
                           "setVoice": "text2speech_setVoice",
                           "setLanguage": "text2speech_setLanguage",
                           "menu_voices": "text2speech_menu_voices",
                           "menu_languages": "text2speech_menu_languages"},

           "translate": {"getTranslate": "translate_getTranslate",
                         "getViewerLanguage": "translate_getViewerLanguage",
                         "menu_languages": "translate_menu_languages"},

           "makeymakey": {"whenMakeyKeyPressed": "makeymakey_whenMakeyKeyPressed",
                          "whenCodePressed": "makeymakey_whenCodePressed",
                          "menu_KEY": "makeymakey_menu_KEY",
                          "menu_SEQUENCE": "makeymakey_menu_SEQUENCE"},

           "microbit": {"whenButtonPressed": "microbit_whenButtonPressed",
                        "isButtonPressed": "microbit_isButtonPressed",
                        "whenGesture": "microbit_whenGesture",
                        "displaySymbol": "microbit_displaySymbol",
                        "displayText": "microbit_displayText",
                        "displayClear": "microbit_displayClear",
                        "whenTilted": "microbit_whenTilted",
                        "isTilted": "microbit_isTilted",
                        "getTiltAngle": "microbit_getTiltAngle",
                        "whenPinConnected": "microbit_whenPinConnected",
                        "menu_buttons": "microbit_menu_buttons",
                        "menu_gestures": "microbit_menu_gestures",
                        "menu_tiltDirectionAny": "microbit_menu_tiltDirectionAny",
                        "menu_tiltDirection": "microbit_menu_tiltDirection",
                        "menu_touchPins": "microbit_menu_touchPins",
                        "menu_pinState": "microbit_menu_pinState"},

           "ev3": {"motorTurnClockwise": "ev3_motorTurnClockwise",
                   "motorTurnCounterClockwise": "ev3_motorTurnCounterClockwise",
                   "motorSetPower": "ev3_motorSetPower",
                   "getMotorPosition": "ev3_getMotorPosition",
                   "whenButtonPressed": "ev3_whenButtonPressed",
                   "whenDistanceLessThan": "ev3_whenDistanceLessThan",
                   "whenBrightnessLessThan": "ev3_whenBrightnessLessThan",
                   "buttonPressed": "ev3_buttonPressed",
                   "getDistance": "ev3_getDistance",
                   "getBrightness": "ev3_getBrightness",
                   "beep": "ev3_beep",
                   "menu_motorPorts": "ev3_menu_motorPorts",
                   "menu_sensorPorts": "ev3_menu_sensorPorts"},

           "boost": {"motorOnFor": "boost_motorOnFor",
                     "motorOnForRotation": "boost_motorOnForRotation",
                     "motorOn": "boost_motorOn",
                     "motorOff": "boost_motorOff",
                     "setMotorPower": "boost_setMotorPower",
                     "setMotorDirection": "boost_setMotorDirection",
                     "getMotorPosition": "boost_getMotorPosition",
                     "whenColor": "boost_whenColor",
                     "seeingColor": "boost_seeingColor",
                     "whenTilted": "boost_whenTilted",
                     "getTiltAngle": "boost_getTiltAngle",
                     "setLightHue": "boost_setLightHue",
                     "menu_MOTOR_ID": "boost_menu_MOTOR_ID",
                     "menu_MOTOR_DIRECTION": "boost_menu_MOTOR_DIRECTION",
                     "menu_MOTOR_REPORTER_ID": "boost_menu_MOTOR_REPORTER_ID",
                     "menu_COLOR": "boost_menu_COLOR",
                     "menu_TILT_DIRECTION_ANY": "boost_menu_TILT_DIRECTION_ANY",
                     "menu_TILT_DIRECTION": "boost_menu_TILT_DIRECTION"},

           "wedo2": {"motorOnFor": "wedo2_motorOnFor",
                     "motorOn": "wedo2_motorOn",
                     "motorOff": "wedo2_motorOff",
                     "startMotorPower": "wedo2_startMotorPower",
                     "setMotorDirection": "wedo2_setMotorDirection",
                     "setLightHue": "wedo2_setLightHue",
                     "whenDistance": "wedo2_whenDistance",
                     "whenTilted": "wedo2_whenTilted",
                     "getDistance": "wedo2_getDistance",
                     "isTilted": "wedo2_isTilted",
                     "getTiltAngle": "wedo2_getTiltAngle",
                     "playNoteFor": "wedo2_playNoteFor",
                     "menu_MOTOR_ID": "wedo2_menu_MOTOR_ID",
                     "menu_MOTOR_DIRECTION": "wedo2_menu_MOTOR_DIRECTION",
                     "menu_OP": "wedo2_menu_OP",
                     "menu_TILT_DIRECTION_ANY": "wedo2_menu_TILT_DIRECTION_ANY",
                     "menu_TILT_DIRECTION": "wedo2_menu_TILT_DIRECTION"},

           "gdxfor": {"whenGesture": "gdxfor_whenGesture",
                      "whenForcePushedOrPulled": "gdxfor_whenForcePushedOrPulled",
                      "getForce": "gdxfor_getForce",
                      "whenTilted": "gdxfor_whenTilted",
                      "isTilted": "gdxfor_isTilted",
                      "getTilt": "gdxfor_getTilt",
                      "isFreeFalling": "gdxfor_isFreeFalling",
                      "getSpinSpeed": "gdxfor_getSpinSpeed",
                      "getAcceleration": "gdxfor_getAcceleration",
                      "menu_gestureOptions": "gdxfor_menu_gestureOptions",
                      "menu_pushPullOptions": "gdxfor_menu_pushPullOptions",
                      "menu_tiltAnyOptions": "gdxfor_menu_tiltAnyOptions",
                      "menu_tiltOptions": "gdxfor_menu_tiltOptions",
                      "menu_axisOptions": "gdxfor_menu_axisOptions"},

           "coreExample": {
               "exampleOpcode": "coreExample_exampleOpcode",
               "exampleWithInlineImage": "coreExample_exampleWithInlineImage"
           },

           "": {"note": "note",
                "matrix": "matrix",
                # The red hat block is just what scratch displays when you give it an invalid opcode. And you *CAN*
                # add a comment, but only using JSON hacking, and it will cause the block to become quite buggy. But
                # the comment will be viewable with TurboWarp, but the connection will not be visible. This is  why
                # I added the block as "red_hat_block" so it is more understandable when viewing the JSON.
                "red_hat_block": "red_hat_block"}}

    class Motion:
        MOVESTEPS = "motion_movesteps"
        TURNRIGHT = "motion_turnright"
        TURNLEFT = "motion_turnleft"
        GOTO = "motion_goto"
        GOTOXY = "motion_gotoxy"
        GLIDETO = "motion_glideto"
        GLIDESECSTOXY = "motion_glidesecstoxy"
        POINTINDIRECTION = "motion_pointindirection"
        POINTTOWARDS = "motion_pointtowards"
        CHANGEXBY = "motion_changexby"
        SETX = "motion_setx"
        CHANGEYBY = "motion_changeyby"
        SETY = "motion_sety"
        IFONEDGEBOUNCE = "motion_ifonedgebounce"
        SETROTATIONSTYLE = "motion_setrotationstyle"
        XPOSITION = "motion_xposition"
        YPOSITION = "motion_yposition"
        DIRECTION = "motion_direction"
        SCROLL_RIGHT = "motion_scroll_right"
        SCROLL_UP = "motion_scroll_up"
        ALIGN_SCENE = "motion_align_scene"
        XSCROLL = "motion_xscroll"
        YSCROLL = "motion_yscroll"
        GOTO_MENU = "motion_goto_menu"
        GLIDETO_MENU = "motion_glideto_menu"
        POINTTOWARDS_MENU = "motion_pointtowards_menu"

    class Looks:
        SAYFORSECS = "looks_sayforsecs"
        SAY = "looks_say"
        THINKFORSECS = "looks_thinkforsecs"
        THINK = "looks_think"
        SWITCHCOSTUMETO = "looks_switchcostumeto"
        NEXTCOSTUME = "looks_nextcostume"
        SWITCHBACKDROPTO = "looks_switchbackdropto"
        SWITCHBACKDROPTOANDWAIT = "looks_switchbackdroptoandwait"
        NEXTBACKDROP = "looks_nextbackdrop"
        CHANGESIZEBY = "looks_changesizeby"
        SETSIZETO = "looks_setsizeto"
        CHANGEEFFECTBY = "looks_changeeffectby"
        SETEFFECTTO = "looks_seteffectto"
        CLEARGRAPHICEFFECTS = "looks_cleargraphiceffects"
        SHOW = "looks_show"
        HIDE = "looks_hide"
        GOTOFRONTBACK = "looks_gotofrontback"
        GOFORWARDBACKWARDLAYERS = "looks_goforwardbackwardlayers"
        COSTUMENUMBERNAME = "looks_costumenumbername"
        BACKDROPNUMBERNAME = "looks_backdropnumbername"
        SIZE = "looks_size"
        HIDEALLSPRITES = "looks_hideallsprites"
        SETSTRETCHTO = "looks_setstretchto"
        CHANGESTRETCHBY = "looks_changestretchby"
        COSTUME = "looks_costume"
        BACKDROPS = "looks_backdrops"

    class Sound:
        PLAYUNTILDONE = "sound_playuntildone"
        PLAY = "sound_play"
        STOPALLSOUNDS = "sound_stopallsounds"
        CHANGEEFFECTBY = "sound_changeeffectby"
        SETEFFECTTO = "sound_seteffectto"
        CLEAREFFECTS = "sound_cleareffects"
        CHANGEVOLUMEBY = "sound_changevolumeby"
        SETVOLUMETO = "sound_setvolumeto"
        VOLUME = "sound_volume"
        SOUNDS_MENU = "sound_sounds_menu"

    class Events:
        WHENFLAGCLICKED = "event_whenflagclicked"
        WHENKEYPRESSED = "event_whenkeypressed"
        WHENTHISSPRITECLICKED = "event_whenthisspriteclicked"
        WHENSTAGECLICKED = "event_whenstageclicked"
        WHENBACKDROPSWITCHESTO = "event_whenbackdropswitchesto"
        WHENGREATERTHAN = "event_whengreaterthan"
        WHENBROADCASTRECEIVED = "event_whenbroadcastreceived"
        BROADCAST = "event_broadcast"
        BROADCASTANDWAIT = "event_broadcastandwait"
        WHENTOUCHINGOBJECT = "event_whentouchingobject"
        BROADCAST_MENU = "event_broadcast_menu"
        TOUCHINGOBJECTMENU = "event_touchingobjectmenu"

    class Control:
        WAIT = "control_wait"
        FOREVER = "control_forever"
        IF = "control_if"
        IF_ELSE = "control_if_else"
        WAIT_UNTIL = "control_wait_until"
        REPEAT_UNTIL = "control_repeat_until"
        STOP = "control_stop"
        START_AS_CLONE = "control_start_as_clone"
        CREATE_CLONE_OF = "control_create_clone_of"
        DELETE_THIS_CLONE = "control_delete_this_clone"
        FOR_EACH = "control_for_each"
        WHILE = "control_while"
        GET_COUNTER = "control_get_counter"
        INCR_COUNTER = "control_incr_counter"
        CLEAR_COUNTER = "control_clear_counter"
        ALL_AT_ONCE = "control_all_at_once"
        CREATE_CLONE_OF_MENU = "control_create_clone_of_menu"

    class Sensing:
        TOUCHINGOBJECT = "sensing_touchingobject"
        TOUCHINGCOLOR = "sensing_touchingcolor"
        COLORISTOUCHINGCOLOR = "sensing_coloristouchingcolor"
        DISTANCETO = "sensing_distanceto"
        ASKANDWAIT = "sensing_askandwait"
        ANSWER = "sensing_answer"
        KEYPRESSED = "sensing_keypressed"
        MOUSEDOWN = "sensing_mousedown"
        MOUSEX = "sensing_mousex"
        MOUSEY = "sensing_mousey"
        SETDRAGMODE = "sensing_setdragmode"
        LOUDNESS = "sensing_loudness"
        TIMER = "sensing_timer"
        RESETTIMER = "sensing_resettimer"
        OF = "sensing_of"
        CURRENT = "sensing_current"
        DAYSSINCE2000 = "sensing_dayssince2000"
        USERNAME = "sensing_username"
        LOUD = "sensing_loud"
        USERID = "sensing_userid"
        TOUCHINGOBJECTMENU = "sensing_touchingobjectmenu"
        DISTANCETOMENU = "sensing_distancetomenu"
        KEYOPTIONS = "sensing_keyoptions"
        OF_OBJECT_MENU = "sensing_of_object_menu"

    class Operator:
        ADD = "operator_add"
        SUBTRACT = "operator_subtract"
        MULTIPLY = "operator_multiply"
        DIVIDE = "operator_divide"
        RANDOM = "operator_random"
        GT = "operator_gt"
        LT = "operator_lt"
        EQUALS = "operator_equals"
        AND = "operator_and"
        OR = "operator_or"
        NOT = "operator_not"
        JOIN = "operator_join"
        LETTER_OF = "operator_letter_of"
        LENGTH = "operator_length"
        CONTAINS = "operator_contains"
        MOD = "operator_mod"
        ROUND = "operator_round"
        MATHOP = "operator_mathop"

    class Data:
        VARIABLE = "data_variable"
        SETVARIABLETO = "data_setvariableto"
        CHANGEVARIABLEBY = "data_changevariableby"
        SHOWVARIABLE = "data_showvariable"
        HIDEVARIABLE = "data_hidevariable"
        LISTCONTENTS = "data_listcontents"
        ADDTOLIST = "data_addtolist"
        DELETEOFLIST = "data_deleteoflist"
        DELETEALLOFLIST = "data_deletealloflist"
        INSERTATLIST = "data_insertatlist"
        REPLACEITEMOFLIST = "data_replaceitemoflist"
        ITEMOFLIST = "data_itemoflist"
        ITEMNUMOFLIST = "data_itemnumoflist"
        LENGTHOFLIST = "data_lengthoflist"
        LISTCONTAINSITEM = "data_listcontainsitem"
        SHOWLIST = "data_showlist"
        HIDELIST = "data_hidelist"
        LISTINDEXALL = "data_listindexall"
        LISTINDEXRANDOM = "data_listindexrandom"

    class Procedures:
        DEFINITION = "procedures_definition"
        CALL = "procedures_call"
        DECLARATION = "procedures_declaration"
        PROTOTYPE = "procedures_prototype"

    class Argument:
        REPORTER_STRING_NUMBER = "argument_reporter_string_number"
        REPORTER_BOOLEAN = "argument_reporter_boolean"
        EDITOR_BOOLEAN = "argument_editor_boolean"
        EDITOR_STRING_NUMBER = "argument_editor_string_number"

    class Music:
        PLAYDRUMFORBEATS = "music_playDrumForBeats"
        RESTFORBEATS = "music_restForBeats"
        PLAYNOTEFORBEATS = "music_playNoteForBeats"
        SETINSTRUMENT = "music_setInstrument"
        SETTEMPO = "music_setTempo"
        CHANGETEMPO = "music_changeTempo"
        GETTEMPO = "music_getTempo"
        MIDIPLAYDRUMFORBEATS = "music_midiPlayDrumForBeats"
        MIDISETINSTRUMENT = "music_midiSetInstrument"
        MENU_DRUM = "music_menu_DRUM"
        MENU_INSTRUMENT = "music_menu_INSTRUMENT"

    class Pen:
        CLEAR = "pen_clear"
        STAMP = "pen_stamp"
        PENDOWN = "pen_penDown"
        PENUP = "pen_penUp"
        SETPENCOLORTOCOLOR = "pen_setPenColorToColor"
        CHANGEPENCOLORPARAMBY = "pen_changePenColorParamBy"
        SETPENCOLORPARAMTO = "pen_setPenColorParamTo"
        CHANGEPENSIZEBY = "pen_changePenSizeBy"
        SETPENSIZETO = "pen_setPenSizeTo"
        SETPENHUETONUMBER = "pen_setPenHueToNumber"
        CHANGEPENHUEBY = "pen_changePenHueBy"
        SETPENSHADETONUMBER = "pen_setPenShadeToNumber"
        CHANGEPENSHADEBY = "pen_changePenShadeBy"
        MENU_COLORPARAM = "pen_menu_colorParam"

    class VideoSensing:
        WHENMOTIONGREATERTHAN = "videoSensing_whenMotionGreaterThan"
        VIDEOON = "videoSensing_videoOn"
        VIDEOTOGGLE = "videoSensing_videoToggle"
        SETVIDEOTRANSPARENCY = "videoSensing_setVideoTransparency"
        MENU_ATTRIBUTE = "videoSensing_menu_ATTRIBUTE"
        MENU_SUBJECT = "videoSensing_menu_SUBJECT"
        MENU_VIDEO_STATE = "videoSensing_menu_VIDEO_STATE"

    class Text2Speech:
        SPEAKANDWAIT = "text2speech_speakAndWait"
        SETVOICE = "text2speech_setVoice"
        SETLANGUAGE = "text2speech_setLanguage"
        MENU_VOICES = "text2speech_menu_voices"
        MENU_LANGUAGES = "text2speech_menu_languages"

    class Translate:
        GETTRANSLATE = "translate_getTranslate"
        GETVIEWERLANGUAGE = "translate_getViewerLanguage"
        MENU_LANGUAGES = "translate_menu_languages"

    class MakeyMakey:
        WHENMAKEYKEYPRESSED = "makeymakey_whenMakeyKeyPressed"
        WHENCODEPRESSED = "makeymakey_whenCodePressed"
        MENU_KEY = "makeymakey_menu_KEY"
        MENU_SEQUENCE = "makeymakey_menu_SEQUENCE"

    class Microbit:
        WHENBUTTONPRESSED = "microbit_whenButtonPressed"
        ISBUTTONPRESSED = "microbit_isButtonPressed"
        WHENGESTURE = "microbit_whenGesture"
        DISPLAYSYMBOL = "microbit_displaySymbol"
        DISPLAYTEXT = "microbit_displayText"
        DISPLAYCLEAR = "microbit_displayClear"
        WHENTILTED = "microbit_whenTilted"
        ISTILTED = "microbit_isTilted"
        GETTILTANGLE = "microbit_getTiltAngle"
        WHENPINCONNECTED = "microbit_whenPinConnected"
        MENU_BUTTONS = "microbit_menu_buttons"
        MENU_GESTURES = "microbit_menu_gestures"
        MENU_TILTDIRECTIONANY = "microbit_menu_tiltDirectionAny"
        MENU_TILTDIRECTION = "microbit_menu_tiltDirection"
        MENU_TOUCHPINS = "microbit_menu_touchPins"
        MENU_PINSTATE = "microbit_menu_pinState"

    class Ev3:
        MOTORTURNCLOCKWISE = "ev3_motorTurnClockwise"
        MOTORTURNCOUNTERCLOCKWISE = "ev3_motorTurnCounterClockwise"
        MOTORSETPOWER = "ev3_motorSetPower"
        GETMOTORPOSITION = "ev3_getMotorPosition"
        WHENBUTTONPRESSED = "ev3_whenButtonPressed"
        WHENDISTANCELESSTHAN = "ev3_whenDistanceLessThan"
        WHENBRIGHTNESSLESSTHAN = "ev3_whenBrightnessLessThan"
        BUTTONPRESSED = "ev3_buttonPressed"
        GETDISTANCE = "ev3_getDistance"
        GETBRIGHTNESS = "ev3_getBrightness"
        BEEP = "ev3_beep"
        MENU_MOTORPORTS = "ev3_menu_motorPorts"
        MENU_SENSORPORTS = "ev3_menu_sensorPorts"

    class Boost:
        MOTORONFOR = "boost_motorOnFor"
        MOTORONFORROTATION = "boost_motorOnForRotation"
        MOTORON = "boost_motorOn"
        MOTOROFF = "boost_motorOff"
        SETMOTORPOWER = "boost_setMotorPower"
        SETMOTORDIRECTION = "boost_setMotorDirection"
        GETMOTORPOSITION = "boost_getMotorPosition"
        WHENCOLOR = "boost_whenColor"
        SEEINGCOLOR = "boost_seeingColor"
        WHENTILTED = "boost_whenTilted"
        GETTILTANGLE = "boost_getTiltAngle"
        SETLIGHTHUE = "boost_setLightHue"
        MENU_MOTOR_ID = "boost_menu_MOTOR_ID"
        MENU_MOTOR_DIRECTION = "boost_menu_MOTOR_DIRECTION"
        MENU_MOTOR_REPORTER_ID = "boost_menu_MOTOR_REPORTER_ID"
        MENU_COLOR = "boost_menu_COLOR"
        MENU_TILT_DIRECTION_ANY = "boost_menu_TILT_DIRECTION_ANY"
        MENU_TILT_DIRECTION = "boost_menu_TILT_DIRECTION"

    class Wedo2:
        MOTORONFOR = "wedo2_motorOnFor"
        MOTORON = "wedo2_motorOn"
        MOTOROFF = "wedo2_motorOff"
        STARTMOTORPOWER = "wedo2_startMotorPower"
        SETMOTORDIRECTION = "wedo2_setMotorDirection"
        SETLIGHTHUE = "wedo2_setLightHue"
        WHENDISTANCE = "wedo2_whenDistance"
        WHENTILTED = "wedo2_whenTilted"
        GETDISTANCE = "wedo2_getDistance"
        ISTILTED = "wedo2_isTilted"
        GETTILTANGLE = "wedo2_getTiltAngle"
        PLAYNOTEFOR = "wedo2_playNoteFor"
        MENU_MOTOR_ID = "wedo2_menu_MOTOR_ID"
        MENU_MOTOR_DIRECTION = "wedo2_menu_MOTOR_DIRECTION"
        MENU_OP = "wedo2_menu_OP"
        MENU_TILT_DIRECTION_ANY = "wedo2_menu_TILT_DIRECTION_ANY"
        MENU_TILT_DIRECTION = "wedo2_menu_TILT_DIRECTION"

    class Gdxfor:
        WHENGESTURE = "gdxfor_whenGesture"
        WHENFORCEPUSHEDORPULLED = "gdxfor_whenForcePushedOrPulled"
        GETFORCE = "gdxfor_getForce"
        WHENTILTED = "gdxfor_whenTilted"
        ISTILTED = "gdxfor_isTilted"
        GETTILT = "gdxfor_getTilt"
        ISFREEFALLING = "gdxfor_isFreeFalling"
        GETSPINSPEED = "gdxfor_getSpinSpeed"
        GETACCELERATION = "gdxfor_getAcceleration"
        MENU_GESTUREOPTIONS = "gdxfor_menu_gestureOptions"
        MENU_PUSHPULLOPTIONS = "gdxfor_menu_pushPullOptions"
        MENU_TILTANYOPTIONS = "gdxfor_menu_tiltAnyOptions"
        MENU_TILTOPTIONS = "gdxfor_menu_tiltOptions"
        MENU_AXISOPTIONS = "gdxfor_menu_axisOptions"

    class Debug:
        """Proccodes for debug blocks."""
        BREAKPOINT = "​​breakpoint​​"
        LOG = "​​log​​ %s"
        WARN = "​​warn​​ %s"
        ERROR = "​​error​​ %s"

    class Other:
        NOTE = "note"
        MATRIX = "matrix"
        RED_HAT_BLOCK = "red_hat_block"

        @staticmethod
        def NUMBER(value: int | float) -> list:
            return [4, value]

        @staticmethod
        def POSITIVE_NUMBER(value: int | float) -> list:
            return [5, value]

        @staticmethod
        def POSITIVE_INTEGER(value: int) -> list:
            return [6, value]

        @staticmethod
        def INTEGER(value: int) -> list:
            return [7, value]

        @staticmethod
        def ANGLE(value: int | float) -> list:
            return [8, value]

        @staticmethod
        def COLOR(hex_code: str) -> list[int, str]:
            """
            Color block/input
            :param hex_code: Hex code of color: must be a "#" followed by the hexadecimal numeral representing the color
            :return: JSON value of color block/input
            """
            return [9, hex_code]

        @staticmethod
        def STRING(value: str) -> list[int, str]:
            return [10, value]

        @staticmethod
        def BROADCAST(name: str, broadcast_id: str) -> [int, str, str]:
            return [11, name, broadcast_id]

        @staticmethod
        def VARIABLE(name: str, var_id: str, *, x: int = None, y: int = None):
            if x is None or y is None:
                return [12, name, var_id]
            return [12, name, var_id, x, y]

        @staticmethod
        def LIST(name: str, list_id: str, *, x: int = None, y: int = None):
            if x is None or y is None:
                return [13, name, list_id]
            return [13, name, list_id, x, y]


class RotationStyles:
    ALL_AROUND = "all around"
    LEFT_RIGHT = "left-right"
    DONT_ROTATE = "don't rotate"


class VideoStates:
    ON = "on"
    OFF = "off"
    ON_FLIPPED = "on-flipped"
