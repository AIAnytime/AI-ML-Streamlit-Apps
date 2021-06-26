import streamlit as st 
import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import seaborn as sns
import altair as alt
from PIL import Image
#------------------------------------------------------------------------------------
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(layout="wide") 

# Load data function
@st.cache
def load_data(data):
    df = pd.read_csv(data)
    return df




def main():
    menu = ["Home", "Data and EDA", "Cluster Modeling", "About Me"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.title("Septic Tank Analytics App")
        st.write(" ")
        st.header("You can find the original data from the below link:")
        st.write("https://data-goldcoast.opendata.arcgis.com/datasets/617f6190e6014b74a55c3acba021804f_0/about")
        st.write("")
        originalData = pd.read_csv("Storage_Tank.csv")
        st.dataframe(originalData)
        st.write("")
        st.markdown(
"""### **This is an explorer app to perform some basic task of data preprocessing and machine learning modeling (clustering in this case).**"
## Explore the options in Menu (Left Side)
- **Exploratory Data Analysis**
- **Machine Learning Modeling Results**
"""
)



    elif choice == "Data and EDA":
        st.title("Exploratory Data Analysis")
        st.write(" ")
        st.subheader("Below is a processed version of the data:")
        X = pd.read_csv("final_data.csv")
        st.dataframe(X)
        st.write("")
        col1,col2 = st.beta_columns([2,1])
        with col2:
            if st.checkbox("Records Inside Data"):
                st.write(X.shape)
        with col1:
            if st.checkbox("Show Data Inputs/Parameters"):
                all_columns = X.columns.to_list()
                st.write(all_columns)
        col1, col2 = st.beta_columns([2,1])
        with col1:
            if st.checkbox("Distribution Of Tank Material"):
                tank_var = X['tank_material'].value_counts()
                st.write(tank_var)
                tank_var_plot = X['tank_material'].value_counts().plot(kind='pie')
                st.write(tank_var_plot)
                st.pyplot()
        with col2:
            if st.checkbox("Show Tank Positioning"):
                st.subheader("Underground or Not?")
                st.write(X['tank_underground'].value_counts().plot(kind = 'bar', color = 'red'))
                st.pyplot()
        col1, col2 = st.beta_columns([2,1])
        with col1:
            if st.checkbox("Show Tank Elements Distribution"):
                tank_elements_var = X['tank_contents'].value_counts()
                st.write(tank_elements_var)
                plt.figure(figsize= (10,12))
                st.write(X['tank_contents'].value_counts().plot(kind = 'pie'))
                st.pyplot()
        with col2:
            if st.checkbox("Volume Inside The Tank"):
                st.write("Maximum Volume in Septic Tank:",X['volume'].max())
                st.write("Minimum Volume in Septic Tank:",X['volume'].min())
                st.write("Average Volume in Septic Tank:",X['volume'].mean())
                st.subheader("Distribution of Volume")
                plt.figure(figsize= (4,6))
                plt.hist(X['volume'])
                plt.xlabel('Volume inside the tank')
                plt.ylabel('Total Number Count')
                st.pyplot()
    
    elif choice == "Cluster Modeling":
        st.title("Machine Learning Modeling Result (Clustering)")
        col1, col2 = st.beta_columns([1,1])
        with col1:
            st.header("Data Prepared For Clustering")
            cluster_data = pd.read_csv("cluster_data.csv")
            st.dataframe(cluster_data)
        with col2:
            first_image = Image.open('elbow.png')
            st.write("")
            st.image(first_image, width = 500)
        st.write("")
        if st.checkbox("Show Clusters and MAP Results"):
            st.header("2D Plot")
            second_image = Image.open('2d.png')
            st.image(second_image)
            st.write("")
            col1, col2 = st.beta_columns([1,1])
            with col1:
                st.header("3D Plot")
                third_image = Image.open('newplot.png')
                st.image(third_image)
            with col2:
                st.header("Pipeline Intercluster Distance Map")
                fourth_image = Image.open("pipeline.png")
                st.image(fourth_image)
            col1, col2 = st.beta_columns([2,1])
            with col1:
                st.header("Cluster Distributions")
                fifth_image = Image.open("distribution.png")
                st.image(fifth_image)
            with col2:
                st.header("Silhouette Metrics")
                sixth_image = Image.open("sil.png")
                st.image(sixth_image)

    else:
        st.markdown(""" ## About Me 👋
**I am an AI Evangelist, Content Creator, and Technopreneur, Currently working on multiple fronts where Deep Learning and Computer Vision are mysterious, including understanding business needs, rethinking AI capacity, and research opportunities that leads to a better society.**
  



###  Find me here :point_down:

-  **Sonu Kumar** :raised_hand:

*  _Email:_  **sonu1000raw@gmail.com**

*  _LinkedIn:_  **[Sonu Kumar](https://www.linkedin.com/in/sonucr7/)**


*  _GitHub:_  **[sonucr7](https://github.com/sonucr7)**

""")
                        

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
            


if __name__ == '__main__':
    main()