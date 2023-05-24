import streamlit as st
import pandas as pd
import numpy as np

def load_view():    
    st.title('Details Page')

    # Fix image layout later
    # st.image("https://www.kimballstock.com/images/car-stock-photos/cutout-car-images.jpg")

    # st.write("Rp. 491.000.000,-")
    # st.write("Kijang Innova Zenix")
    # st.write("Honda")
    # st.write("Gasoline 2.0 G CVT")
    # st.write("M20A-FKS 4 cylinders, in-line 16-Valve DOHC, chain drive Dual VVT-i")

    @st.cache_data(ttl=600)
    def load_data(sheets_url: str):
        csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
        return pd.read_csv(csv_url)

    # terus code dibawah ini tuh buat ngeload aja, bukan buat nampilin datanya
    df = load_data(st.secrets["price_table"])

    maker = []
    genmodel = []
    year = []
    Entry_price = []

    # Show the data
    for row in df.itertuples():
        maker.append(row.Maker)
        genmodel.append(row.Genmodel)
        year.append(row.Year)
        Entry_price.append(row.Entry_price)

    price = pd.DataFrame({"Maker" : maker, "Genmodel" : genmodel, "Year" : year, "Entry Price" : Entry_price})

    st.table(price) # setelah variable "price" ny d luar, pke st.table()