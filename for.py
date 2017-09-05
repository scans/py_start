#encoding=utf-8

for a in [1,2,3,4]:
    print a


for a,b in [[1,2],[3,4]]:
    print a,b


scope={'chen':100,'li':60,'ou':'90'}

for key in scope:
    print key

for value in scope.itervalues():
    print value

for item in scope.iteritems():
    print item
