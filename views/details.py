import streamlit as st
import pandas as pd
import numpy as np

def load_view():    
    st.title('Details Page')

    @st.cache_data(ttl=600)
    def load_data(sheets_url: str):
        csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
        return pd.read_csv(csv_url)

    df = load_data(st.secrets["price_table"])

    makers = []
    for row in df.itertuples():
        if(not makers.__contains__(row.Maker)):
            makers.append(row.Maker)

    selectedMaker = st.selectbox("Filter by Maker:", makers)
    tablef1 = df[df['Maker'] == selectedMaker]

    genmodels = []
    for row in tablef1.itertuples():
        if(not genmodels.__contains__(row.Genmodel)):
            genmodels.append(row.Genmodel)

    selectedGenmodel = st.selectbox("Filter by Genmodel:", genmodels)
    tablef2 = tablef1[tablef1['Genmodel'] == selectedGenmodel]
    st.table(tablef2)

    tableDropped = tablef2.drop(['Maker', 'Genmodel', 'Genmodel_ID'], axis = 1)

    year = []
    entry_price = []
    for row in tableDropped.itertuples():
        year.append(row.Year)
        entry_price.append(row.Entry_price)

    chart_data = pd.DataFrame({selectedGenmodel : entry_price}, index = year)

    st.line_chart(chart_data)