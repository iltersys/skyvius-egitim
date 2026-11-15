# P1 - Batarya ve mesafeye göre karar

## Ne yaptım?

Python programı toplam batarya voltajını 4 hücreye bölerek hücre başına voltajı hesaplar. Örnek eşiklere göre batarya ve mesafeyi değerlendirip bir karar yazdırır.

## Nasıl çalıştırılır?

Bu klasörde terminal açıp çalıştır:

```powershell
python p1_karar.py
```

Örnek girişler: `15.2` ve `500`; `14.6` ve `500`; `15.2` ve `1600`. Voltajı ondalık noktayla, mesafeyi metre cinsinden tam sayı olarak gir.

## Ne buldum?

15,2 V / 4 = 3,80 V/hücre olduğunda 500 m için karar “Devam et”; 14,6 V / 4 = 3,65 V/hücre olduğunda karar “Bataryayı şarj et”; 15,2 V ve 1600 m olduğunda karar “Mesafe çok uzak” olur. Üç terminal çıktısı ve hesap tablosu `rapor.md` dosyasındadır.

## Dosyalar

- `p1_karar.py` - alıştırma programı
- `rapor.md` - giriş, hesap, karar tablosu, terminal çıktıları ve kısa araştırma
