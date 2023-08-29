def yasHesapla(dogumYılı):
    mevcutYıl=2023
    if dogumYılı>mevcutYıl:
        raise ValueError("Henüz doğmadınız lütfen geçerli bir yıl giriniz. ")

    if dogumYılı==mevcutYıl:
        raise ValueError("Daha yeni doğdunuz yaşınızı hesaplamak için biraz zaman ihtiyaç var. ")
    
    
    yas=mevcutYıl-dogumYılı
    return yas
while True:
    try:
        dogumYılı=int(input("Lütfen doğum yılınızı giriniz: "))
        yas=yasHesapla(dogumYılı)
        print(f"Yaşınız",yas)
        break

    except ValueError as e:
        print(f"Geçerli bir yıl giriniz.{e} ")

   