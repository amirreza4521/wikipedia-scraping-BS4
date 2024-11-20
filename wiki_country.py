import requests
from bs4 import BeautifulSoup
import json
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

}
all_country=[]
url="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
response=requests.get(url=url,headers=header)
# print(response.reason)
soup=BeautifulSoup(response.text,"html.parser")
div_table=soup.select_one("div.mw-content-ltr.mw-parser-output")
table=div_table.find("table",class_="wikitable")
table_header=[]
for row in table.find("tbody").find("tr").find_all("th"):
    header=row.get_text().strip()
    table_header.append(header)
# print(table_header)
for row in table.find("tbody").find_all("tr")[1:]:
    values=[]
    for column in row.find_all("td"):
        value=column.get_text().strip()
        values.append(value)

    country_table={table_header[i]:values[i] for i in range(len(values))}
    all_country.append(country_table)
    # print(country_table)
for i,country in enumerate(all_country):
    print(f"{i} added")
with open("country_population.json","w") as f:
    json.dump(all_country,f,indent=4)