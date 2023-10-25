import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

fifa=pd.read_csv('players_20.csv')
fifa.head()
for col in fifa.columns:
    print(col)

fifa.shape
print("\n")
#total Country and how much member from his country
print(fifa['nationality'].value_counts())
print("\n")
#10 country
print(fifa['nationality'].value_counts()[0:10])
print("\n")
#5 country
print(fifa['nationality'].value_counts()[0:5])
print("\n")
print(fifa['nationality'].value_counts()[0:5].keys())
print("\n")
plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color="green")
plt.show()
player_salary=fifa[['short_name','wage_eur']]
print(player_salary.head())
print("\n")
player_salary=player_salary.sort_values(by=['wage_eur'],ascending=False)
print(player_salary.head())
print("\n")
plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'])[0:5],list(player_salary['wage_eur'])[0:5],color="r")
plt.show()
fifa['nationality']=='Germany'
Germany=fifa[fifa['nationality']=='Germany']
print(Germany.head(10))
print("\n")
Germany.sort_values(by=['height_cm'],ascending=False)
print(Germany.head())
print("\n")
Germany.sort_values(by=['weight_kg'],ascending=False)
print(Germany.head())
print("\n")
Germany.sort_values(by=['wage_eur'],ascending=False)
print(Germany.head())
print("\n")
Germany[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False)
print(Germany.head())
print("\n")
player_shooting=fifa[['short_name','shooting']]
player_shooting.sort_values(by=['shooting'],ascending=False)
print(player_shooting.head())


