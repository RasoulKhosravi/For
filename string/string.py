
name = input ()
name = name.lower()
withoutVois = ['a', 'u', 'e', 'i', 'o']
output = ''
for i in name:
    if i in withoutVois:
        output = output + '.'
    else:
        output = output + i 
print (output)
