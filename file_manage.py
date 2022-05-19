def pathRead():
    import configparser
    c = configparser.ConfigParser()
    c.read('path.ini', encoding='utf-8')
    datafile = c['PATH']['DATA_FILE']
    catmeta = c['PATH']['CAT_META']
    errmeta = c['PATH']['ERR_META']
    return datafile, catmeta, errmeta

def makeFile(Filename, id, name, dict_name):
    with open(Filename, 'w', encoding='UTF-8') as f:
        for id, name in dict_name.items():
            f.write(f"{id} \t {name}\n")