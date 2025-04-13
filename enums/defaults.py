import os
import time
class Defaults:
    DEFAULT_SETUP_PATH = os.path.join(
        os.getenv("LocalAppData"),
        "Asena"
    )
    DEFAULT_CRASH_STR = "Hata oluştu, :/ Hata raporu paketlenecek eğer sizinde ricanız olursa ekran kayıt bilgileride bu rapora dahil olucak ekran kayıtlarının dahil edilmesini istiyor musunuz ? "
    DEFAULT_MAX_WINDOW_SIZE = 16777215
    DEFAULT_TIME_FORMAT = "%d_%m_%y"
    DEFAULT_LOG_FILENAME = "asena_%s.log" % (time.strftime(DEFAULT_TIME_FORMAT))
    DEFAULT_LOG_DIR_PATH = os.path.join(os.getenv("LocalAppData"),"Asena_Logs")
    DEFAULT_LOG_FILE_PATH = os.path.join(DEFAULT_LOG_DIR_PATH,DEFAULT_LOG_FILENAME)
    DEFAULT_REGISTRY_PERSISTANCE_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"
    DEFAULT_REGISTRY_PATH = r"Software\Asena"