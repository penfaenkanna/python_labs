a = float(input('a: ').replace(',', '.'))
b = float(input('b: ').replace(',', '.'))
print('sum=', round(a+b, 2), '; ', 'avg=', round(avg, 2), sep='')
print(f'sum={a+b:.2f}; avg={(a+b)/2:.2f}')
