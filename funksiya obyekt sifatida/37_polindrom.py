l=lambda x: True if x.lower()==x[::-1].lower() else False
print(l("non"))