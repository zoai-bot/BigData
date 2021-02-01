import re

global string
string = '가나다 가나다라마 바사아자차 가나 abc abcde fghigk zzz 사랑합니다 길가의 <입력값>'
string_list = string.split(" ")
print("기본문장: " + string)
print("---------------"*5)

def finda(generalization):
    result = generalization.findall(string)
    print(result)

#[]대괄호 안의 입력값은 하나의 문자를 뜻함
#문자열안에 ㄱ-ㅎ or 가-힣 문자열을 반환
#'+'는 단어끝
gener = re.compile(r'[ㄱ-ㅎ|가-힣]+')
finda(gener)

gener = re.compile('[a-z|A-Z]+')
finda(gener)

#'.'은 아무문자
#'*'무한값
gener = re.compile('<.*>')
finda(gener)

def substitute(generalizaion):
    result = generalizaion.sub('',string)
    print(result)

#가,나,다 한 문자들을 ''로 전환
gener = re.compile('[가나다]')
substitute(gener)


gener = re.compile('\s+?의')
substitute(gener)



