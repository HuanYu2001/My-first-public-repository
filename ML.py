import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# 載入你的模型
model = tf.keras.models.load_model('your_model.h5')

def predict_image(img):
    # 預處理圖片
    img = img.resize((150, 150))
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # 使用模型進行預測
    prediction = model.predict(img_array)
    return prediction[0][0]

def main():
    st.title("貓狗圖片辨識")
    uploaded_file = st.file_uploader("請選擇一張圖片", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='上傳的圖片')
        prediction = predict_image(image)
        if prediction > 0.5:
            st.write("這是一隻狗！")
        else:
            st.write("這是一隻貓！")

if __name__ == "__main__":
    main()
