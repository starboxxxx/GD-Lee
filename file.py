file = open('Fullmeta_20220428162419.txt', "r", encoding="euc-kr")

dict = {'cat_id' : 'cat_name'}
error = {'cat_id' : 'cat_name'}

while True:
    data1 = file.readline()
    if not data1:
        break
    data2 = data1.split('\t')
    try:
        Category_fullname2 = data2[31]
        Category_menu_code2 = data2[55]
    except:
        continue
    Category_fullname = Category_fullname2.split('>')
    Category_menu_code = Category_menu_code2.split('>')

    if Category_fullname[0] == '키즈랜드':
        s = len(Category_menu_code)
        if s > 4:
            for i in range(1, 4):
                if Category_menu_code[i] in dict:
                    if Category_fullname[i] != dict[Category_menu_code[i]]:
                        error[Category_menu_code[i]] = Category_fullname[i]
                    else:
                        continue
                else:
                    dict[Category_menu_code[i]] = Category_fullname[i]
        elif s <= 4:
            if Category_menu_code[s-1].startswith("CV"):
                for i in range(1, s-1):
                    if Category_menu_code[i] in dict:
                        if Category_fullname[i] != dict[Category_menu_code[i]]:
                            error[Category_menu_code[i]] = Category_fullname[i]
                        else:
                            continue
                    else:
                        dict[Category_menu_code[i]] = Category_fullname[i]
            else:
                for i in range(1, s):
                    if Category_menu_code[i] in dict:
                        if Category_fullname[i] != dict[Category_menu_code[i]]:
                            error[Category_menu_code[i]] = Category_fullname[i]
                        else:
                            continue
                    else:
                        dict[Category_menu_code[i]] = Category_fullname[i]
    else:
        continue


with open('category_meta.txt', 'w', encoding='UTF-8') as f:
    for cat_id,cat_name in dict.items():
        f.write(f"{cat_id} \t {cat_name}\n")

with open('cat_id_key_err.txt', 'w', encoding='UTF-8') as f:
    for err_id, err_name in error.items():
        f.write(f"{err_id} \t {err_name}\n")

file.close()