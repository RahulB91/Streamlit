import streamlit as st
import pandas as pd
st.subheader('Upload the csv file')    #Upload
df=st.file_uploader("Upload the csv file ",type=['csv','xlsx'])


st.subheader('Load the csv file')   #load
df=pd.read_csv('Football.csv')
if df is not None:
    st.table(df.head())

st.subheader('Dealing with image directly')   #lmage
st.image('AI.png')

st.subheader('Dealing with image Indirectly')   #lmage
im=st.file_uploader("Upload the image file ",type=['png','jpeg'])
if im is not None:
    st.image('AI.png')


st.subheader('Dealing with video')
vdfile=st.file_uploader("Upload the video file ",type=['mp4','mkv'])
if vdfile is not None:
    st.video(vdfile,start_time=0)

st.subheader('Dealing with Audio')
adfile=st.file_uploader("Upload the Audio file ",type=['mp3','wav'])
if adfile is not None:
    st.audio(adfile.read())
