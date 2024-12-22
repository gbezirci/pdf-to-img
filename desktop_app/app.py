import sys
from pathlib import Path
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                            QWidget, QFileDialog, QLabel, QProgressBar, QScrollArea)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

# Ana dizini Python path'ine ekle
sys.path.append(str(Path(__file__).parent.parent))
from pdf_converter import PDFConverter

class PDFConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.converter = PDFConverter()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('PDF\'den PNG\'ye Dönüştürücü')
        self.setGeometry(100, 100, 800, 600)
        
        # Ana widget ve layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Dosya seçme düğmesi
        self.select_button = QPushButton('PDF Dosyası Seç')
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)
        
        # Durum etiketi
        self.status_label = QLabel('Bir PDF dosyası seçin')
        layout.addWidget(self.status_label)
        
        # İlerleme çubuğu
        self.progress_bar = QProgressBar()
        self.progress_bar.hide()
        layout.addWidget(self.progress_bar)
        
        # Görüntüleri göstermek için kaydırılabilir alan
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        scroll.setWidget(self.scroll_content)
        layout.addWidget(scroll)
        
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'PDF Dosyası Seç', '', 'PDF Dosyaları (*.pdf)'
        )
        
        if file_path:
            self.status_label.setText('Dönüştürülüyor...')
            self.progress_bar.show()
            self.progress_bar.setRange(0, 0)  # Belirsiz ilerleme
            
            try:
                # PDF'yi dönüştür
                image_paths = self.converter.convert_pdf(file_path)
                
                # Görüntüleri göster
                self.show_images(image_paths)
                self.status_label.setText('Dönüştürme tamamlandı!')
                
            except Exception as e:
                self.status_label.setText(f'Hata: {str(e)}')
                
            self.progress_bar.hide()
            
    def show_images(self, image_paths):
        # Önceki görüntüleri temizle
        for i in reversed(range(self.scroll_layout.count())): 
            self.scroll_layout.itemAt(i).widget().setParent(None)
        
        # Yeni görüntüleri ekle
        for i, path in enumerate(image_paths):
            # Görüntü etiketi
            image_label = QLabel(f'Sayfa {i + 1}')
            pixmap = QPixmap(path)
            image_label.setPixmap(pixmap.scaled(
                700, 700, Qt.AspectRatioMode.KeepAspectRatio
            ))
            self.scroll_layout.addWidget(image_label)
            
            # İndirme düğmesi
            download_button = QPushButton(f'Sayfa {i + 1}\'i Kaydet')
            download_button.clicked.connect(
                lambda checked, p=path: self.save_image(p)
            )
            self.scroll_layout.addWidget(download_button)

    def save_image(self, image_path):
        save_path, _ = QFileDialog.getSaveFileName(
            self, 'PNG Kaydet', '', 'PNG Dosyaları (*.png)'
        )
        if save_path:
            pixmap = QPixmap(image_path)
            pixmap.save(save_path, 'PNG')
            self.status_label.setText('Görüntü kaydedildi!')

def main():
    app = QApplication(sys.argv)
    window = PDFConverterApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()