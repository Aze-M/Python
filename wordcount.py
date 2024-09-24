import re

file = open("./shakespeare.txt", encoding="utf-8", errors="ignore")
lines = file.readlines()
word_dict = {}

for line in lines:
    buffer = line.split(" ")

    for word in buffer:
        word = re.sub("\\W+|[_+]","",word)

        if word == " " or word == "":
            continue

        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1

out_list = []

for word in word_dict.keys():
    out_list.append((word,word_dict[word]))

out_list.sort(key = lambda x : -x[1])
tally = 0

for word in out_list:
    tally+=word[1]
    print(f"{word[0]} was found {word[1]} times.")

print(f"A total of {tally} words were used.")
print(f"A total of {len(out_list)} different words were used.")
print(f"Most common word was: '{out_list[0][0]}' at a count of {out_list[0][1]}.")