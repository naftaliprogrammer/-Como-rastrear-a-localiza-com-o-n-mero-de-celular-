import phonenumbers
from phonenumbers import geocoder

import numero_celular

pepnumber = phonenumbers.parse(numero_celular.numbers)
localizacao = geocoder.description_for_number(pepnumber, "pt")
print(localizacao)
