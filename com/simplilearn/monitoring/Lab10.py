import psutil

print(psutil.net_io_counters())

# snetio(bytes_sent=138310656, bytes_recv=41390080, packets_sent=263997, packets_recv=168050, errin=0, errout=0, dropin=0, dropout=0)