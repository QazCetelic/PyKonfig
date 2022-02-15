import enum
from util import __set_value_for_key_in_file, __get_value_for_key_in_file, home

plasma_user_feedback_path = f"{home}/.config/PlasmaUserFeedback"

# Set the behaviour for the numlock state on plasma startup
class FEEDBACK_LEVEL(enum.Enum):
    DISABLED = 0
    BASIC_SYSTEM_INFORMATION = 16
    BASIC_SYSTEM_INFORMATION_AND_USAGE_STATISTICS = 32
    DETAILED_SYSTEM_INFORMATION_AND_BASIC_USAGE_STATISTICS = 48
    DETAILED_SYSTEM_INFORMATION_AND_BASIC_STATISTICS = 64
def set_feedback_level(numlock_startup: FEEDBACK_LEVEL):
    __set_value_for_key_in_file(plasma_user_feedback_path, "FeedbackLevel", numlock_startup.value)
def get_feedback_level() -> FEEDBACK_LEVEL:
    return FEEDBACK_LEVEL(int(__get_value_for_key_in_file(plasma_user_feedback_path, "FeedbackLevel")))
