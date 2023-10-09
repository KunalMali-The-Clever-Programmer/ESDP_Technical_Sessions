# Matching Pattern ............
import re 
pattern =r"Hi"
match="Hi I am the best."
val=re.match(pattern,match)
print(val)

#output is span=(0, 2), match='Hi'

# Non matching Pattern ............

# import re 
# pattern =r"Bye"
# match="Hi I am the best."
# val=re.match(pattern,match)
# print(val)

#output is None for Non matching pattern ..........