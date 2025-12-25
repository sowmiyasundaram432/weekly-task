word=input("Enter the sentence:").lower().split()
count={}
for i in word:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
for j,k in count.items():
    print(j,k)