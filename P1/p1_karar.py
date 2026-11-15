"""Batarya ve mesafeye göre örnek karar alıştırması.

Kullanılan eşikler eğitim amaçlıdır; gerçek bir uçuş ayarı değildir.
"""

HUCRE_SAYISI = 4
MIN_HUCRE_VOLT = 3.7
MAKS_MESAFE_METRE = 1000

try:
    toplam_volt = float(input("Toplam batarya voltajını girin (V): "))
    mesafe_metre = int(input("Mesafeyi girin (m): "))
except ValueError:
    print("Hata: Voltaj için sayı, mesafe için tam sayı girin.")
else:
    hucre_volt = toplam_volt / HUCRE_SAYISI
    print(f"Hücre başına voltaj: {hucre_volt:.2f} V")

    if hucre_volt < MIN_HUCRE_VOLT:
        karar = "Bataryayı şarj et"
    elif mesafe_metre > MAKS_MESAFE_METRE:
        karar = "Mesafe çok uzak"
    else:
        karar = "Devam et"

    print(f"Karar: {karar}")
