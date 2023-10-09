import re
pattern=r'[A-Za-z]+unal'
text="Kunal Lunal Zunal hffg fjefer erjererbgr erjgrgerjer rbgergerger jerberjber"
match=re.findall(pattern,text)
print(match)