n = int(input("Enter the number of card"))

cards = list(map(int,input().split()))


def play():
    i = 0
    j = n - 1
    serja_score = 0
    dima_score = 0
    is_serjas_turn = True
    while i<=j:
        if is_serjas_turn:
            if cards[i]>=cards[j]:
                serja_score+=cards[i]
                i+=1
            else:
                serja_score+=cards[j]
                j-=1
            is_serjas_turn=False
        else:
            if cards[i]>=cards[j]:
                dima_score+=cards[i]
                i+=1
            else:
                dima_score+=cards[j]
                j-=1
            is_serjas_turn = True
    return serja_score,dima_score
print(play())






