#write a function to count occurance of "a" in given string 
def count_frequency(str, target):
    count_frequency=0
    for i in str:
        if i==target:
            count_frequency=count_frequency+1
    print("Count_frequency of",target,"is:",count_frequency)
count_frequency("india", "i")
