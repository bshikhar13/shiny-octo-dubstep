def IMEI_IMSI (imsilist):

	import MySQLdb

	db = MySQLdb.connect(host="localhost", 
	                     user="root", 
	                      passwd="bshikhar13", 
	                      db="cdr") 

	cur = db.cursor() 
	
	finalSuspicious = []
	finalUnsuspicios = []


	#query = "SELECT DISTINCT 'IMEI_Number' FROM (SELECT * FROM cdr WHERE (IMSI_Number = " +str(imsi)+ " AND Type = '1') OR (IMSI_Number = " +str(imsi)+" AND Type = '0'))"
	query = "SELECT t1.IMSI_number, t1.IMEI_number, t2.IMSI_number, t2.IMEI_number FROM cdr_voice as t1 JOIN cdr_voice as t2 ON ((t1.Type = '1' and t2.Type = '1') or (t1.Type = '0' and t2.Type = '0')) and t1.IMSI_number != '' and t1.IMEI_number != '' and t2.IMSI_number != '' and t2.IMEI_number != '' and t1.IMSI_number != t2.IMSI_number and t1.IMEI_number = t2.IMEI_number"
	#print query
	cur.execute(query)
	import collections
	D = collections.defaultdict(list)

	def hashIMEI_IMSI (a,b):
		D[a].append(b)

	S = []
	for row in cur.fetchall():
		S.append(row[0])
		S.append(row[2])


	for imsi in imsilist :
		if imsi in S :
			finalSuspicious.append(imsi)
		else:
			finalUnsuspicios.append(imsi)





	result = []

	result.append(finalSuspicious)
	result.append(finalUnsuspicios)

	return result