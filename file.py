import file_manage as fm
import setting as set

DATA_FILE, CAT_META, ERR_META = fm.pathRead()
file = open(DATA_FILE, "r", encoding="euc-kr")

# 데이터 파일에서 가져온 값들 중 조건에 충족하는 값을 넣을 딕셔너리 생성
dict = {}

# 값은 같지만 키가 다른 예외들을 넣을 딕셔너리 생성
error = {}

A,B = set.headerName(file, dict, error)
while True:
    data1 = file.readline()
    if not data1:
        break
    data2 = data1.split('\t')

    # 위에서 지정한 헤더 명이 'Category_fullname'과 'Category_menu_code'인 필드의 인덱스 번호를 활용하여 해당하는 필드 값을 한줄 씩 저장
    Category_fullname2 = data2[A]
    Category_menu_code2 = data2[B]

    # 구분자를 '>'를 이용해 값들을 리스트 형태로 정렬
    Category_fullname = Category_fullname2.split('>')
    Category_menu_code = Category_menu_code2.split('>')

    # 0 depth 값이 값이 키즈랜드인지 아닌지 확인
    set.depthSetting(Category_menu_code, Category_fullname, dict, error)

# 메타파일 생성
fm.makeFile(CAT_META,"cat_id","cat_name", dict)
fm.makeFile(ERR_META,"err_id","err_name", error)

file.close()