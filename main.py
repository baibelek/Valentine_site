from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    img_dir = os.path.join('static', 'images')
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    
    # Сортируем фото по названию, чтобы был порядок
    photos = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))])
    return render_template('index.html', photos=photos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))