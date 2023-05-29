import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit.components.v1 import html
import utils as utl

st.set_page_config(layout= "wide" ,page_title= "Apollos Wheel")
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

col1, col2 = st.columns(2)

from views import about,details,sales_data

def navigation():
    route = utl.get_current_route()
    if route == "about":
        about.load_view()
    elif route == "details":
        details.load_view()
    elif route == "sales data":
        sales_data.load_view()
    else:   
        with st.columns(3)[1]:
         style = "<style>h2 {text-align: center;}</style>"
         st.markdown(style, unsafe_allow_html=True)
         st.header("WELCOME TO")
         image = Image.open("Logo Website.png")
         st.image(image, caption='Made By Vannes Cristian')
         st.image("https://www.kimballstock.com/images/car-stock-photos/cutout-car-images.jpg")  

        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            st.markdown('<a href="/?nav=about" target="_self"> <button style="font-size: 20px; width: 100%; color: white; border: 2px solid black; background-color:#57A0D2; border-radius: 12px; padding: 15px 32px;">ABOUT</button></a>', unsafe_allow_html=True)
        with col2:
            st.markdown('<a href="/?nav=sales%20data" target="_self"> <button style="font-size: 20px; width: 100%; color: white; border: 2px solid black; background-color:#57A0D2; border-radius: 12px; padding: 15px 32px;">SALES DATA</button> </a>', unsafe_allow_html=True)
        with col3:
            st.markdown('<a href="/?nav=details" target="_self"> <button style="font-size: 20px; width: 100%; color: white; border: 2px solid black; background-color:#57A0D2; border-radius: 12px; padding: 15px 32px;">DETAIL</button> </a>', unsafe_allow_html=True)

        # st.image("https://www.kimballstock.com/images/car-stock-photos/cutout-car-images.jpg")
        # st.image("https://www.kimballstock.com/images/car-stock-photos/cutout-car-images.jpg")
        
navigation()