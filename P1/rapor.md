# Batarya ve mesafeye göre karar

Bu çalışma bir programlama alıştırmasıdır; eşikler örnek amaçlı seçilmiştir ve uçuş ayarı değildir. Programda hücre sayısı 4, hücre başına en düşük örnek voltaj 3,7 V ve en yüksek örnek mesafe 1000 m olarak tanımlandı. Önce toplam voltaj dörde bölünür; ardından düşük voltaj öncelikli olarak, sonra mesafe karşılaştırılır.

## Giriş → hesap → karar

| Toplam voltaj | Mesafe | Hücre başına hesap | Program kararı |
|---:|---:|---:|---|
| 15,2 V | 500 m | 15,2 / 4 = 3,80 V | Devam et |
| 14,6 V | 500 m | 14,6 / 4 = 3,65 V | Bataryayı şarj et |
| 15,2 V | 1600 m | 15,2 / 4 = 3,80 V | Mesafe çok uzak |

## Üç terminal çıktısı

### 1. giriş

```text
> python p1_karar.py
Toplam batarya voltajını girin (V): 15.2
Mesafeyi girin (m): 500
Hücre başına voltaj: 3.80 V
Karar: Devam et
```

### 2. giriş

```text
> python p1_karar.py
Toplam batarya voltajını girin (V): 14.6
Mesafeyi girin (m): 500
Hücre başına voltaj: 3.65 V
Karar: Bataryayı şarj et
```

### 3. giriş

```text
> python p1_karar.py
Toplam batarya voltajını girin (V): 15.2
Mesafeyi girin (m): 1600
Hücre başına voltaj: 3.80 V
Karar: Mesafe çok uzak
```

## Kararlar için kısa açıklamalar

- **Devam et:** Hücre başına 3,80 V örnek alt sınırın üzerinde ve 500 m örnek mesafe sınırın içindedir.
- **Bataryayı şarj et:** Hücre başına 3,65 V, örnek 3,7 V alt sınırının altındadır.
- **Mesafe çok uzak:** Hücre başına voltaj yeterli olsa da 1600 m, örnek 1000 m mesafe sınırını aşar.

## Kısa araştırma

Python belgelerine göre `input()` kullanıcıdan bir satır alır ve sonucu metin (`str`) olarak verir; `float()` bu metni ondalıklı sayıya dönüştürebilir. Böylece voltajı bölme ve eşiklerle sayısal karşılaştırma yapmak mümkün olur. [Python yerleşik fonksiyonları belgeleri](https://docs.python.org/3/library/functions.html#input)

## Soru: `input()` sonucunu neden sayıya çevirdin?

`input()` her zaman metin döndürdüğü için voltajı bölmek ve sayıları karşılaştırmak amacıyla `float()` ile sayıya çevirdim. Mesafe tam sayı olarak girildiğinden onu `int()` ile dönüştürdüm.
