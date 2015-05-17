import psycopg2
import sys

class coonexion():
	def __init__(self):
		
	def connect():
		#Define our connection string
		conn_string = "host='localhost' dbname='pfaDB' user='postgres' password='root'"
 
		# print the connection string we will use to connect
		print ("Connecting to database\n")
 
		# get a connection, if a connect cannot be made an exception will be raised here
		conn = psycopg2.connect(conn_string)
 	
		print ("Connected!\n")

		return conn
