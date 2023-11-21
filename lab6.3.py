S = [3, 6, 1, -6, 54, -27, -2, 21]
min_number = S[0]
max_number = S[0]
summ = 0
for number in S:
    if number > 0:
        summ += number
    else :
        number *= (-1)
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

proizvedenia = 1
is_between = False

for x in S:
    if not is_between and (x == max_number or x==min_number):
        is_between = True
    elif is_between and (x == max_number or x == min_number):
        break

    if is_between:
        proizvedenia *= x
print(proizvedenia)

print(max_number, min_number)
print(summ)
