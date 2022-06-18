# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')

#print(df.head(5))
import pandas as pd
taxi = pd.read_csv('/Users/annch/Downloads/2_taxi_nyc.csv', encoding='Windows-1251', sep=',')
#pd.read_csv('path_to_your.csv', encoding='Windows-1251', sep=';')

def temp_to_celcius(temp):
    temp_f = ((temp - 32) * 5.0) / 9.0
    return (temp_f)


taxi['temp_C'] = temp_to_celcius(taxi['temp'])
print(taxi)

#pickups_by_mon_bor = taxi.groupby(['borough', 'pickup_month'], as_index = False).agg({'pickups': 'sum'}).sort_values('pickups', ascending= False)

#print(pickups_by_mon_bor)