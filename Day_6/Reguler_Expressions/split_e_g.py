import re
pattern=r'\W*'
text="Kunal Lunal Zunal hffg fjefer erjererbgr erjgrgerjer rbgergerger jerberjber"
match=re.split(pattern,text)
print(match)

"""output : ['', 'K', 'u', 'n', 'a', 'l', '', 'L', 'u', 'n', 'a', 'l', '', 'Z', 'u', 'n', 'a', 'l', '', 'h', 'f', 'f', 'g', '', 'f', 'j', 'e', 'f', 'e', 'r', '', 'e', 'r', 'j', 'e', 'r', 'e', 'r', 'b', 'g', 'r', '', 'e', 'r', 'j', 'g', 'r', 'g', 'e', 'r', 'j', 'e', 'r', '', 'r', 'b', 'g', 
'e', 'r', 'g', 'e', 'r', 'g', 'e', 'r', '', 'j', 'e', 'r', 'b', 'e', 'r', 'j', 'b', 'e', 'r', '']
"""