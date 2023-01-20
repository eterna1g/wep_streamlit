import io
import streamlit as st
from PIL import Image
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
import numpy as np

def load_model():
    return EfficientNetB0(weights='imagenet')

def preprocess_image(img):
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x


def load_image():
    uploaded_file = st.file_uploader(label='Оберіть зображення')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None

def print_predictions(preds):
    classes = decode_predictions(preds, top=3)[0]
    for cl in classes:
        print(cl[1], cl[2])

model = load_model()

st.title('Класифікація зображень')
img = load_image()
result = st.button('розпізнати зображення')
if result:
    x = preprocess_image(img)
    preds = model.predict(x)
    st.write("результати розпізнавання")
    print_predictions(preds)
    classes = decode_predictions(preds, top=3)[0]
    for cl in classes:
        st.write((cl[1], cl[2]))
