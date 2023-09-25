import pandas as pd
import matplotlib.pyplot as plt

# Saves the Spotify data as a Pandas frame
data = pd.read_csv('cost_of_living.csv')

# This limits the results down to just the country name and their cost of living score. Failed Attempt
USA = data.loc[data['Countries'] == 'USA', 'Countries']
USA_Cost = data.loc[data['Countries'] == 'USA', 'Cost of living, 2017']
UK = data.loc[data['Countries'] == 'UK', ['Countries', 'Cost of living, 2017']]
Canada = data.loc[data['Countries'] == 'Canada', ['Countries', 'Cost of living, 2017']]
Japan = data.loc[data['Countries'] == 'Japan', ['Countries', 'Cost of living, 2017']]
Germany = data.loc[data['Countries'] == 'Germany', ['Countries', 'Cost of living, 2017']]
Russia = data.loc[data['Countries'] == 'Russia', ['Countries', 'Cost of living, 2017']]
China = data.loc[data['Countries'] == 'China', ['Countries', 'Cost of living, 2017']]

# Testing purposes
All = [USA, UK, Canada, Japan, Germany, Russia, China]

def getCountry(countries):
    # Pulls the country for the X axis
    Name = data.loc[data['Countries'] == countries, 'Countries']

    # Create an empty list for the countries
    countryList = []

    # Loop through Country names and add them to the list
    for country in Name['Countries']:
        countryList.append(country)

    return countryList

def getNames():

    Countries = []

    print("Please enter 5 countries to check the cost of living in.")

    for i in range(1, 6):

        while True:
            print("Enter Country name " + str(i))
            Country = input("> ")

            try:
                print("Checking Country name")
                data.describe()
                Countries.append(Country)
                print("Valid Country name!")
                break
            except:
                print("This is not a valid country name. Please check your spelling and try again!")

    return Countries