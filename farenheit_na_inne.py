kelvin_offset = 273.15
far_to_cel = 5 / 9
far_constant = 32
temp_far = int(input("Wprowadz temperature w stopniach Farenheita: "))
temp_kel = temp_far + kelvin_offset
temp_cel = (temp_far - far_constant) * far_to_cel

print("Temperatura w Farenheitach wynosi", temp_far)
print("Temperatura w Kelvinach wynosi", temp_kel)
print("Temperatura w Celcjuszach wynosi", temp_cel)