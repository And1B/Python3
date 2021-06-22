highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(",")

highlighted_poems_stripped = []

for temp in highlighted_poems_list:
  highlighted_poems_stripped.append(temp.strip())

highlighted_poems_details = []
for temp in highlighted_poems_stripped:
  highlighted_poems_details.append(temp.split(':'))

titles = []
poets = []
dates = []

for temp in highlighted_poems_details:
  titles.append(temp[0])
  poets.append(temp[1])
  dates.append(temp[-1])

print("Titles: \n", titles)
print("Poets: \n", poets)
print("Dates: \n", dates)
