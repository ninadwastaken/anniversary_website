import streamlit as st
st.set_page_config(layout='wide')


st.markdown("<h1 style='text-align: center; color: white;'>HAPPY THIRD BABYYYYYYYYYYY <3<3<3</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>youre fr amaaaaaaaaaaaaaaazing</h1>", unsafe_allow_html=True)
st.info("hope the flight wasnt tiring.")
st.info(r"i love you a while True: print('i love you') lot.")
st.info("wanna squeeze. also look at this")
st.info("you're so beautiful, could look at this forever <3")


with open("imagenames.txt",'r') as f:
    files = [path[:-1] for path in f.readlines()]
files[-1] = files[-1] + "g"

col1, col2 = st.columns(2)

with col1:
    for file in files[::2]:
        st.image(f"images/{file}")
with col2:
    for file in files[1::2]:
        st.image(f"images/{file}")

st.markdown("<h1 style='text-align: center; color: white;'>i love you so much cant wait to hold you</h1>", unsafe_allow_html=True)





