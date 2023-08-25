import requests
from bs4 import BeautifulSoup
import csv

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []
 
count = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = title.text
    count += 1
    titles_list.append(d)
 
filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name'])
    w.writeheader()
     
    w.writerows(titles_list)

# print(soup.text)
# print(soup.title.name)
# print(soup.title.parent.name)

# for link in soup.find_all('a'):

#     print(link.get('href'))

# images_list = []
 
# images = soup.select('img')
# for image in images:
#     src = image.get('src')
#     alt = image.get('alt')
#     images_list.append({"src": src, "alt": alt})
     
# for image in images_list:
#     print(image)

