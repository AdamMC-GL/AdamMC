string ='lepelioio'
stringreverse = ''

for i in string:
    stringreverse = i + stringreverse

if stringreverse == string:
    print('Het woord ' + string + ' een palindroom')
else:
    print('Het woord ' + string + ' geen palindroom')
