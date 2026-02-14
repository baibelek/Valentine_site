from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Путь к папке с картинками
    img_dir = os.path.join('static', 'images')
    
    # Создаем папку, если её нет, чтобы код не выдал ошибку
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
        
    # Получаем список файлов в папке static/images
    photos = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('index.html', photos=photos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
