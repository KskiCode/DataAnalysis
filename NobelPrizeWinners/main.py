import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt

data = pd.read_csv('./data/nobel_final.csv')
data.head()

print(data.info())
# Question: Average age of winners when they won the prize? - 59.8 years
data.describe()

# Comparing male and female noble prize winners
data_gender = data['gender'].value_counts()
print(data_gender)


data_gender.plot.pie(autopct='%1.1f%%')
plt.title('Noble Prize Winners By Gender')

# Question: name of university with most winners? Also quite a lot of universities listed (more than 300) thus only the top 20 are considered (.nlargest()
# Note: a lot of missing values
university = data['name_of_university'].value_counts().nlargest(20)
print(university)

plt.figure(figsize=(10, 5))
university.plot.barh(university)
plt.title('Top 20 University With Most Nobel Prize Winners (1901-2020)')


# Question: What country has the most winners (Where the winners are born)? 
# Note: Also here top 20 countries.
country = data['born_country_code'].value_counts().nlargest(20)
print(country)

plt.figure('Nobel Prize Winners By Country (Where Winner is born)')
country.plot.barh()
plt.show()