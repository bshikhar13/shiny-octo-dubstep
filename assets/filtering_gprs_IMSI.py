def filtering_gprs_IMSI(imsilist):
	import MySQLdb

	db = MySQLdb.connect(host="localhost", 
                     user="root", 
                      passwd="bshikhar13", 
                      db="cdr") 
	cur_cdr = db.cursor() 

	finalUnsuspicios = []
	finalSuspicious = []

	for imsi in imsilist:
	
		query_cdr = "SELECT count(*) from cdr WHERE servedIMSI = " + str(imsi) + " LIMIT 1"
		cur_cdr.execute(query_cdr)
		threshhold = 1
		
		for row in cur_cdr.fetchall() :
			gprscount = row[0]
			if gprscount >= threshhold:
				finalUnsuspicios.append(imsi)
			else:
				finalSuspicious.append(imsi)


	result = []
	
	result.append(finalSuspicious)
	result.append(finalUnsuspicios)

	return result