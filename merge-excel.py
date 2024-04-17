import pandas as pd
import time


city_states = {
    'Ahmedabad': 'Gujarat',
    'Amaravati': 'AndhraPradesh',
    'Amritsar': 'Punjab',
    'Bengaluru': 'Karnataka',
    'Bhopal': 'MadhyaPradesh',
    'Brajrajnagar': 'Odisha',
    'Chandigarh': 'Punjab',
    'Chennai': 'TamilNadu',
    'Coimbatore': 'TamilNadu',
    'Delhi': 'Delhi',
    'Ernakulam': 'Kerala',
    'Gurugram': 'Haryana',
    'Guwahati': 'Assam',
    'Hyderabad': 'Telangana',
    'Jaipur': 'Rajasthan',
    'Kochi': 'Kerala',
    'Kolkata': 'WestBengal',
    'Lucknow': 'UttarPradesh',
    'Mumbai': 'Maharasthra',
    'Patna': 'Bihar',
    'Shillong': 'Meghalaya',
    'Talcher': 'Odisha',
    'Thiruvananthapuram': 'Kerala',
    'Visakhapatnam': 'AndhraPradesh'
}

# Now you can access the state corresponding to each city
for city in city_states:
    print(f"{city}: {city_states[city]}")

for city in city_states :

    print(f"{city}: {city_states[city]}")

    df1 = pd.read_csv("air_quality_data.csv")

    column_name = 'City'
    filter_value = city

    print('filter_value '+filter_value)

    df1 = df1[df1[column_name] == filter_value]

    state=''
    df2 = pd.read_excel(f"./state-wise-data/{city_states[city]}.xlsx")
    df2 = df2.drop(columns=['To Date','Station','State'])

    column_name_mapping = {
        'Ozone': 'O3',
        'From Date':'Date'
    }
    df2 = df2.rename(columns=column_name_mapping)

    df2['Date'] = pd.to_datetime(df2['Date'], format='%d-%m-%Y %H:%M')

    df2['Date'] = df2['Date'].dt.strftime('%Y-%m-%d')


    df2 = df2[df2[column_name] == filter_value]

    desired_column_order = ['City', 'Date', 'PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3']  
    df2 = df2[desired_column_order]           
    # print(df2)


    result = pd.merge(df1, df2, on=['City', 'Date', 'PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3'], how='outer')
    # time.sleep(3)


    print(result)

    result.to_csv("final_data.csv", mode='a', header=False, index=False)

