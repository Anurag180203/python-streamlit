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


