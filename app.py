import streamlit as st
#>python -m streamlit run app.py


st.title('Welcome to Geeks for Geeks')       #title tag
st.header('Hello Data Science Geeks')        #header tag
st.subheader('Hello World program ')    #subheader tag
st.text('Text')                      #text tag

st.markdown('# HI')
st.markdown('## HI')
st.markdown('### HI')           #markdown tag
st.markdown('#### HI')
st.markdown('##### HI')
st.markdown('HI')

st.success('Data is submitted')      #success tag

st.info('Information')             #info tag

st.warning('Warning')           #warning tag

st.error('Error')              #error tag

exp=ZeroDivisionError('not divide by zero')
st.exception(exp)                                         #exception tag


st.help(ZeroDivisionError)                   #help tag

st.write("range(1,10)")
st.write(range(1,10))                     #write tag
st.write(1+2+3)

st.code('x=10 \n'
         'for i in range(x): \n'      #code tag
               '\tprint(i)')

st.checkbox('Male')             #checkbox tag
if(st.checkbox('Adult')):
    st.write('you are an Adult')            #checkbox tag with validation




rb=st.radio('Select ',('Male','Female','Other'))
if(rb=='Male'):                                             #radio button tag
    st.write('You are a Male')
elif(rb=='Female'):
    st.write('You are a Female')
elif(rb=='Other'):
    st.write('You are a Other')

st.subheader('Select Box')             #selectbox tag
selectbox=st.selectbox("Data Science: ", ['Data Analysis', 'Machine Learning','Deep Learning','Web Scrapping','Computer vision'])
st.write("You are selected",selectbox)

st.subheader('Multi Select Box')
mltsltbox=st.multiselect("Data Science: ", ['Data Analysis', 'Machine Learning','Deep Learning','Web Scrapping','Computer vision'])
st.write("You are selected",len(mltsltbox),'courses')

st.subheader('Button')
if(st.button('Click me')):
    st.write("Thanks for clicking")                    #button tag


st.subheader('Slider')            #Slider
vol=st.slider('Select the volume',1,100,step=1)
st.write("Volume is: ",vol)


st.subheader('Text input')          #Text input
name=st.text_input('UserName: ')
password=st.text_input('Password: ',type='password')

st.subheader('Text Area')      #text Area
text_Area=st.text_area('Write intersting on yourself')

st.subheader('input Number')   #input Number
st.number_input("Select your Age ",18,110)

st.subheader('input Date')   #input Date
st.date_input("Date")

st.subheader('input Date')   #input time
st.time_input("Time")
