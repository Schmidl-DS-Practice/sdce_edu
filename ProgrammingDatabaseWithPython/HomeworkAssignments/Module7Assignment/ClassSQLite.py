#TEST_QUERY CAN BE USED TO GET ALL TABLES IN DATABASE
#test_query = """SELECT name
#                FROM sqlite_master
#                WHERE type='table';""""

import sqlite3
import logging
import os

class EsQuLite:

    def __init__(self, filename, db_title):
        """SETS LOGGING CONFIGURATION AND CHECKS FOR FILEPATH

        Args:
            filename (STRING): DB TO CONNECT
            db_title (STRING): DB TITLE FOR LOGGING
        """

        self.filename = filename
        self.db_title = db_title

        logging.basicConfig(level=logging.DEBUG,format=f"[{db_title}]: %(asctime)s: %(levelname)s: %(message)s")

        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            logging.debug(f"{filename} found and not zero size.")
        else:
            logging.error(f"{filename} not found or zero size.")

    def db_connect(self):
        """CONNECTS TO DATABASE

        Args:
            filename (STRING): .SQLITE OR .DB FILE

        Returns:
            CONNECTION OBJECT: CONNECTION TO THE DATABASE
        """

        con = sqlite3.connect(self.filename, check_same_thread=False)
        logging.debug("Successfully Connected to Database...")
        self.con = con
        return con

    def db_cursor(self, con):
        """SETS THE CURSOR OBJECT

        Args:
            con (OBJECT): CONNECTION TO THE DATABASE

        Returns:
            CURSOR OBJECT: CURSOR OBJECT ON WHICH SQL QUERIES CAN BE EXECUTED
        """

        cur = con.cursor()
        logging.debug("Cursor has been set.")
        return cur

    def db_runquery(self, cur, query):
        """RUN A QUERY

        Args:
            cur (CURSOR OBJECT): THE CURSOR OBJECT ON WHICH SQL QUERIES CAN BE EXECUTED
            query (STRING): SQL QUERY TO EXECUTE

        Returns:
            LIST: RESULTS FROM THE QUERY
        """

        cur.execute(query)
        result = cur.fetchall()
        logging.debug("Successfully executed and returned query.")
        return result

    def db_close(self):
        if self.con:
            self.con.close()
            print()
            logging.debug("Database has been closed...")
