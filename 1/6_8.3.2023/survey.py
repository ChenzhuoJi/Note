favorite_language={'jen':'python',
                   'alice':'c',
                   'newton':'c++',
                   'quenn':'python'}
namelist={'jen':'investageted',
          'alice':'to be investagetd',
          'newton':'to be investageted',
          'queen':'investageted',
          'king':'to be investageted'
          }
for name,situation in namelist.items():
    if situation=='investageted':
        print(f'\nHi {name.title()},thank you')
    else:
        print(f'\nWelcome to our survey,{name.title()}')