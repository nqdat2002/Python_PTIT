s = input()
l = s.split('.')
if len(l) > 2 or l[-1].lower() != 'py':
    print('no')
else:
    print('yes')