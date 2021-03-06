'''Quiz 1) 당신은 (주)나도출판의 편집자입니다.
최근에 파이썬에 관한 책을 기획 중인데 양질의 컨텐츠를 제공하는 유튜버들을 발견하여 제안서를 보내고자 합니다.
동일한 내용의 매일에 유튜버 이름만 변경하여 파일로 저장하는 프로그램을 만드시오.

[조건]
1. 유튜버 이름은 리스트로 제공 (최소 2명 이상)
예) names = ['유튜버1', '유튜버2', '유튜버3', '유튜버4']

2. 파일명은 '유튜버 이름.txt'로 저장
예) 나도코딩.txt, 너도코딩.txt

[메일 본문]
안녕하세요? xxx님.

(주)나도출판 편집자 나코입니다.
현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
xxx님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요 ^^
감사합니다.

- 나코 드림.
'''
####################################################################################################
# unit 27 파일 사용하기 복습.
# 1. 파일에 문자열 작성
# file = open(파일이름, 파일모드) # 파일열기. w는 쓰기, r은 읽기모드
# file.write('문자열') # 파일에 문자열 저장
# file close() # 파일 객체 닫기

# 2. 작성한 파일에서 문자열 읽기
# file = open(파일이름, 'r')
# 변수 = file.read()
# print(변수)
# file close()

# 3. 파일 자동으로 닫기
# with open(파일이름, 파일모드) as file:
# 작업할 내용.
# 예) s = file.read()
# print(s)

# 4. 여러 줄 파일에 쓰기
# 4-1) 반복문으로
# with open('hello.txt', 'w') as file:
# for i in range(3):
#   file write(f'Hello, world! {i}\n')
# 4-2) 리스트로 # 이걸로 문제 풀 수 있겠다
# file.writelines(문자열리스트)
####################################################################################################


# test_lines = ['안녕하세요? xxx님.\n\n''(주)나도출판 편집자 나코입니다.\n''현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n''xxx님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n''자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n\n''좋은 하루 보내세요 ^^\n''감사합니다.\n\n''- 나코 드림.\n']

# file = open('practiceQuiz.txt', 'w', encoding='utf-8')
# file.writelines(test_lines)
# file.close()

# 파일 생성만 되고 내용 작성이 되지 않았던 문제 > 실행을 shift+enter로 해서. 주피터노트에 너무 익숙해졌다... f5로 하니 잘 됨.
# 작성한 내용이 깨져서 나오는 문제 > 한글 인코딩 안 함. encoding='utf-8' 추가해서 해결.

# 이제 문제 시작.

"""
names = ['Xl', 'Hc', 'Mq', 'Fx']

for i in names:
    test_lines = [f'안녕하세요? {i}님.\n\n''(주)나도출판 편집자 나코입니다.\n''현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n'f'{i}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n''자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n\n''좋은 하루 보내세요 ^^\n''감사합니다.\n\n''- 나코 드림.\n']
    file = open(f'{i}.txt', 'w', encoding='utf-8')
    file.writelines(test_lines)
    file.close()
"""
# 처음에 f를 안 쓰고 실행했더니 파일 이름과 본문 내용 모두 '{i}'로 출력됨 > f 붙여서 해결.


# 풀이

'''
names = ['Xl', 'Hc', 'Mq', 'Fx']

for name in names:
    with open(f"{name}.txt", "w", encoding="utf8") as email_file:
        email_file.write(f"""
안녕하세요? {name}님.

(주)나도출판 편집자 나코입니다.
현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
{name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요 ^^
감사합니다.

- 나코 드림.
""")
'''

# 이게..되네^^...리스트 만들고...줄바꿈 안 해도...되네^^....이하 영상에서 문장도 들여쓰기 맞추는 방법
# 윗줄에 그냥 들여쓰기 하면 들여쓰기 한 내용까지 파일에 저장됨.

"""
names = ['Xl', 'Hc', 'Mq', 'Fx']

for name in names:
    with open(f"{name}.txt", "w", encoding="utf8") as email_file:
        contents = (f"안녕하세요? {name}님.\n\n"
            "(주)나도출판 편집자 나코입니다.\n"
            "현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n"
            f"{name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n"
            "자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n\n"
            "좋은 하루 보내세요 ^^\n"
            "감사합니다.\n\n"
            "- 나코 드림.")
        email_file.write(contents)
"""

# 이렇게 하더라. list를 먼저 만들어서 writelines(list)를 쓰느냐, 작성 내용에 그대로 집어넣느냐
# 더불어 파일 닫을 때 file.close() 안 쓰고 파일 열 때 'with open(파일이름, 파일모드) as file:'
# + 파일객체(file) 부분은 이름 바꿀 수 있음.





"""
Quiz2) 행맨 게임 만들기
1. 리스트에 3개 이상의 단어를 추가
2. 위 리스트에서 랜덤으로 1개의 단어 선택
3. 단어의 길이에 맞게 밑줄 출력
4. 사용자로부터 한 글자씩 입력을 받아 입력값이 단어에 포함된 글자라면 'Correct', 아니라면 'Wrong' 출력
5. 매번 입력 받을 때마다 현재까지 맞힌 글자들 표시(맞히지 못한 글자는 밑줄 출력)
6. 정답을 맞히면 'Success' 출력 후 프로그램 종료(단, 횟수 제한은 없음)
"""

# 리스트 만들기/랜덤으로 단어 뽑아주기(random 모듈?)/나온 단어 길이 뽑아서(len) 밑줄 출력(print)/입력받기(input)/입력값으로 검색(find?)/
# 정답일 때, 아닐 때 다른 문장 출력(if)/맞힌 글자는 그대로 표시/다 맞히면 단어 출력 후 종료

# import random # 랜덤 써야 하니 모듈 가져오고
# test_game = ['today','is','very', 'exciting'] # 문제를 뽑아올 리스트 만듦
# question = str(random.choice(test_game)) # 문제로 낼 단어 랜덤으로 하나 가져오기

"""
question = 'exciting'
qa = len(question) # 실행할 때 제발 f5ㅠㅠ
# 밑줄 출력 어떻게 하지? 밑줄 변수를 하나 만들까?
ul = '_' # 밑줄. 얘를 qa만큼 출력합시다.
ul_look = ul*qa
print(ul_look)
# 이제 입력을 받아
answer = input()
# 받은 알파벳이 question에 해당되는지 찾기. 어떻게 찾지? 문자열로? > 문자열로 가 보자.
ai = question.find(answer) # 해당하는 문자가 있으면 인덱스값 반환.
print(ai)
# 반환 받은 인덱스 값에 입력받은 글자를 넣..기 전에 아~ 중복 글자는 어쩌지. for로 다 바꿔
# find 가 -1을 반환할 때까지 같은 글자를 찾아서 바꾸는 코드

if ai >= 0:
    nul_look = ul_look[:ai] + answer + ul_look[ai+1:] # 문자열에서 바꿀 부분 인덱스값을 알 때 슬라이스로 바꿔치기 하기. 검색해서 봄. 세상에.
elif ai == -1:
    nul_look = ul_look
    print('Wrong')
print(nul_look) # 이걸 반복!
"""
# 여기까지 다시 정리.
"""
question = 'exciting'
qa = len(question)
ul_look = '_'*qa
que = question
print(ul_look)

while question != ul_look:
    answer = input()
    ai = question.find(answer) # 입력받은 스펠이 있는지 인덱스값 찾기
    if ai >= 0:
        while ai != -1: # 인덱스 값이 존재하는 동안 반복함.
            ai = que.find(answer)
            if ai >= 0:
                ul_look = ul_look[:ai] + answer + ul_look[ai+1:]
                que = que[:ai] + '_' + que[ai+1:]
            else:
                print('Correct')
                print(ul_look)
    print('Wrong')
    print(ul_look)
print('Success')
"""
# 작동은 하는데... 중복되는 글자를 못 잡아낸다. 아, 인덱스값은 무조건 앞에서부터 찾아서.. 그럼 두 번째 이후를 찾으려면...?
# >> 인덱스 찾을 변수도 같이 바꿔서 해결

# 작동은 하는데222 같은 글자 한 번에 찾으려면..?
# 찾긴 하는데 무한히 돌아감. 됐다! 이제 출력 정리.

# 다시!

"""
question = 'exciting' # 문제로 낼 단어
qa = len(question) # 단어의 길이를 qa에 저장
ul_look = '_'*qa # 화면으로 보여줄 모습. 단어 길이만큼 _ 출력
que = question # 정답을 맞히면 que의 글자를 _로 바꿔서 판단할 예정
nul_look = ul_look
print(ul_look) # 처음 문제 제시.

while question != nul_look: # 문제와 밑줄이 같지 않으면 반복하는 코드
    answer = input() # 답을 입력 받는다.
    ai = question.find(answer) # 입력받은 스펠이 있는지 판단.
    if ai == -1: # 입력받은 스펠이 없는 경우 출력문 내보내고 다시 답을 입력 받음.
        print('Wrong')
        print(nul_look)
    else: # 입력받은 스펠이 있는 경우
        while ai != -1: # 인덱스 값이 존재하는 동안 반복함. 
            ai = que.find(answer)
            if ai >= 0: 
                nul_look = nul_look[:ai] + answer + nul_look[ai+1:]
                que = que[:ai] + '_' + que[ai+1:]
        print('Correct')
        print(nul_look)
print('Success')
"""
# 됐다! 정답인 경우 출력이 뒤에 계속 붙어서 이어지는 상황 > ai = que.find(answer) 가 if 밑에 있어서 인덱스 값이 -1로 변해서 발생. 위로 뺌.

###########################################################################
# 최종
"""
import random # 랜덤 써야 하니 모듈 가져오고
test_game = ['today','is','very', 'exciting'] # 문제 뽑아올 리스트
question = str(random.choice(test_game))

qa = len(question) # 단어의 길이를 qa에 저장
ul_look = '_'*qa # 화면으로 보여줄 모습. 단어 길이만큼 _ 출력
que = question # 정답을 맞히면 que의 글자를 _로 바꿔서 판단할 예정
nul_look = ul_look
print(ul_look) # 처음 문제 제시.

while question != nul_look: # 문제와 밑줄이 같지 않으면 반복하는 코드
    answer = input() # 답을 입력 받는다.
    ai = question.find(answer) # 입력받은 스펠이 있는지 판단.
    if ai == -1: # 입력받은 스펠이 없는 경우 출력문 내보내고 다시 답을 입력 받음.
        print('Wrong')
        print(nul_look)
    else: # 입력받은 스펠이 있는 경우
        while ai != -1: # 인덱스 값이 존재하는 동안 반복함. 
            ai = que.find(answer)
            if ai >= 0: 
                nul_look = nul_look[:ai] + answer + nul_look[ai+1:]
                que = que[:ai] + '_' + que[ai+1:]
        print('Correct')
        print(nul_look)
print('Success')
"""

##########################################################################
# 코드 정리 / 내 풀이
"""
import random # 랜덤 써야 하니 모듈 가져오고
# question = input('영어 단어를 입력하세요.:')
question_list = ['apple', 'banana', 'sky', 'miss']
question = random.choice(question_list)

ul_look = '_'*len(question) # 화면으로 보여줄 모습. 단어 길이만큼 _ 출력
que = question # 정답을 맞히면 que의 글자를 _로 바꿔서 언제까지 반복돌릴지 판단할 예정
print(ul_look) # 처음 문제 제시.

while question != ul_look: # 문제와 밑줄이 같지 않으면 반복하는 코드
    answer = input() # 답을 입력 받는다.
    ai = question.find(answer) # 입력받은 스펠이 있는지 판단.
    if ai == -1: # 입력받은 스펠이 없는 경우 출력문 내보내고 다시 답을 입력 받음.
        print('Wrong')
        print(ul_look)
    else: # 입력받은 스펠이 있는 경우
        while ai != -1: # 인덱스 값이 존재하는 동안 반복함. 
            ai = que.find(answer)
            if ai >= 0: 
                ul_look = ul_look[:ai] + answer + ul_look[ai+1:]
                que = que[:ai] + '_' + que[ai+1:]
        print('Correct')
        print(ul_look)
print('Success')
"""



from random import *
words = ["apple", "banana", "orange"]
word = choice(words)
print("answer : " + word)
letters = "" # 사용자로부터 지금까지 입력받은 모든 알파벳을 모음

while True:
    succeed = True
    print()
    for w in word:      # word를 돌면서 letters에 있는 철자는 표시, 없으면 _
        if w in letters:
            print(w, end=' ')
        else:
            print("_", end=' ')
            succeed = False
    print()

    if succeed:         # 전부 맞히면 'success'출력 후 break
        print('success')
        break

    letter = input("Input letter > ")   # 사용자 입력 받기
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("Correct")
    else:
        print("Wrong")