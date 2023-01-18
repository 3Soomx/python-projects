import random
a = int(input("entar the starting num.: "))
b = int(input("entar the ending num.: "))
rand_num = random.randint(a,b)
y = 0
for i in range (a,b+1):
   y = y + 1
   x = int(input("Enter num in reang : "))
   if x == rand_num :
    print("Correct! you got it in ", y,"guesses")
    quit()               # to stop the loop when guss is correct.
   elif x > rand_num:
    print("plz Enter a Smallr Num: ")
   elif x < rand_num:
    print("Plz Enter a Bigger Num: ")
   else: print("Error , Plz Enter num in the reang")
