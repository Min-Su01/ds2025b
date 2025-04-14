from queue import Queue


q = Queue()
q.put("Database")          #enqueue
q.put("Data Structure")
print(q.get())            #dequeue
print(q.get())
