import streamlit as st
import pandas as pd
import plotly.express as px

def aqi_data_component():
    st.title("AQI DATA")
    
    # Load the air quality dataset
    df = pd.read_csv('./final_data.csv')

    # Remove rows with missing values in the date column
    # df = df.dropna(subset=['Date'])

    # Convert the date column to a datetime object
    # print(type(df['Date'][0]))
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    print(type(df['Date'][0]))

    # ------------- Pollutants Diagram -----------------
    # Create a selectbox widget to allow the user to select the city
    cities = df['City'].unique()
    selected_city = st.selectbox('Select city', cities)

    # Filter the data to only include rows for the selected city
    df = df[df['City'] == selected_city]

    # Create a multiselect widget to allow the user to select the pollutants to display
    pollutants = st.multiselect('Select pollutants', ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene'])

    # Create a scatter plot to display the selected pollutants over time for each city
    if pollutants:
        chart_data = df.melt(id_vars=['Date', 'City'], value_vars=pollutants, var_name='pollutant', value_name='level')
        fig = px.scatter(chart_data, x='Date', y='level', color='pollutant')
        
        # Update the title of each subplot
        fig.update_layout({'xaxis1': {'title': {'text': f'Air Quality of {selected_city}'}}})
        
        st.plotly_chart(fig, width=800, height=600)
        
    else:
        st.write('Please select at least one pollutant.')



    # ------------- Indicators Acceptable Levels -----------------
    # Create a DataFrame with the acceptable levels of various air pollutants
    data = {'Pollutant': ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene'],
            'Acceptable Level': [12, 50, 53, 100, 100, 100, 9, 75, 70, 5, 7.5, 150]}
    acceptable_levels = pd.DataFrame(data)

    # Set the index of the acceptable_levels DataFrame to the 'Pollutant' column
    acceptable_levels = acceptable_levels.set_index('Pollutant')

    # Define a CSS style for centering text in a column
    css_style = """
    <style>
        td:nth-child(2) {
            text-align: center;
        }
    </style>
    """
    # Display the acceptable levels as a table without row numbers
    st.markdown(f'## Level of Air Pollutants in {selected_city}')

    # Group the data by city and year
    grouped = df.groupby([df['City'], df['Date'].dt.year])

    # Calculate the mean of each pollutant column
    annual_averages = grouped[['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']].mean().round(1)

    # Reset the index to move the group labels into columns
    annual_averages = annual_averages.reset_index()

    # Rename the 'Date' column to 'Year'
    annual_averages = annual_averages.rename(columns={'Date': 'Year'})

    # Melt the annual_averages DataFrame to create a long format table
    long_table = annual_averages.melt(id_vars=['City', 'Year'], var_name='Pollutant', value_name='Value')

    # Filter the data to only include rows for the selected city
    long_table = long_table[long_table['City'] == selected_city]

    # Pivot the long_table DataFrame to create a wide format table with columns for each year
    pollutant_table = long_table.pivot_table(index='Pollutant', columns='Year', values='Value')

    # Reindex the pollutant_table DataFrame to match the order of pollutants in the acceptable_levels DataFrame
    pollutant_table = pollutant_table.reindex(acceptable_levels.index)
    # Add a column for the acceptable levels
    pollutant_table.insert(0, 'Acceptable Level', acceptable_levels['Acceptable Level'])

    # Convert the DataFrame to an HTML table
    html_table2 = pollutant_table.to_html(formatters={'Acceptable Level': '{:,.0f}'.format})
    # st.markdown(css_style + html_table2, unsafe_allow_html=True)


    # Display the resulting table
    st.dataframe(pollutant_table)




    #Map 

    #Implementations - Air Quality Policies 
    #About the World 
        