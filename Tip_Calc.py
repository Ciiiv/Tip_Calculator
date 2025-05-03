while True:
    try:
        food_amount = float(input('What is the food amount? $:'))
        break
    except ValueError:
        print('You did not enter a number.')

while True:
    try:
        tip_percent = float(input('What is the tip percent? %:'))
        break
    except ValueError:
        print('You did not enter a number.')

#Convert percent to decimal
tip_amount = (food_amount) * (tip_percent / 100)
total = (food_amount) + (tip_amount)

print('\n')
print('----------------------------------')
print(f'Food Amount = ${food_amount}')
print(f'Tip Amount = ${round(tip_amount, 2)}')

#Use original percent value
if tip_percent >= 18:
    print("You're a Saint!")
elif 15 <= tip_percent < 18:
    print('Good Tip!')
else:
    print('CHEAPSKATE!')

print('\n')
print(f'Total = ${round(total, 2)}')
print('----------------------------------')