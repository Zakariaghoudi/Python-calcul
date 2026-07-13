secret_num = ""
count = 3
while secret_num != "7" and count > 0 :
   secret_num = input("input number 0-9:")
   count -= 1 
   if secret_num != "7" or count > 3 :
      print("your number incorrect. Remaining attemps: " + str(count))
if secret_num == "7" :
   print("correct answer")
else:
   print("Game Over! Out of attemps")
   
