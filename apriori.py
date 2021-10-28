minsup=3
freq = dict()

#Generate dictionary key
def getStr(arr=list()):
    arr.sort()
    s=""
    for a in arr:
        s=s+','+a
    if len(s)>0:
        return s[1:]
    else:
        return s
#Proper subset-> a is subset of b
def subset(a,b):
    check=True

    for i in a:
        if i not in b:
            check=False
    #print(a,b,check)
    return check

#data=[['A','B','C'],['B','C','D'],['D','E'],['A','B','D'],['A','B','C','E'],['A','B','C','D']]
data=[['A','B','E'],['D','B','E','A'],['B','D'],['B','C'],['A','B','D'],['A','C'],['B','C'],['A','C'],['A','B','C','E'],['A','B','C']]


#First run to get all the individual frequencies
for i in range(len(data)):
    for j in range(len(data[i])):
        freq[data[i][j]]=freq.get(data[i][j],0)+1
    
#  I have defined this variable to divide the total frequency
#  by size of itemset at each iteration so that we can ignore
#  repetations
n=2
final=list()
print("\nApriori Algorithm by Agarwal and Srikant")
while(len(freq)>0):

    prune = dict()
    for i in freq:
        if(freq.get(i))>=minsup:
            prune[i]=freq[i]
    #if len(prune)>0:
    # for p in list(prune.keys()):
    #     for f in final:
    #         if subset(f.split(","),p.split(",")):
    #             print("Remove",f)
    #             final.remove(f)
    for p in list(prune.keys()):
        final.append(p)
    if len(prune)==0:
        break
    print("\n",(n-1),"-itemset: ")
    for p in list(sorted(prune.keys())):
        print(p," : ",prune.get(p))
    freq=dict()

    #Scan Database
    for i in range(len(data)):
        for p in list(prune.keys()):
            for d in data[i]:
                if d not in p:
                    #join previous pruned list with new items
                    t=p.split(",")+list(d)
                    if subset(t,data[i]):
                        #Count frequency
                        freq[getStr(t)]=freq.get(getStr(t),0)+1           

    for f in list(freq.keys()):
        freq[f]=int(freq.get(f)/n)
    n=n+1

#Recommendation
products = input("Enter what have you bought: ").split(",")

for i in range(len(final)):
    for j in range(len(final)):
        if final[i] is not  final[j]:
            if subset(list(final[i].split(",")),list(final[j].split(","))):
                final[i]='Z'
while 'Z' in final:
    final.remove('Z')

final.reverse()
    
for items in final:
    check = True
    for x in products:
        if x not in items:
            check = False
            break
    if check:
        item=items.split(",")
    
        print("Frequently bought together: ")
        for it in item:
            if it not in products:
                print(it)
        break