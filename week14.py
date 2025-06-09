#백준 1929번
def is_prime(n) -> bool:
  if n <= 1:
      return False
  else:
    for i in range(2, n):
        if n % i == 0:
          return False
  return True

s, e = map(int, input().split())  #s, e의 입력값 넣기. 스플릿 사용하니 리스트로 반환됨
                                 #만약 3. 16 넣으면 ['3', '16'] 으로 반환되는 것.
for i in range(s, e+1):
  if is_prime(i):
    print(i)