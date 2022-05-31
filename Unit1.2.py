any_string = str(input())
print(len(any_string), 'the length of the string user entered')
any_string = any_string[:2] + any_string[(2+1):-1]
for i in any_string:
    if i == 'c':
        print(i, "There is a 'c'")
    else:
        print(i)
print(len(any_string), 'the length of the string after processing')


