the_things_about_pizza=['thick','rich','ooey gooey','thinner crust','cheese','dough','meat']
pz1=the_things_about_pizza
pz2=pz1[:]
pz2.append('sauce')

print('pz1 includes the things below')
print(pz1)

print('\npz2 includes the things below')
print(pz2)

print('\nThis the list of pz1')
for thing1 in pz1:
    print(thing1)

print('\nThis is the list of pz2')
for thing2 in pz2:
    print(thing2)