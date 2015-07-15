def IMEI_IMSI (imsilist):

	import MySQLdb

	db = MySQLdb.connect(host="localhost", 
	                     user="root", 
	                      passwd="bshikhar13", 
	                      db="cdr") 

	cur = db.cursor() 
	
	finalSuspicious = []
	finalUnsuspicios = []

	for imsi in imsilist:
		#query = "SELECT DISTINCT 'IMEI_Number' FROM (SELECT * FROM cdr WHERE (IMSI_Number = " +str(imsi)+ " AND Type = '1') OR (IMSI_Number = " +str(imsi)+" AND Type = '0'))"
		query = "SELECT IMEI_Number FROM cdr_voice WHERE IMSI_Number = "+str(imsi)+ " AND (Type = 0 OR Type = 1)"
		#print query
		cur.execute(query)
		
		S = []
		for row in cur.fetchall():
			S.append(row[0])


		row = len(list(set(S)))

		if row == 1 :
			finalUnsuspicios.append(imsi)
		else:
			finalSuspicious.append(imsi)	



	result = []
	
	result.append(finalSuspicious)
	result.append(finalUnsuspicios)

	return result