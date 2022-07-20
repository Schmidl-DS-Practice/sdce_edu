import sqlite3
import logging
import os
#logging.critical()
#logging.error()
#logging.warning())
#logging.info()
#logging.debug()

# LOG LEVELS ARE LABELS YOU ADD TO YOUR LOG ENTRIES
# DISPLAY TO CONSOLE: Level=logging.DEBUG
# PRINT TO A FILE: filename='test.log'
# ADD TIMESTAMP: format='' (asctime: time; levelname: keep DEBUG level name; message: keep string message print)
# LEVEL: logging.CRITICAL; logging.ERROR; logging.WARNING; logging.INFO; logging.DEBUG
logging.basicConfig(level=logging.DEBUG,format="[Artists]:%(asctime)s:%(levelname)s:%(message)s")

# Track and Analyze Key Activities
def db_checkfile(dbfile):
    if os.path.exists(dbfile) and os.path.getsize(dbfile) > 0:
        # logging.debug (method of logging module. can pass same string that would be in print statement)
        # logger1 = logging.getLogger("module_1")
        # logger1.debug("Module 1 debugger")
        # OUTPUT: DEBUG:module_1:Module 1 debugger
        logging.debug("{a} found and not zero size".format(a=dbfile))
    else:
        logging.error("{a} not found or zero size".format(a=dbfile))

def db_connect(dbfile):
    con = sqlite3.connect(dbfile)
    logging.debug("DB Connected".format())
    return con


def main():

    dbfile = 'movies_test.db'
    db_checkfile(dbfile)
    con = db_connect(dbfile)
    if con:
        con.close()
        logging.debug('DB Closed')


if __name__ == '__main__':
    main()