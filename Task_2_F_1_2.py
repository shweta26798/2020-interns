import json
import requests
import matplotlib.pyplot as pl

dates=[]
dateList=[]
Rate=[]
ListofDatesSym1=[]
ListofRatesSym1=[]
cntDate=0
dateRate={}
d1={}
cnt1=0
startD=""
endD=""
RateSym1=[]
ListofDatesSym2=[]
ListofRatesSym2=[]
dateRateSym1={}
dateRateSym2={}
RateSym2=[]
date1=[]
cntDate=0
d1={}
d2={}

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
currencySym1=input("\nEnter First Currency Symbol:")
currencySym2=input("\nEnter Second Currency Symbol:")
#[T-1 F 1-2]Plot graph for given currency symbol and in given date range
startDate=startD.split("-")
endDate=endD.split("-")
for i in data['rates']:
    dates=i.split("-")
    if dates[1]==startDate[1] and dates[0]==startDate[0] or dates[1]==endDate[1] and dates[0]==endDate[0] :
        cntDate=cntDate+1                                                   #Counting No of Dates in range 1 Jan 2019 to 31 Jan 2019


#Finding dates in given range and there corresponding currency symbol1 values
for k,v in data.items():
 if(cnt1!=cntDate):
    for j in v.items():
        dates=j[0].split("-")
        if dates[1]==startDate[1] and dates[0]==startDate[0] or dates[1]==endDate[1] and dates[0]==endDate[0] :
            print(dates)
            ListofDatesSym1.append(j[0])
            cnt1=cnt1+1
            for m,n in j[1].items():
                if(m==currencySym1):
                    print(m, n)
                    ListofRatesSym1.append(n)
                    break
#Creating dictionary of dates and there corresponding currency symbol1 values(this dictionary is unsorted)
for i in range(0,cntDate):
    d1[ListofDatesSym1[i]]=ListofRatesSym1[i]
print(d1)
#Sorting values according to date and adding it to a dictionary dateRate
for key in sorted(d1):
    print("%s: %s" % (key, d1[key]))
    dateRate[key]=d1[key]
print(dateRate)

#Making two separate lists of date and there corresponding currency symbol1 values
for k in dateRate:
    dateList.append(k)
    Rate.append(dateRate[k])
print(dateList)
print(Rate)

#---------------------------For Currency Symbol2-------------------------------------
cnt1=0
for k,v in data.items():
 if(cnt1!=cntDate):
    for j in v.items():
        dates=j[0].split("-")
        if dates[1]==startDate[1] and dates[0]==startDate[0] or dates[1]==endDate[1] and dates[0]==endDate[0] :
            print(dates)
            ListofDatesSym2.append(j[0])
            cnt1=cnt1+1
            for m,n in j[1].items():
                if(m==currencySym2):
                    print(m, n)
                    ListofRatesSym2.append(n)
                    break

#Creating dictionary of dates and there corresponding currency symbol2 values(this dictionary is unsorted)
for i in range(0,cntDate):
    d2[ListofDatesSym2[i]]=ListofRatesSym2[i]
print(d2)
#Sorting values according to date and adding it to a dictionary dateRate
for key in sorted(d2):
    print("%s: %s" % (key, d2[key]))
    dateRateSym2[key]=d2[key]
print(dateRateSym2)

#Making two separate lists of date and there corresponding currencySym2 values
for k in dateRateSym2:
    date1.append(k)
    RateSym2.append(dateRateSym2[k])
print(date1)
print(RateSym2)

#plotting graph
fig,ax1=pl.subplots()

#plotting for currencySym1
ax1.plot(dateList, Rate, color='blue', linewidth = 1, marker='o', markerfacecolor='black', markersize=5)
pl.xticks(rotation=90)
ax1.set_xlabel("Dates")
ax1.set_ylabel(currencySym1,color="blue")
pl.title('Graph for '+currencySym1+' and '+currencySym2+' against EUR from '+startD+' to '+endD)

#plotting for currencySym2
ax2=ax1.twinx()
ax2.set_ylabel(currencySym2,color="red")
ax2.plot(dateList, RateSym2, color='red', linewidth = 1, marker='o', markerfacecolor='black', markersize=5)

fig.tight_layout()
pl.show()














