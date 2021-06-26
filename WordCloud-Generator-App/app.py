import streamlit as st
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import nltk
import os
import base64

from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS
st.set_option('deprecation.showPyplotGlobalUse', False)

#draw config
#mpl.rcParams['figure.figsize']=(8.0,6.0)    #(6.0,4.0)
mpl.rcParams['font.size']=12                #10 
mpl.rcParams['savefig.dpi']=100             #72 
mpl.rcParams['figure.subplot.bottom']=.1 


#function to load the data
def load_data(data):
    df = pd.read_csv(data)
    return df



def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

#-------------------------------------------------------

def main():

   
    menu = ["Generate Word Cloud"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Generate Word Cloud":
        st.title("Generate WordCloud on Ideation Data")
        st.markdown("""
This app generates word cloud on **[Udemy](https://udemy.com) dataset**.
- The data is available here on Kaggle: https://www.kaggle.com/andrewmvd/udemy-courses
""")
        st.subheader("Below dataset is the generated Word Cloud:👇")
        st.write(" ")
        udemy_data = load_data("udemy_courses.csv")
        st.dataframe(udemy_data)
        st.write(" ")

        if st.button("Generate WordCloud"): 

            stopwords = set(STOPWORDS)
            wordcloud = WordCloud(
                                    background_color='white',
                                    stopwords=stopwords,
                                    max_words=1000,
                                    max_font_size=40, 
                                    random_state=42
                                    ).generate(str(udemy_data['course_title']))

            #st.write(wordcloud)
            fig = plt.figure(1)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.show()
            st.pyplot()
            fig.savefig("wordcloud.png", dpi=900)
            cloud_img = wordcloud.to_file("result.png")

            st.markdown(get_binary_file_downloader_html('result.png', 'Output Image'),
            unsafe_allow_html=True)
            

            #frequency distribution
            # top_numbers = 10
            # a = udemy_data['course_title'].str.lower().str.cat(sep=' ')
            # words = nltk.tokenize.word_tokenize(a)
            # word_dist = nltk.FreqDist(words)
            # #st.write(word_dist)
            # result = pd.DataFrame(word_dist.most_common(top_numbers),
            # columns=['Word', 'Frequency'])
            # st.dataframe(result)

if __name__ == '__main__':
    main()