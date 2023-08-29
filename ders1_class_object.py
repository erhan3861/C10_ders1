# sınıflar -> fabrikaya benzer
# nesneler -> ürünleri

class Ogrenci():
    "Bu sınıf öğrenciyi tanımlar."
    def __init__(self):
        "Bu metot nesne tanımlandığında otomatik olarak çalışır"
        self.name = "Çağlar"
        self.age = 14
        self.coding_lesson = "python"

ogr1 = Ogrenci()
print(ogr1.name)

ogr2 = Ogrenci()
print(ogr2.name, ogr2.age, ogr2.coding_lesson)


class Ogrenci2():
    counter = 0 # sınıfa ait bir değişken
    def __init__(self, name, age, coding_lesson):
        self.name = name
        self.age = age
        self.coding_lesson = coding_lesson

        Ogrenci2.counter += 1

    def get_info(self): # nesne metotlarında self kelimesi yazılır
        print("isim =", self.name, "yaş =", self.age, "ders =", self.coding_lesson)

    def update_info(self, lesson="Java"):
        self.coding_lesson = lesson 
        self.get_info()

    def __str__(self):
        return self.name # geri döndür


ogr3 = Ogrenci2("Selman", 14, "Python")

ogr4 = Ogrenci2("İhsan", 14, "Javascript")

print(ogr3.name, ogr4.name) # Selman İhsan
ogr4.get_info() # isim =  İhsan yaş =  14 ders =  Javascript

# get_info() # get_info is not defined -> tanımlanmamış

# Ogrenci2.update_info() missing 1 required positional argument: 'lesson'

ogr4.update_info("İleri seviye python")
print("sonrası = ", ogr4.coding_lesson)

ogr4.update_info() # hata vermiyecek, çünkü öntanımlama yapıldı (default değer) 


print(f"Toplam öğrenci sayısı = {Ogrenci2.counter}") 
# Toplam öğrenci sayısı = 2

print(ogr4) # <__main__.Ogrenci2 object at 0x000002697B159D50>


