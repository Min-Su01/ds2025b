class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)] #배열의 배열 생성


G1 = Graph(4)
G3 = Graph(4)
G_self = Graph(4)

# 0 == A,   1 == B,  2 == C, 3 == D , 그래프 연결 코드로 구현
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1 #A는 B,C,D와 모두 연결
G1.graph[1][0] = 1; G1.graph[1][2] = 1; #B는 A,C와 연결
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1 #C는 A,B,D와 모두 연결
G1.graph[3][0] = 1; G1.graph[3][2] = 1; #D는 A,C와 연결

#G1 무방향 그래프!!!
print("G1 무방향 그래프")
for r in range(G1.SIZE):
    for c in range (G1.SIZE):
        print(G1.graph[r][c], end = ' ')
    print()


# 0 == A,   1 == B,  2 == C, 3 == D , 그래프 연결 코드로 구현
print("G3 방향 그래프")
G3.graph[0][1] = 1; G3.graph[0][2] = 1; #A는 B,C와 연결
 #B는 연결 x
G3.graph[3][0] = 1; G3.graph[3][2] = 1; #D는 A,C와 연결
for r in range(G3.SIZE):
    for c in range (G3.SIZE):
        print(G3.graph[r][c], end = ' ')
    print()

G_self.graph[0][3] = 1
G_self.graph[1][2] = 1; G_self.graph[1][3] = 1;
G_self.graph[2][1] = 1
G_self.graph[3][0] = 1; G_self.graph[3][1] = 1;

#G_self 무방향 그래프!!!
print("G_self 무방향 그래프")
for r in range(G_self.SIZE):
    for c in range (G_self.SIZE):
        print(G_self.graph[r][c], end = ' ')
    print()
