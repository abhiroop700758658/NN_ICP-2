in_file=open("input.txt","r")
lines=in_file.readlines()
unique_words = set(lines)
word_list=[]
print("".join(lines))
print("\nWord_count:\n")


out_file=open("output.txt","w")
out_file.write("".join(lines))
out_file.write("\nWord_count:\n")

for line in lines:
        words = line.strip().split()
        for word in words:
            word_list.append(word)
unique = list(set(word_list))
for i in range(len(unique)):
      out_file.write(unique[i]+": "+str(word_list.count(unique[i]))+"\n")
      print(unique[i]+": "+str(word_list.count(unique[i]))+"\n")
