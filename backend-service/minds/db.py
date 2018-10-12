import psycopg2
import operator
import hashlib
from collections import Counter
import json
from .password import *

class DBConnection:
	def __init__(self):
		self.conn = psycopg2.connect(host=db_host(),dbname=db_dbname(), user=db_user(), password=db_password())
		self.cur = self.conn.cursor()


	def insert(self, user_id, json_data):
		query =  "INSERT INTO client VALUES (%s, %s);"
		data = (user_id, json.dumps(json_data))
		self.cur.execute(query, data)
		self.conn.commit()

	def get(self, user_id):
		if self.check_exist(user_id):
			query =  "SELECT user_data FROM client WHERE user_id = '{}';".format(user_id)
			self.cur.execute(query)
			result = self.cur.fetchone()[0]
		else:
			return []
		return result

	def update(self, user_id, json_data):
		query =  "UPDATE client SET user_data = %s WHERE user_id = %s;"
		data = (json.dumps(json_data),user_id)
		self.cur.execute(query, data)
		self.conn.commit()

	def update_with_item(self, user_id, item):
		json_data = self.get(user_id)
		json_data['items'].append(item)
		self.update(user_id, json_data)

	def check_exist(self, user_id):
		query =  "SELECT * FROM client WHERE user_id = '{}';".format(user_id)
		self.cur.execute(query)
		return self.cur.rowcount

	def get_all_client(self):
		query =  "SELECT * FROM client;"
		self.cur.execute(query)
		rows = self.cur.fetchall() # rows is a list of tuples

		arrayclient = []

		for r in rows:
			user_data = r[1]
			arrayclient.append(user_data)
		return arrayclient
