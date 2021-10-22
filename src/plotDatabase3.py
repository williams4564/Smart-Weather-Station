import matplotlib.pyplot as plt
import csv
import numpy as np

x=[]
y=[]
#loop will read the data and convert it to an integer array
with open('database3.csv','r') as csvfile:
	points = open('database3.csv').read().splitlines()  
	
	i = 0
	for row in points:
		nums = [int(k) for k in row.split()]
		y.append(nums)
		x.append(i)
		i = i + 1
flaty = []  #converts list of lists to single list
for elem in y:
	flaty.extend(elem)

print(flaty)

plt.plot(x, flaty)
plt.grid(True)

plt.ylim([-55,155])  #sets limits of y range
plt.title("Thermistor Reading")
plt.xlabel("Time")
plt.ylabel("Temperature")


plt.savefig('static/graph3.png')
plt.savefig('graph3.png')  #save in multiple places for safety
plt.savefig('templates/static/graph3.png')
plt.savefig('templates/graph3.png')
plt.savefig('templates/img/graph3.png')

plt.show()