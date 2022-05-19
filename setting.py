def headerName(fileName, x, y):

    data1 = fileName.readline()
    data2 = data1.split('\t')

    for i in data2:
        if i == 'Category_fullname' or 'Category_menu_code':
            a = data2.index('Category_fullname')
            b = data2.index('Category_menu_code')
            CAT_NAME_FIELD = data2[a]
            CAT_ID_FIELD = data2[b]
            x[CAT_ID_FIELD] = CAT_NAME_FIELD
            y[CAT_ID_FIELD] = CAT_NAME_FIELD
            return a,b
        else:
            continue

def func(x,y,a,b):
    if y in a:
        if x != a[y]:
            b[y] = x
    else:
        a[y] = x

def depthSetting(Category_menu_code_1, Category_fullname_1, dict, error):

    s = 0
    if Category_fullname_1[0] == '키즈랜드':
        s = len(Category_menu_code_1)

    if s > 4:
        for i in range(1, 4):
            func(Category_fullname_1[i], Category_menu_code_1[i], dict, error)
    elif s <= 4:
        if Category_menu_code_1[s - 1].startswith("CV"):
            for i in range(1, s - 1):
                func(Category_fullname_1[i], Category_menu_code_1[i], dict, error)
        else:
            for i in range(1, s):
                func(Category_fullname_1[i], Category_menu_code_1[i], dict, error)