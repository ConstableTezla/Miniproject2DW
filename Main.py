import pandas as pd
import matplotlib.pyplot as plt

# Saves the Spotify data as a Pandas frame
data = pd.read_csv('cost_of_living.csv')

# This limits the results down to just the country name and their cost of living score
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

plt.plot(USA, USA_Cost)
plt.show()
