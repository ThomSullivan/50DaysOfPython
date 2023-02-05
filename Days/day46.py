#       Day 46: Create a DataFrame
# Create a Dataframe using pandas. You are going to create a 
# code to put the following into a Dataframe. You will use the 
# information in the table below. Basically, you are going to 
# recreate this table using pandas. Use the information in the table 
# to recreate the table.
# year  Title       genre
#--------------------------
# 2009 | Brothers   | Drama
# 2002 | Spider-Man | Sci-fi
# 2009 | WatchMen   | Drama
# 2010 | Inception  | Sci-fi
# 2009 | Avatar     | Fantasy
#       Extra Challenge: Website Data with Pandas
# Create a code that extracts data from a website. You will extract a 
# table from the website. And from that table you will extract columns 
# about the data types in Python and their mutability. You will extract 
# information from the following website:
# https://en.wikipedia.org/wiki/Python_(programming_language)
# The following table (next page) is what you will extract from the website
import requests
import pandas as pd

data ={
    'year':[2009, 2002, 2009, 2010, 2009],
    'Title':['Brothers', 'Spider-man', 'WatchMen', 'Inception', 'Avatar'],
    'genre': ['Drama','Sci-fi','Drama','Sci-fi','Fantasy']
}
frame = pd.DataFrame(data)



html = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)').content 
site = pd.read_html(html)
table = site[1]
data = {
    'Data type':[x for x in table['Type']],
    'Mutability':[x for x in table['Mutability']]
}
webFrame = pd.DataFrame(data)


print(frame)
print('----------------------------')
print(webFrame)

