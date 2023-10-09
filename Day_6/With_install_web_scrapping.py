import re,urllib
import urllib.request
site="google microsoft youtube".split()
print(site)

for i in site:
    print("Searching..... ",i)
    u=urllib.request.urlopen("https://"+i+".com")
    text=u.read()
    title=re.findall("<title>.*</title>",str(text),re.I)
    print(title[0])