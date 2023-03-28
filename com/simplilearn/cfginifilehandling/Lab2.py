import configparser

config_file = configparser.ConfigParser()


config_file.add_section("FTPSettings")
config_file.set("FTPSettings","ftpUrl","demoftp.simplilearn.com")
config_file.set("FTPSettings","username","user")
config_file.set("FTPSettings","password","admin#super#secret@password")

with open("ciscoconfiguration.ini",'w') as file:
    config_file.write(file)
    file.flush()
    file.close()

print("Cisco Config File Created and data Saved")

read_file=open("ciscoconfiguration.ini",'r')
content = read_file.read()
print("Content of the Cisco Config File is : ")
print(content)
read_file.flush()
read_file.close()
