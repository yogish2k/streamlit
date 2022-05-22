# https://www.youtube.com/watch?v=Sb0A9i6d320
import pandas as pd
# import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
df = pd.read_excel(
    io="c:\\Users\\YOGI\\Downloads\\supermarkt_sales.xlsx",
    engine='openpyxl',
    sheet_name='Sales',
    skiprows=3,
    usecols='B:R',
    nrows=1000,

)

# st.dataframe(df)
st.sidebar.header("Please Filter Here")
city = st.sidebar.multiselect(
    "select the city here",
    options=df["City"].unique(),
    default=df["City"].unique()
)

gender = st.sidebar.multiselect(
    "select the Gender here",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

customer_type = st.sidebar.multiselect(
    "select the Customer_type here",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)

st.dataframe(df_selection)

