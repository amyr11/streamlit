import streamlit as st

st.write('# Calculator')
first = st.number_input('Insert first number')
second = st.number_input('Insert second number')
sum = first + second

st.write(f'## = {sum}')
