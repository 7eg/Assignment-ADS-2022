import streamlit as st 
import pandas as pd
import altair as alt
GPAPP = pd.read_csv('assignment\googleplaystore.csv')
GPAPP['Price'] = GPAPP['Price'].str.replace('$','')
GPAPP['Price'] = GPAPP['Price'].str.replace('Everyone','0')
GPAPP['Reviews'] = GPAPP['Reviews'].str.replace('M','')
GPAPP = GPAPP.astype({'Price':float,'Reviews':float})
st.title('googleplay Application')
GPAPP.astype({'Rating':float})
playStoreApp = st.selectbox("Select App Price", GPAPP['Price'].unique())
st.write(playStoreApp)
plot_type = st.radio("select the plot type",['scatter','line'])
if plot_type == 'scatter':
  pl = alt.Chart(GPAPP[GPAPP['Price'] == playStoreApp]).mark_circle().encode(
    x = 'Rating',
    y = 'Price',
    tooltip = ['Rating','Price']
).interactive()
else:
  pl = alt.Chart(GPAPP[GPAPP['Price'] == playStoreApp]).mark_line().encode(
    x = 'Rating',
    y = 'Price',
    tooltip = ['Rating','Price']
).interactive()
st.altair_chart(pl)
