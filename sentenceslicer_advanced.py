# let the user input a sentence
sentence = input("Please insert a sentence: ")

# calculate the length of the input sentence
length = (len(sentence))

# calculate the middle part of the sentence (from 25% to 75%)
start = round(length * 25 / 100)
end = round(length * 75 / 100)

# print the middle of the sentence calculated earlier (to compare to the other result)
print(sentence[start:end])

# split the sentence input by the user by a space and created a list for it
sentence_split = sentence.split(" ")

# # calculate the length of the split sentence
length_split = (len(sentence_split))

# calculate the middle part of the split sentence (from 25% to 75%)
start_split = round(length_split * 25 / 100)
end_split = round(length_split * 75 / 100)

# calculate the middle of the split sentence
sentence_split = sentence_split[start_split:end_split]

# define a variable for joining the split sentence back together
glue = " "

# join the split sentence back together from the list
sentence_split = glue.join(sentence_split)

# print the middle of the joined sentence (and compare it to the other result)
print(sentence_split)