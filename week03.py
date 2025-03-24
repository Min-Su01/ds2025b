
#city = ['Incheon','Incheon' ,'Seoul', 'Gimpo'] #리스트나 튜플 등을 {} set에 주면 중복되는 것들 삭제
city = {'Incheon','Incheon','Seoul', 'Gimpo'}  #set사용으로 중복 삭제
city = set(city)
city.add('Anyang')
city.add('Seoul') #set사용으로 중복삭제!
print(city)