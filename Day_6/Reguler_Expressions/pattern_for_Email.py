import re
pattern=r'[A-Za-z0-9.-_]+@+[\w]+\.+[$]'
text="Kunal123@gmail.com"
match=re.match(pattern,text)
if match:
    print("email  is valid:")
else:
    print("Can`t valid")




# for @gamil.com pattern : 

# import re
# pattern=r'[A-Za-z0-9.-_]+@gmail.com'
# text="Kunal123@gmail.com"
# match=re.match(pattern,text)
# if match:
#     print("email  is valid:")
# else:
#     print("Can`t valid")

