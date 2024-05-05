import streamlit as st
from PIL import Image
import requests
from bs4 import BeautifulSoup
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

model = load_model('FV.h5')

labels = {0: 'elma', 1: 'muz', 2: 'pancar', 3: 'biber', 4: 'lahana', 5: 'biber', 6: 'havuç',
          7: 'karnabahar', 8: 'acı biber', 9: 'mısır', 10: 'salatalık', 11: 'patlıcan', 12: 'sarımsak', 13: 'zencefil',
          14: 'üzüm', 15: 'jalapeno', 16: 'kivi', 17: 'limon', 18: 'marul',
          19: 'mango', 20: 'soğan', 21: 'portakal', 22: 'kapya biber', 23: 'armut', 24: 'bezelye', 25: 'ananas',
          26: 'nar', 27: 'patates', 28: 'turp', 29: 'soya fasulyesi', 30: 'ıspanak', 31: 'mısır', 32: 'tatlı patates',
          33: 'domates', 34: 'şalgam', 35: 'karpuz'}

fruits = ['Elma', 'Muz', 'Biber', 'Acı Biber', 'Üzüm', 'Jalapeno', 'Kivi', 'Limon', 'Mango', 'Portakal',
          'Kapya Biber', 'Armut', 'Ananas', 'Nar', 'Karpuz']
vegetables = ['Şalgam', 'Lahana', 'Biber', 'Havuç', 'Karnabahar', 'Mısır', 'Salatalık', 'Patlıcan', 'Zencefil',
              'Marul', 'Soğan', 'Bezelye', 'Patates', 'Turp', 'Soya Fasulyesi', 'Ispanak', 'Mısır', 'Tatlı Patates',
              'Domates', 'Şalgam']


def fetch_calories(prediction):
    try:
        url = 'https://www.google.com/search?q=kalori ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        kaloriler = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return kaloriler
    except Exception as e:
        st.error("Kaloriler alınamıyor")
        print(e)


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


def run():
    st.title("Meyve🍍-Sebze🍅 Sınıflandırma")
    img_file = st.file_uploader("Resim Seçiniz", type=["jpg", "png"])
    if img_file is not None:
        img = Image.open(img_file).resize((250, 250))
        st.image(img, use_column_width=False)
        save_image_path = './images/' + img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        # if st.button("Predict"):
        if img_file is not None:
            result = prepare_image(save_image_path)
            if result in vegetables:
                st.info('**Kategori : Sebze**')
            else:
                st.info('**Kategori : Meyve**')
            st.success("**Tahmin Edilen : " + result + '**')
            cal = fetch_calories(result)
            if cal:
                st.warning('**' + cal + '(100 grams)**')


run()
