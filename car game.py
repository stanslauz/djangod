sta = "start"
sto = "stop"
qui = "quit"
count = 0
enter = ""
while enter != qui:
     enter = str(input("enter the mode"))
     if enter == sta:
         print("car engine starts")
     elif enter == sto:
         print("car engine stop")
     elif enter == qui:
         break
     else:
         print("invalid")

