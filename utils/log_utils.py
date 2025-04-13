import os
import logging
from enums.defaults import Defaults
from zipfile import ZipFile

from source.build import create_credential_str
def create_new_logger_instance(module_name = __name__,filename = None) -> logging.Logger:

    """
    Creates a logger instance
    filename and module name automatically setted
    but if you wish you can change
    Default Path : %LocalAppData%/Asena_Logs
    :param module_name: default value: __name__
    :param filename:
    :return:
    """
    if filename is None:
        if not os.path.exists(Defaults.DEFAULT_LOG_DIR_PATH):
            os.makedirs(Defaults.DEFAULT_LOG_DIR_PATH)
        filename = Defaults.DEFAULT_LOG_FILE_PATH
    logging.basicConfig(level = logging.NOTSET)
    log = logging.getLogger(module_name)
    if not log.handlers:
        filepath = filename
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        file_handler = logging.FileHandler(filename, encoding="utf-8",mode="a+")
        file_handler.setFormatter(log_format)
        file_handler.setLevel(logging.NOTSET) # LOG ALL LEVELS
        log.addHandler(file_handler)
    return log
logger = create_new_logger_instance()
def pack_log_files(zip_path: str,*zip_files) -> bool:
    credential_str = create_credential_str()
    try:
        with ZipFile(zip_path,mode = "w") as zip:

            for zip_file in zip_files[:]:
                dirname_of_zip_file = os.path.dirname(zip_file)
                if dirname_of_zip_file != "":
                    os.chdir(dirname_of_zip_file)
                zip.write(os.path.basename(zip_file))
            zip.writestr("version_credentials.txt",credential_str)
        logger.info("Succesfully packed log files !")
    except Exception as e:
        logger.warning("Cannot pack ! log files : %s" % (e))
        return False
    return True
