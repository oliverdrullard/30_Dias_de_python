"""
    Escriba un script de Python que muestre la siguiente tabla
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125

"""
# Primera forma de hacerlo 
matx = [[1,1,1,1,1],
        [2,1,2,4,8],
        [3,1,3,9,27],
        [4,1,4,16,64],
        [5,1,5,25,125]

        ]

matx_len = len(matx)

for i in range(matx_len):
    print(matx[i])

# Segunda forma de hacerlo, en este caso la matriz no tendra cologna 

matx2= [[1,1,1,1,1],
        [2,1,2,4,8],
        [3,1,3,9,27],
        [4,1,4,16,64],
        [5,1,5,25,125]

        ]
print(matx2)



