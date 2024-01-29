import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

char_data=pd.DataFrame(np.random.randn(20,3), columns=['Line-1','Line-2','Line-3'])

st.subheader('Line Chart')
st.line_chart(char_data)

st.subheader('Area Chart')
st.area_chart(char_data)

st.subheader('Bar Chart')
st.bar_chart(char_data)

st.header('Working with Data Visualization matplotlib and seaborn')
st.subheader('Loading the DataFrame')
df=pd.read_csv('iris.csv')
st.dataframe(df)

st.subheader('Bar graph with matplotlib')
fig=plt.figure(figsize=(10,5))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)


st.subheader('Distribution Plot with seaborn')
fig=plt.figure(figsize=(10,5))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.header('Multiple Graphs in one columns')
col1,col2=st.columns(2)
with col1:
    col1.header='KDE=False'
    col1.write('KDE=False')
    fig1=plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'],kde=False)
    st.pyplot(fig1)
with col2:
    col2.header='Hist=False'
    col1.write('KDE=False')
    fig2=plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'],hist=False)
    st.pyplot(fig2)

st.header('Changing Style')
col1,col2=st.columns(2)
with col1:
    fig=plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig)
with col2:
    fig=plt.figure()
    sns.set_theme(context='poster', style='darkgrid')
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig)

st.header('Exploring Diffrent Graphs')
st.subheader('Scatter Plot')
fig,ax=plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader('Count Plot')
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df, x='species')
st.pyplot(fig)

st.subheader('Box Plot')
fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df, x='species',y='petal_length')
st.pyplot(fig)

st.subheader('Violin Plot')
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df, x='species',y='petal_length')
st.pyplot(fig)
