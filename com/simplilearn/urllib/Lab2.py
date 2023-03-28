
googlesearch = [
    "best restaurants in bangalore",
    "best malls in bangalore",
    "best place in bangalore",
    "best hills in bangalore"
    ]

# https://www.google.com/search?q=best+hills+in+bangalore
baseurl="https://www.google.com/search?q="
urls=[ baseurl + t.replace(" ","+") for t in googlesearch ]
#print(urls)

for url in urls :
    print(url)







