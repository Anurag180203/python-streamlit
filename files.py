import streamlit as st
import pandas as pd

file = st.file_uploader("upload a CSV file:", type=["csv","xlsx"])



if file is not None:
    df = pd.read_csv(file)
    st.table(df.head(10)) # you may also use st.dataframe(df)

st.subheader("Dealing with images")

image1 = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])
if image1 is not None:
    st.image(image1,width=500,caption="Uploaded Image") # you may also use exact file path instead of image1

st.subheader('Working with videos')
video_file = st.file_uploader("Upload a video", type=["mp4","mkv"])
if video_file is not None:
    st.video(video_file,start_time=0)

st.subheader('Working with audio')
audio_file = st.file_uploader("Upload an audio", type=["mp3","wav"])
if audio_file is not None:
    st.audio(audio_file)