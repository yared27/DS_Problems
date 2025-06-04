import math
from collections import Counter

n, I = map(int, input().split())
a = list(map(int, input().split()))

# Calculate how many distinct values we are allowed to store
max_bits = (8 * I) // n
if max_bits > 30:
    max_K = len(set(a))  # we can store all
else:
    max_K = min(len(set(a)), 2 ** max_bits)

# Count occurrences of each value
freq = Counter(a)
sorted_vals = sorted(freq.keys())  # Unique, sorted values
prefix = [0]  # prefix sum of frequencies

for val in sorted_vals:
    prefix.append(prefix[-1] + freq[val])

min_changes = n

# Sliding window over sorted unique values of size <= max_K
for i in range(len(sorted_vals) - max_K + 1):
    # How many values are in [sorted_vals[i], ..., sorted_vals[i+max_K-1]]
    kept = prefix[i + max_K] - prefix[i]
    min_changes = min(min_changes, n - kept)

print(min_changes)
