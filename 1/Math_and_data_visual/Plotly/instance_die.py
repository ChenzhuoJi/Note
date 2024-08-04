from die import Die
import plotly.express as px
results=[]
die1=Die()
die2=Die()

for roll_num in range(100000):
    result=die1.roll()*die2.roll()#the function in class is an operation,a verb
    #class's object is a noun  
    #and we should def a instance
    #let class's attribute passed to it
    results.append(result)

frequencies=[]
poss_results=range(1,die1.num_sides**2+1)
frequency=results.count(value for value in poss_results)
frequencies.append(frequency)
print(frequencies)
title="Result of Rolling One D6 1_000 Times"
labels={"x":"Result","y":"Frequnecy of result" }
fig=px.bar(x=poss_results,y=frequencies,title=title,labels=labels)


fig.show()