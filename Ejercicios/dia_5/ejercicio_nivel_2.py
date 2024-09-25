#Ejercicios: Nivel 2

# La siguiente es una lista de 10 estudiantes por edades

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordena la lista y encuentra la edad mínima y máxima

ages.sort()
edad_minima = min(ages)
edad_maxima = max(ages)
print("Edades: ",ages)
print("La edad maxima es:",edad_maxima)
print("La edad minima es:",edad_minima )

# Agregue la edad mínima y la edad máxima nuevamente a la lista

ages.append(edad_maxima)
ages.append(edad_minima)
print(ages)

# Encuentra la edad media (un elemento intermedio o dos elementos intermedios divididos por dos)

edad_promedio = ages[6] + ages[7]/2
print(edad_promedio)

# Encuentra la edad promedio (suma de todos los elementos dividida por su número)

suma_iten = sum(ages)
numeros_str = [str(num) for num in ages]
dividendo = len(numeros_str)
edad_promedi = suma_iten/dividendo

print(edad_promedi)

# Encuentra el rango de edades (máximo menos mínimo)

valor_maximo = max(ages)
valor_minimo = min(ages)

rango_edades = valor_maximo - valor_minimo

print("El rando de edades esta entre: ",rango_edades)

# Compare el valor de (mín - promedio) y (máx - promedio), use el método abs()

valor_maximo = max(ages)
valor_minimo = min(ages)

promedio = sum(ages)/len(ages)

diferencia_min = abs(valor_minimo - promedio)
diferencia_max = abs(valor_maximo - promedio)

print(f"La diferencia minima es: {diferencia_min} y la maxima es: {diferencia_max}")


paises_muchos = [
  'Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# Encuentre el país o los países intermedios en la lista de países

intermedio = paises_muchos [1:-1] # Esto incluye todos los item menos el primero que es el elemento 0 y el ultimo que es el negativo 1

print(intermedio)

# Dividir la lista de países en dos listas iguales si es par o no hay un país más para la primera mitad.

longitud_lista = len(paises_muchos)
mitad = longitud_lista // 2

lista_primaria = paises_muchos[:mitad]
lista_secundaria = paises_muchos[mitad:]

print("primera mitad",lista_primaria)
print("segunda mitad",lista_secundaria)

# ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']. 
# Desglose los primeros tres países y el resto como países escandinavo

lista_nw = ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']


print("Los tres primeros paises:", lista_nw[0:3])
print("Paises escandinavos",lista_nw[3:])
