import streamlit as st
import pandas as pd
import plotly.express as px

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
    st.markdown("<h3 style='text-align: center;'>Confirmed Cases</h3>",
                unsafe_allow_html=True)
    num1 = df['Confirmed'][0]
    st.markdown(
        f"<h2 style='text-align: center; color: blue;'>{num1}</h2>", unsafe_allow_html=True)

with rec:
    st.markdown("<h3 style='text-align: center;'>Recovered Cases</h3>",
                unsafe_allow_html=True)
    num2 = df['Recovered'][0]
    st.markdown(
        f"<h2 style='text-align: center; color: green;'>{num2}</h2>", unsafe_allow_html=True)

with det:
    st.markdown("<h3 style='text-align: center;'>Deceased Cases</h3>",
                unsafe_allow_html=True)
    num3 = df['Deaths'][0]
    st.markdown(
        f"<h2 style='text-align: center; color: red;'>{num3}</h2>", unsafe_allow_html=True)

with act:
    st.markdown("<h3 style='text-align: center;'>Active Cases</h3>",
                unsafe_allow_html=True)
    num3 = df['Active'][0]
    st.markdown(
        f"<h2 style='text-align: center; color: orange;'>{num3}</h2>", unsafe_allow_html=True)

st.markdown("---")

# kpi2

df1 = pd.read_csv(
    "https://api.covid19india.org/csv/latest/case_time_series.csv")

st.markdown("<h2 style='text-align: center;'>Visualizing Total and Daily Cases</h2>",
            unsafe_allow_html=True)

first_chart, second_chart = st.beta_columns(2)

with first_chart:
    fig = px.line(df1, x="Date", y=["Total Confirmed",
                                    "Total Deceased", "Total Recovered"], title="Total Confirmed, Recovered and Deceased")
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)

with second_chart:
    fig = px.line(df1, x="Date", y=["Daily Confirmed",
                                    "Daily Deceased", "Daily Recovered"], title="Daily Confirmed, Recovered and Deceased")
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# kpi3
st.write(df1.head())

# Scattermap

fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="State", hover_data=["Confirmed", "Recovered", "Deaths", "Active"],
                        color_discrete_sequence=["darkblue"], zoom=3.3, height=500)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.markdown("## State-wise, detailed Scattermap")
st.plotly_chart(fig, use_container_width=True)
