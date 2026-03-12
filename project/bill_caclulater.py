# Electricty Bill Calculater unit
print(":-welcome:-")
Value=float(input("Howmany use the electricty  in unit:= "))

match Value:
    case Value if(Value<=0):
        print("your Electricty bill amount is Rs-0.00 ")

    case Value if (Value>0 and Value<=100) :
        print("your Electricty bill amount is Rs-",Value*5)
    case Value if (Value>100 and Value<=200):
        print("your Electricty bill amount is Rs-",Value*7)

    case Value if (Value>200 and Value<=300):
        print("your Electricty bill amount is Rs-",Value*10)
    case Value if (Value>300 and Value<=1000):
        print("your Electricty bill amount is Rs-",Value*15)




    



