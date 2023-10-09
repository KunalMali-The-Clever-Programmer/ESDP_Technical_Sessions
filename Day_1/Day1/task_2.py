cost=int(input("Enter the cost price plseze : "))
user_type =input("you are student or not (y/n): ")

if(user_type =="y" and cost>=500):
    print("Congratulastion You are saving 10% cost on your shopping ")
    after_dis_cost=((cost//100)*10)
    print(f"your total shopping cost from {cost} is : ",cost-after_dis_cost)
elif(user_type =="y" and cost<500):
    print("Congratulastion You are saving 5% cost on your shopping ")
    after_dis_cost1=((cost//100)*5)
    print(f"your total shopping cost from {cost} is : ",cost-after_dis_cost1)
elif(user_type =="n" and cost>=500):
    print("Congratulastion You are saving 8% cost on your shopping ")
    after_dis_cost2=((cost//100)*8)
    print(f"your total shopping cost from {cost} is : ",cost-after_dis_cost2)
elif(user_type =="n" and cost<500):
    print("Congratulastion You are saving 2% cost on your shopping ")
    after_dis_cost3=((cost//100)*2)
    print(f"your total shopping cost from {cost} is : ",cost-after_dis_cost3)

