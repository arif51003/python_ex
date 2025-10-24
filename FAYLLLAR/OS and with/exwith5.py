with open("text.txt","r+") as a:
    a.read()
    raise FileNotFoundError