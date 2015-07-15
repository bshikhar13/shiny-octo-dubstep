def SMS_USSD(imsilist):
	
	import MySQLdb

	db = MySQLdb.connect(host="localhost", 
	                     user="root", 
	                      passwd="bshikhar13", 
	                      db="cdr") 

	

	
	frequency = []
	imsifrequency = []
	for imsi in imsilist:
		if imsi :
			query = "SELECT count(*) from cdr_voice WHERE LongType = 'Short Message Service, Mobile' AND IMSI_Number =  "+str(imsi)
			#print query
			cur = db.cursor() 

			cur.execute(query)

			

			count = 0
			for row in cur.fetchall() :
				freq = row[0] 
				frequency.append(freq)
				imsifrequency.append(freq)


	import numpy as np
	threshhold = np.mean(frequency) + np.std(frequency)

	counter = 0

	finalUnsuspicios = []
	finalSuspicious = []

	for imsi in imsilist :
		if imsifrequency[counter] >=threshhold :
			finalUnsuspicios.append(imsi)
		else :
			finalSuspicious.append(imsi)
		counter = counter +1
			
	result = []
	
	result.append(finalSuspicious)
	result.append(finalUnsuspicios)

	return result

	# print "Total Unique IMSIs in the data using SMS/USSD: " +str(counter)
	# print "Suspicious : " +str(len(finalSuspicious))
	# print "UnSuspicious : " +str(len(finalUnsuspicios))		

