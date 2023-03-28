import ftplib

HOSTNAME = 'ftp.dlptest.com'
USERNAME = 'dlpuser'
PASSORD  = 'rNrKYTX9g7z3RgJRmxWuGHbeu'

print("***Start Connect***")
ftp_server=ftplib.FTP(HOSTNAME,USERNAME,PASSORD)
print("***END Connect***")

ftp_server.encoding="utf-8"
fileName="testsb013.txt"

with open(fileName,"rb") as file:
    ftp_server.storbinary(f"STOR {fileName}",file)

ftp_server.dir()
ftp_server.quit()