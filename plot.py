import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff
# Altair Scatter plot
st.header('Altair Scatter Plot')
chart_data=pd.DataFrame(np.random.randn(500,5), columns=['a','b','c','d','e'])
chart=alt.Chart(chart_data).mark_circle().encode(x= 'a', y='b',size='c',
            tooltip=['a','b','c','d','e'])
st.altair_chart(chart)

st.header('Interactive charts')
st.subheader('Line charts')
df=pd.read_csv('lang_data.csv')
lang_list=df.columns.tolist()
lang_choice=st.multiselect('choose your language',lang_list)
new_df=df[lang_choice]
st.line_chart(new_df)

st.subheader('Area charts')
st.area_chart(new_df)

st.header('Data Visualization with Plotly')
st.subheader('Display the Data')
df=pd.read_csv('tips.csv')
st.dataframe(df.head())

st.subheader('Pie chart ')
fig=px.pie(df, values='total_bill', names='day')
st.plotly_chart(fig)

st.subheader('Pie chart with multiple parameter ')
fig=px.pie(df, values='total_bill', names='day',opacity=.7,
     color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader('Histogram')
x1=np.random.randn(200) -2
x2=np.random.randn(200)
x3=np.random.randn(200) +2

hist_data=[x1,x2,x3]
group_labels=['Group-1', 'Group-2','Group-3']
fig=ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
st.plotly_chart(fig)
