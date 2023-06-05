import streamlit as st

st.title('title -> GeeksforGeeks')
st.header('header -> This is a header message')
st.subheader('subheader -> This is a subheader message')
st.text('text -> Hello GeeksforGeeks')

st.markdown('markdown -> Streamlit is **_really_ cool**.')
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('###### Hi')

st.success('Data is submitted successfully')
st.info('This is an information message')
st.warning('This is a warning message')
st.error('This is an error message')

st.exception(ZeroDivisionError('Division not possible with 0'))

st.help(ZeroDivisionError)

st.write(range(1,10))
st.write(1+2+3)
st.write('1+2+3')
st.write('This is a string', 1.0, 2.0)

st.code('x=10\n'
        'for i in range(x):\n'
            '\tprint(i)\n')

st.checkbox('Male')
st.checkbox('Female')

if(st.checkbox('Adult')):
    st.write('You are an adult')

radioButton = st.radio('Select :' ,('Male','Female','Other'))
if(radioButton == 'Male'):
    st.write('You are a male')
elif(radioButton == 'Female'):
    st.write('You are a female')
else:
    st.write('You are an other gender')

st.subheader('Select Box')
Selectbox = st.selectbox('Data Science : ', ['Data Analysis', 'Web Scraping', 'Machine Learning', 'Deep Learning', 'Natural Language Processing','Computer Vision','Image Processing'])
st.write('You selected : ', Selectbox)

st.subheader('MultiSelect Box')
multiselectbox = st.multiselect('Data Science : ', ['Data Analysis', 'Web Scraping', 'Machine Learning', 'Deep Learning', 'Natural Language Processing','Computer Vision','Image Processing'])
st.write('You selected : ', len(multiselectbox), 'options, which are', multiselectbox)

st.subheader('Button')
if(st.button('Click me')):
    st.write('Button is clicked')

st.subheader('Slider')
vol = st.slider('Slide me', min_value = 0, max_value = 100, value = 50, step = 5)
st.write('You selected : ', vol)

st.subheader('Text Input')
name = st.text_input('Enter your Username : ')
password = st.text_input('Enter your Password : ', type = 'password')
if name:
    st.write('Your name is : ', name)

st.subheader('Text Area')
textarea = st.text_area('Write something interesting about yourself in 500 words',max_chars=5000)
st.write('You wrote : ', textarea)  

st.subheader('input number')
age = st.number_input('Enter age : ', min_value = 1, max_value = 100)
st.write('Your age is : ', age)

st.subheader('input date')
date = st.date_input('Enter date')
st.write('Date is : ', date)

st.subheader('input time')
time = st.time_input('Enter time')
st.write('Time is : ', time)

