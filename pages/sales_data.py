import streamlit as st
import pandas as pd
import numpy as np

st.warning("This section marks the menu bar")
st.write("Home    Menu    Katalog     Sales")

cabang = st.selectbox("Sort Cabang:", ["Jakarta", "Bandung", "Surabaya"])

if cabang == "Jakarta":
    bar_data = pd.DataFrame({
        'Model' : ['Kijang Innova', 'BR-V', 'Avanza'],
        'Total Penjualan Unit' : [800, 450, 600]
    })
    st.bar_chart(bar_data.set_index('Model'))

elif cabang == "Bandung":
    st.write("Not implemented yet")

elif cabang == "Surabaya":
    st.write("Not implemented yet")