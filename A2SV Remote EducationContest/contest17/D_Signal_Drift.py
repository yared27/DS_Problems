from math import comb

s1 = input().strip()
s2 = input().strip()

target_pos = s1.count('+') - s1.count('-')
current_pos = s2.count('+') - s2.count('-')
q = s2.count('?')

diff = target_pos - current_pos

if (diff + q) % 2 != 0 or abs(diff) > q:
    print("0.000000000000")
else:
    plus_needed = (diff + q) // 2
    ways = comb(q, plus_needed)
    total = 2 ** q
    probability = ways / total
    print(f"{probability:.12f}")
