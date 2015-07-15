def unique_IMSI(limit):
	import MySQLdb

	db = MySQLdb.connect(host="localhost", 
	                     user="root", 
	                      passwd="bshikhar13", 
	                      db="cdr") 

	cur = db.cursor() 

	
	#same IMSI with different IMEI
	#query = "SELECT t1.IMSI_number, t1.IMEI_number, t2.IMSI_number, t2.IMEI_number FROM cdr_voice as t1 JOIN cdr_voice as t2 ON t1.Type = '0' and t2.Type = '0' and t1.IMSI_number != '' and t1.IMEI_number != '' and t2.IMSI_number != '' and t2.IMEI_number != '' and t1.IMSI_number = t2.IMSI_number and t1.IMEI_number != t2.IMEI_number LIMIT " + str(limit)

	#same IMEI with different IMSI

	query = "SELECT IMSI_number from cdr_voice LIMIT " + str(limit)
	cur.execute(query)

	
	imsilist = []

	count = 0
	for row in cur.fetchall() :
		imsilist.append(row[0])	

	result = []
	imsilist = list(set(imsilist))
	imsilist = filter(None,imsilist)
	
	result.append(imsilist)
	result.append(len(imsilist))
	#print result[0]
	return result

	# print "Total Unique IMSIs in the data using SMS/USSD: " +str(counter)
	# print "Suspicious : " +str(len(finalSuspicious))
	# print "UnSuspicious : " +str(len(finalUnsuspicios))		

