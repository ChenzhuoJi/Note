def strix(A,pixel):
    Classify_A={}
    A_X=[]
    for row in A:
        key=row[0]
        A_X.append(row[0])
        if key not in Classify_A:
            Classify_A[key]=[]
        Classify_A[key].append(row[1])
    CA=Classify_A

    str=''
    i=0
    while i<=max(A_X):
        if i in A_X:
            j,kj=0,0
            #print(i)
            while True:
                #print(j)
                if kj<=len(CA[i])-1:
                    if j==CA[i][kj]:
                        j+=1
                        kj+=1
                        str+=pixel
                    elif j<CA[i][kj]:
                        j+=1
                        str+=' '
                    else:
                        i+=1
                        str+='\n'
                        break
            
                else:
                    i+=1
                    str+='\n'
                    break
        else:
            i+=1
            str+='\n'
    return(str)

        