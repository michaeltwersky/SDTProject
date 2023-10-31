import streamlit as st
import pandas as pd
import plotly.express as px

cars = pd.read_csv('C:/Users/User/Documents/TripleTen/Sprints/Sprint 4/SDTProject/vehicles_us.csv')

st.title('Vehicle Data Analysis')

st.markdown("""
This web app analyzes and plots vehicle data
* **Python libraries:** pandas, streamlit, base64, plotly.express
* **Data source:** CSV File
""")

cars['manufacturer'] = cars['model'].apply(lambda x: x.split()[0])

st.header('Data Viewer')
st.dataframe(cars)



cars.duplicated().sum()

cars.isnull().sum()

cars['model_year'] = cars['model_year'].fillna(value='unknown')
cars['cylinders'] = cars['cylinders'].fillna(value=cars['cylinders'].mean())
# I wasn't sure what to replace the unknown odometer values with (median, mean, or unknown).
cars['odometer'] = cars['odometer'].fillna(value='unknown')
cars['paint_color'] = cars['paint_color'].fillna(value='unknown')
cars['is_4wd'] = cars['is_4wd'].fillna(value='unknown')

fig = px.scatter(cars, x='model_year', y='price', title='Vehicle Model Year to Price')
st.plotly_chart(fig)


fig2 = px.bar(cars, x='model_year', y='condition', color='condition', title='Vehicle Model Year to Condition')
st.plotly_chart(fig2)

fig3 = px.scatter(cars, x='days_listed', y='price', hover_name='model', trendline='ols', trendline_color_override='pink', title='Correlation of Days Listed to Sale Price')
st.plotly_chart(fig3)