import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df = pd.read_csv("state_wise.csv")
df['Date'] = df['Last_Updated_Time'].astype('datetime64[ns]')

st.set_page_config(page_title='Streamlit Dashboard',
                   layout='wide',
                   page_icon='💹')

st.markdown("<h1 style='text-align: center; color: red;'>COVID19 DASHBOARD - INDIA</h1>",
            unsafe_allow_html=True)

st.markdown('This dashboard visualizes the current Covid-19 Situation in India')


st.markdown("<h2 style='text-align: center;'>CASES ACROSS INDIA</h2>",
            unsafe_allow_html=True)

# kpi 1

con, rec, det, act = st.beta_columns(4)

with con:
    st.markdown("**Total Confirmed Cases**")
    num1 = df['Confirmed'][0]
    st.markdown(
        f"<h2 style='text-align: center; color: blue;'>{num1}</h2>", unsafe_allow_html=True)

with rec:
    st.markdown("**Recovered Cases**")
    num2 = df['Recovered'][0]
    st.markdown(
        f"<h2 style='text-align: center; color: green;'>{num2}</h2>", unsafe_allow_html=True)

with det:
    st.markdown("**Deaths**")
    num3 = df['Deaths'][0]
    st.markdown(
        f"<h2 style='text-align: center; color: red;'>{num3}</h2>", unsafe_allow_html=True)

with act:
    st.markdown("**Active Cases**")
    num3 = df['Active'][0]
    st.markdown(
        f"<h2 style='text-align: center; color: orange;'>{num3}</h2>", unsafe_allow_html=True)

st.markdown("---")


st.markdown("## Chart Section: 1")

#st.line_chart(df['Date'], df['Recovered'])
fig = px.line(df, x="Date", y="Recovered")
st.plotly_chart(fig)


st.markdown("## Chart Section: 2")

first_chart, second_chart = st.beta_columns(2)


with first_chart:
    chart_data = pd.DataFrame(np.random.randn(100, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with second_chart:
    chart_data = pd.DataFrame(np.random.randn(
        2000, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)


fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="State", hover_data=["Confirmed", "Recovered", "Deaths"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(fig, use_container_width=True)
