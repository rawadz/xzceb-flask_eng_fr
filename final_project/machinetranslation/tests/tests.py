import translator

e2f_test_null = translator.english_to_french('')
print(e2f_test_null)

f2e_test_null = translator.french_to_english('')
print(f2e_test_null)

e2f_test = translator.english_to_french('Hello')
print(e2f_test)

f2e_test = translator.french_to_english('Bonjour')
print(f2e_test)
