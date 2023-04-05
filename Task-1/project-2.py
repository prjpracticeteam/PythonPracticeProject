# 2nd divisibilty rule
def div2(n):
    return n[-1] in ["0","2","4","6","8"]

# 3rd divisibilty rule
def div3(n):
    sum = 0
    for i in str(n):
        i = int(i)
        sum = sum + i
    if sum > 9:
        return div3(sum)
    else:
        return sum in [3,6,9]

# 4th divisibilty rule
def div4(n):
    if int(n) > 8:
        res = int(n[-2:])
        if res/4 == int(res/4):
            return True
        else:
            return False
    else:
        return n in ["4","8"]

# 5th divisibilty rule
def div5(n):
    return n[-1] in ["0","5"]

# 6th divisibilty rule
def div6(n):
    return div2(n) and div3(n)

# 7th divisibilty rule
def div7(n):
    if int(n) > 7:
        last_digit = n[-1]
        rest_digit = n[:-1]
        sum = int(last_digit)*5 + int(rest_digit)
        if sum/7 == int(sum/7):
            return True
        else:
            return False
    else:
        return n in ["7"]

# 8th divisibilty rule
def div8(n):
    if int(n)>8:
        res = int(n[-3:])
        if res/8 == int(res/8):
            return True
        else:
            return False
    else:
        return n in ["8"]

# 9th divisibilty rule
def div9(n):
    sum = 0
    for i in str(n):
        i = int(i)
        sum = sum + i
    if sum > 9:
        return div9(sum)
    else:
        return sum in [9]

raw_num = "100,23,81"
num = raw_num.split(',')
functions = [div2,div3,div4,div5,div6,div7,div8,div9]
for i in num:
    if i.isdigit():
        divisible = []
        for j in functions:
            if j(i) is True:
                divisible.append(j.__name__[-1])
        # print(result)
        if divisible:
            print(f"{i}: is divisible by {', '.join(divisible)}")
        else:
            print(f"{i}: is not divisible")    
