import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

# Saves the Country data as a Pandas frame
data = pd.read_csv('cost_of_living.csv')

# This limits the results down to just the country name and their cost of living score. Failed Attempt
# USA = data.loc[data['Countries'] == 'USA', 'Countries']
# USA_Cost = data.loc[data['Countries'] == 'USA', 'Cost of living, 2017']
# UK = data.loc[data['Countries'] == 'UK', ['Countries', 'Cost of living, 2017']]
# Canada = data.loc[data['Countries'] == 'Canada', ['Countries', 'Cost of living, 2017']]
# Japan = data.loc[data['Countries'] == 'Japan', ['Countries', 'Cost of living, 2017']]
# Germany = data.loc[data['Countries'] == 'Germany', ['Countries', 'Cost of living, 2017']]
# Russia = data.loc[data['Countries'] == 'Russia', ['Countries', 'Cost of living, 2017']]
# China = data.loc[data['Countries'] == 'China', ['Countries', 'Cost of living, 2017']]

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
                name = data
                name.discribe()
                Countries.append(Country)
                print("Valid Country name!")
                break
            except:
                print("This is not a valid country name. Please check your spelling and try again!")

    return Countries

def getCost(COL):
    # Pulls the cost of living for the Y axis
    Cost = data.loc[data['Countries'] == COL, 'Cost of living, 2017']

    # Create a list of costs for each Country
    countryCost = []

    for price in Cost['Countries']:
        countryCost.append(price)

    return countryCost

def printGraph(Country):

    # X axis
    countryNames = np.array(getCountry())

    # Y axis
    COL = np.array(getCost())

    # creates the chart
    plt.plot(countryNames, COL)

    # labels for the graph
    plt.xlabel('Country')
    plt.ylabel('Cost of Living')
    plt.title('Cost of Living Between Countries')

    # names and saves the chart as a png file
    savefile = "charts/" + countryNames + ".png"
    plt.savefig(savefile)

    # prints the graph
    plt.show()

# Start of program

# Creating charts folder

try:
    Path("Charts").mkdir()
except FileExistsError:
    pass

for name in getNames():
    getCountry()
    getCost()
    printGraph()
