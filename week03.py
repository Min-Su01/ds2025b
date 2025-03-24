def duplicate_city(cities):
    result = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result.append(city)
    return result


#city = {'Incheon','Incheon' ,'Seoul', 'Gimpo'} #리스트나 튜플 등을 {} set에 주면 중복되는 것들 삭제
cities = ['Incheon','Incheon','Seoul', 'Gimpo']  #set사용으로 중복 삭제
cities.append('Anyang')
cities.append('Seoul') #set사용으로 중복삭제!
print(cities)
print(set(duplicate_city(cities)))