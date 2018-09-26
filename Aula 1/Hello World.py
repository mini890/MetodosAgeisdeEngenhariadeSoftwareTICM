x = 10
#x #Doesn't print

print (x)

y = x + 12
s1 = "alfa"
s1 = 'alfa'
s2 = '''
alfa
beta
gama'''

print (s2)

s = "um dois três"

print (s[2])

print (s[2:4]) #Primeiro está incluido, segundo não

print (s[-1]) #Começa do fim

print (len(s)) #Comprimento

print (s[len(s)-1])

print (s[1:-1]) #Deita fora o 1º e o ultimo

print (s[1:-1:2]) #???? Dois é a direção?

print (s[-1:0:-1] + s[0]) #Inverte string

a = [12, 34, 15, 17]

print (a[0]) #12

print (a[-1]) #17

b = []

print (len(b))

b.append(23)

print (b) #23

b.append(24)

print (b) #23, 24