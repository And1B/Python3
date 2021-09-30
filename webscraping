import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#requesting and parsing the entire website
content = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(content.content, "html.parser")

#extracting all ratings into list
raiting = (soup.find_all(attrs={"class": "Rating"}))
raiting_header = raiting.pop(0)
Rating = []
for numbers in raiting:
  Rating.append(float(numbers.get_text()))

#plt.show(plt.hist(raitings)) 

#extracting all companies into list
names = (soup.find_all(attrs={"class": "Company"}))
names.pop(0)
cmpnames = []
for companies in names:
  cmpnames.append(companies.get_text())

#creating a DataFrame with Company and Ratings as rows
#df = {"Company": cmpnames, "Ratings": raitings}
#complete_df = pd.DataFrame.from_dict(df)
#grouping a new DataFrame with rows as Company and Ratings as column
#grouped_df = complete_df.groupby("Company").mean()
#Extracting the companies with the 10 highest Ratings
#top_ten = grouped_df.nlargest(10, "Ratings")

#extracting all percentages
percentages = (soup.find_all(attrs={"class": "CocoaPercent"}))
percentages.pop(0)
CocoaPercentage = []
for percentage in percentages:
  CocoaPercentage.append(float(percentage.get_text().replace("%", "")))

dictionary = {"Company": cmpnames, "Rating": Rating, "CocoaPercentage": CocoaPercentage}
dataframe = pd.DataFrame.from_dict(dictionary)
top = dataframe.nlargest(20, "Rating")
top.set_index(["Rating", "CocoaPercentage"]).count(level="Rating")

#shows the correlation betweeen Perecentage and Rating in a scatter
#plt.scatter(CocoaPercentage, Rating)
#plt.show()
