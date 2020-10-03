# #파일 입출력
# f = open("test.txt", "w", encoding="utf-8")
# #파일에 내용을 입력하는 방법
# f.write("안녕, 스파르타!\n")
# f.write("안녕, 스파르타!\n")
# f.write("안녕, 스파르타!\n")
# f.write("안녕, 스파르타!\n")
# f.write("안녕, 스파르타!")
#
# #
# for i in [1,2,3,4,5]:
#     f.write(f'{i}번째 줄이에요\n ')
# f.close()

# with open("test.txt", "r", encoding="utf-8") as f:
#     #파일의 모든 줄을 읽어라
#     lines = f.readlines()
#     for line in lines:
#         #출력해라
#         print(line)
from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ''
#with open(해당 txt 파일)
with open("kakaotalk_1.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            #split으로 문자열을 분리한다
            #replace로 해당문자열을 제거한다
            text += line.split('] ')[2].replace('검색',"").replace('샵',"").replace('ㅋ',"").replace('ㅎ','').replace('이모티콘\ㅜ','').replace('사진','').replace('이모티콘','')



#다운 받은 cloud.png의 태두리 안에 워드클라우드를 넣는다.
mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/Hancom Gothic Bold.ttf', background_color="white", mask=mask)
wc.generate(text)
#저장할 파일의 이름을 적는다
wc.to_file("result_masked.png")