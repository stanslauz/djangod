guess_word = 12
count = 0
count_limit = 3

while count < count_limit:
    gswd = int(input("enter the word please"))
    count = count + 1
    if gswd == guess_word:
        print("correct word")
        break

    else:
        print("nope")