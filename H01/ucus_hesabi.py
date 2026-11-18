kapasite_mah = 5000      # batarya kapasitesi
kullanilabilir = 0.8     # bataryanin en fazla %80'ini kullan
ortalama_akim_a = 18     # havada asili dururken toplam akim
toplam_agirlik_g = 1600  # batarya dahil kalkis agirligi
motor_itkisi_g = 950     # tam gazda tek motor itkisi
motor_sayisi = 4

sure_dk = kapasite_mah / 1000 * kullanilabilir / ortalama_akim_a * 60
itki_agirlik = motor_itkisi_g * motor_sayisi / toplam_agirlik_g

print(f"Yaklasik ucus suresi: {sure_dk:.1f} dk")
print(f"Itki/agirlik orani: {itki_agirlik:.2f} (en az 2 olmali)")
