fuck = """
11물개 12쥐 13소 14말 15돼지 16거북이 17악어 18호랑이 19표범 20치타
21늑대 22여우 23스컹크 24두더지 25돌고래 26도마뱀 27독소리 28바다표범 29가재
30랍스타 31원앙 32까마귀 33오리 34앵무새 35부엉이 36참새 37꾀꼬리 38나비
39잠자리 40이구아나 41카멜레온 42개미핥기 43거미 44잉어 45곰 46펭귄 47거위
48박쥐 49병아리 50닭 51멧돼지 52갈매기 53코뿔소 54사슴 55코끼리 56하마
57다람쥐 58가오리 59미어캣 60코브라 61자라 62두꺼비 63까치 64복어 65문어
66오징어 67쭈꾸미 68해파리 69오리너구리 70너구리 71양 72꿩 73개구리
74메추라기 75살모사 76매미 77하늘소 78매 79망둥어 80말똥구리 81벌 82산양
83비둘기 84풍뎅이 85산양 86딱따구리 87등에 88두루미 89달팽이 90다슬기
91노루 92오솔개 93누에 94아나콘다 95남생이 96뻐꾸기 97낙지 98제비 99사자
"""
output_string = ""

for i in fuck:
    if not i.isdigit():
        if i == " ":
            i = "\n"

        output_string = output_string + i


import random


abc = """
가냘픈
가는
가엾은
가파른
같은
거센
거친
검은
게으른
게을러빠진
게을러터진
고달픈
고른
고마운
고운
고픈
곧은
괜찮은
구석진
굳은
굵은
귀여운
그런
그른
그리운
기다란
기쁜
긴
깊은
깎아지른
깨끗한
나쁜
나은
난데없는
날랜
날카로운
낮은
너그러운
너른
널따란
넓은
네모난
노란
높은
누런
눅은
느닷없는
느린
늦은
다른
더러운
더운
덜된
동그란
돼먹잖은
된
둥그런
둥근
뒤늦은
드문
딱한
때늦은
뛰어난
뜨거운
막다른
많은
매운
먼
멋진
메마른
메스꺼운
모난
못난
못된
못생긴
무거운
무딘
무른
무서운
미끈미끈한
미운
바람직스러운
반가운
밝은
밤늦은
보드라운
보람찬
보잘것없는
부드러운
부른
붉은
비싼
빠른
빨간
뻘건
뼈저린
뽀얀
뿌연
새로운
서툰
섣부른
설운
성가신
센
수다스러운
수줍은
쉬운
스스러운
슬픈
시원찮은
싫은
싼
쌀쌀맞은
쏜살같은
쓰디쓴
쓰린
쓴
아니꼬운
아닌
아름다운
아쉬운
아픈
안된
안쓰러운
안타까운
않은
알맞은
약빠른
약은
얇은
얕은
어두운
어려운
어린
언짢은
엄청난
없는
여문
열띤
예쁜
올바른
옳은
외로운
우스운
의심쩍은
이른
익은
있는
작은
잘난
잘빠진
잘생긴
재미있는
적은
젊은
점잖은
조그만
좁은
좋은
주제넘은
줄기찬
즐거운
지나친
지혜로운
질긴
짓궂은
짙은
짠
짧은
케케묵은
큰
탐스러운
턱없는
푸른
하나같은
한결같은
흐린
희망찬
흰
힘겨운
힘찬
"""


list1 = output_string.split("\n")
list2 = abc.split("\n")
list3 = []

for a in range(0, len(list1)):
    if list1[a] == "":
        list3.append(a)

list3.reverse()

for a in list3:
    del list1[a]

print("랜덤 (형용사 + 동물) : ", random.choice(list2), random.choice(list1))
