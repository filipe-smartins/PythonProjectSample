from module1_dir.module1 import print_lower_name, print_upper_name, print_capitalized_name
from module2_dir.module2 import soma
from settings.settings import name

print("Your name is: ", name)
print(print_lower_name(name))
print(print_upper_name(name))
print(print_capitalized_name(name))

print(soma('R$2.500', 'R$2.500'))
print(soma('R$ 2.500', 'R$ 2.500'))
print(soma('USD2.500', 'USD 2.500'))
print(soma('2.500', 'R$2.500'))
print(soma('2500', '2500'))
