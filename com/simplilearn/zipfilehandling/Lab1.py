from zipfile import *

print("************** START-Zip FIle Handling **************")
zipfile=ZipFile("simplilearn.zip",'w',ZIP_DEFLATED)
zipfile.write("abc.txt")
zipfile.write("book.txt")
zipfile.write("books.csv")
zipfile.write("booksauthor.csv")
zipfile.write("data.txt")
zipfile.close()

print("************** Zip FIle Created **************")


print("************** END-Zip FIle Handling **************")