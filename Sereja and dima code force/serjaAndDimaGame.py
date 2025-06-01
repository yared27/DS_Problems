n = int(input())
cards = list(map(int, input().split()))

i = 0
j = n - 1
serja_score = 0
dima_score = 0
is_serjas_turn = True

while i <= j:
    if cards[i] >= cards[j]:
        chosen = cards[i]
        i += 1
    else:
        chosen = cards[j]
        j -= 1

    if is_serjas_turn:
        serja_score += chosen
    else:
        dima_score += chosen

    is_serjas_turn = not is_serjas_turn

print(serja_score, dima_score)
