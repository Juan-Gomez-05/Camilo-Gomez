Datos={
    "gender": "female",
    "date_of_birth": "05.08.02",
    "enrollment_semester": "Summer 2022",
    "semester_number": 6,
    "major": "Data Analytics",
    "number": 22100
 }
def NuevaClave(Clave,valor):
    flag=False
    for key in dict.keys():
        if key!=Clave:
            dict[key]=valor
            #print(f"key={key} claves={key}")
            return("La clave ya existe")
        else:
            flag=True
        return dict            




miclave=input("ingrese la nueva clave")
mivalor=input("ingrese valor asociado a la clave")
print(nuevaClave)=(Datos,miclave,mivalor)
print(Datos)




























# generar un diccionario 
#gnerar una nuva clave valor
#dado un valor buscar en el diccionario y devolver su clave