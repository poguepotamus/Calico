#!/usr/bin/python


import psycopg2
from config import config
import logging
import re # RegEx

class SQLDB():
	def __init__(self):
		# Creating a config object that we will use to make SQL calls
		self._connectionParamaters = self._setupConfig()

        # Setting up the general logger
        self._setupLogger()

    def _setupLogger(self):
        # Bottom level at which the logger will write
        loggingLevel = logging.DEBUG
        logFile      = 'CalicoLog.txt'
        logging.basicConfig(filename = logFile, level = loggingLevel, format = '%(asctime)s %(levelname)-8s %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')

    ####################################################################################################################
    ### SQLDB Setup functions
    ####################################################################################################################

	def _setupConfig(self, filename='database.ini', section='postgresql'):
        # Creating a parser and feeding it a filename
        parser = ConfigParser()
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db


    def createTable(self, tableName, tableArguments=None):
        '''Creates a table with the database configured in self._setupConfig()
        '''

        # Checking for bad name
        if not re.match(r'[a-z|_|-]+', tableName, re.IGNORECASE):
            logging.
            raise ValueError(f'"{tableName}" is not a valid table name. Valid table names match regex "[a-z|_|-]".')

        # Collects a cursor for the database
        cursor = psycopg2.connect(self._connectionParamaters).cursor()

        # We check if there are any table arguments, if none, then we continue creating a table with no arguments
        if tableArguments is None:f
            # Setting the command to execute later
            command = f'CREATE TABLE {tableName.strip()}'

        # If tableArguments have been set
        else:
            # Creating the command to execute
            for argument in tableArguments:

                # Were going to concatenate the arguments into one string
                tableContents += f'\n{argument}'

            # Creating the command to be executed later
            command = f'{tableName.strip()}'






if __name__ == '__main__':
    connect()