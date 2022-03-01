import pathlib
from pathlib import Path

__home: str = pathlib.Path.home().__str__()
__kcminputrc_path = f"{__home}/.config/kcminputrc"
__kxkbrc_path = f"{__home}/.config/kxkbrc"
__kdeglobals_path = f"{__home}/.config/kdeglobals"
__plasma_user_feedback_path = f"{__home}/.config/PlasmaUserFeedback"
__kgammarc_path = f"{__home}/.config/kgammarc"

def __set_value_for_key_in_file(file_path: str, key: str, value):
    file = open(file_path, "a")
    lines = file.readlines()
    new_lines: [str] = []
    found = False
    for line in lines:
        if not found and line.startswith(key):
            # Make boolean values lowercase
            if isinstance(value, bool):
                value = str(value).lower()

            new_lines += f"{key}={value}"
            found = True
        else:
            new_lines += line

    file.write('\n'.join(new_lines))
    file.close()


def __get_value_for_key_in_file(file_path: str, key: str):
    file = open(file_path, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        if line.startswith(key):
            return line.removeprefix(key + "=").strip()

    return None

def __append_key_after_key(file_path: str, key: str, key_before: str, value: str = ""):
    file = open(file_path, "a")
    lines = file.readlines()
    new_lines: [str] = []
    found = False
    for line in lines:
        new_lines += [line]
        if not found and line.startswith(key_before):
            new_lines += f"{key}={value}"
            found = True

    file.write('\n'.join(new_lines))
    file.close()

def __append_key_to_group(file_path: str, group: str, key: str, value: str = ""):
    file = open(file_path, "a")
    lines = file.readlines()
    new_lines: [str] = []
    found = False
    for line in lines:
        new_lines.append(line)
        if not found and line == f"[{group}]":
            new_lines.append(f"{key}={value}")
            found = True

    file.write('\n'.join(new_lines))
    file.close()

def __remove_key_from_file(file_path: str, key: str):
    file = open(file_path, "a")
    new_lines = filter(lambda line: not line.startswith(key), file.readlines())
    file.write('\n'.join(new_lines))
    file.close()
