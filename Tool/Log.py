class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Debug:

    @staticmethod
    def log(args):
        txt_log = f"{bcolors.OKGREEN} [INFO]\t{args}"
        print(txt_log)

    @staticmethod
    def warning(args):
        txt_log = f"{bcolors.WARNING} [WARNING]\t{args}"
        print(txt_log)

    @staticmethod
    def error(args):
        txt_log = f"{bcolors.FAIL} [ERROR]\t{args}"
        print(txt_log)