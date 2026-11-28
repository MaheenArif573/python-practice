array = [int(x) for x in input("Enter integers by space: ").split()]
max_subarray = [array[0]]
curr_subarray = [array[0]]
max_sum = array[0]
curr_sum = array[0]

for num in array[1:]:
    curr_sum += num
    print("Curr sum:", curr_sum)
    if curr_sum < num:
        curr_subarray.clear()
        curr_subarray.append(num)
        curr_sum = num
    else:
        curr_subarray.append(num)
        print("curr array:", curr_subarray)

    if curr_sum > max_sum:
        max_sum = curr_sum
        max_subarray = curr_subarray.copy()
        print("max subarray:", max_subarray)
    else:
        continue

print("Sub-Array giving maximum sum", max_sum, "is", max_subarray)