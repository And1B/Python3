import codecademylib
import pandas as pd

#columns: user_id, utm_source, day, ad_click_timestamp, experimental_group

#reads csv into DataFrame
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
#new Df with amount of users per source
print(ad_clicks.groupby("utm_source").user_id.count().reset_index())

#adds a new boolean column informing if ad has been clicked or not
ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()

#displays amount of clicks per source
clicks_by_source = ad_clicks.groupby(("utm_source", "is_click")).user_id.count().reset_index()

print(clicks_by_source)
#pivots that DateFrame for better readability
clicks_pivot = clicks_by_source.pivot(
  columns = "is_click",
  index = "utm_source",
  values = "user_id"
)

#adds a column with the percentage or clicks per sources
clicks_pivot["percent_clicked"] = \
  clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

#displays if both experimental groups received equal amount of ads
print(ad_clicks.groupby("experimental_group").user_id.count().reset_index())

#counts the amount of clicks per group
print(ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index().pivot(
  index = 'experimental_group',
  columns = 'is_click',
  values = 'user_id'
).reset_index())

a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
#print(b_clicks)

a_clicks_pivot = a_clicks.groupby(["is_click", "day"]).user_id.count().reset_index().pivot(
  index = "day",
  columns = "is_click",
  values = "user_id"
).reset_index()

b_clicks_pivot = b_clicks.groupby(["is_click", "day"]).user_id.count().reset_index().pivot(
  index = "day",
  columns = "is_click",
  values = "user_id"
).reset_index()

print(a_clicks_pivot)
a_clicks_pivot["Percentage"] = a_clicks_pivot[True] / (a_clicks_pivot[False] + a_clicks_pivot[True])
print(a_clicks_pivot)

b_clicks_pivot["Percentage"] = b_clicks_pivot[True] / (b_clicks_pivot[False] + b_clicks_pivot[True])
print(b_clicks_pivot)


