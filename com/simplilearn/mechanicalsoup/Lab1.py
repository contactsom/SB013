import mechanicalsoup

brouser=mechanicalsoup.StatefulBrowser()
brouser.open("https://steemit.com/")

articils=list(brouser.get_current_page().find('ul',class_="PostsList__summaries"))[:10]

for child in articils:
    user=child.find('span',class_="author").text
    #print(user)

    title=child.h2.text
    #print(title)

    print("USER : ",user," TITLE : ",title)