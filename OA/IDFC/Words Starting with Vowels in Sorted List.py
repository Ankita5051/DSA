def solve(sen):
    words=sen.split()
    words=sorted(words,key=lambda x:x.lower())

    found=False
    vowels=set("aeiou")

    for i,w in enumerate(words):
        if w[0] in vowels:
            print(w," ",i+1)
            found=True
    if not found:
        print(0)
solve("apple is a great food")