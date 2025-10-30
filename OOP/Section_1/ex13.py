class Cheker:
    def chek_mail(s):
        if "@" and "." in s:
            return True
        return False
    
a="arifmasharipow@gmail.com"

print(Cheker.chek_mail(a))