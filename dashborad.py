import streamlit as st


st.markdown("## KPI First Row")

# kpi 1

kpi1, kpi2, kpi3 = st.beta_columns(3)

with kpi1:
    st.markdown("**First KPI**")
    num1 = 111
    st.markdown(
        f"<h1 style='text-align: center; color: red;'>{num1}</h1>", unsafe_allow_html=True)

with kpi2:
    st.markdown("**First KPI**")
    num2 = 222
    st.markdown(
        f"<h1 style='text-align: center; color: red;'>{num2}</h1>", unsafe_allow_html=True)

with kpi3:
    st.markdown("**First KPI**")
    num3 = 333
    st.markdown(
        f"<h1 style='text-align: center; color: red;'>{num3}</h1>", unsafe_allow_html=True)
