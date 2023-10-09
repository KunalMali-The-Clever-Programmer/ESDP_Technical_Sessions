import re
pattern=r'[A-Za-z]+unal'
text="Kunal Lunal Zunal hffg fjefer erjererbgr erjgrgerjer rbgergerger jerberjber"
match=re.finditer(pattern,text)
for i in match :
    print(i)

#finditer it return the index of charter and value also but in findall in on;y return the value


'''output:Match object; span=(0, 5), match='Kunal'>
<re.Match object; span=(6, 11), match='Lunal'>
<re.Match object; span=(12, 17), match='Zunal'>'''
