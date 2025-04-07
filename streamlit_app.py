import streamlit as st
from sqlalchemy import  create_engine, text
import pandas as pd
from queries import Query_1, Query_2, Query_3, Query_4

DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL, echo=True)

## TODO Faire l'interface ici 