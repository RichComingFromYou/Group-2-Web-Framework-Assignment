import streamlit as st
import pandas as pd
import numpy as np
import utils as utl

st.set_page_config(page_title= "Apollos Wheel")
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

from views import about,details, sales_data

def navigation():
    route = utl.get_current_route()
    if route == "about":
        about.load_view()
    elif route == "analysis":
        details.load_view()
    elif route == "options":
        sales_data.load_view()
        
navigation()

# Fix image layout later
st.image("https://www.kimballstock.com/images/car-stock-photos/cutout-car-images.jpg")
st.image("https://www.kimballstock.com/images/car-stock-photos/cutout-car-images.jpg")
