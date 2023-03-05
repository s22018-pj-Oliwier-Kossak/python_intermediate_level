scrambles = [

    { 'scramble': 'D R2 F L2 U2 F2 D2 B2 U2 R2 B\' U2 L D2 L\' D F D\' U2 R\''},

    { 'scramble': 'B\' R2 F2 L\' B2 R2 F2 D2 L\' B2 L\' U2 F2 D\' F U\' L2 B\' R F\'' },

    { 'scramble': 'B\' D2 L2 U2 B2 R U2 F2 L\' D2 R2 B\' U B F\' R2 D2 F D2'} ]

for i in scrambles:
    if len(i['scramble']) < 53:
        break
else:
    print("correct scrambles")
