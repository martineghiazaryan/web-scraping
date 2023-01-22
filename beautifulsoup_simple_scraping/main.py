from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# with open('home.html', 'r')as html_file:
#     content = html_file.read()
    
#     soup = BeautifulSoup(content, 'lxml')
#     course_cards = soup.find_all('div', class_='card')
#     for course in course_cards:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1]

#         print(f'{course_name} costs {course_price}')


# html_text = requests.get('https://staff.am/en/jobs?JobsFilter%5Bcompany%5D=&JobsFilter%5Bkey_word%5D=&JobsFilter%5Bjob_candidate_level%5D=&JobsFilter%5Bjob_candidate_level%5D%5B%5D=2&JobsFilter%5Bcategory%5D=&JobsFilter%5Bjob_type%5D=&JobsFilter%5Bsalary%5D=&JobsFilter%5Bjob_term%5D=&JobsFilter%5Bjob_city%5D=&JobsFilter%5Bsort_by%5D=&&JobsFilter%5Bsort_by%5D=0').text

# soup = BeautifulSoup(html_text, 'lxml')
# jobs = soup.find_all('p', class_='job_list_company_title')

# # for job in jobs:
# #     if 'Ucom ' in job.text:
# #         print(job)

# job_list = soup.select_one('p.job_list_company_title:contains("Ucom")')

# print(job_list)


html=requests.get("https://carousell.com/search/products/?cc_id=2195&query=I7&sort_by=time_created%2Cdescending")
soup=BeautifulSoup(html.text,"html.parser")
atag=soup.find_all('a', class_=re.compile("-ab"))
itemtitle=[]
itemprice=[]
for a in atag:
  for title,price in zip(a.find_all('div', class_=re.compile("-m")),a.find_all('div', class_=re.compile("-k"))):
      itemtitle.append(title.text)
      itemprice.append(price.find('div').text)

df=pd.DataFrame({"Title" :itemtitle, "Price" : itemprice})
print(df)