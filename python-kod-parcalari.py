cmd, *args = input().split() # * birden fazla parametre almayi saglar

# USAGE
#   a, b, *rest = range(5)
#   >>> a, b, rest
#   (0, 1, [2,3,4])

b = any() #parametre olarak aldigi degerlerde hiç True var mı onu bulur 

#USAGE
#   print any(c.isalnum()  for c in str)

eval() #parametre olarak aldigi stringi kod olarak koşmayı sağlar

#USAGE

#   for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
#        any(eval("c." + test + "()") for c in s)

