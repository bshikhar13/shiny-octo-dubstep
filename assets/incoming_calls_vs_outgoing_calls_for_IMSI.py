def incoming_calls_vs_outgoing_calls_for_IMSI (imsilist):
	import MySQLdb
	import numpy as np
	db = MySQLdb.connect(host="localhost",user="root",passwd="bshikhar13",db="cdr") 
	cur = db.cursor() 

	MOCA = []
	MTCA = []
	sim = []
	counter = 1
	for IMSI in imsilist :
		innercur_MOCA = db.cursor()
		innercur_MTCA = db.cursor()
			
		innerquery_MOCA = "SELECT count(*) FROM cdr_voice WHERE LongType = 'Mobile Originated Call Attempt' AND IMSI_number = " +str(IMSI) + " LIMIT 0,1000000"
		innerquery_MTCA = "SELECT count(*) FROM cdr_voice WHERE LongType = 'Mobile Terminated Call Attempt' AND IMSI_number = " +str(IMSI) + " LIMIT 0,1000000"
			#print IMSI
			#print innerquery
		innercur_MOCA.execute(innerquery_MOCA)
		innercur_MTCA.execute(innerquery_MTCA)

		mtca = 0
		moca = 0

		for innerrow_MOCA in innercur_MOCA.fetchall():
			moca = innerrow_MOCA[0]

		for innerrow_MTCA in innercur_MOCA.fetchall():
			mtca = innerrow_MTCA[0]
			
		moca = moca + 1
		mtca = mtca + 1
		MOCA.append(moca)
		MTCA.append(mtca)
			
		counter = counter + 1	

	tempx = MOCA
	tempy = MTCA

	newlist= [float(x)/float(y) for x,y in zip(tempx,tempy)]


	threshhold = np.mean(newlist) + 1*np.std(newlist)


	finalSuspicious = []
	finalUnsuspicios = []
	counter = 0;

	for x in newlist:
		if x <= threshhold:
			finalSuspicious.append(imsilist[counter])
		else:
			finalUnsuspicios.append(imsilist[counter])
		counter = counter + 1
	



	result = []
	
	result.append(finalSuspicious)
	result.append(finalUnsuspicios)

	return result