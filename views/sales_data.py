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
    df = load_data(st.secrets["sales_table"])

    makers = []
    for row in df.itertuples():
        if(not makers.__contains__(row.Maker)):
            makers.append(row.Maker)

    selectedMaker = st.selectbox("Filter by Maker:", makers)
    table = df[df['Maker'] == selectedMaker]
    st.table(table)

    # Remove Maker and Genmodel ID from table
    table = table.drop(['Maker', 'Genmodel_ID'], axis = 1)

    # Transpose Column to row and row to column
    table = table.T 
    header_row = table.iloc[0]
    table.columns = header_row
    table = table.drop(['Genmodel'], axis = 0)

    st.line_chart(table)