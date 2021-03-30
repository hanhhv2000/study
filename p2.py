import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.title("Share Price analysis for May 2019 to May 2020:")
st.sidebar.title("Share Price analysis for May 2019 to May 2020:")
st.markdown(
    "This application is a Share Price dashboard for Top 5 Gainers and Losers:")
st.sidebar.markdown(
    "This application is a Share Price dashboard for Top 5 Gainers and Losers:")

html_string = "<h3>this is an html string</h3>"

st.markdown(html_string, unsafe_allow_html=True)
