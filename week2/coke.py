insert_num = 0
while(insert_num < 50):
    x = int(input("Insert Coin: "))
    if x == 5 or x == 10 or x == 25:
        insert_num += x
        if insert_num < 50:
            print("Amount Due: "+str(50-insert_num))
    else:
        print("Amount Due: "+str(50-insert_num))
print("Change Owed: "+str(insert_num-50))