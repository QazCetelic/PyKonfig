import enum
from util import __set_value_for_key_in_file, __get_value_for_key_in_file, home, __append_key_to_file, \
    __remove_key_from_file

kcminputrc_path = f"{home}/.config/kcminputrc"
kxkbrc_path = f"{home}/.config/kxkbrc"

# Set the behaviour for the numlock state on plasma startup
class NUMLOCK_STARTUP(enum.Enum):
    TURN_ON = 0
    TURN_OFF = 1
    LEAVE_UNCHANGED = 2
def set_numlock_on_startup(numlock_startup: NUMLOCK_STARTUP):
    __set_value_for_key_in_file(kcminputrc_path, "NumLock", numlock_startup.value)
def get_numlock_on_startup() -> NUMLOCK_STARTUP:
    return NUMLOCK_STARTUP(int(__get_value_for_key_in_file(kcminputrc_path, "NumLock")))

# Set the behaviour for holding down the key
class HOLD_KEY(enum.Enum):
    REPEAT_THE_KEY = "repeat"
    DO_NOTHING = "nothing"
def set_hold_key(hold_key: HOLD_KEY):
    __set_value_for_key_in_file(kcminputrc_path, "KeyRepeat", hold_key.value)
def get_hold_key() -> HOLD_KEY:
    return LAYOUT_SWITCHING_POLICY(int(__get_value_for_key_in_file(kcminputrc_path, "KeyRepeat")))

# Set the delay for repeating a key
def set_repeat_delay(repeat_delay: int):
    __set_value_for_key_in_file(kcminputrc_path, "RepeatDelay", repeat_delay)
def get_repeat_delay() -> int:
    return __get_value_for_key_in_file(kcminputrc_path, "RepeatDelay")

# Set the rare for repeating a key
def set_repeat_rate(repeat_rate: int):
    __set_value_for_key_in_file(kcminputrc_path, "RepeatRate", repeat_rate)
def get_repeat_rate() -> int:
    return __get_value_for_key_in_file(kcminputrc_path, "RepeatRate")

# Set natural scroll
def set_natural_scroll(natural_scroll: bool):
    __set_value_for_key_in_file(kcminputrc_path, "NaturalScroll", natural_scroll)
def get_natural_scroll() -> bool:
    return __get_value_for_key_in_file(kcminputrc_path, "NaturalScroll")

# Set tap to click
def set_tap_to_click(tap_to_click: bool):
    __set_value_for_key_in_file(kcminputrc_path, "TapToClick", tap_to_click)
def get_tap_to_click() -> bool:
    return __get_value_for_key_in_file(kcminputrc_path, "TapToClick")

# Set the policy for switching keyboard layouts
class LAYOUT_SWITCHING_POLICY(enum.Enum):
    GLOBAL = "Global"
    DESKTOP = "Desktop"
    APPLICATION = "Application"
    WINDOW = "Window"
def set_layout_switching_policy(layout_switching_policy: LAYOUT_SWITCHING_POLICY):
    __set_value_for_key_in_file(kxkbrc_path, "SwitchMode", layout_switching_policy.value)
def get_layout_switching_policy() -> LAYOUT_SWITCHING_POLICY:
    return LAYOUT_SWITCHING_POLICY(__get_value_for_key_in_file(kxkbrc_path, "SwitchMode"))

def enable_keyboard_options():
    __append_key_to_file(kxkbrc_path, "Options", "Model")

def disable_keyboard_options():
    __remove_key_from_file(kxkbrc_path, "Options")

# Sets the advanced layout options such as the position of the compose key
def set_keyboard_options(options: {str: [str]}) -> None:
    option_string = ""
    # Goes through the various options
    for option in options.items():
        # Goes through each key assigned for the option
        for key in option[1]:
            option_string += f"{option}:{option[1]},"
    __set_value_for_key_in_file(kxkbrc_path, "Options", option_string.removesuffix(","))
def get_keyboard_options() -> {str: [str]}:
    option_string = __get_value_for_key_in_file(kxkbrc_path, "Options")
    # In case the config key is removed because it's disabled
    if option_string is None:
        return {}
    options: {str: [str]} = {}

    option_string_parts = option_string.split(",")
    # In case there are no options
    if option_string_parts == ['']:
        return {}
    # "compose:menu,compose:prsc" -> ["compose:menu", "compose:prsc"]
    for option in option_string_parts:
        # "compose:menu" -> ["compose", "menu"]
        # The first part of the tuple is the option name and the second is the name of the key that is assigned to it
        # e.g: ("compose", "menu")
        (option, key) = option.split(":")

        # Add key to the list of keys for the option
        if option not in options:
            options[option] = []
        options[option].append(key)

    return options

get_keyboard_options.__doc__ = "Returns a dict with options and the keys assigned to them e.g. {'compose': ['menu']}"

# Sets the list of various layouts types and variants
def set_layout_list(layout_list: [(str, str)]):
    type_list_string = ""
    variant_list_string = ""
    for layout in layout_list:
        type_list_string += f"{layout[0]},"
        variant_list_string += f"{layout[1]},"

    type_list_string = type_list_string.removesuffix(",")
    variant_list_string = variant_list_string.removesuffix(",")

    __set_value_for_key_in_file(kxkbrc_path, "LayoutList", type_list_string)
    __set_value_for_key_in_file(kxkbrc_path, "VariantList", variant_list_string)

def get_layout_list() -> [(str, str)]:
    type_list = __get_value_for_key_in_file(kxkbrc_path, "LayoutList").split(",")
    variant_list = __get_value_for_key_in_file(kxkbrc_path, "VariantList").split(",")
    layout_list: [(str, str)] = []
    if len(type_list) == len(variant_list):
        for i in range(len(type_list)):
            layout_list.append((type_list[i], variant_list[i]))
    else:
        raise Exception("The number of layout types and variants must be the same, the configs are not valid")
    return layout_list

get_layout_list.__doc__ = "Returns a list of all layouts; consisting of a layout type e.g. 'us' and type e.g. 'euro'"

def get_keyboard_model() -> str:
    return __get_value_for_key_in_file(kxkbrc_path, "Model")
def set_keyboard_model(model: str):
    __set_value_for_key_in_file(kxkbrc_path, "Model", model)