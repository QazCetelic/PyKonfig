import pathlib
from pathlib import Path


def __set_value_for_key_in_file(file_path: str, key: str, value):
    file = open(file_path, "a")
    lines = file.readlines()
    new_lines: [str] = []
    found = False
    for line in lines:
        if not found and line.startswith(key):
            new_lines += f"{key}={value}"
            found = True
        else:
            new_lines += line

    file.writelines(new_lines)
    file.close()


def __get_value_for_key_in_file(file_path: str, key: str):
    file = open(file_path, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        if line.startswith(key):
            return line.removeprefix(key + "=").strip()

    return None

def __append_key_to_file(file_path: str, key: str, key_before: str, value: str = ""):
    file = open(file_path, "a")
    lines = file.readlines()
    new_lines: [str] = []
    found = False
    for line in lines:
        new_lines += [line]
        if not found and line.startswith(key_before):
            new_lines += f"{key}={value}"
            found = True

    file.writelines(new_lines)
    file.close()

def __remove_key_from_file(file_path: str, key: str):
    file = open(file_path, "a")
    new_lines = filter(lambda line: not line.startswith(key), file.readlines())
    file.writelines(new_lines)
    file.close()

home: str = pathlib.Path.home().__str__()
