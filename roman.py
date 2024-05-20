roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
numerical_values = [1, 5, 10, 50, 100, 500, 1000]

roman_numeral = input("Enter a Roman numeral: ").upper()
total = 0
prev_value = 0

for symbol in reversed(roman_numeral):
    value = numerical_values[roman_numerals.index(symbol)]
    if value < prev_value:
        total -= value
    else:
        total += value
    prev_value = value

print("Numerical value:", total)


#numerical_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#roman_numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

#number = int(input("Enter a number: "))
#roman_numeral = ''

#for i in range(len(numerical_values)):
#    while number >= numerical_values[i]:
#        roman_numeral += roman_numerals[i]
#        number -= numerical_values[i]

# print("Roman numeral:", roman_numeral)
