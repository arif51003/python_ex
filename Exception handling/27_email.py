def download(n):
    try:
        if not n=="saccesful":
            raise Exception("error")
        return n
    except:
        return "yuklashda hatolik"
    
print(download("fail"))     