"""
Name: Shashank Reddy Bobbala
Student ID: 22083114
Course: 7PAM2000-0901-2023 - Applied Data Science 1
University: Msc Data Science (SW) with Placement Year
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def linePlot(df):
    '''
    Parameters
    ----------
    df : The dataframe used to plot line graph for plotting the CO2 emission from liquid fuel data

    Returns
    -------
    The function plots the line graphs over the years 2003-2015 for various countries, for the emission of CO2 from liquid fuel consumption
    '''
    df.plot(kind="line", figsize=(10, 5))
    plt.title("CO2 Emissions from Liquid Fuel Consumption")
    plt.xlabel("Year")
    plt.ylabel("CO2 Emissions")
    plt.legend()
    
    # Show the chart
    plt.show()
    
def histogram(filename):
    '''
    Parameters
    ----------
    df : The Dataframe parsed from main function which is extracted from world bank data for analyzing the climate changes.

    Returns
    -------
    The function doesn't return any value but it plots the histogram chart from the parsed dataframe'

    '''
    data = pd.read_csv(filename, skiprows=3)

    # Filter data for the United Kingdom and CO2 emissions from liquid fuel consumption
    data_uk = data[data['Country Name'] == 'United Kingdom']
    data_co2_liq = data_uk[data_uk["Indicator Name"] == 'CO2 emissions from liquid fuel consumption (% of total)']
    data_co2_sol = data_uk[data_uk["Indicator Name"] == 'CO2 emissions from solid fuel consumption (% of total)']
    data_co2_gas = data_uk[data_uk["Indicator Name"] == 'CO2 emissions from gaseous fuel consumption (% of total)']
    
    # Select specific years
    selected_years = ["2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]
    data_selected_years_liq = data_co2_liq[selected_years]
    data_selected_years_sol = data_co2_sol[selected_years]
    data_selected_years_gas = data_co2_gas[selected_years]
    
    # Transpose the data for plotting
    data_transposed_liq = data_selected_years_liq.transpose()
    data_transposed_sol = data_selected_years_sol.transpose()
    data_transposed_gas = data_selected_years_gas.transpose()
    
    # Plotting histogram with years on the x-axis
    data_transposed_liq.plot(kind='bar', legend=False, edgecolor='black')
    plt.title('CO2 Emissions from Liquid Fuel Consumption in the United Kingdom (2003-2015)')
    plt.xlabel('Year')
    plt.ylabel('CO2 Emissions (kt)')
    plt.show()
    
    # Plotting histogram with years on the x-axis
    data_transposed_sol.plot(kind='bar', legend=False, edgecolor='black')
    plt.title('CO2 Emissions from Solid Fuel Consumption in the United Kingdom (2003-2015)')
    plt.xlabel('Year')
    plt.ylabel('CO2 Emissions (kt)')
    plt.show()
    
    # Plotting histogram with years on the x-axis
    data_transposed_gas.plot(kind='bar', legend=False, edgecolor='black')
    plt.title('CO2 Emissions from Gaseous Fuel Consumption in the United Kingdom (2003-2015)')
    plt.xlabel('Year')
    plt.ylabel('CO2 Emissions (kt)')
    plt.show()
    
def barchart(df):
    '''
    Parameters
    ----------
    df : The dataframe used to plotting bar graph for plotting the CO2 emission from liquid fuel data

    Returns
    -------
    The function plots the bar graphs over the years 2005-2015 for various countries, for the emission of CO2 from liquid fuel consumption
    '''
    df = df.loc[:,["2005","2010","2015"]]
    df.plot(kind="bar", figsize=(10, 5))
    plt.title("CO2 emissions from liquid fuel consumption (kt)")
    plt.xlabel("Countries")
    plt.ylabel("CO2 Emission")
    plt.legend()
    plt.show()
    
def readCSV(file):
    '''
    Parameters
    ----------
    file : The file is filename parsed from the main function for reading the database and analyzing the data.

    Returns
    -------
    This function reads the data from the provided filename and create two dataframes where one a coutries as columns and other as year as columns.
    '''
    #read the csv file using pandas
    df = pd.read_csv(file, skiprows=3)

    # Set the index to 'Country Name'
    df.set_index('Country Name', inplace=True)
    
    # List of countries to filter
    countries = ["United Kingdom", "Italy", "Norway", "Finland", "Germany", "Mexico"]
    
    # Filter the DataFrame for the indicator "CO2 emissions from liquid fuel consumption (kt)"
    df_CO2 = df[df["Indicator Name"] == "CO2 emissions from liquid fuel consumption (kt)"]
    
    # Select specific columns for the years 2003 to 2015
    selected_years = ["2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]
    df_CO2 = df_CO2[selected_years]
    
    df_CO2 = df_CO2.loc[countries]
    
    df_CO2_T = df_CO2.transpose()
    
    df_CO2.info()
    df_CO2_T.describe()
    
    linePlot(df_CO2_T)
    barchart(df_CO2)
    
def heatmap(file, country):
    # Selecting the indicators which could be the correlation to one another
    indicators = ['EN.ATM.CO2E.KT', 'EN.ATM.CO2E.LF.KT', 'EN.ATM.CO2E.SF.ZS', 'EN.ATM.CO2E.GF.ZS']

    # Get the data from the World Bank dataset
    data = pd.read_csv(file, skiprows=(3))

    # Clean and format the data for the specified country and required indicators
    data = data.loc[data['Country Name'] == country]
    data = data.loc[data['Indicator Code'].isin(indicators)]
    data = data.loc[:, ["Indicator Name", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]]

    # Drop non-numeric rows
    data = data.dropna(subset=["2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"], how="any", axis=0)

    # Set "Indicator Name" as index
    data.set_index("Indicator Name", inplace=True)

    # Transpose the data for plotting
    data_transposed = data.transpose()

    # Convert data to numeric (excluding the "Country Name" column)
    data_transposed = data_transposed.apply(pd.to_numeric, errors='coerce')

    # Plotting heatmap with the correlation between the mentioned indicators
    plt.figure(figsize=(10, 6))
    sns.heatmap(data_transposed.corr(), annot=True, fmt='.2f', cmap='YlGnBu')

    # Add title and axis labels
    plt.title(f'{country} Indicators Heatmap')
    plt.xlabel('Indicator')
    plt.ylabel('Year')

    # Show the plot
    plt.show()


#Main Function
filename = "API_19_DS2_en_csv_v2_6183479.csv"

#Read the csv file
readCSV(filename)

heatmap(filename,'United Kingdom')
heatmap(filename,'India')
histogram(filename)
