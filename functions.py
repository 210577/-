def polynomial(tier,arr):
    while True:
        if tier == 0:
            arr.append(input("상수항을 입력해 주세요 : (q를 입력하면 끊깁니다) "))
        else:
            arr.append(input("%d차항을 입력해 주세요 : (q를 입력하면 끊깁니다)" % tier))
        tier += 1
        if arr[tier-1] == 'q':
            arr[tier-1] = 0
            tier -= 2
            break
    return [tier,arr]


def irrational(a,b,c,d):
    while True:
        a = input("\"y = a√(bx + c) + d\"에서 a의 값을 입력해 주세요.")
        if a.isalpha() == False:
            break
    while True:
        b = input("\"y = a√(bx + c) + d\"에서 b의 값을 입력해 주세요.")
        if b.isalpha() == False:
            if b != '0':
                break
    while True:
        c = input("\"y = a√(bx + c) + d\"에서 c의 값을 입력해 주세요.")
        if c.isalpha() == False:
            break
    while True:
        d = input("\"y = a√(bx + c) + d\"에서 d의 값을 입력해 주세요.")
        if d.isalpha() == False:
            break
    return [float(a),float(b),float(c),float(d)]


def rational(a,b,c,d):
    while True:
        a = input("\"y = (ax+b) / (cx+d)\"에서 a의 값을 입력해 주세요.")
        if a.isalpha() == False:
            break
    while True:
        b = input("\"y = (ax+b) / (cx+d)\"에서 b의 값을 입력해 주세요.")
        if b.isalpha() == False:
            break
    while True:
        c = input("\"y = (ax+b) / (cx+d)\"에서 c의 값을 입력해 주세요.")
        if c.isalpha() == False:
            if c != '0':
                break     
    while True:
        d = input("\"y = (ax+b) / (cx+d)\"에서 d의 값을 입력해 주세요.")
        if d.isalpha() == False:
            break      
    return [float(a),float(b),float(c),float(d)]
