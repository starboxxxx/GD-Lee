# 출력파일, 에러파일, 데이터파일의 경로를 저장하는 설정파일 생성
import configparser
c = configparser.ConfigParser()
c['PATH'] = {}
c['PATH']['data_file'] = 'C:/pycharm/PyCharm Community Edition 2021.3.3/pythonProject/practice/GD-Lee/Fullmeta_20220428162419.txt'
c['PATH']['cat_meta'] = 'C:/pycharm/PyCharm Community Edition 2021.3.3/pythonProject/practice/GD-Lee/category_meta.txt'
c['PATH']['err_meta'] = 'C:/pycharm/PyCharm Community Edition 2021.3.3/pythonProject/practice/GD-Lee/cat_id_key_err.txt'

with open('path.ini', 'w', encoding = 'utf-8') as configfile:
    c.write(configfile)

# 설정파일을 읽은 후 변수에 해당 경로들을 저장
c.read('path.ini', encoding='utf-8')
DATA_FILE = c['PATH']['DATA_FILE']
CAT_META = c['PATH']['CAT_META']
ERR_META = c['PATH']['ERR_META']

file = open(DATA_FILE, "r", encoding="euc-kr")

# 데이터 파일에서 가져온 값들 중 조건에 충족하는 값을 넣을 딕셔너리 생성
dict = {}

# 값은 같지만 키가 다른 예외들을 넣을 딕셔너리 생성
error = {}

# 데이터파일의 헤더를 읽고 리스트형태로 저장
data1 = file.readline()
data2 = data1.split('\t')

# 헤더에 있는 필드명 중 'Category_fullname'과 'Category_menu_code'인 필드 명의 인덱스 번호와 이름을 각각 변수에 저장
for i in data2:
    if  i == 'Category_fullname' or 'Category_menu_code':
        x = data2.index('Category_fullname')
        y = data2.index('Category_menu_code')
        CAT_NAME_FIELD = data2[data2.index('Category_name')]
        CAT_ID_FIELD = data2[data2.index('Category_menu_code')]
    else:
        continue

# 헤더명이 저장된 변수를 이용하여 딕셔너리에 첫 번째 값으로 설정
dict[CAT_ID_FIELD] = CAT_NAME_FIELD
error[CAT_ID_FIELD] = CAT_NAME_FIELD

#
def func(x,y):
    if y in dict:
        if x != dict[y]:
            error[y] = x
    else:
        dict[y] = x


while True:
    data1 = file.readline()
    if not data1:
        break
    data2 = data1.split('\t')

    # 위에서 지정한 헤더명이 'Category_fullname'과 'Category_menu_code'인 필드의 인덱스 번호를 활용하여 필드 값을 저장
    Category_fullname2 = data2[x]
    Category_menu_code2 = data2[y]

    # 구분자를 '>'를 이용해 값들을 리스트 형태로 정렬
    Category_fullname = Category_fullname2.split('>')
    Category_menu_code = Category_menu_code2.split('>')

    # 리스트의 인덱스 값이 0번인 값이 키즈랜드인지 아닌지 확인
    if Category_fullname[0] == '키즈랜드':
        s = len(Category_menu_code)

        # 2~4depth만 이용하라는 조건이 있으므로 총 길이가 4 초과인 경우와 이하인 것으로 나눔
        if s > 4:
            for i in range(1, 4):
                func(Category_fullname[i], Category_menu_code[i])
        elif s <= 4:
            if Category_menu_code[s - 1].startswith("CV"):
                for i in range(1, s - 1):
                    func(Category_fullname[i], Category_menu_code[i])
            else:
                for i in range(1, s):
                    func(Category_fullname[i], Category_menu_code[i])
    else:
        continue

# 조건에 만족하는 필드 값들을 위에서 지정한 경로와 파일이름으로 저장
with open(CAT_META, 'w', encoding='UTF-8') as f:
    for cat_id, cat_name in dict.items():
        f.write(f"{cat_id} \t {cat_name}\n")

# 예외의 필드 값들을 위에서 지정한 경로와 파일이름으로 저장
with open(ERR_META, 'w', encoding='UTF-8') as f:
    for err_id, err_name in error.items():
        f.write(f"{err_id} \t {err_name}\n")

file.close()