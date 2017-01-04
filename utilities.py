from pandas import DataFrame
import pandas as pd
import  json
from twitter import *
import twitter
import csv
import MySQLdb 




def mysqlConnect(hostname='localhost',username='root',pwd='12345',dbname='test'):
	con = MySQLdb.connect(host=hostname, user=username, passwd=pwd,
                                          db=dbname)
	return con

def getMySQlDF(table,fields):
	conn = mysqlConnect()
	query = ''
	if fields==None or len(fields) == 0:
		query = "SELECT * FROM "+table;
	else:
		query = "SELECT ";
		query += fields[0];
		for i in  range(1,len(fields)):
			query += ', '+fields[i]
		query+="  FROM "+table;
	print query
	df = pd.read_sql(query, con=conn)
	return df



def getCSVData(filename,fields=None):
	df = pd.read_csv(filename)
	if fields:
		return df[fields]
	return df



def getTwitterData(keyword):
	api = twitter.Api(
		consumer_key="WLNqYRHIelUzBeRffk93NznLt",
		consumer_secret="c0MLYczAAA1qtyvSdbJXIhp52LqypwLzkMmdVk44810b0nc578",
		access_token_key="2507891046-bTEMCZJPfAO6qITqu3BqQRIo8lth6U89XywtKzS",
		access_token_secret="k5IyHUq4c5AErNcyBvuhr0rskcH6peIWmrwnQwgM0lsYt"
		)
	search_results = api.GetSearch(term=keyword, lang='en', result_type='recent', count=20, max_id='')
	df = DataFrame(columns = ['u_id','Name','ScreenName','text'])
	res=''
	for tweet in search_results:
		try:
			df.loc[len(df.index)]=[tweet.user.id,tweet.user.name,tweet.user.screen_name,tweet.text]
		except:
			pass
	return df



def joinOperation(dataFrames, keys, joinType):
	print keys
	joinedDF = pd.merge(dataFrames[0], dataFrames[1], on=keys, how=joinType)
	for i in range(2,len(dataFrames)):
		joinedDF = pd.merge(joinedDF, dataFrames[i], on=keys, how=joinType)
	return joinedDF


def uniqueWords(df):
	df['uniqueWords'] = [ len(set(words.split())) for words in df['text'] ]
	dfres = df
	return dfres

def sortDF(df,fields):
	df = df.sort(columns=fields)
	return df


		

