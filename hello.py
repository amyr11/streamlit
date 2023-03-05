import streamlit as st

st.write('# Calculator V2.0')
col1, col2 = st.columns([1, 1])
first = col1.number_input('Insert first number')
second = col2.number_input('Insert second number')
sum = first + second

st.write(f'## = {sum}')
