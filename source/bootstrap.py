# splash screen bootstrap

import hashlib
import os

from source.Qthread import Signals
from source.Qthread import ThreadWorker
from source.Qthread import CreateNewThread

from utils.reg_utils import HKEY
from utils.reg_utils import Registry
from utils.reg_utils import REGTYPES
from utils.log_utils import create_new_logger_instance

from enums.defaults import Defaults
logger = create_new_logger_instance()
class BootStrapModule:
    def __init__(self):
        self.thread = CreateNewThread()
        self.signal = Signals()
        self.worker = ThreadWorker(self)
        self.hash_table = {
            "auto_test.py":[
                    hashlib.sha256(os.urandom(32)),
                    b'\x10XE4\t4[\x86|\x14\x93\xe9\x9b\xef\x06N1\x893Yw\xa7\r\x89\xce\x1d\xa2t\xdd(V\xb2'
                ],
            "auto_initialize.py":[
                hashlib.sha256(os.urandom(32)),
                b'z\xf3\xea\x81\xbf\xcfH\xbe\xf6>\xea\x1d\x08\x84\xd7Y\x04F\xb9\x87\x87v\xb6\x88\x08\x99\xab\x1d\x98\xb9\x96\xea',
                ],
            "pwd.py":[
                hashlib.sha256(os.urandom(32)),
                b'\x0ex\xe1@\x7fK\x8dE(\xf0\x8dZg\x0b\x95$\xcfk\xad\xf4l\x1cN%\xed\xcb\x9d\xf8\x90\x8b\x11\xef'
                ],
            "asena_cli.py":[
                hashlib.sha256(os.urandom(32)),
                b'\xe8\xa8\xb3\xa6\x0e\x08\x80Z\xfe7\xea\xc6U\xd9vwU\xb2\xed\x04j\xe8\xf3\x05\n\xc4\x81\xd4\x02\xd9\xf1\x15'
                ],
            "resources.rpk":
                [
                    hashlib.sha256(os.urandom(32)),
                    b'\x15s\x17\x99\x85r\xce\xf2\x9dO\xc6>\x91[P\x93#[\xd1\x97\x86\xdd\n\xf1\xd0\xeb\nT\xd3\x80\xadI'
            ]
        }
        self.registry = Registry(HKEY.HKEY_CURRENT_USER,Defaults.DEFAULT_REGISTRY_PATH)
    def start(self):
        """
        Thread worker sınıfı bu fonksiyonu çağıracak
        :return:
        """
    def compare_file_hash(self):
        logger.info(" Comparing File Hashes ")
        for filename,filehash in self.hash_table.items():
            current_hash = filehash[0]
            original_hash = self.registry.read_key(os.path.splitext(filename)[0])[0]
            if current_hash != original_hash:
                logger.warning("Bad file hash: %s Original Hash: %s Current Hash: %s" % (filename,original_hash,current_hash))
    def write_file_hashes_to_registry(self):
        logger.info(" Creating File Hashes ")
        for filename,filehash in self.hash_table.items():
            current_hash = filehash[0]
            original_hash = filehash[1]
            self.registry.write_key(os.path.splitext(filename)[0],original_hash)