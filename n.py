str1='abcda'
l1=list(str1[i:j] for i in range(len(str1)+1) for j in range(i+1,len(str1)+1))
#print(l1)
for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if len(l1[i]) > len(l1[j]):
                temp = l1[i]
                l1[i] = l1[j]
                l1[j] = temp
l1.reverse()
mx=0
#print(l1)
for i in l1:
  in1=list(i)
  in1=set(i)
  if mx<len(in1):
    mx=len(in1)
print(mx)

