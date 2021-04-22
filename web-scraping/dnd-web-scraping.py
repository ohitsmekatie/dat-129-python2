import urllib
from bs4 import BeautifulSoup
import pandas as pd

req = urllib.request.Request('https://5e.tools/bestiary.html')

with urllib.request.urlopen(req) as response:
    page_content = response.read()

print(page_content)

soup = BeautifulSoup(page_content, "html.parser")
print(soup)


# df_monsters = pd.read_html('https://donjon.bin.sh/5e/monsters/')

# # print(df_monsters)

# df = df_monsters[1]['Name']
