def is_one_digit(v):
    
    if  -10 < v < 10 and v.is_integer():
        return True
    else:
        return False

def check(v1,v2,v3):

    v1 = float(v1)
    v2 = float(v2)
    

    msg = ""
    
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + " ... lazy"     
         
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + " ... very lazy"                     

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 =="-"):
        msg = msg + " ... very, very lazy"                    
        
    if msg != "":
        msg = "You are" + msg

    print(msg)      

M = 0

while True:
    print("Enter an equation")
    x = 0
    y = 0

    oper_list = ["+", "-", "*", "/"]


    try:
        x, oper, y = input().split()

        if x == "M" and y == "M":
            x = M
            y = M

        elif x == "M":
            x = M

        elif y == "M":
            y = M

        else:
            x = float(x)
            y = float(y)

    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        continue
    else:
        if oper not in oper_list:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            continue

        else:
            check(x,y,oper)

            if oper == "+":
                result = float(x) + float(y)
                print(result)

            elif oper == "-":
                result = float(x) - float(y)
                print(result)

            elif oper == "*":
                result = float(x) * float(y)
                print(result)

            elif oper == "/":
                try:
                    result = float(x) / float(y)
                except ZeroDivisionError:
                    print("Yeah... division by zero. Smart move...")
                    continue
                else:
                    print(result)

            print("Do you want to store the result? (y / n):")
            ans_1 = input()
            if ans_1 == "y":
                if is_one_digit(result):
                    print("Are you sure? It is only one digit! (y / n)")
                    ans_3 = input()
                    if ans_3 == "y":
                        print("Don't be silly! It's just one number! Add to the memory? (y / n)")
                        ans_4 = input()
                        if ans_4 == "y":
                            print("Last chance! Do you really want to embarrass yourself? (y / n)")                                                
                            ans_5 = input()
                            if ans_5 == "y":  
                                M = result
                                
                else:
                    M = result
                

            print("Do you want to continue calculations? (y / n):")
            ans_2 = input()
            if ans_2 == "n":
                break


                        
                        
                        
                        
                    
