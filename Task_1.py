import json
import matplotlib.pyplot as pl

f=open('C://Users//Lenovo//Desktop//Winsoft-Assignment//2020-interns//data.json')
data = json.load(f)
dates=[]
dateList=[]
Rate=[]
ListofDates=[]
ListofRates=[]
cntDate=0
dateRate={}
d1={}
cnt1=0
#[T-1]-Plot the graph of INR exchange rate against EUR from 1 Jan 2019 to 31 Jan 2019
for i in data['rates']:
    dates=i.split("-")
    if dates[1]=="01" and dates[0]=="2019":
        cntDate=cntDate+1                                                   #Counting No of Dates in range 1 Jan 2019 to 31 Jan 2019

#Finding dates in given range and there corresponding inr values
for k,v in data.items():
 if(cnt1!=cntDate):
    for j in v.items():
        dates=j[0].split("-")
        if dates[1]=="01" and dates[0]=="2019":
            print(dates)
            ListofDates.append(j[0])
            cnt1=cnt1+1
            for m,n in j[1].items():
                if(m=="INR"):
                    print(m, n)
                    ListofRates.append(n)
                    break
#Creating dictionary of dates and there corresponding inr values(this dictionary is unsorted)
for i in range(0,cntDate):
    d1[ListofDates[i]]=ListofRates[i]
print(d1)
#Sorting values according to date and adding it to a dictionary dateRate
for key in sorted(d1):
    print("%s: %s" % (key, d1[key]))
    dateRate[key]=d1[key]
print(dateRate)

#Making two separate lists of date and there corresponding inr values
for k in dateRate:
    dateList.append(k)
    Rate.append(dateRate[k])
print(dateList)
print(Rate)

#plotting graph
pl.plot(dateList, Rate, color='blue',linewidth = 1,marker='o', markerfacecolor='black', markersize=5)
pl.xticks(rotation=90)
pl.xlabel("Dates")
pl.ylabel('INR')
pl.title('INR exchange rate against EUR from 1 Jan 2019 to 31 Jan 2019(T-1)')
pl.show()













