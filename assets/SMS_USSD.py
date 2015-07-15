def SMS_USSD(limit):
	import MySQLdb

	db = MySQLdb.connect(host="localhost", 
	                     user="root", 
	                      passwd="bshikhar13", 
	                      db="cdr") 

	cur = db.cursor() 

	
	#same IMSI with different IMEI
	#query = "SELECT t1.IMSI_number, t1.IMEI_number, t2.IMSI_number, t2.IMEI_number FROM cdr_voice as t1 JOIN cdr_voice as t2 ON t1.Type = '0' and t2.Type = '0' and t1.IMSI_number != '' and t1.IMEI_number != '' and t2.IMSI_number != '' and t2.IMEI_number != '' and t1.IMSI_number = t2.IMSI_number and t1.IMEI_number != t2.IMEI_number LIMIT " + str(limit)

	#same IMEI with different IMSI

	query = "SELECT IMSI_number from cdr_voice WHERE LongType = 'Short Message Service, Mobile' LIMIT " + str(limit)
	cur.execute(query)

	import collections
	D = collections.defaultdict(list)

	def hashIMEI_IMSI (a,b):
		D[a].append(b)

	count = 0
	for row in cur.fetchall() :
		imsinumber = row[0] 
		hashIMEI_IMSI(imsinumber,1)
		count = count+1

	#print D
	frequency = []
	for k,v in D.items():
		#print k + " :: " + str(len(v))
		frequency.append(len(v))





	#import numpy as np
	#mport pandas as pd
	#from scipy import stats, integrate
	#import matplotlib.pyplot as plt



	#print min(frequency)
	#print np.mean(frequency)
	#print np.std(frequency)
	import numpy as np
	threshhold = np.mean(frequency) + np.std(frequency)

	counter = 0

	finalUnsuspicios = []
	finalSuspicious = []

	for k,v in D.items():
		counter = counter +1
		#print k + " :: " + str(len(v))
		#frequency.append(len(v))
		if len(v) >= threshhold:
			finalUnsuspicios.append(k)
		else:
			finalSuspicious.append(k)	


	#print "Total CDR SMS Records : " + str(count)
	result = []
	result.append(counter)
	result.append(finalSuspicious)
	result.append(finalUnsuspicios)

	return result

	# print "Total Unique IMSIs in the data using SMS/USSD: " +str(counter)
	# print "Suspicious : " +str(len(finalSuspicious))
	# print "UnSuspicious : " +str(len(finalUnsuspicios))		

