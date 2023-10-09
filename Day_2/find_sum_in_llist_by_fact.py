# def sum_list1(list1):  
#     for i in range(len(list1)):
#         sum=sum+list([i])
#     return sum
# list1=[1,2,3,4]
# print("list of sum is : ",sum_list1(list1))
# def sum_nestedlist( l ):
   
#     total = 0
     
#     for j in range(len(l)):
       
#         if type(l[j]) == list :
           
#             total+= sum_nestedlist(l[j])
#         else:
           
#             total += l[j]  
             
#     return total
             
# print(sum_nestedlist([1,2,3,7]))

def s_list(li):
    if len(li)==0:
        return 0
    else:
        return li[0]+s_list(li[1:])
li=[1,2,3,4]
print("sum: ",s_list(li))