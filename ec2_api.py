import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from flask import Flask, jsonify, request

model = load_model('FV.h5')

labels = {0: 'elma', 1: 'muz', 2: 'pancar', 3: 'biber', 4: 'lahana', 5: 'biber', 6: 'havuç',
          7: 'karnabahar', 8: 'acı biber', 9: 'mısır', 10: 'salatalık', 11: 'patlıcan', 12: 'sarımsak', 13: 'zencefil',
          14: 'üzüm', 15: 'jalapeno', 16: 'kivi', 17: 'limon', 18: 'marul',
          19: 'mango', 20: 'soğan', 21: 'portakal', 22: 'kapya biber', 23: 'armut', 24: 'bezelye', 25: 'ananas',
          26: 'nar', 27: 'patates', 28: 'turp', 29: 'soya fasulyesi', 30: 'ıspanak', 31: 'mısır', 32: 'tatlı patates',
          33: 'domates', 34: 'şalgam', 35: 'karpuz'}


def prepare_image(img_path):
    img = load_img(img_path, target_size=(224, 224, 3))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    print(res)
    return res.capitalize()


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def infer_image():
    if 'file' not in request.files:
        return jsonify(error="Please try again. The Image doesn't exist")

    file = request.files.get('file')
    img_bytes = file.read()
    img_path = "./upload_images/test.jpg"
    with open(img_path, "wb") as img:
        img.write(img_bytes)
    result = prepare_image(img_path)
    return jsonify(prediction=result)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
