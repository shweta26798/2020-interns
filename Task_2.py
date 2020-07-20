import json
import matplotlib.pyplot as pl

f=open('C://Users//Lenovo//Desktop//Winsoft-Assignment//2020-interns//data.json')
data = json.load(f)
dates=[]
dateList=[]
RateINR=[]
ListofDatesofINR=[]
ListofRatesofINR=[]
ListofDatesofGBP=[]
ListofRatesofGBP=[]
dateRateofINR={}
dateRateofGBP={}
RateGBP=[]
date1=[]
cntDate=0
d1={}
d2={}
cnt1=0
# [T-2] Plot the graph of INR and GBP exchange rate against EUR from 1 Jan 2019 to 31 Jan 2019.
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
            ListofDatesofINR.append(j[0])
            cnt1=cnt1+1
            for m,n in j[1].items():
                if(m=="INR"):
                    print(m, n)
                    ListofRatesofINR.append(n)
                    break
#Creating dictionary of dates and there corresponfing INR values(this dictionary is unsorted)
for i in range(0,cntDate):
    d1[ListofDatesofINR[i]]=ListofRatesofINR[i]
print(d1)
#Sorting values according to date and adding it to a dictionary dateRate
for key in sorted(d1):
    print("%s: %s" % (key, d1[key]))
    dateRateofINR[key]=d1[key]
print(dateRateofINR)

#Making two separate lists of date and there corresponding inr values
for k in dateRateofINR:
    dateList.append(k)
    RateINR.append(dateRateofINR[k])
print(dateList)
print(RateINR)

#-----------------------------------------------------------------------------------------------------------------------
print("-------------------------GBP---------------------------------------")
#Finding dates in given range and there corresponding GBP values
cnt1=0
for k,v in data.items():
 if(cnt1!=cntDate):
    for j in v.items():
        dates=j[0].split("-")
        if dates[1]=="01" and dates[0]=="2019":
            print(dates)
            ListofDatesofGBP.append(j[0])
            cnt1=cnt1+1
            for m,n in j[1].items():
                if(m=="GBP"):
                    print(m, n)
                    ListofRatesofGBP.append(n)
                    break

#Creating dictionary of dates and there corresponding INR values(this dictionary is unsorted)
for i in range(0,cntDate):
    d2[ListofDatesofGBP[i]]=ListofRatesofGBP[i]
print(d2)
#Sorting values according to date and adding it to a dictionary dateRate
for key in sorted(d2):
    print("%s: %s" % (key, d2[key]))
    dateRateofGBP[key]=d2[key]
print(dateRateofGBP)

#Making two separate lists of date and there corresponding inr values
for k in dateRateofGBP:
    date1.append(k)
    RateGBP.append(dateRateofGBP[k])
print(date1)
print(RateGBP)

#plotting graph
fig,ax1=pl.subplots()

#plotting for INR
ax1.plot(dateList, RateINR, color='blue', linewidth = 1, marker='o', markerfacecolor='black', markersize=5)
pl.xticks(rotation=90)
ax1.set_xlabel("Dates")
ax1.set_ylabel('INR')
pl.title("Plot the graph of INR and GBP exchange rate against EUR from 1 Jan 2019 to 31 Jan 2019(T-2)")

#plotting for GBP
ax2=ax1.twinx()
ax2.set_ylabel("GBP")
ax2.plot(dateList,RateGBP,color='red', linewidth = 1, marker='o', markerfacecolor='black', markersize=5)

fig.tight_layout()
pl.show()













