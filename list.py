fruits=['mango','banana','apple','grapes']
print(fruits[2])                    #apple
print(fruits[3])                    #grapes
fruit=fruits                        #does not copy the list 
print(fruit)                        #['mango','banana','apple','grapes']
print(fruits)                       #['mango','banana','apple','grapes']
fruit.append('orange')              #aappending new element
print(fruit)                        #['mango','banan','apple','grapes','orange']
print(fruits)                       #['mango','banana','apple','grapes','orange']
#for in python
squares=[1,4,9,16]
sum=0
for num in squares:
     sum += num
print(sum)                          #30
list=['gopika','anupria','anushree']
for i in list:
    print(i)                        #gopika
                                    #anupria
                                    #anushree
list2=['anu','ammu','chinnu']
if 'ammu' in list2:                 #tests if value is in list
    print('yea')                   #yea
#list methods
ls=['nyn','ram','geethu']
print(ls)
ls.append('jino')
print(ls)
ls.insert(0,'emil')
ls2=['a','b','c']
ls.extend(ls2)
print(ls)
ls.remove('emil')
print(ls)
ls.reverse()
ls.pop(0)
print(ls)
#list slicing
ls3=['a','b','c','d','e']
print(ls3[1:-1])                 #['b','c','d']
print(ls3[0:4])                  #['a','b','c','d'] 
ls3[0:2]='h'                 
print(ls3)                       #['h','c','d','e']

