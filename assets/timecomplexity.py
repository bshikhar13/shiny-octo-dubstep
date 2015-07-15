
import os
import time
epochs = 35
timefreq = []
x = []
for i in range(5,epochs):
	j = 30*i
	command = "python master.py " + str(j) + " 1 1 1 1 0";
	
	start_time = time.time()
	os.system(command)
	timenow = time.time() - start_time
	timefreq.append(timenow)
	x.append(j)

print(timefreq)	
import matplotlib.pyplot as pp

pp.plot(timefreq)
#pp.plot(timefreq, len(timefreq) * [1], "x")
pp.show()
pp.scatter(x,timefreq)
#pp.show()
#print min(frequency)
#print np.mean(frequency)
#print np.std(frequency)
