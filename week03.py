groups = ['Hot','Seventeen','Black Pink', 'NJZ']
ratings = [1, 2, 3, 4]
#groups와 rating 합치기, rating을 1,2 등 갯 수를 줄여도 있는 것까지만 합함

group_rataing = list(zip(groups, ratings))
print(group_rataing)