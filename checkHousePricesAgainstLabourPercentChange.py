from pylab import *
import csv
import scipy.stats

lpc = csv.reader(open('LabourPercentChange.csv'))

wardToLPC = dict()

lpc.next()

# Load the ward names into a dictionary
for entry in lpc:
    wardName = entry[0] + ": " + entry[1]
    if entry[2] != '':
        change = float(entry[2])
        wardToLPC[wardName] = float(change)

lmhp = csv.reader(open('London_Mean_House_Prices.csv'))

lmhp.next()

ldata = list()
# Check the ward name is already in the dictionary and add a data
# point if it is
for entry in lmhp:
    wardName = entry[0] + ": " + entry[1]
    if entry[8] != 0:
        if wardName in wardToLPC:
            ldata.append((wardToLPC[wardName],float(entry[8])))

data = array(ldata)

plot (data[:,0],data[:,1],'x')

# What's the correlation between the two data sets
print "Pearson R correlation"
pr = scipy.stats.pearsonr(data[:,0],data[:,1])
print "coefficient =",pr[0]
print "R squared =",pr[0]*pr[0]
print "significance =",pr[1]


# Fit a line to the data and plot it
lineFit = polyfit (data[:,0],data[:,1],1)
xs = array((min(data[:,0]),max(data[:,0])))
ys = xs * lineFit[0] + lineFit[1]

plot (xs,ys)

xlabel ('% change in labour vote')
ylabel ('% change in house price')
show()


    
