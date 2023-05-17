import streamlit as st
import pandas as pd
import numpy as np

def load_view():    
    st.title('Sales Data Page')

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

@st.cache_data(ttl=600)
def load_data(sheets_url: str):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

# terus code dibawah ini tuh buat ngeload aja, bukan buat nampilin datanya
df = load_data(st.secrets["public_gsheets_url"])

maker = []
genmodel = []

# Show the data
for row in df.itertuples():
    maker.append(row.Maker)
    genmodel.append(row.Genmodel)
    
    # Tadi yang salah disini
    # car = pd.DataFrame({"Maker" : maker, "Genmodel" : genmodel })

# variable car hrs ny d luar loop
car = pd.DataFrame({"Maker" : maker, "Genmodel" : genmodel })

st.table(car) # setelah variable "car" ny d luar, pke st.table()
