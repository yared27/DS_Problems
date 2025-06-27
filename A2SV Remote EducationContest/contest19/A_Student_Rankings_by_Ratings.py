n = int(input())
ratings = list(map(int, input().split()))

indexed_ratings = [(rating, idx) for idx, rating in enumerate(ratings)]
indexed_ratings.sort(reverse=True)

positions = [0] * n
current_rank = 1

for i, (rating, original_index) in enumerate(indexed_ratings):
    if i > 0 and rating == indexed_ratings[i - 1][0]:
        positions[original_index] = current_rank
    else:
        current_rank = i + 1
        positions[original_index] = current_rank

print(' '.join(map(str, positions)))
