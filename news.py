from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')


wb = Workbook()
ws1 = wb.active
#시트제목
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사","썸네일"])


for article in articles :
    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    company = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')
    # thumbnails = soup.select_one('#sp_nws1 > dl > dt > a')['href']
    thumbnails = article.select_one('div > a')['href']
    ws1.append([title, url, company,thumbnails])

driver.quit()

wb.save(filename='articles.xlsx')