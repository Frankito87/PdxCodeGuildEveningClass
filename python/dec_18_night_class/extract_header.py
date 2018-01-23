email = input("Give me an email address: ")

at_index = email.index('@')

# com_index = email.index('.com')

com_index = email.rindex('.')



print(email[at_index + 1:com_index])
