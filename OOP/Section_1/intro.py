# class Car():
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
        
#     def __str__(self):
#         return f"{self.brand}"      
    
    
# my_car=Car(
#     brand="Toyota",
#     model="Camry"
# )

# car_of_Asror=Car(
#     brand="Chevrolet",
#     model="Nexia_2"
# )

# print(my_car)


# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     # def __str__(self):
#     #     return f"Name:{self.name}\nAge:{self.age}"
    
#     def introduce(self):
#         return f"Hi, I am {self.name}"

# arif=Person(
#     name="Arif",
#     age=22
# )    

# asror=Person(
#     name="Asror",
#     age=19
# )

# print(arif.introduce())

# class Library:
#     def __init__(self,nomi,muallifi,yil):
#         self.nomi=nomi
#         self.muallifi=muallifi
#         self.yil=yil
#     def __str__(self):
#         return f"Kitob nomi:{self.nomi} Muallif:{self.muallifi} Yili:{self.yil}"
    
# kitob1=Library(
#     nomi="Molxona",
#     muallifi="Jorj Oruvel",
#     yil=1946
# )


# kitob2=Library(
#     nomi="O'tkan kunlar",
#     muallifi="O'tkir Hoshimov",
#     yil=1984
# )

# kitob3=Library(
#     nomi="Erkuel Puaro",
#     muallifi="Agata Christa",
#     yil=1994
# )

# print(kitob3)


# class Rectangle():
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def primetr(self):
#         return (self.width+self.height)*2
    
# a=Rectangle(
#     width=5,
#     height=4
# )

# print(a.primetr())


# class Hayvon:
#     def __init__(self, nomi,rangi):
#         self.nomi = nomi
#         self.rangi=rangi
    
#     def tovush_ber(self):
#         print("Hayvon tovush chiqardi")
    
#     def __str__(self):
#         return f"{self.nomi} {self.rangi} rangda"

# class It(Hayvon):

#     def tovush_ber(self):
#         print("Vov-vov!")

# class Mushuk(Hayvon):

#     def tovush_ber(self):
#         print("Miyov!")

# it = It("Rex","white")
# mushuk = Mushuk("Tom","black")

# it.tovush_ber()      # Vov-vov!
# mushuk.tovush_ber()  # Miyov!

# print(mushuk)




# class Car:
#     wheels = 4  # class variable

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.engine_on = False

#     def start(self):
#         self.engine_on = True
#         print(f"{self.brand} {self.model} started.")

#     def stop(self):
#         self.engine_on = False
#         print(f"{self.brand} {self.model} stopped.")

# car1 = Car("Tesla", "Model 3")
# car2 = Car("BMW", "M3")
# car1.start()
# print(car2.wheels)





# class Bankomat():
#     def __init__(self,parol,depos):
#         self.parol=parol
#         self.depos=depos
        
#     def pul_yechish(self):
#         def p(n):
#             n="uzbek"
#             while True:
#                 parol=input("parol:")
#                 if parol==self.parol:
#                     return True
#                 continue
            
#         def amaliyot():
#             if p(input("Til tanlang")):
                
        
        
        
        
        
        
        
        
        
        
class Bankamat:
    def __init__(self,id,parol,depozit):
        self.id=id
        self.parol=parol
        self.depozit=depozit
    def __repr__(self,):
        return f"id:{self.id} parol:{self.parol} depozit:{self.depozit}"    
    def pul_yechish(self):
        
        def pP(n):
         if n=="uzbek":
           while True:
              parol=input("parolni kiritng: ")
              if parol==self.parol:
                return True
              continue
          
        def  amaliyot():
           if pP(input("tilni tanlang;")) :     
             while True:
                print(f"naqd pul olish-----1\nsms kod ulash uchun-----2\nbalansni tekshirish-----3\nparol o'zgartirish-----4\ndasturdan chiqish----exit")
                n=input("amalyotni tanlang: ")
                if n=="1":
                    print("50 ming----0\n100 ming----5\n200 ming----6\n500 ming----7\nboshqa summani tanlang----8")
                    j=int(input("tanlang:"))
                    if j==0:
                        if self.depozit>=50:
                            self.depozit-=50
                            l=input("chek chiqarilsinmi?(ha,yuq)")
                            if l=="ha":
                             print(f"{50} ming so'm yechildi\n hisobinngizda {self.depozit} mablag' qolid")    
                            break
                        else:
                            print("hisobingizda mablag' yetarli emas ")
                            continue             
                    elif j==5:    
                        if self.depozit>=100:
                            self.depozit-=100
                            l=input("chek chiqarilsinmi?(ha,yuq)")
                            if l=="ha":
                                print(f"{100} ming so'm yechildi\n hisobinngizda {self.depozit} mablag' qolid")
                            break
                        else:
                            print("hisobingizda mablag' yetarli emas ")
                            continue        
                    elif j==7:    
                        if self.depozit>=500:
                            self.depozit-=500
                            l=input("chek chiqarilsinmi?(ha,yuq)")
                            if l=="ha":
                                print(f"{500} ming so'm yechildi\n hisobinngizda {self.depozit} mablag' qolid")
                            break
                        else:
                            print("hisobingizda mablag' yetarli emas ")
                            continue                                
                    elif j==8:    
                        k=int(input("summani kiritng; "))
                        if self.depozit>=k:
                            l=input("chek chiqarilsinmi?(ha,yuq)")
                            if l=="ha":
                                print(f"{k} ming so'm yechildi\n hisobinngizda {self.depozit-k} mablag' qolid")
                            self.depozit-=k
                            break
                        else:
                            print("hisobingizda mablag' yetarli emas ")
                            continue       
                elif n=="3":
                    print(f"hisobinghzida shuncha mablag' bor:{self.depozit}")
                    k=input("boshqa amaliyot bajarishni istaysizmi?(ha,yuq)")
                    if k=="ha":
                        continue
                    else:
                       break
                elif n=="4":
                    parol=input("yangi parolni kiritng: ")
                    self.parol=parol
                    k=input("boshqa amaliyot bajarishni istaysizmi?(ha,yuq)")
                    if k=="ha":
                        continue
                    else:
                       break
                elif n=="exit":
                    print("Etiboringiz uchun raxamt !!!!!!") 
                    break  
                        
                
        
        
        
        return amaliyot
    def __str__(self):
        return f"id:{self.id} parol:{self.parol} depozit:{self.depozit}"



                                             
                                                 
l=Bankamat("3434350540","0540",3000)
# print(repr(l))
(l.pul_yechish()())

# print(l)
