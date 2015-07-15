def home_group(imsilist):
    import MySQLdb
    db = MySQLdb.connect(host="localhost",user="root",passwd="bshikhar13",db="cdr")

    cur = db.cursor()

    import collections

    finalSuspicious = []
    finalUnsuspicios = []

    def hash_number_of_calls_vs_subscriber(D,a, b):
        D[a].append(b)

    yo = 0
    count = 0
    for imsi in imsilist:
        count = count +1
        
        if imsi:
            innerquery = "SELECT Called_Number FROM cdr_voice WHERE LongType = 'Mobile Originated Call Attempt' AND IMSI_number = " + str(imsi)
            innercur = db.cursor()
            innercur.execute(innerquery)
            D = collections.defaultdict(list)
            number_of_users = 0
            number_of_calls = 0
            for innerrow in innercur.fetchall():
                called_number = innerrow[0];
                hash_number_of_calls_vs_subscriber(D,called_number, 1);  # print D
    
            import math        
            for k, v in D.items():
                D[k] = len(v)
                number_of_users = number_of_users + 1
                number_of_calls = number_of_calls + len(v)
            
            twentypercentusers = math.ceil(number_of_users * 0.3)
            eightypercentcalls = math.ceil(number_of_calls * 0.5)

           
            import operator
            sorted_x = sorted(D.items(), key=operator.itemgetter(1),reverse=True)
           

            decider = 0
            lim = int(math.ceil(twentypercentusers))
           
            if lim >= 0:
                for i in range (0,lim):
                    decider = decider + int(sorted_x[i][1])

           
                if decider <= eightypercentcalls:
           
                    yo =yo +1
                    finalSuspicious.append(imsi)
                else :
                    finalUnsuspicios.append(imsi)
           


    result = []
    
    result.append(finalSuspicious)
    result.append(finalUnsuspicios)

    return result