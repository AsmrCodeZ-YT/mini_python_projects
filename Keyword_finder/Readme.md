
**Find KeyWord**
##best for linkedin and job describtion
![txt2img-stable2](Keyword_finder\Src\PICK.png)


`
counter = 0
counts = {}

#########################################
file = input("Give me Your FIle ::: ")

with open(file, "r") as f:
    for item in f.readlines():
        b = item.splitlines()

        words = b[0].split()

        for word in words:
            counts.setdefault(word, 0)
            counts[word] = counts[word] + 1

            listofkeys = list(counts.keys())

        result = sorted(counts.items(),
                        key=lambda x: x[+1])


f = open("output.txt", "w")

num = 0
for t in result:

    line = " ".join(str(x) for x in t)

    if t[1] != num:
        num = t[1]
        f.writelines("\n")
        f.writelines("*"*80)
        f.writelines("\n")
    if t[1] != 1:
        f.writelines(f"({line}), ")
        counter += 1
        if counter == 5:
            f.writelines("\n")
            counter = 0

f.close()

print(result)


`