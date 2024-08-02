import art
import sys 

# Variables
print(art.filtro_ascii)

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}




#  Funciones
def user_inputs():
    user_input= []
    for i in range(len(sys.argv)):
        user_input.append(sys.argv[i])
    return user_input
    

def filtro(precios, cut_value, mayor = True):
    productos_filtrados = []
    if mayor ==True:
        productos_filtrados = [key for key,value in precios.items() if int(value) > int(cut_value)]
    else:
        productos_filtrados = [key for key,value in precios.items()  if int(value) < int(cut_value)]
    
    print(",".join(productos_filtrados))
       
            

user = user_inputs()

if(len(user) <= 2):
    filtro(precios, user[1])
elif(len(user) <= 3):
     filter_selec = False if(str(user[2]).lower() == 'menor') else True
     filtro(precios, int(user[1]), filter_selec)
else:
    print("Lo sentimos, no es una operación válida")
   
