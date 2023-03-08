text_list = ['x','xxx','xxxxx','xxxxxxx','']

string_len = list( map(lambda x: len(x),text_list))
print(string_len)


x = list(zip(string_len,text_list))


for i, (j,y) in enumerate(x,1):
    print(i,j,y)

