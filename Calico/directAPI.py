#!/usr/bin/python

from configparser import ConfigParser


class directAPI():
	def __init__(self):
		# Creating a config object that we will use to make SQL calls
		self._connectionParamaters = self._createConfig()

	def executeCommand(self, command):
		connection = None
		try:
			# Connecting to the PostgreSQL server
			connection = psycopg2.connect(**self._connectionParamaters)
			cursor = conn.cursor()

			# Executing the given command
			cursor.execute(command)

			# Closing communication with the PostgreSQL database server
			cursor.close()

			# Commiting changes to the database
			connection.commit()

		# Catching all exceptions and printing them to the console
		except(Exception, psycopg2.DatabaseError as error:
			print(error)

		finally:
			# If there was an error and connection isn't closed, we close it now.
			if connection is not None:
				connection.close()

	def _setupConfig(self, filename='database.ini', section='postgresql'):
		    # create a parser
			parser = ConfigParser()
			# read config file
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