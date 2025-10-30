class Movie:
    def __init__(self,nom,yil,janr):
        self.nom=nom
        self.yil=yil
        self.janr=janr
        
    def info(self):
        return f"{self.nom}, {self.janr} {self.yil}  "
movie1=Movie("Harry Potter", 2000, "Fantastik")


print(movie1.info())