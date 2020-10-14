###Bu bölgede "Kick Start" deyimine adım atacaz

#String ifade için [" --- "] tırnak içinde veri girilmelidir
#örn.
a = "Gökhan"

#Not değişken isimler asla sayıyla başlamaz ve noktalama işaretiyle başlamaz

#int değer için verilecek veri normal yazılır tırnak içine alınmasına gerek duyulmaz
#örn.
a1 = 18

#Decimal veriler namı diğer "Ondalıklı" veriler
#örn.
a3 = 1.2847

#Bool,Boolean (0,1) var yada yok , evet veya hayır, true-false ikilisidir
#örn.
a4 = True

#"type()" kodu verilen değişkenin hangi tipte yazıldığına (Bool,int,String(str diye de kısaltılabilir))
print(type(a))

#Yazdırmak için [print("Veri" yada değişken adı)]şeklinde yazılır
#örn.

print("Kahvaltı Hazır!")
print(a)

#Matematiksel işlemler (+,-,*,/)
#Eğerkine 2 adet string değer yazarsanız alacağınız sonuç 2 (veya daha çok kod bölümünde çıktısını almak istediğiniz kodda ne kadar değişken belirtirseniz o kadar)
#2 adet değişken verisinin yan yana yazılmış halini ortaya çıkartır bu hataya eğer ekrana yazı yazdırma işlemi düşünmüyorsanız düşmemenizi isterim
# hatalı matematik işlemi / ekrana string ifade yazdıran durum
b1 = "12"
b2 = "Dev adam"
print(b1 + b2) #ortaya çıkacak sonuç ("12Dev adam") olacaktır
#Dikkat burda belirtilen durum sadece + işlemi için geçerlidir , olurda toplama dışında 2 ve daha çok string değeri diğer matematiksel işlemlere
#tabii tutarsanız direkt olarak hatayla karşı karşıya kalacaksınızdır

# TOPLAMA (+)
#düzgün matematik / Integer değer üzerinden işlem yapma
b3=4
print(b1+b3) #ortaya çıkacak sonuç ("16") olacaktır

# ÇIKARMA (-)
print(b1 - b3)

# ÇARPMA (*)
#Not: Çarpma işleminde 1adet string veri tipi kullanırsanız bu belirtilen string veri tipini kaç kez tekrarlayacağını belirtir
#örn.
print(b2 * b3) # sonuç ("Dev adamDev adamDev adamDev adam") olacaktır

# BÖLME (/)
print(b1 / b3) # sonuç ("3") olacaktır çünki 12 sayısı, 4 rakamına bölünmüştür.

