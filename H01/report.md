# H01 - Generic Quadrotor X Sistem Raporu

## 1. Seçilen İHA Modeli

Bu çalışmada Generic Quadrotor X modeli seçilmiştir. Bu model X düzeninde yerleştirilmiş dört motora sahip bir multikopterdir. Sistem; batarya, ESC, motor, uçuş kontrolcüsü, alıcı, telemetri modülü ve görev bilgisayarından oluşmaktadır.

## 2. Bileşenlerin Görevleri

| Bileşen | Görevi |
|---|---|
| Batarya (Battery) | İHA'nın ihtiyaç duyduğu elektrik enerjisini sağlar. |
| ESC | Motorların hızını kontrol eder. |
| Motor / Pervane | İtki üreterek İHA'nın havalanmasını ve hareket etmesini sağlar. |
| Uçuş Kontrolcüsü (Flight Controller) | Sensör verilerini işler ve İHA'nın uçuşunu kontrol eder. |
| Alıcı (Receiver) | Pilotun kumandasından gelen komutları alır. |
| Telemetri (Telemetry) | İHA ile yer istasyonu arasında veri iletişimi sağlar. |
| Görev Bilgisayarı (Companion Computer) | Görüntü işleme ve gelişmiş görevleri gerçekleştirir. |

## 3. Güç Bağlantıları

Batarya, elektrik enerjisini Power Distribution Board (PDB) üzerinden sisteme dağıtır. PDB, ESC'lere güç sağlar ve elektronik bileşenlere uygun voltajda enerji iletilmesine yardımcı olur.

Her ESC bir motoru kontrol eder.

**Güç Akışı:**

Batarya → PDB → ESC → Motor

## 4. Veri ve Kontrol Bağlantıları

Alıcı, pilotun kumanda komutlarını uçuş kontrolcüsüne iletir. Uçuş kontrolcüsü bu komutları ve sensör verilerini değerlendirerek ESC'lere motor kontrol sinyalleri gönderir.

Telemetri modülü, uçuş kontrolcüsü ile yer istasyonu arasında çift yönlü veri iletişimi sağlar.

Kamera görüntüleri görev bilgisayarına aktarılır. Görev bilgisayarı ise uçuş kontrolcüsüyle görev verilerini paylaşır.

**Veri Akışı:**

- Alıcı → Uçuş Kontrolcüsü
- Uçuş Kontrolcüsü → ESC'ler
- Uçuş Kontrolcüsü ↔ Telemetri ↔ Yer İstasyonu
- Kamera → Görev Bilgisayarı
- Görev Bilgisayarı ↔ Uçuş Kontrolcüsü

## 5. Sonuç

İHA sisteminde batarya enerji sağlar, uçuş kontrolcüsü uçuşu yönetir ve ESC'ler motorları kontrol eder. Alıcı pilot komutlarını iletirken telemetri yer istasyonuyla haberleşmeyi sağlar. Görev bilgisayarı ise görüntü işleme gibi gelişmiş görevleri yürütür.