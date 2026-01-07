Amount=int(input("Please Enter Amount For Withdrawal:"))
note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10
print("Notes For 100 Rupee",note_1)
print("Notes For 50 Rupee",note_2)
print("Notes For 10 Rupee",note_3)
