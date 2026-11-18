# H01 - İHA Temel Bileşenleri

## 1. Batarya (Battery)
İHA sisteminin ihtiyaç duyduğu elektrik enerjisini sağlar. Motorlar ve elektronik bileşenler enerjilerini bataryadan alır.

## 2. ESC (Electronic Speed Controller)
Uçuş kontrolcüsünden gelen komutlara göre motorun hızını kontrol eder.

## 3. Motor (Brushless Motor)
Elektrik enerjisini mekanik harekete dönüştürür ve pervaneyi döndürerek itki üretir.

## 4. Uçuş Kontrolcüsü (Flight Controller)
Sensörlerden gelen verileri değerlendirir aracın dengesini ve hareketlerini kontrol eder. Motorlara gönderilecek komutları hesaplar.

## 5. Alıcı (Receiver)
Pilotun kumandadan gönderdiği kontrol komutlarını alarak uçuş kontrolcüsüne iletir.

## 6. Telemetri (Telemetry)
İHA ile yer istasyonu arasında çift yönlü veri iletişimi sağlar. Uçuş bilgileri yer istasyonuna aktarılır.

## 7. Görev Bilgisayarı (Companion Computer)
Kamera görüntülerini işleme, nesne tanıma ve otonom görevler gibi gelişmiş işlemleri gerçekleştirir.

---

## Güç Yolu

Batarya → ESC → Motor

## Bilgi ve Kontrol Yolu

Alıcı → Uçuş Kontrolcüsü → ESC → Motor

Telemetri ↔ Yer İstasyonu

Kamera → Görev Bilgisayarı

---

## Sonuç

İHA sisteminde batarya enerji sağlar, uçuş kontrolcüsü karar verir ve ESC motorları sürer. Alıcı pilotun komutlarını taşırken telemetri araç ile yer istasyonu arasındaki veri iletişimini sağlar. Görev bilgisayarı ise görüntü işleme ve gelişmiş görevleri yürütür.