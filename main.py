# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#변수 & 기본연산
print('hello sparta')
a= 3
b = a+1
a = a+1
num1 = a*b
num2 = 99

#자로형
name = 'bob'
num = 12
is_number = True

#리스트형
a_list = []
a_list.append(1)
a_list.append([2.3])

print(a_list)
print(a_list[1])
print(a_list[1][0])

#dictionary 형
a_dict = {}
a_dict = {'name' : 'bob' , 'age' : 21}
print(a_dict)

a_dict['height' ] = 178
print(a_dict)

print(a_dict['name'])

#Dictionary  형과 list 형의 조합
people = [{'name' : 'bob' , 'age' : 20 } , {'name' : 'carry' , 'age' : 38}]
print(people)
print(people[1])
print(people[1]['age'])

person = {'name' : 'john' , 'age' : 7}
people.append(person)

print(people)
print(people[2]['age'])

#조건문
#IF / ELSE로 구성
# aa =  int(input('나이를 입력하세요 : ').split())
# aa = int(aa)
aa = 20
print('여기부분 사용자에게 입력받아서 할 수 있게 알아보기')
if aa > 20:
    print('성인입니다.')
else :
    print('청소년입니다.')

#반복문
fruits = ['사과' , '배' , '감' , '귤']

for fruit in fruits :
    print(fruit)

#리스트 예제
fruits = ['사과' , '배' , '배' , '감' , '수박' , '귤' , '딸기' , '사과' , '배' , '수박']
count = 0
print(fruits)
for fruit in fruits :
    if fruit == '배':
         count +=1
print(count)

#딕셔너리 예제
people = [{'name' : 'bob' , 'age' : 20},
          {'name' : 'carry' , 'age' : 38},
          {'name' : 'john' , 'age' : 7},
          {'name' : 'smith' , 'age' : 17},
          {'name' : 'ben' , 'age' : 27},]


for person in people :
    print(person['name'] , person['age'])


print('이중에서 20실 이상인 사람은 ')
for person in people :
    if person['age'] > 20 :
        print(person['name'] , person['age'])


#문자열 자르기
#split 함수 사용
txt = 'sparta@gmail.com'

result = txt.split('@')[1].split('.')[0]

print(result)


#문자열 바꾸기
#replace 함수 사용
txt = 'sparta@gmaiol.com'
result = txt.replace('gmail' , 'naver')
print(result)















