#s2 = input("enter the line: ")
#for x in s2.split("a"):
#    print(x)

"""You can use the .split() function to split a string by spaces and that will give you back a list of words that you can then loop and print them out.

The function accepts a string that will be used as the delimiter (e.g ",")
if this argument is not specified or is None it will run an algorithm that will consider a sequence of whitespaces as a single separator and hence, as a result,
no matter how many spaces there are between the words you will get a list of words with no whitespaces at the start or the end of each substring."""

phrase = input("Enter a phrase: ")
words = phrase.split()  # ['I', 'need', 'practice']
print(words)
for word in words:
  print(word)