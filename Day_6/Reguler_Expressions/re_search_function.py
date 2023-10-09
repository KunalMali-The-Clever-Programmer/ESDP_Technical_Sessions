# search only one charater (left to right).......
import re
patter =r"\d" # '\d' for search numbre in string
text="Hello923@gmail.com"
match=re.search(patter,text)
if match:
    print("Match Found ",match.group())  # match.group() it usind to return value (numbre of Matchs ...) 
    #output is: Match Found  9
else:
    print("Match Not Found ")