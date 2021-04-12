import urllib
from bs4 import BeautifulSoup


def get_search_url_goodreads(search_term):
    url = 'https://www.goodreads.com/search?query=%s' % (str(search_term))
    return url


def get_search_url_bgg(search_term):
    url = 'https://boardgamegeek.com/geeksearch.php?action=search&objecttype=boardgame&q=%s' % (
        str(search_term))
    return url


def get_page_content(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.read()


user_input = input("What board game content would you like to look up: ")
print()
page_content = get_page_content(get_search_url_bgg(user_input.lower()))
soup = BeautifulSoup(page_content, "html.parser")
# print(soup)


# print(game_name.text)

# gets all the available board game names with given name
print("Here are the list of board games on boardgamgeek.com with",
      user_input, "in the title:")
print()

# looks up only primary class in a tags
game_list = soup.find_all("a", class_="primary")

for item in game_list:
    print(item.text)


# game_name = soup.find(id="results_objectname2")

# for kid in game_name.children:
#     print(kid.string)


# user_input = input("What book content would you like to look up: ")
# print()

# page_content = get_page_content(get_search_url_goodreads(user_input.lower()))

# #print(page_content)
# soup = BeautifulSoup(page_content, 'html.parser')
# # print(soup)
# # bookTitle is the class

# s = soup.find_all('a','bookTitle')
# # print(s)

# total_titles = 0
# subtitles = 0

# for item in s:
#     # finds everything in the span element to just get the titles
#     t = item.find('span').string
#     print(t)
#     total_titles = total_titles + 1
#     # if there is a title with : in it it has a subtitle
#     if ":" in t:
#         subtitles = subtitles + 1

# print()
# print()
# print("Total Titles on the first page: ", str(total_titles))
