from pdf2image import convert_from_path
import os
from pathlib import Path

class PDFConverter:
    def __init__(self):
        # Çıktı klasörünü oluştur
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
    
    def convert_pdf(self, pdf_path):
        """
        PDF dosyasını PNG'ye dönüştürür ve dosya yollarını döndürür
        """
        try:
            # PDF'yi görüntülere dönüştür
            images = convert_from_path(pdf_path)
            
            # Her sayfayı PNG olarak kaydet
            image_paths = []
            for i, image in enumerate(images):
                # Çıktı dosya adını oluştur
                output_file = self.output_dir / f"page_{i + 1}.png"
                
                # Görüntüyü kaydet
                image.save(str(output_file), "PNG")
                image_paths.append(str(output_file))
            
            return image_paths
            
        except Exception as e:
            raise Exception(f"PDF dönüştürme hatası: {str(e)}")
