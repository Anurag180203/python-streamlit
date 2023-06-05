import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

chartdata = pd.DataFrame(np.random.randn(20,3),columns=['Line1','Line2','Line3'])

st.subheader('Line Chart')
st.line_chart(chartdata)

st.subheader('Area Chart')
st.area_chart(chartdata)

st.subheader('Bar Chart')
st.bar_chart(chartdata)

st.header('Data Visualisation with Matplotlib and Seaborn')
st.subheader('Loading the dataframe')
iris = sns.load_dataset('iris')
st.dataframe(iris)

st.subheader('Distribution Plot with Matplotlib')
fig = plt.figure(figsize=(15,8))
iris['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Distribution Plot with seaborn')
fig = plt.figure(figsize=(15,8))
sns.distplot(iris['sepal_length'])
st.pyplot(fig)

st.subheader('Working with multiple graphs')
fig = plt.figure(figsize=(16,8))
plt.subplot(2,2,1).bar(iris['sepal_length'],iris['sepal_width']).set_label('Sepal')
plt.subplot(2,2,1).legend()
plt.subplot(2,2,2).hist(iris['petal_length'],bins=10)
plt.subplot(2,2,3).plot(iris['sepal_length'],iris['petal_length'])
plt.subplot(2,2,4).plot(iris['sepal_width'],iris['petal_width'])
plt.tight_layout()
st.pyplot(fig)

st.header('Multiple graphs in one row')

col1,col2 = st.columns(2)
with col1:
    col1.header = 'KDE = False'
    fig1 = plt.figure(figsize=(5,5))
    sns.distplot(iris['sepal_length'],kde=False)
    st.pyplot(fig1)

with col2:
    col2.header = 'Hist = False'
    fig2 = plt.figure(figsize=(5,5))
    sns.distplot(iris['sepal_length'],hist=False)
    st.pyplot(fig2)

st.header('Changing the style of the graph')
col1,col2 = st.columns(2)
with col1:
    fig1 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(iris['petal_length'],hist=False)
    st.pyplot(fig1)

with col2:
    fig2 = plt.figure()
    sns.set_theme(style='darkgrid',context='notebook')
    sns.distplot(iris['petal_length'],hist=False)
    st.pyplot(fig2)

st.header('Exploring different Graphs')

st.subheader('Scatter Plot')
fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader('Count Plot')
fig = plt.figure(figsize=(15,8))
sns.countplot(data = iris,x = 'species')
st.pyplot(fig)

st.subheader('Box Plot')
fig = plt.figure(figsize=(15,8))
sns.boxplot(data = iris,x='species',y='petal_length')
st.pyplot(fig)

st.subheader('Violin Plot')
fig = plt.figure(figsize=(15,8))
sns.violinplot(data = iris,x='species',y='petal_length')
st.pyplot(fig)