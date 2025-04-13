from enum import IntEnum

class AccessTypes(IntEnum):
    ACCESS_FILE_READ = 0x80000000
    ACCESS_FILE_WRITE = 0x40000000

    ACCESS_DIR = 0x02000000
    ACCESS_FILE = 0x80
