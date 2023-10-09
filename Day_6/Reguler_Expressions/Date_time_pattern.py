import re
pattern=r'\d{2}[/-]\d{2}[/-]\d{4}'
text="09/10/2023"
match=re.match(pattern,text)
if match:
    print("Date is valid:")
else:
    print("Can`t valid")
