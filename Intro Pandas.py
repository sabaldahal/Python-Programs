import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import numpy as np

# read data from csv file into sh_raw
sh_raw = pd.read_csv('./movies.csv', header=None,
                     names=['Year', 'Title', 'Comic', 'IMDB', 'RT',
                            'CompositeRating', 'OpeningWeekendBoxOffice',
                            'AvgTicketPriceThatYear', 'EstdOpeningAttendance',
                            'USPopThatYear'])
# remove movies having NaN val in OpeningWeekendBoxOffice
sh = sh_raw[np.isfinite(sh_raw.OpeningWeekendBoxOffice)]
# normalizing the values
imdb_normalized = sh.IMDB / 10
rt_normalized = sh.RT / 100
# adding normalized values in new columns
sh.insert(10, 'IMDBNormalized', imdb_normalized)
sh.insert(11, 'RTNormalized', rt_normalized)

# show only the DC movies
print('Displaying DC movies stats')
print(sh[sh.Comic == 'DC'])
print()

# Show Year, Title and OpeningWeekendBoxOffice columns
print('Displaying colums: Year, Title and OpeningWeekendBoxOffice')
print(sh[['Year', 'Title', 'OpeningWeekendBoxOffice']])
print()

# Show Year and Title of only Marvel movies
print('Displaying Year and Title for Marvel movies')
print(sh[sh.Comic == 'Marvel'][['Year', 'Title']])
print()

# Plot a line for AvgTicketPriceThatYear with Year on the x-axis
colors = 'black'
sh.plot.line(x='Year', y='AvgTicketPriceThatYear', c=colors, alpha=1.0)
plt.show()
