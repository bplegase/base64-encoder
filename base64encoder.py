import base64
import sys

# converting to base64
for i in range(1, 101):
  i = str(i)                          # converting i to a string
  ibytes = i.encode("utf-8")          # converting i to bytes for b64 encoding
  encoded = base64.b64encode(ibytes)  # base64-encoding i
  encoded = str(encoded)              # converting type from bytes to str
  sys.stdout = open('base64-encoded.txt', 'a')
  print(encoded[2:6]) 

# referenced https://stackoverflow.com/questions/45482272/typeerror-a-bytes-lik$