# Import libraries
import requests
from bs4 import BeautifulSoup
 
# URL from which pdfs to be downloaded
url = "http://mscs.dac.gov.in/MSCS/FiledAR_Old.aspx"
 
# Requests URL and get response object
response = requests.get(url)
 
# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)

mydivs = soup.find("table", {"class": "mGrid"})
#print(mydivs)

trs = mydivs.find_all('tr', recursive=False)

trs[:]=trs[1:]
print(len(trs))

for tr in trs:
    tds=tr.find_all("td",recursive=False)
    title=tds[1].text.strip()
    year=tds[3].text.strip()
    activity_link = tr.find_all('td')[5].find('a')['href']
    statement_link = tr.find_all('td')[6].find('a')['href']
    activity_response = requests.get(activity_link)
    with open(f'{title}_{year}_activity.pdf', 'wb') as f:
        f.write(activity_response.content)
    statement_response = requests.get(statement_link)
    with open(f'{title}_{year}_statement.pdf', 'wb') as f:
        f.write(statement_response.content)
    
    break

