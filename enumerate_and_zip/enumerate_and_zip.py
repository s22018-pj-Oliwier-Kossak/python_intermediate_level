projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']


for i,j in zip(projects,leaders):
    print(f'The leader of {i} is {j}')

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

projects_dates = list(enumerate(zip(projects,dates)))
print(projects_dates)

print()

for x,y,z in zip(dates,leaders,projects):
    print(x,y,z)

print()

for i, (x,y,z) in enumerate(zip(dates,leaders,projects)):
    print(i+1,x,y,z)