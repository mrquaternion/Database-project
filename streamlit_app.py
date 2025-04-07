import os
import streamlit as st
from sqlalchemy import  create_engine, text
import pandas as pd
from queries import Query_1, Query_2, Query_3, Query_4

# CSS

st.markdown(
    """
    <style>
    .stButton>button {
        font-size: 20px;
        padding: 15px 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# DB_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/postgres"
engine = create_engine(DATABASE_URL, echo=True)

## TODO Faire l'interface ici
def execute_query(query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df

# Streamlit app
st.title("La coupe du monde des nations du football")

# Query 1
if st.button("Équipes avec le plus grand nombre de cartons rouges"):
    df = execute_query(Query_1)
    st.write(df)

# Query 2
if st.button("Arbitres qui ont arbitré le plus de parties"):
    df = execute_query(Query_2)
    st.write(df)

# Query 3
if st.button("Stades qui ont accueilli plus de 5 parties"):
    df = execute_query(Query_3)
    st.write(df)

# Query 4
if st.button("Parties avec un score total supérieur à 6"):
    df = execute_query(Query_4)
    st.write(df)