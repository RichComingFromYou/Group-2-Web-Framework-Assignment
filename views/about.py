import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def load_view():    
    st.title('About Page')
    image = Image.open('D:\\Kerich\\UAS SEMES 6\\UAS WebDevPython\\Group-2-Web-Framework-Assignment\\assets\\Photo\\Logo Website.png')
    st.image(image, caption='Made By Vannes Cristian')

    st.divider()

    st.header("Company History")
    image = Image.open('D:\\Kerich\\UAS SEMES 6\\UAS WebDevPython\\Group-2-Web-Framework-Assignment\\assets\\Photo\\Apollo.png')
    st.image(image, caption='The Greek God Apollo and his Solar Chariot')
    st.write("Apollo's Wheel originated from 4 young adults who dreamed of having their own start up company. The name 'Apollo's wheel' originated from the Greek God's himself Apollo, while the 'wheel' is referring to his famous Solar Chariot where he rode through the sky every day to bring light to the world. The idea is we hope that we as a company could also be the bringer of light, the bringer of good news, and the name itself sounds really cool")
    st.write("Our enthusiastic passion about cars drives us to make it more accessible for everyone to access any information regarding cars. whether physically, emotionally, or mentally, our desire to share our passion will never cease to end.")
   
    st.divider()
    
    st.header("Company Motto")
    st.write("Our Company Motto is 'Bringing You The Most Accurate Information There Is'")

    st.divider()

    st.header("Company Founder")
    st.write("- Vincent George Chandra  \n- Timmothy James Wijaya  \n- Vannes Cristian  \n- Kerich")

    st.divider()

    st.header("Website Developer")
    st.write("Kelompok 2")

    st.divider()

    st.header("Contact")
    st.write("No. Handphone: 087777420727")
    st.write("Email: apollo.wheels@gmail.com")