# this module created for file system operations

import os
import ctypes

from enums.defaults import Defaults
from enums.fs_enums import AccessTypes
from utils.log_utils import create_new_logger_instance
logger = create_new_logger_instance()

def WriteOk(path: str) -> bool:
    """
    it's checks file or directory can readable
    :param path:
    :return:
    """
    access_type = AccessTypes.ACCESS_FILE if os.path.isfile(path) else AccessTypes.ACCESS_DIR
    access_mode = AccessTypes.ACCESS_FILE_WRITE
    handle = ctypes.windll.kernel32.CreateFileW(
        path, access_mode, 0, None, 3, access_type, None
    )
    if handle == -1:
        return False
    ctypes.windll.kernel32.CloseHandle(handle)
    return True


def ReadOk(path: str) -> bool:
    """
    it's checks file or directory can readable
    :param path:
    :return:
    """
    access_type = AccessTypes.ACCESS_FILE if os.path.isfile(path) else AccessTypes.ACCESS_DIR
    access_mode = AccessTypes.ACCESS_FILE_READ
    handle = ctypes.windll.kernel32.CreateFileW(
        path, access_mode.value, 0, None, 3, access_type.value, None
    )
    if handle == -1:
        return False
    ctypes.windll.kernel32.CloseHandle(handle)
    return True

def create_file(filename: str,throw_exc = False,force = False) -> bool:
    """
    creates a file that doesn't exist, the force parameter forces it to be recreated if it exists
    if you want to throw an error, you must set the throw_exc parameter to true

    :param filename:
    :param throw_exc:
    :return:
    """
    if os.path.exists(filename) and not force:
        return True
    try:
        with open(filename,"w"):
            pass
    except Exception as error:
        if throw_exc:
            raise Exception(error)
        logger.critical("Cannot Create file: %s - %s" % (filename,error))
        return False

def create_directory(directory_name: str,throw_exc = False,force = False) -> bool:
    """
    creates a folder that doesn't exist
    if you want to throw an error, you must set the throw_exc parameter to true
    """
    try:
        os.makedirs(directory_name)
    except Exception as error:
        if throw_exc:
            raise Exception(error)
        logger.critical("Cannot create directory: %s - %s" % (directory_name,error))
        return False
    return True

def copyfile2dst(source: str,dest: str,force = False,throw_exc = False) -> bool:
    """
    copies a file to destination  the force parameter forces it to be recreated if it exists
    :param source:
    :param dest:
    :return:
    """
    if os.path.exists(dest) and not force:
        return True
    try:
        with open(source,"rb") as src:
            with open(dest,"wb") as dst:
                dst.write(src.read())
    except Exception as copy_error:
        if throw_exc:
            raise Exception(copy_error)
        logger.critical("Cannot copy %s to %s (%s)" % (source,dest,copy_error))
        return False
    return True
