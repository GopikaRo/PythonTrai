strg="""welcome to python's
       world"""
print(strg)
print(len(strg))         ##  32(including all white spaces)
print(strg[5])           ##  m
print(strg+' python')    ##  welcome to python's world python(concatenate)
#print(strg[33])          ##  index out of range
pi=3.14
text='the value of pi is ' + str(pi)
print(text)               ##   the value of pi is 3.14
#string methods
s=" Gopika"
print(s.lower())          # gopika
print(s.upper())          # GOPIKA
print(s.strip())          #Gopika(remove white spaces)
print(s.isalpha())        #false
print(s.isdigit())        #false
print(s.isspace())        #false
print(s.startswith(' '))  #True(here starts with space)
print(s.endswith('a'))    #True
print(s.find('p'))        #3
print(s.find('r'))        #-1(r not found)
print(s.replace('o','r')) #Grpika
#string slices
t='helloworld'
print(t[1:5])             #ello
print(t[0:3])             #hel
print(t[2:])              #lloworld
print(t[-1])              #d
print(t[-2:])             #ld
print(t[:-3])             #hellowo
#STRING FORMAT
name='Gopika'
print('my name is {}'.format(name))    #my name is Gopika     (format() methond)
print(f'my name is {name}')            #my name is Gopika     (f-strings)
mydict={'name':'antony'}
print(f'my name is {mydict["name"]}')  #my name is antony
mydict={'tires':4,'doors':2}
print(f'mydict={mydict}')
#STRING %
text=("a farmer had %d sons,"
   "they always %s among themselves,"
    "their father %s to live in peace"
    %(4,'quarreled','advised'))
print(text)                           #a farmer had 4 sons,they always quarreled among themselves,their father advised to live in 
