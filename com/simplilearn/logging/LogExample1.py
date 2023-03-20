import logging

print("This is the Logging Example")
print("******** START ***********")

#logging.basicConfig(filename="CISCO-SB013.log",level=logging.NOTSET)
#logging.basicConfig(filename="CISCO-SB013.log",level=logging.DEBUG)
#logging.basicConfig(filename="CISCO-SB013.log",level=logging.INFO)
#logging.basicConfig(filename="CISCO-SB013.log",level=logging.WARNING)
logging.basicConfig(filename="CISCO-SB013.log",level=logging.ERROR)


logging.debug("I am debug Message 1")
logging.debug("I am debug Message 1")
logging.debug("I am debug Message 1")
logging.debug("I am debug Message 1")


logging.info("I am info Message 1")
logging.info("I am info Message 1")
logging.info("I am info Message 1")
logging.info("I am info Message 1")


logging.warning("I am warning Message 1")
logging.warning("I am warning Message 1")
logging.warning("I am warning Message 1")
logging.warning("I am warning Message 1")


logging.error("I am error Message 1")
logging.error("I am error Message 1")
logging.error("I am error Message 1")
logging.error("I am error Message 1")


logging.critical("I am critical Message 1")
logging.critical("I am critical Message 1")
logging.critical("I am critical Message 1")
logging.critical("I am critical Message 1")

print("----------------")


print("******** END ***********")