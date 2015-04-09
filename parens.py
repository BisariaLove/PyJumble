name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for lines in handle:
    if lines.startswith("From: "):
        words = lines.split()
        count[words[1]] = count.get(words[1],0)+1
bigcount= None
bigword = None
for word,num in count.items():
    if bigcount is None or num > bigcount:
        bigcount = num
        bigword = word
print bigword, bigcount


