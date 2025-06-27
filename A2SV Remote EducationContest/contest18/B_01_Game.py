t = int(input())
for _ in range(t):
    s = input()
    zero = s.count('0')
    one = s.count('1')
    moves = min(zero, one)
    print("DA" if moves % 2 == 1 else "NET")
