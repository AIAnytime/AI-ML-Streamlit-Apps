import streamlit as st
import streamlit.components.v1 as stc
import numpy
import time
from PIL import Image
import tensorflow as tf
import requests
from io import BytesIO

st.set_option('deprecation.showfileUploaderEncoding', False)

st.set_page_config(
    page_title="Potato Care",
    page_icon="🥔",
    layout="wide"
)

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy Potato Leaf"]

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style.css")



def main():
    st.title("Potato Blight Diseases Identification")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### **Potato Care 🥔**
        This is a simple app that uses **AI** to help you care for your potato.
        """)
        st.markdown("""
        Read more about the [Blight Diseases in Potato](https://www.gardeningknowhow.com/edible/vegetables/potato/potato-blight-diseases.htm).
        """)

        st.markdown("""
        #### **Instructions**
        1. Choose an image to upload or paste an image URL.
        2. Click on **Identify** button.
        """)

        st.markdown("""See samples images here: [Sample1](https://i.ibb.co/6cQH7qN/Early-blight-on-a-potato-plant-Solanum-tuberosum-This-blight-is-caused-by-the-fungus-Alternaria-sola.jpg)  [Sample2](https://i.ibb.co/5Kg518C/ca2020-early-blight-potato-damage1.png) [Sample3](
https://i.ibb.co/t2kRTwv/potato-leaf-isolated-on-white-full-depth-of-field-field-with-clipping-path-2-ATDN6-E.jpg)""")
      
        st.markdown("""
        #### **Credits**
        * **Created by:** [Sonu Kumar](https://www.linkedin.com/in/sonucr7/)👋""")

        menu = st.radio("Select Image Upload Option 👇", ("Upload an Image", "Use Image URL"))

        if menu == "Upload an Image":
            image_file = st.file_uploader("Upload an image of Potato's leaf", type = ['jpg', 'jpeg', 'png'])
            if image_file is not None:
                image = Image.open(image_file)
        elif menu == "Use Image URL":
            image_url = st.text_input("Enter Image URL (Press Enter to apply)")
            try:
                if image_url is not None:
                    with st.spinner('Downloading Image...'):
                        response = requests.get(image_url)
                        image = Image.open(BytesIO(response.content))
                else:
                    st.error("Please enter a valid URL")
            except:
                pass
        
        # image_file = st.file_uploader("Upload an image of Potato's leaf", type = ['jpg', 'jpeg', 'png'])


    with col2:
        try:
            if image is not None:
                show_image = image.resize((700, 450), Image.ANTIALIAS)
                st.image(show_image, caption='Uploaded Image.', use_column_width=True)
                if st.button("Identify"):
                    new_model = tf.keras.models.load_model('potatoes.h5')
                    if new_model is not None:
                        image_array = numpy.asarray(image)
                        image_array = numpy.expand_dims(image_array, axis=0)
                        predictions = new_model.predict(image_array)
                        predicted_class = CLASS_NAMES[numpy.argmax(predictions[0])]
                        confidence = round(100 * (numpy.max(predictions[0])), 2)
                        st.write(" ")
                        with st.spinner("Model is running..."):
                            time.sleep(2)
                        st.success("This is {} with {:.2f}% confidence.".format
                        (predicted_class, confidence))
        except:
            pass
                        





if __name__ == '__main__':
    main()