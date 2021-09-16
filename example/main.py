from urllib import request


link = "https://yandex.ru"
with request.urlopen(link) as f :
    file = f.read()

    with open("index.txt", "wb") as f :
        f.write(file)
        f.close()
print(' writing procedure is finished')

with open ('index.txt','r')as f :
    print(f.read())

    