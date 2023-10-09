import re
pattern=r'[A-Za-z]+unal'
text="Kunal Lunal Zunal hffg fjefer erjererbgr erjgrgerjer rbgergerger jerberjber"
match=re.sub(pattern,"K",text) # sub just replace by any charter in text ....
#output is : K K K hffg fjefer erjererbgr erjgrgerjer rbgergerger jerberjber
print(match)