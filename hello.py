# 변수, 자료형, 조건분, 반복문, 기타 라이브러리

#변수
a= 2
b = 3
print(a+b)
#문자열
first_name = 'seungjin'
last_name = 'park'
print(first_name + last_name)
#문자열 더하기 문자열은 붙어서 나온다
#str(변수) -> 문자열 화
a_list = ['사과', '감','베']
print(a_list[1])
b_list  =['영희','철수',['사과','배']]
print(b_list[2][1])
#.append 를 사용하여 추가하는 방법
a_list = ['사과', '감','베']
a_list.append('수박')
print(a_list)
#key변수 dict는 key값으로 찾는다
#list는 숫자로 찾는다
a_dict = {'name': 'bob', 'age' : 24}
print(a_dict['name'])
a_dict['height'] = 178
print(a_dict)
a_list = ['수박', '참외','배']
a_dict['fruits'] = a_list
print(a_dict)
print(a_dict['fruits'][0])
#조건문
age = 24
if age > 20:
    print('성인입니다')
else:
    print('청소년입니다')
#반복문
#for 변수 in 리스트
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0
for fruit in fruits:

    if fruit == '사과':
        print(fruit)
        count += 1

print(count)
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    print(person['name'])
    print(person['age'])

for person in people:
    if person['age'] > 20:
        print(person['name'])

#파이썬 내장함수
#split 내장함수 #문자열 쪼개기
myemail = 'sparta@naver.com'
# result = myemail.split('@')[1].split('.')[0]
# print(result)
# print(result[1] )

#replace로 문자열 교체하기
result = myemail.replace('naver','gmail')
print(result)



# import dload
# dload.save("https://post-phinf.pstatic.net/MjAxOTEyMjRfODgg/MDAxNTc3MTY0NzE3ODI0.td40390rDg76HqexxOaLbmw4FMvAE5-taBjKL0QqGw4g.O1S4JTJnFfVcGPgHiCn09gNG2VtFZDO6umEH6e6fqygg.JPEG/%EC%A0%9C%EC%A3%BC%EB%8F%84_%EB%9A%9C%EB%B2%85%EC%9D%B4_%EC%97%AC%ED%96%89.jpg?type=w1200")

from selenium import webdriver
driver = webdriver.Chrome('chromedriver')

driver.get("http://www.naver.com")

import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EC%9D%B4%ED%9A%A8%EB%A6%AC")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select('#imgList > div > a > img')
i = 1
for thumbnail in thumbnails :
    img = thumbnail['src']
    dload.save(img,f'imgs_homework/{i}.jpg')
    i+=1
driver.quit()
