str = input('Enter a string : ')
# if the len of intesection of str and "aeiou" is greater or equal
# than 5 than all vowels are present in str
if len(set(str.lower()).intersection("aeiou")) >= 5:
    print('Accepted')
else:
    print('Rejected')
