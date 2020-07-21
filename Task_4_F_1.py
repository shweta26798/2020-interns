import json
import requests

#[F-1]
print("Enter the Date Range")
startD=input("\nEnter Start Date(yy-mm-dd):")
endD=input("\nEnter End Date(yy-mm-dd):")
url='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&Base=EUR'.format(startD,endD)
response=requests.get(url)
file=response.text
data=json.loads(file)
print(data)

json_object = json.dumps(data, indent = 4)
#Replacing data.json file
with open("C://Users//Lenovo//Desktop//Winsoft-Assignment//2020-interns//data.json", "w") as outfile:
    outfile.write(json_object)