import streamlit as st
import pandas as pd
import plotly.express as px

# Loading the dataset
cars = pd.read_csv('vehicles_us.csv')

# Title of the Web App
st.title('Vehicle Data Analysis')

# Project Description and Libraries Used
st.markdown("""
This web app analyzes and plots vehicle data
* **Python libraries:** pandas, streamlit, base64, plotly.express
* **Data source:** CSV File
""")

# Adding a column that shows just the manufacturer 
cars['manufacturer'] = cars['model'].apply(lambda x: x.split()[0])

# Displaying the dataframe
st.header('Data Viewer')
st.dataframe(cars)


# Finding duplicated and missing values in the dataframe

cars.duplicated().sum()

cars.isnull().sum()

# Filling missing model year values with unknown
cars['model_year'] = cars['model_year'].fillna(value='unknown')

# Filling missing number of cylinders with the mean. This is because there were no outliers in the limited range of possibilities of number of cylinders.
cars['cylinders'] = cars['cylinders'].fillna(value=cars['cylinders'].mean())

# I wasn't sure what to replace the unknown odometer values with (median, mean, or unknown).

# Filling missing odometer color values with unknown as the range in possibile values is very large and likely contains outliers
cars['odometer'] = cars['odometer'].fillna(value='unknown')

# Filling missing paint color values with unknown
cars['paint_color'] = cars['paint_color'].fillna(value='unknown')

# Filling missing values in this column with - to keep the column as type bool.
cars['is_4wd'] = cars['is_4wd'].fillna(value=0)

# Plotting a scatterplot with relationship between model year and vehicle price. The checkbox is to...
check = st.checkbox('Show Model Year to Price Scatter Plot')

if check:
    fig = px.scatter(cars, x='model_year', y='price', title='Vehicle Model Year to Price')
    st.plotly_chart(fig)

# Plotting an interactive bar chart with the model year and conditions of the car
fig2 = px.bar(cars, x='model_year', y='condition', color='condition', title='Vehicle Model Year to Condition')
st.plotly_chart(fig2)

# Plotting a scatterplot with a line of best fit correlating days listed for sale with price of vehicle
fig3 = px.scatter(cars, x='days_listed', y='price', hover_name='model', trendline='ols', trendline_color_override='pink', title='Correlation of Days Listed to Sale Price')
st.plotly_chart(fig3)
