
import numpy as np
word1=input("Enter word which is to transformed")
word2=input("Enter word which from which a word is to be transformed")
lenword1=len(word1)
lenword2=len(word2)
costmatrix=np.zeros([len(word1)+1,len(word2)+1],dtype=int)
operationmatrix=np.chararray([len(word1)+1,len(word2)+1],unicode=True)
operationmatrix[0][0]='H'
for i in range(0,lenword1+1):
    for j in range(0,lenword2+1):
        if i==0 and j>0:
            costmatrix[i][j]=costmatrix[0][j-1]+1
            operationmatrix[i][j]='I'
        if j==0 and i>0:
            costmatrix[i][j]=costmatrix[i-1][0]+1
            operationmatrix[i][j]='D'
        if i>0 and j >0:
            insertcost=costmatrix[i][j-1] + 1
            deletecost=costmatrix[i-1][j] + 1
            if word1[i-1]==word2[j-1]:
                updatecost=costmatrix[i-1][j-1]
            else:
                updatecost=costmatrix[i-1][j-1]+2
            minimum=min(insertcost,deletecost,updatecost)
            costmatrix[i][j]=minimum
            if minimum==updatecost:
                operationmatrix[i][j]='U'
            elif minimum==insertcost:
                operationmatrix[i][j]='I'
            else:
                operationmatrix[i][j]='D'
print(operationmatrix,costmatrix,sep="\n")
print("\nCost of editing is:",costmatrix[lenword1][lenword2])
a=[]
b=[0,0,0]
i=lenword1
j=lenword2
p=0
while i>-1 or j>-1:
    if operationmatrix[i][j]=='U':
        operation='U'
        cost=costmatrix[i][j]
        i-=1
        j-=1
        b[0]=b[0]+1
    elif operationmatrix[i][j]=='I':
        operation='I'
        cost=costmatrix[i][j]
        j-=1
        b[1]=b[1]+1
    elif operationmatrix[i][j]=='D': 
        operation='D'
        cost=costmatrix[i][j]
        i-=1
        b[2]=b[2]+1
    elif  operationmatrix[i][j]=='H': 
        operation='H'
        cost=0
        i-=1
        j-=1
    a.append([]) 
    a[p] = [cost,operation]
    p=p+1
print("\nPATH:",a)
print("\nNUMBER OF UPDATES:",b[0])
print("\nNUMBER OF INSERT:",b[1])
print("\nNUMBER OF DELETE:",b[2])

    
        
        
            
            
    
        



