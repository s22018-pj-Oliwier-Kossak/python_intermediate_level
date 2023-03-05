days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()
workdays.pop()
workdays.pop()

print(workdays)
print(days)

print(id(days))
print(id(workdays))

print()
tab = [1,2,3]
tab2 = [1,2,3]
tab3 = tab
tab3 +=[4]
print(id(tab))
print(id(tab2))
print(id(tab3))
print(tab)
print(tab3)