from pytube import *

print("Hello")
url = "https://www.youtube.com/watch?v=elgYoEpuuog"
path = "D:\\"
ob = YouTube(url)
# strms = ob.streams
# for s in strms:
#     print(s)
strm = ob.streams.first()
print(strm)