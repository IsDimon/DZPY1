numticket = (input("Введите шестизначный номер билета:  "))
if len(numticket)==6:
     if (int(numticket[0])+int(numticket[1])+int(numticket[2]))==(int(numticket[3])+int(numticket[4])+int(numticket[5])):
        print("Ваш билет счастливый")
     else: 
         print("Увы, ваш билет не счастливый")
else:
    print("Введено неверное значение")