###Kütüphane liste şeklindeki veri olayı
#örn.
#int_list = [1,2,3,4,5]

names = [nomad,vergil,acepaladin]

#bu yukarda belirtilen names artık ufak bir veri kütüphanesidir ve ordan veri çağırılabilir ama unutmayın veriler aslında 0 dan başlayıpta ilerler
#misal names = [nomad = 0,vergil = 1, acepaladin = 2] şeklinde görüyor sistem aslında

print(names[0]) #ekrana "nomad" yazdırır

###EKLE/ÇIKAR/BELİRLİ YERE EKLE
#kütüphaneye veri eklemek için
names.append("Gökhan") #buraya "Gökhan" verisini ekletir

#Kütüphaneden veri silmek için
names.remove("Gökhan")

#Belirli yere veri ekleme/belirtilmiş veriyi yeni girilenle değiştir
names.insert(1, "Gökhan")

###FOR döngüsü
#en basitinden anlatmam gerekirse bir oyuna katıldıkça oyunda ["isim" oyuncu katıldı] diye gösterir
#burda For döngüsü baş göstermektedir

a = ["oyuncu"]

for herGiren in oyuncular:
  print(a, " ","katıldı")
