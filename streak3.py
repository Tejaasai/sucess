import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


st.title('My First Dashboard')

file_upload=st.file_uploader('Upload csv file',type='CSV')

if file_upload is None:
    st.write('CSV file is not uploaded')

else:
    df=pd.read_csv(file_upload)
    st.subheader('Preview of the data')
    st.dataframe(df)

    columns1=df.columns.to_list()
    selected_column=st.sidebar.selectbox('select the value',columns1)


    if selected_column=='price':
        st.subheader('Price analysis')
        # col1,col2=st.columns(2)

        # with col1:
            
        fig=plt.figure()
        sns.histplot(x=df[selected_column],kde=True,color='skyblue')
        plt.title('Price analysis using Histogram')
        st.pyplot(fig)

        # with col2:
        fig=plt.figure()
        sns.boxplot(x=df[selected_column],color='lightgreen')
        plt.title('Price analysis using boxplot')
        st.pyplot(fig)

    elif selected_column=='name':
        wordcloud=WordCloud(height=400,width=800,background_color='white').generate(' '.join(df[selected_column]))
        fig=plt.figure()
        plt.imshow(wordcloud,interpolation='bilinear')
        plt.title('Analysis using wordcloud')
        plt.axis('off')
        st.pyplot(fig)


    elif selected_column=='rating':
        fig=plt.figure()
        sns.countplot(x=df[selected_column],palette='viridis')
        plt.title('Rating analysis')
        st.pyplot(fig)

    else:
        df[selected_column]=df[selected_column].str.replace('%','').astype(int)
        st.write('Products with highest discount')
        st.dataframe(df.nlargest(10,'discount')[['name','price','discount']])


        







    


