class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)] #배열의 배열 생성


G1 = Graph(4)

print(G1.SIZE)
print(G1.graph)