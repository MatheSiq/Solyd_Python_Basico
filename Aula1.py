# a = 10
# b = 20
#
# print(a+b)

import re

texto_exemplo = "I like and banana, but not orange."
padrao = r"apple|banana"

resultados = re.findall(padrao, texto_exemplo)
print(resultados)  # Saída: ['apple', 'banana']