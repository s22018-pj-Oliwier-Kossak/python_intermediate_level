ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

ports_list = []

for i in ports:
    for j in ports:
        if i != j:
            ports_list.append((i,j))

print(ports_list)


ports_list2 = [(i,j) for i in ports  for j in ports if j
    != i ]

print(ports_list2)

ports_list3 = [(i,j) for i in ports  for j in ports if i < j ]
print(ports_list3)

print(list(enumerate(ports_list3,1)))

for i ,(x,y,z) in enumerate(zip(ports_list,ports_list2,ports_list3)):
    print(i,(x,y,z))


