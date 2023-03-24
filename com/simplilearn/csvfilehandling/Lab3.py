import csv

with open("booksauthor.csv",mode='w') as csvfile:
    data=csv.DictReader(csvfile)
    writer=csv.writer(csvfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['TITLE','AUTHOR','GENRE','SUB-GENRE','HEIGHT','PUBLISHER'])
    writer.writerow(['Fundamentals of Wavelets', 'Goswami, Jaideva', 'tech', 'signal_processing', '228', 'Wiley'])
    writer.writerow(['Data Smart', 'Foreman, John', 'tech', 'data_science', '235', 'Wiley'])
    writer.writerow(['God Created the Integers', 'Hawking, Stephen', 'tech', 'mathematics', '197', 'Penguin'])