import re
pattern=r'[A-Za-z]+unal'
text="Kunal Lunal Zunal hffg fjefer erjererbgr erjgrgerjer rbgergerger jerberjber"
match=re.split(pattern,text) # split  just split word in text
#output is : ['', ' ', ' ', ' hffg fjefer erjererbgr erjgrgerjer rbgergerger jerberjber']
print(match)

