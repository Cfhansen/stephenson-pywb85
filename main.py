###solution to exercise 85 in ben stephenson's "the python workbook".

def get_ordinal(num_):

  mydict = {  1:  'first',
            2:  'second',
            3:  'third',
            4:  'fourth',
            5:  'fifth',
            6:  'sixth',
            7:  'seventh',
            8:  'eighth',
            9:  'ninth',
            10: 'tenth',
            11: 'eleventh',
            12: 'twelfth' }

  if not (num_ in range(1,13)):
    return ''
  else:
    return mydict[num_]

for i in range(1,13):
  print(f'{i} is the {get_ordinal(i)} number.')
