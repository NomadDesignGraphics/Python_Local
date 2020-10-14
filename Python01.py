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
print(12+4) #ortaya çıkacak sonuç ("16") olacaktır

# ÇIKARMA (-)
print(12 - 4) # sonuç ("8") olacaktır

# ÇARPMA (*)
#Not: Çarpma işleminde 1adet string veri tipi kullanırsanız bu belirtilen string veri tipini kaç kez tekrarlayacağını belirtir
#örn.
print(b2 * 4) # sonuç ("Dev adamDev adamDev adamDev adam") olacaktır

# BÖLME (/)
print(12 / 4) # sonuç ("3") olacaktır çünki 12 sayısı, 4 rakamına bölünmüştür.

###Veri tipi değiştirme 
#yukarda belirttiğim "b1" değişkeninde 12 aslında bir string ifadedir
#şimdi bunu integer bir değer e çevirecez
c1 = int(b1) #Bu kodda şimdi c1 değişkeni , b1 değişkeninde belirtilen sayının string ifadeden integer ifadeye dönüştürülmüştür
print(c1 * 4) #sonuç ("48") olacaktır 

###if-else
#öyleyse yada değilse için oluşturulmuş kodlardır bütün yazılım dillerinde vardır hepsinde farklılık gösterecektir ama ortak yönlerle
#biz python dan devam edelim 
if a1 > c1:
  print("18 sayısı 12 den büyüktür") 
  else:
  print("nasıl oldu bilmiyorum ama 18 rakamı 12 den küçük geldi")
#Şimdi burda ne oldu diye sorarsanız sisteme sorgu göndermiş oldunuz ve sorguda 
#(a1 değşkeninde belirtilen veri c1 değişkeninde belirtilen veriden büyükse [18 sayısı 12 den büyüktür] yazar)
#şayet a1 değişkenindeki veri c1 değişkeninden küçük kalsaydı "else" kısmında belirtilen kod harekete geçirilecektir
