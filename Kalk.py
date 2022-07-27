import operator

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

memory = 0

def is_one_digit(v):
    try:
        if v > -10 and v < 10 and v.is_integer():
            output = True
        else:
            output = False
        return output
    except:
        if v > -10 and v < 10:
            output = True
        else:
            output = False
        return output

def check(v1,v2,v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


        
while 1 > 0:
    x = 0
    y = 0
    resetter = False
    msg_index = 10
    print(msg_0)
    x, oper, y = input().split()
    try:
        # Hentingen av det lagrede nummeret
        if x == "M" and y == "M":
            x = memory
            y = memory
        elif x == "M":
            x = memory
            y = float(y)
        elif y == "M":
            y = memory
            x = float(x)
        else:
            x = float(x)
            y = float(y)
    except ValueError:
        print(msg_1)
        resetter = True
    else:

        # Utregningen
        try:
            check(x,y,oper)
            result = ops[oper](x,y)
            print(result)
        
        # Om du bruker en operator utenfor listen
        except KeyError:

            print(msg_2)
            resetter = True
        
        # Deler på 0
        except ZeroDivisionError:
            print(msg_3)
            resetter = True

    # Lagrings loop
    while resetter == False:
        print(msg_4)
        answer = input()
        while True:

            # Lagringen av tallet til 'M'
            if answer == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while msg_index <= 12:
                        print(msg_[msg_index])
                        answer = input()
                        if answer == "y":
                            msg_index = msg_index + 1
                        elif answer == "n":
                            msg_index = 10
                            break
                    else:
                        memory = result
                else:
                    memory = result
                break
            elif answer == "n":
                break
            else:
                continue
        break
    print(msg_5)
    answer = input()
    # Sjekker svaret ditt angående å skru av programmet
    if resetter == True:
        continue
    elif answer == "n":
        break
    elif answer == "y":
        continue
