with open("cookie.txt", encoding='utf-8') as cookie_file:
    for line in cookie_file.readlines():
        bulk = line.split("	")
        print("\"{name}\":\"{value}\",".format(name=bulk[0], value=bulk[1]))
