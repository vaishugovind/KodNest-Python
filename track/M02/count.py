# Initialize the counters and total
positive_count = 0
negative_count = 0
zero_count = 0
total = 0

# Read and analyze each number
number_counter = int(input())
for i in range(1, number_counter + 1):
    num = int(input())          # read a new number each time
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1
    total += num                 # add the actual number, inside the loop

print(f"Positive Count: {positive_count}")
print(f"Negative Count: {negative_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total}")