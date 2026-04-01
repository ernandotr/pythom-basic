from datetime import datetime
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
new_format = now.strftime("%d/%m/%Y %I:%M %p")
print("Data e hora formatada:", formatted_date)
print("Nova formatação:", new_format)


#Number formatting
number = 1234567.89123
formatted_number = "{:,.2f}".format(number)
print("Número formatado:", formatted_number)
formatted_price = "${:,.2f}".format(number)
print("Preço formatado:", formatted_price)
#String formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)