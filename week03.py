def interss(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    #return list(s1.intersection(s2)) #set에서 지원해주는 intersection함수 사용
    return list(s1 & s2)

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 19, 27, 13, 41]
print(interss(l1,l2))  #l1, l2의 중복값들 고르기