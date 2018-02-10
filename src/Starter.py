from CustomLogger.LoggerWrapper import CLoggerWrapper ;


objCustomLogger = CLoggerWrapper("Testlog.txt",CLoggerWrapper.LOG_INFO,False)


def main():

    a=5
    objCustomLogger.print_log(CLoggerWrapper.LOG_INFO,"Hello World A %d b %d c %s ",a,6,"QBB")

if __name__ == "__main__":

    main();