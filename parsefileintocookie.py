with open("cookie.txt", encoding='utf-8') as cookie_file:
    for line in cookie_file.readlines():
        bulk = line.split("	")
        # print(bulk[2])
        if not bulk[2].__contains__('.lagou.com'):
            continue
        if bulk[1] == "\"\"":
            bulk[1] = ""
        print("\"{name}\":\"{value}\",".format(name=bulk[0], value=bulk[1]))
