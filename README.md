# PDF'den PNG'ye Dönüştürücü

Bu proje, PDF dosyalarını PNG formatına dönüştüren hem web hem de masaüstü uygulaması sunar. Her iki uygulama da aynı PDF dönüştürme motorunu kullanır ve benzer özellikler sunar.

## Özellikler

### Web Uygulaması
- Sürükle-bırak ile kolay dosya yükleme
- Tüm sayfaları önizleme
- Her sayfayı ayrı ayrı indirme
- Duyarlı tasarım ile mobil uyumluluk
- İlerleme göstergesi

### Masaüstü Uygulaması
- Basit ve kullanıcı dostu arayüz
- Dosya gezgini ile PDF seçme
- Dönüştürme ilerleme göstergesi
- Sayfaları önizleme
- Her sayfayı ayrı kaydetme seçeneği

## Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- Poppler (PDF işleme için gerekli)

### Poppler Kurulumu

#### Windows
1. [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/) adresinden poppler-windows paketini indirin
2. İndirilen dosyayı bir klasöre çıkarın
3. Çıkarılan klasörü sistem PATH değişkenine ekleyin

#### MacOS
```bash
brew install poppler
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install poppler-utils
```

### Python Bağımlılıklarının Kurulumu

```bash
pip install -r requirements.txt
```

## Kullanım

### Web Uygulaması

1. Terminal veya komut istemcisinde web_app klasörüne gidin:
```bash
cd web_app
```

2. Flask uygulamasını başlatın:
```bash
python app.py
```

3. Tarayıcınızda `http://localhost:5000` adresine gidin

### Masaüstü Uygulaması

1. Terminal veya komut istemcisinde desktop_app klasörüne gidin:
```bash
cd desktop_app
```

2. Uygulamayı başlatın:
```bash
python app.py
```

## Proje Yapısı

```
pdf-to-img/
├── README.md
├── requirements.txt
├── pdf_converter.py           # Ana dönüştürme modülü
├── web_app/
│   ├── app.py                # Flask web uygulaması
│   └── templates/
│       ├── index.html        # Ana sayfa şablonu
│       └── result.html       # Sonuç sayfası şablonu
└── desktop_app/
    └── app.py                # PyQt6 masaüstü uygulaması
```

## Güvenlik Notları

- Uygulama, yüklenen PDF dosyalarını geçici olarak saklar
- İşlem tamamlandıktan sonra dosyalar otomatik olarak temizlenmez
- Hassas bilgiler içeren PDF'ler için dosyaları manuel olarak temizlemeniz önerilir

## Katkıda Bulunma

1. Bu projeyi fork edin
2. Yeni bir özellik dalı oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: özet'`)
4. Dalınıza push yapın (`git push origin yeni-ozellik`)
5. Bir Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
