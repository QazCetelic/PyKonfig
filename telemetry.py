import enum
from util import __set_value_for_key_in_file, __get_value_for_key_in_file, __home, __plasma_user_feedback_path


# Set the behaviour for the numlock state on plasma startup
class FEEDBACK_LEVEL(enum.Enum):
    DISABLED = 0
    BASIC_SYSTEM_INFORMATION = 16
    BASIC_SYSTEM_INFORMATION_AND_USAGE_STATISTICS = 32
    DETAILED_SYSTEM_INFORMATION_AND_BASIC_USAGE_STATISTICS = 48
    DETAILED_SYSTEM_INFORMATION_AND_BASIC_STATISTICS = 64
def set_feedback_level(numlock_startup: FEEDBACK_LEVEL):
    __set_value_for_key_in_file(__plasma_user_feedback_path, "FeedbackLevel", numlock_startup.value)
def get_feedback_level() -> FEEDBACK_LEVEL:
    return FEEDBACK_LEVEL(int(__get_value_for_key_in_file(__plasma_user_feedback_path, "FeedbackLevel")))

get_feedback_level.__doc__ = "Returns enum e.g. BASIC_SYSTEM_INFORMATION"
