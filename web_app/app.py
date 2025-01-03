from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os
from pathlib import Path
import sys
from PIL import Image
import io

# Ana dizini Python path'ine ekle
sys.path.append(str(Path(__file__).parent.parent))
from pdf_converter import PDFConverter

app = Flask(__name__)

# Dosya yükleme klasörünü yapılandır
UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# PDF dönüştürücüyü başlat
converter = PDFConverter()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'pdf_file' not in request.files:
        return 'Dosya yüklenmedi', 400
    
    file = request.files['pdf_file']
    if file.filename == '':
        return 'Dosya seçilmedi', 400
        
    if file and file.filename.endswith('.pdf'):
        # Dosyayı güvenli bir şekilde kaydet
        filename = secure_filename(file.filename)
        filepath = app.config['UPLOAD_FOLDER'] / filename
        file.save(str(filepath))
        
        try:
            # PDF'yi PNG'ye dönüştür
            image_paths = converter.convert_pdf(str(filepath))
            return render_template('result.html', images=image_paths)
            
        except Exception as e:
            return str(e), 500
            
    return 'Geçersiz dosya türü', 400

@app.route('/compress', methods=['POST'])
def compress_image():
    try:
        # İstek parametrelerini al
        image_path = request.form.get('image_path')
        quality = int(request.form.get('quality', 50))  # Varsayılan kalite %50
        
        if not image_path or not Path(image_path).exists():
            return jsonify({'error': 'Görsel bulunamadı'}), 404

        # Görseli aç
        with Image.open(image_path) as img:
            # Sıkıştırılmış görsel için yeni dosya adı oluştur
            compressed_path = Path(image_path).parent / f"compressed_{Path(image_path).name}"
            
            # Görseli sıkıştır ve kaydet
            img.save(
                str(compressed_path),
                'PNG',
                optimize=True,
                quality=quality
            )
            
            return jsonify({
                'success': True,
                'compressed_path': str(compressed_path),
                'original_size': Path(image_path).stat().st_size,
                'compressed_size': Path(compressed_path).stat().st_size
            })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
