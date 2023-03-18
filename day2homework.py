""" ÖDEV TANIMI:

Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

Bu öğrenci kayıt sistemine;

Aldığı isim soy isim ile listeye öğrenci ekleyen
Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
Listeye birden fazla öğrenci eklemeyi mümkün kılan
Listedeki tüm öğrencileri tek tek ekrana yazdıran
Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir."""

ögrenciler = ["Sema Kaygu","Mustafa Aydın","Halil İşçi","Yeliz Soran"]
"""def ögrenciEkle():
    ad=input("Adınızı giriniz: ")
    soyad=input("Soyadınızı giriniz: ")
    bilgi= ad + " " + soyad 
    if bilgi in ögrenciler:
        print("Girdiğiniz isim listede zaten var.")
    else:
        ögrenciler.append(bilgi)
        print(bilgi + "  adlı öğrenci listeye başarıyla eklendi.")
    print(ögrenciler)

ögrenciEkle() """


"""def ögrenciSil():
    ad=input("Adınızı giriniz: ")
    soyad=input("Soyadınızı giriniz: ")
    bilgi=ad + " " + soyad 
    if bilgi in ögrenciler:
        ögrenciler.remove(bilgi)
        print(bilgi + " adlı öğrenci silindi")
    else:
        ögrenciler.append(bilgi)
        print(bilgi + " adlı öğrenci başarıyla eklendi")
        print(ögrenciler)
ögrenciSil() 

def cokÖgrenciEkle():
    soru=int(input("Kaç öğrenci gireceksiniz?: "))
    x=0
    while x < soru:
        x+=1
        ad=input("Adınızı giriniz: ")
        soyad=input("Soyadınızı giriniz: ")
        bilgi=ad + " " + soyad
        ögrenciler.append(bilgi)
        print("Başarıyla Eklendi.")
cokÖgrenciEkle()"""

"""for i in ögrenciler:
    print(i) """
#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan

"""for no in ögrenciler:
    no = int(input("Numaranızı giriniz: "))
    if no ==0 :
     print(ögrenciler[0])
    if no==1 :
     print(ögrenciler[1])
    if no==2 :
     print(ögrenciler[2])
    if no==3 :
     print(ögrenciler[3]) """
#Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)

ögrenciler = ["Sema Kaygu","Mustafa Aydın","Halil İşçi","Yeliz Soran"]

def cokÖgrenciSil():
     bilgi=int(input("Kaç öğrenci sileceksiniz?: "))
     i=0
     while i<bilgi :
        ad=input("Silmek istediğiniz öğrencinin adını yazınız: ")
        soyad=input("Silmek istediğiniz öğrencinin soyadını yazınız: ")
        toplam=ad + " " + soyad
        ögrenciler.remove(toplam)
        print("Girmiş olduğunuz isim silindi.")
        print(ögrenciler)
        i+=1
        
    
cokÖgrenciSil()
