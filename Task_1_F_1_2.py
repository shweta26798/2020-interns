import json
import requests
import matplotlib.pyplot as pl

dates=[]
dateList=[]
Rate=[]
ListofDates=[]
ListofRates=[]
cntDate=0
dateRate={}
d1={}
cnt1=0
startD=""
endD=""

#[F-1]
print("Enter the Date Range")
startD=input("\nEnter Start Date(yy-mm-dd):")
endD=input("\nEnter End Date(yy-mm-dd):")
url='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&Base=EUR'.format(startD,endD)
response=requests.get(url)
file=response.text
data=json.loads(file)
print(data)

#[F-2]
currencySym=input("\nEnter Currency Symbol:")

#[T-1 F 1-2]Plot graph for given currency symbol and in given date range
startDate=startD.split("-")
endDate=endD.split("-")
for i in data['rates']:
    dates=i.split("-")
    if dates[1]==startDate[1] and dates[0]==startDate[0] or dates[1]==endDate[1] and dates[0]==endDate[0] :
        cntDate=cntDate+1                                                   #Counting No of Dates in range 1 Jan 2019 to 31 Jan 2019


#Finding dates in given range and there corresponding currency symbol values
for k,v in data.items():
 if(cnt1!=cntDate):
    for j in v.items():
        dates=j[0].split("-")
        if dates[1]==startDate[1] and dates[0]==startDate[0] or dates[1]==endDate[1] and dates[0]==endDate[0] :
            print(dates)
            ListofDates.append(j[0])
            cnt1=cnt1+1
            for m,n in j[1].items():
                if(m==currencySym):
                    print(m, n)
                    ListofRates.append(n)
                    break
#Creating dictionary of dates and there corresponding currency symbol values(this dictionary is unsorted)
for i in range(0,cntDate):
    d1[ListofDates[i]]=ListofRates[i]
print(d1)
#Sorting values according to date and adding it to a dictionary dateRate
for key in sorted(d1):
    print("%s: %s" % (key, d1[key]))
    dateRate[key]=d1[key]
print(dateRate)

#Making two separate lists of date and there corresponding currency symbol values
for k in dateRate:
    dateList.append(k)
    Rate.append(dateRate[k])
print(dateList)
print(Rate)

#plotting graph
pl.plot(dateList, Rate, color='blue',linewidth = 1,marker='o', markerfacecolor='black', markersize=5)
pl.xticks(rotation=90)
pl.xlabel("Dates")
pl.ylabel(currencySym)
pl.title('Graph for '+currencySym+' from '+startD+' to '+endD)
pl.show()













