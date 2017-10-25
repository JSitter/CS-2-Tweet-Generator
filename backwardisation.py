import sys

#create a set

number = len(sys.argv)-1
words = sys.argv[1:]
backwords = []

index = -1
while len(words) > 0:
    backwords.append(words.pop())

for item in backwords:
    print(item, end=" ")

print("")
