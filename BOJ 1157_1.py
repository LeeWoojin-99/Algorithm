entry = input().upper()
max = 0

for i in entry:
    if max < entry.count(i):
        max = entry.count(i)
        max_chr = i
    elif max == entry.count(i) and max_chr != i:
        max_chr = '?'

print(max_chr)

#시간 초과 오류.