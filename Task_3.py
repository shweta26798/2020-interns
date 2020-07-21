import json
import datetime
import requests
import matplotlib.pyplot as pl

f=open('C://Users//Lenovo//Desktop//Winsoft-Assignment//2020-interns//data.json')
data = json.load(f)
cnt=0
currentRate=[]
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
#current date
x=datetime.datetime.now().date()
# [T-3]Plot the graph of INR and GBP exchange rate against EUR from 1 Jan 2019 to 31 Jan 2019 and also indicate the current rate for INR and GBP on the graph itself.
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

#------------------------------Current Rate of INR and GBP----------------------------------------------

url='https://api.exchangeratesapi.io/latest?symbols=INR,GBP'
response=requests.get(url)
file=response.text
file_content=json.loads(file)
print(file_content)

for k,v in file_content.items():
    if(cnt!=2):
        for i in v.items():
            currentRate.append(i[1])
            cnt=cnt+1
print(currentRate)

#Graph
fig,ax1=pl.subplots()
pl.xticks(rotation=90)
ax1.set_xlabel("Dates")
ax1.set_ylabel('INR',color="blue")

pl.title("Graph of INR and GBP exchange rate against EUR from 1 Jan 2019 to 31 Jan 2019 and current rate for INR and GBP")

ax2=ax1.twinx()
ax2.set_ylabel("GBP",color="red")
#plotting for INR
ax1.plot(dateList, RateINR, color='blue', linewidth = 1, marker='o', markerfacecolor='black', markersize=5)
#plotting for GBP
ax2.plot(dateList,RateGBP,color='red', linewidth = 1, marker='o', markerfacecolor='black', markersize=5)
#plottig for INR and GBP Current rate(both the values coincide according to left(inr scale) and right(gbp scale) yaxis
ax2.plot([str(x)],[currentRate[1]],color="red",marker='o',markerfacecolor='blue',markersize=7,label="INR GBP Current Rate")
pl.legend()
pl.show()



