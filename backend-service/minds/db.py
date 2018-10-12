# import pyotp
import psycopg2
import operator
import hashlib
from collections import Counter
import json
from .password import *
# from urllib.parse import urlparse

# from .URL import URL
# from .Topic import Topic
# from .User import User

#  CREATE TABLE revamp_data (
#      user_id VARCHAR(255) NOT NULL PRIMARY KEY,
#      user_data JSON
#  );

class DBConnection:
	def __init__(self):
		self.conn = psycopg2.connect(host=db_host(),dbname=db_dbname(), user=db_user(), password=db_password())
		self.cur = self.conn.cursor()


	def insert(self, user_id, json_data):
		query =  "INSERT INTO revamp_data VALUES (%s, %s);"
		data = (user_id, json.dumps(json_data))
		self.cur.execute(query, data)
		self.conn.commit()

	def empty_json_data(self):
		data = {
			"lists": {
				"current":{
					"items":[]
				}
			},
			"shopping":{
				"items":[]
			}
		}
		return data

	def get(self, user_id):
		if self.check_exist(user_id):
			query =  "SELECT user_data FROM revamp_data WHERE user_id = '{}';".format(user_id)
			self.cur.execute(query)
			result = self.cur.fetchone()[0]
		else:
			result = self.empty_json_data()
			self.insert(user_id, result)
		return result

	def update(self, user_id, json_data):
		query =  "UPDATE revamp_data SET user_data = %s WHERE user_id = %s;"
		data = (json.dumps(json_data),user_id)
		self.cur.execute(query, data)
		self.conn.commit()

	def update_with_item(self, user_id, item):
		json_data = self.get(user_id)
		json_data['items'].append(item)
		self.update(user_id, json_data)

	def check_exist(self, user_id):
		# Check if email exists in User Table
		query =  "SELECT * FROM revamp_data WHERE user_id = '{}';".format(user_id)
		self.cur.execute(query)
		return self.cur.rowcount

	# ##########################################
	# ''' HELPER FUNCTIONS '''
	# ##########################################
	# def hashURL(self, url_string):
	# 	url_hash = hashlib.sha1(url_string.encode('utf-8'))
	# 	return url_hash.hexdigest()

	##########################################
	''' URL AND TOPIC FUNCTIONS '''
	##########################################

	# Check if the domain of the url is within the trusted domains table.
	# def checkDomain(self, url_string):
	# 	parsed_uri = urlparse(url_string)
	# 	domain = '{uri.netloc}'.format(uri=parsed_uri)

	# 	query = "SELECT * FROM tblDomain WHERE doRootDomain = '{}';".format(domain)
	# 	self.cur.execute(query)

	# 	found = self.cur.fetchone()

	# 	if found:
	# 		return True
	# 	else:
	# 		return False

	# # Retrieve keywords of a given topic / URL
	# def getKeywordList(self, ID, topicOrURL):
	# 	if topicOrURL == "topic": 	# Select TopicKeywords
	# 		query = "SELECT tokeKeyword, tokeDfScore FROM tblTopicsKeywords WHERE toketoID = '{}';".format(ID)
	# 	else:						# Select URLKeywords
	# 		query = "SELECT urkeKeyword, urkeTfscore FROM tblURLKeywords WHERE urkeUrID = '{}';".format(ID)

	# 	self.cur.execute(query)
	# 	keyword_rows = self.cur.fetchall()

	# 	# Create dictionary of keywords
	# 	keywords = {}
	# 	for k in keyword_rows:
	# 		keywords[k[0]] = k[1]	# { keyword: df }
	# 	return keywords

	# # Retrieve all topics from database and return list of Topic objects
	# def getTopics(self):
	# 	query =  "SELECT toID, toUrCount FROM tblTopics;"
	# 	self.cur.execute(query)
	# 	rows = self.cur.fetchall() # rows is a list of tuples

	# 	topics_list = []

	# 	for r in rows:
	# 		url_count = r[1]
	# 		topicID = r[0]
	# 		keywords = self.getKeywordList(topicID, topicOrURL="topic")

	# 		# Create Topic object and append to list
	# 		topic = Topic(topicID, keywords, url_count)
	# 		topics_list.append(topic)
	# 	return topics_list

	# # Retrieve all URLs assigned to this topic and return list of URL objects
	# def getURLsForTopic(self, topic):	
	# 	query = "SELECT urID, urURL, urConfidence FROM tblURL WHERE urToID = %s;"
	# 	data = (topic.topicID,)
	# 	self.cur.execute(query, data)
	# 	rows = self.cur.fetchall()

	# 	url_list = []
	# 	for r in rows:
	# 		urlID = r[0]
	# 		url_string = r[1]
	# 		confidence = r[2]
	# 		keywords = self.getKeywordList(urlID, topicOrURL="url")

	# 		# Create URL object and append to list
	# 		url = URL(url=url_string, keywords=keywords, urlID=urlID, topicID=topic.topicID, confidence=confidence)
	# 		url_list.append(url)

	# 	return url_list

	# # Retrieve topicID for given url_string
	# def getTopicForURL(self, url_string):
	# 	urlID = self.hashURL(url_string)			# Generate URL ID using hash
	# 	query = "SELECT urToID FROM tblURL WHERE urID = '{}';".format(urlID)
	# 	self.cur.execute(query)
	# 	result = self.cur.fetchone()[0]
	# 	return result

	# # Check if URL exists in the database
	# def isURLIndexed(self, url_string):
	# 	urlID = self.hashURL(url_string)
	# 	query = "SELECT * FROM tblURL WHERE urID = '{}';".format(urlID)
	# 	self.cur.execute(query)
	# 	return self.cur.rowcount 

	# # Assign URL to topic
	# def indexURL(self, url_string, keywords):
	# 	# Create url object
	# 	url = URL(url_string, keywords)

	# 	# Get list of topics
	# 	topics = self.getTopics()

	# 	if len(topics) == 0:
	# 		topic = self.createNewTopic()

	# 	else: 
	# 		topic_index, conf_value = self.matchURLToTopic(url,topics)
	# 		if conf_value < self.similarity_threshold:
	# 			print ('CREATING NEW TOPIC')
	# 			topic = self.createNewTopic()
	# 		else:
	# 			print ('ADDING TO CURRENT TOPIC')
	# 			topic = topics[topic_index]
		
	# 	self.assignURLToTopic(url,topic)
	# 	return topic.topicID

	# def matchURLToTopic(self, url, topics):
	# 	confScores = [topic.computeSimilarityWithURL(url) for topic in topics]
	# 	topic_index, conf_value = max(enumerate(confScores), key=operator.itemgetter(1))
	# 	return topic_index, conf_value

	# def createNewTopic(self):
	# 	# Insert to tblTopics
	# 	query = "INSERT INTO tblTopics(toTitle) VALUES ('empty title');"
	# 	self.cur.execute(query)
	# 	self.cur.execute('SELECT LASTVAL()')
	# 	topicID = self.cur.fetchone()[0]
	# 	self.conn.commit()

	# 	# Create new Topic object using ID of newly created entry in tblTopics
	# 	new_topic = Topic(topicID, Counter(), 0)
	# 	print (new_topic.topicID)

	# 	return new_topic

	# def assignURLToTopic(self,url,topic):
	# 	# Recompute df values from adding new keywords
	# 	topic.addKeywords(url.keywords)

	# 	# Insert url object into DB
	# 	url.topicID = topic.topicID
	# 	url.confidence = 0 # Initialise as 0 first. Going to recompute later.
	# 	self.insertURLAndKeywords(url)

	# 	# Insert to tblTopicsKeywords (OR update tblTopicsKeywords df values. need trigger)
	# 	query = "INSERT INTO tblTopicsKeywords VALUES (%s, %s, %s);"
	# 	for k in topic.keywords:
	# 		data = (topic.topicID, k, topic.keywords[k])
	# 		self.cur.execute(query, data)
	# 	self.conn.commit()

	# 	url_list = self.getURLsForTopic(topic)

	# 	# Recompute confidence scores for all URLs belonging to the topic
	# 	for url in url_list:
	# 		conf = topic.computeSimilarityWithURL(url)
	# 		url.topic = topic.topicID
	# 		url.confidence = conf

	# 	# Update confidence scores for all URLs in database
	# 	query = "UPDATE tblURL SET urConfidence = %s WHERE urID = %s;"
	# 	for url in url_list:
	# 		data = (url.confidence, url.urlID)
	# 		self.cur.execute(query, data)
	# 	self.conn.commit()

	# 	# Increment topic URL count
	# 	query = "UPDATE tblTopics SET toUrCount = toUrCount+1 WHERE toID = '{}';".format(topic.topicID)
	# 	self.cur.execute(query)
	# 	self.conn.commit()

	# 	# Update title of topic
	# 	keywords = Counter(topic.keywords)
	# 	top_entities = keywords.most_common(10)
	# 	top_entities = [t[0] for t in top_entities]
	# 	title = ', '.join(top_entities)
	# 	query = "UPDATE tblTopics SET toTitle = '{}' WHERE toID = '{}';".format(title, topic.topicID)
	# 	self.cur.execute(query)
	# 	self.conn.commit()

	# def insertURLAndKeywords(self, url):		
	# 	try: # in case the URL has already been inserted
	# 		# Inserting into URL table
	# 		query = "INSERT INTO tblURL(urID, urURL, urRootDomain, urToID, urConfidence) VALUES(%s, %s, %s, %s, %s);"
	# 		data = (url.urlID, url.url, url.domain, url.topicID, url.confidence)
	# 		self.cur.execute(query, data)
	# 		self.conn.commit()

	# 	except psycopg2.IntegrityError as e:
	# 		print ('Error: You probably tried to insert a duplicate urlID key. Or the domain is not in the trusted domain table.')
	# 		self.conn.rollback()
	# 		pass

	# 	try:
	# 		# Inserting into URLKeywords table
	# 		query = "INSERT INTO tblURLKeywords(urkeUrID, urkeKeyword, urkeTfscore) VALUES(%s, %s, %s);"

	# 		# keywords is a dictionary containing the entities and their frequencies
	# 		for e in url.keywords:
	# 			data = (url.urlID, e, url.keywords[e])
	# 			self.cur.execute(query, data)
	# 			self.conn.commit()

	# 	except psycopg2.IntegrityError as e:
	# 		print ('Error: There may be a problem with the trigger for adding new keywords.')
	# 		self.conn.rollback()
	# 		pass

	# ##########################################
	# ''' USER SPECIFIC FUNCTIONS '''
	# ##########################################
	# def hasUserSeenTopic(self, user, topicID):
	# 	query = "SELECT * FROM tblUserTopics WHERE ustoUsEmail = %s AND ustoToID = %s;"
	# 	data = (user, topicID)
	# 	self.cur.execute(query, data)
	# 	return self.cur.rowcount 

	# def addToUserTopics(self, user, topicID):
	# 	query = "INSERT INTO tblUserTopics(ustoUsEmail, ustoToID) VALUES(%s, %s);"
	# 	data = (user, topicID)
	# 	self.cur.execute(query, data)
	# 	self.conn.commit()

	# def checkUserExists(self, email):
	# 	# Check if email exists in User Table
	# 	query =  "SELECT * FROM tblUser WHERE usEmail = '{}';".format(email)
	# 	self.cur.execute(query)
	# 	return self.cur.rowcount

	# def getUser(self, email):
	# 	# Check if email exists in User Table
	# 	query =  "SELECT * FROM tblUser WHERE usEmail = '{}';".format(email)
	# 	self.cur.execute(query)
	# 	rows = self.cur.fetchall()

	# 	# If yes, we extract the relevant details
	# 	if self.cur.rowcount == 1:
	# 		email = rows[0][0]
	# 		key = rows[0][1]

	# 	# Else, insert into DB and return user
	# 	else:
	# 		key = pyotp.random_base32()
	# 		query =  "INSERT INTO tblUser (usEmail,usPassword,usHideUntrusted) VALUES (%s, %s, %s);"
	# 		data = (email, key, -1)
	# 		self.cur.execute(query, data)
	# 		self.conn.commit()

	# 	return User(email,key)

	# def authUser(self, email, token):
	# 	if not self.checkUserExists(email):
	# 		return False
	# 	u = self.getUser(email)
	# 	return u.key == token

	# ##########################################
	# ''' ADD-ON SPECIFIC FUNCTIONS '''
	# ##########################################
	# def getMutedOption(self, user_email, topicID):
	# 	query = "SELECT ustoMuted FROM tblUserTopics WHERE ustoUsEmail = %s AND ustoToID = %s;"
	# 	data = (user_email, topicID)
	# 	self.cur.execute(query, data)
	# 	result = self.cur.fetchone()[0]
	# 	return result

	# def getURLTrustScore(self, url_string):
	# 	urlID = self.hashURL(url_string)			# Generate URL ID using hash
	# 	query = "SELECT urTrustLevel FROM tblURL WHERE urID =%s;"
	# 	data = (urlID,)
	# 	self.cur.execute(query, data)
	# 	result = self.cur.fetchone()[0]
	# 	return max(0, min(result, 100))						# 0 <= trust score <= 100

	# def trustURL(self, user_email, url_string, flag):
	# 	urlID = self.hashURL(url_string)			# Generate URL ID using hash
	# 	query = "INSERT INTO tblUserURLTrust(usurtrUsEmail, usurtrUrID, usurtrTrust) VALUES (%s, %s, %s);"
	# 	data = (user_email, urlID, flag)
	# 	self.cur.execute(query, data)
	# 	self.conn.commit()

	# def muteTopic(self, user_email, topicID, flag):
	# 	query = "UPDATE tblUserTopics SET ustoMuted = %s WHERE (ustoUsEmail =%s AND ustoToID = %s);"
	# 	data = (flag, user_email, topicID)
	# 	self.cur.execute(query, data)
	# 	self.conn.commit()

	# def seeRelated(self, topicID, url_string):
	# 	urlID = self.hashURL(url_string)			# Generate URL ID using hash
	# 	query = "SELECT ururl,urConfidence FROM tblURL WHERE urToId=%s AND urID<>%s ORDER BY urConfidence desc limit 3;"
	# 	data = (topicID, urlID)
	# 	self.cur.execute(query, data)
	# 	rows = self.cur.fetchall()
	# 	url_list = []
	# 	for r in rows:
	# 		url_list.append(r[0])
	# 	return url_list

	# def getUserTrustThreshold(self, user_email):
	# 	query = "SELECT usHideUntrusted FROM tblUser WHERE usEmail=%s;"
	# 	data = (user_email,)
	# 	self.cur.execute(query, data)
	# 	result = self.cur.fetchone()[0]
	# 	return result

	# def suggestDomain(self, user_email, url_string):
	# 	parsed_uri = urlparse(url_string)
	# 	domain = '{uri.netloc}'.format(uri=parsed_uri)
	# 	try:
	# 		query = "INSERT INTO tblUserSuggestions(ussuUsEmail, ussuDomain) VALUES (%s, %s)"
	# 		data = (user_email, url_string)
	# 		self.cur.execute(query, data)
	# 		self.conn.commit()
	# 	except psycopg2.IntegrityError as e:
	# 		print ('User tried to suggest the same domain again.')
	# 		self.conn.rollback()
	# 		return False
	# 	return True

if __name__ == '__main__':
	DB = DBConnection()
	print(DB.getTopics())
	print(DB.isURLIndexed('a.com'))
	print(DB.getUser('test@gmail.com'))

	#keywords = {'hi': 1, 'hello': 2}
	#print(DB.indexURL('a.com', keywords))