#write a function to count occurance of "a" in given string 
def count_frequency():
    string_name="Vaishnavi"
    count_frequency=0
    for i in string_name:
        if i=="a":
            count_frequency=count_frequency+1
    print("Count_frequency of a:",count_frequency)
count_frequency()
