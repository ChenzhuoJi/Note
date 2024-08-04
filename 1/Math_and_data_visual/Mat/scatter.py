import matplotlib.pyplot as plt
import time
start=time.time()
def find_prinme(n):
    Prime=[]
    for a in range(2,n):
        for b in range(2,a):
            if a%b == 0:
                break
        else:
            Prime.append(a)
    return(len(Prime))
Prime=find_prinme(10000)
print(Prime)
end=time.time()
print(end-start)        
x_values=range(2,3001)
y_values=[find_prinme(x) for x in x_values]

fig,ax=plt.subplots()

ax.scatter(x_values,y_values,c=y_values,s=10)
ax.set_title("Squares nubmer",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of value",fontsize=14)
ax.tick_params(labelsize=14)
plt.show()


