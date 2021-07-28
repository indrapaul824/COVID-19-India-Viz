import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Streamlit Dashboard',
                   layout='wide',
                   page_icon='💹')


st.markdown("<h1 style='text-align: center;'>Main KPIs</h1>",
            unsafe_allow_html=True)

# kpi 1

kpi1, kpi2, kpi3 = st.beta_columns(3)

with kpi1:
    st.markdown("**First KPI**")
    num1 = 111
    st.markdown(
        f"<h1 style='text-align: center; color: red;'>{num1}</h1>", unsafe_allow_html=True)

with kpi2:
    st.markdown("**Second KPI**")
    num2 = 222
    st.markdown(
        f"<h1 style='text-align: center; color: red;'>{num2}</h1>", unsafe_allow_html=True)

with kpi3:
    st.markdown("**Third KPI**")
    num3 = 333
    st.markdown(
        f"<h1 style='text-align: center; color: red;'>{num3}</h1>", unsafe_allow_html=True)

st.markdown("---")

# second row

st.markdown("<h1 style='text-align: center;'>Secondary KPIs</h1>",
            unsafe_allow_html=True)

first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.beta_columns(
    6)


with first_kpi:
    st.markdown("**First KPI**")
    number1 = 111
    st.markdown(
        f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**Second KPI**")
    number2 = 222
    st.markdown(
        f"<h1 style='text-align: center; color: yellow;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Third KPI**")
    number3 = 333
    st.markdown(
        f"<h1 style='text-align: center; color: yellow;'>{number3}</h1>", unsafe_allow_html=True)

with fourth_kpi:
    st.markdown("**First KPI**")
    number1 = 111
    st.markdown(
        f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with fifth_kpi:
    st.markdown("**Second KPI**")
    number2 = 222
    st.markdown(
        f"<h1 style='text-align: center; color: yellow;'>{number2}</h1>", unsafe_allow_html=True)

with sixth_kpi:
    st.markdown("**Third KPI**")
    number3 = 333
    st.markdown(
        f"<h1 style='text-align: center; color: yellow;'>{number3}</h1>", unsafe_allow_html=True)

st.markdown("---")


st.markdown("## Chart Section: 1")

first_chart, second_chart = st.beta_columns(2)


with first_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with second_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)


st.markdown("## Chart Section: 2")

first_chart, second_chart = st.beta_columns(2)


with first_chart:
    chart_data = pd.DataFrame(np.random.randn(100, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with second_chart:
    chart_data = pd.DataFrame(np.random.randn(
        2000, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
