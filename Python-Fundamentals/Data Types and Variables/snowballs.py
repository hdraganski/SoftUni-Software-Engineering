import sys

number_of_snowballs = int(input())
max_value = -sys.maxsize
max_weight = 0
max_time = 0
max_quality = 0
for snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    current_value = int((weight_of_snowball / time_needed) ** quality)
    if current_value > max_value:
        max_value = current_value
        max_weight = weight_of_snowball
        max_time = time_needed
        max_quality = quality
print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")
