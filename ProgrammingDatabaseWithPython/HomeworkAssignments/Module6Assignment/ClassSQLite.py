#TEST_QUERY CAN BE USED TO GET ALL TABLES IN DATABASE
#test_query = """SELECT name
#                FROM sqlite_master
#                WHERE type='table';""""

import sqlite3
import logging
import os

class ClassSQLite:

    def __init__(self, filename, db_title):
        """SETS LOGGING CONFIGURATION AND CHECKS FOR FILEPATH

        Args:
            filename (STRING): DB TO CONNECT
            db_title (STRING): DB TITLE FOR LOGGING
        """

        self.filename = filename
        self.db_title = db_title

        logging.basicConfig(level=logging.DEBUG,format=f"[{db_title}]: %(asctime)s: %(levelname)s: %(message)s")
        logging.getLogger('matplotlib.font_manager').disabled = True

        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            logging.debug(f"{filename} found and not zero size.")
        else:
            logging.error(f"{filename} not found or zero size.")

    def db_checkfile(self):
        """CHECKS DATABASE EXISTS

        Returns:
            BOOLEAN DEPENDING ON IF DATABASE EXISTS
        """

        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            logging.debug(f"{self.filename} found and not zero size.")
            return True
        else:
            logging.error(f"{self.filename} not found or zero size.")
            return False

    def db_connect(self):
        """CONNECTS TO DATABASE

        Returns:
            CONNECTION OBJECT: CONNECTION TO THE DATABASE
        """

        con = sqlite3.connect(self.filename)
        logging.debug("Successfully Connected to Database...")
        self.con = con
        return con

    def db_cursor(self):
        """SETS THE CURSOR OBJECT

        Returns:
            CURSOR OBJECT: CURSOR OBJECT ON WHICH SQL QUERIES CAN BE EXECUTED
        """

        cur = self.con.cursor()
        self.cur = cur
        logging.debug("Cursor has been set.")
        return cur

    def db_runquery(self, query):
        """RUN A QUERY

        Args:
            cur (CURSOR OBJECT): THE CURSOR OBJECT ON WHICH SQL QUERIES CAN BE EXECUTED
            query (STRING): SQL QUERY TO EXECUTE

        Returns:
            LIST: RESULTS FROM THE QUERY
        """

        self.cur.execute(query)
        result = self.cur.fetchall()
        logging.debug("Successfully executed and returned query.")
        return result

    def db_close(self):
        if self.con:
            self.con.close()
            print()
            logging.debug("Database has been closed...")