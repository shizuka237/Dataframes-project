from utilities import mysqlConnect,getMySQlDF,getCSVData,getTwitterData,joinOperation,uniqueWords,sortDF
from sqlalchemy import create_engine




def tester():
	print "Enter no of DataSources you want to join/ Enter tweet in case of twitter "
	inp = raw_input()
	if( inp.isdigit()):
		inp = int(inp)
		df_list = []
		print "Enter the type(csv /sql) , (filename/tablename) , (fields)  in following "+str(inp)+" lines"
		for i in range(inp):
			params = raw_input().split(',')
			inptype = params[0]
			tablename = params[1]
			fields = params[2:len(params)]
			if(inptype == 'csv'):
				df = getCSVData(tablename,fields)
				print df.head()
				df_list.append(df)
			else :
				df = getMySQlDF(tablename,fields)
				print df.head()
				df_list.append(df)
			print '-----------------------------------------------'

		print "Enter Join Field names (separated by Commas)"
		joinfl = raw_input().split(',')
		print "-----Joining------"
		result = joinOperation(df_list,joinfl,'outer')
		print result.head()
		print "enter fields names on which u want to sort"
		fls = raw_input().split(',')
		res = sortDF(result,fls)
		print res.head()


	else:
		print 'enter the topic name to mine tweets on'
		topic = raw_input()
		twdf = getTwitterData(topic)
		print twdf
		print '---implimenting word count---'
		result = uniqueWords(twdf)
		print result


tester()
