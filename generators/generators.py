ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

ports_all_with_all = ((i,j) for i in ports for j in ports)

for i in enumerate(ports_all_with_all,1):
    print(i)

ports_all_with_all2 = ((i,j) for i in ports for j in ports if i != j)

for i in enumerate(ports_all_with_all2,1):
    print(i)


ports_all_with_all3 = ((i,j) for i in ports for j in ports if i < j)

for (i,j) in enumerate(ports_all_with_all3):
    print("{} {}".format(i,j))
