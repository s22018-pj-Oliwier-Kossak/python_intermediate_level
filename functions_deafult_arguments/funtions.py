def christams_tree(character="*",how_many=2):
    space = how_many
    for i in range(how_many):

        print(' '*space+character*(i*2-1))
        space -= 1


christams_tree(how_many=10)
