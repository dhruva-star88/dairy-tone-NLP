import streamlit as st
import plotly.express as px
from functions import get_pos_scores, get_neg_scores, get_dates

# Give the Title
st.title("Dairy Tone")
# "Positivity" Header
st.header("Positivity")
# Mention the Attributes of the graph
figure = px.line(x=get_dates(), y=get_pos_scores(), labels={"x": "Date", "y": "Positivity"})
# Render the graph
st.plotly_chart(figure)

# "Negativity" Header
st.header("Negativity")
# Mention the Attributes of the graph
figure = px.line(x=get_dates(), y=get_neg_scores(), labels={"x": "Date", "y": "Negativity"})
# Render the graph
st.plotly_chart(figure)
