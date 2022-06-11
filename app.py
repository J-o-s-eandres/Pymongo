from pymongo import MongoClient

MONGO_URI= 'mongodb://localhost' #conectar, ¿donde esta mi servidor?, ahorita local, en trabajo real se pone IP

client=MongoClient(MONGO_URI) #cursor o conexion a la BD, obtenemos las funciones CRUD 

db = client['teststore'] # almacenamos la db que estamos usando

collection= db['products']# almacenamos la coleccion que estamos usando


#collection.insert_one({"_id":2,"nombre": "Teclado", "Precio":300})#insertamos un documento a la bd y la coleccion para que esta se cree

#product_one ={"_id":1234,"nombre":"Monitor", "Precio":150}#creamos documentos
#product_two={"_id":12345,"nombre":"Mouse","Precio":100,"Stock":20}#sin necesidad de tener los mismos campos

#collection.insert_many([product_one,product_two])#al pasar varios datos (2) en este momento lo pasamos mediante una lista osea []

#results =collection.find({"_id": 2})#podemos filtrar poniendo entre {} la clave y valor a buscar

#for r in results:#recorremos los valores de la variable results e imprimimos
  #  print(r)      #obtenemos todo
    #print(r['nombre']) #obtener un campo especifico


#result =collection.find_one({"nombre": "Mouse"})#find_one es para 1 solo valor a buscar
#print(result)# como buscamos 1 valor se vuelve objeto y lo podemos imprimir si  recorrerlo son un simple print

#collection.delete_one({"Precio": 300})# elimina 1 elemento con las caracteristicas entre{}

#collection.delete_many({"Precio": 300})# elimina todo lo que tenga las caracteristicas entre {}

#collection.delete_many({})#PELIGROOOO ELIMINA TODOS LOS DATOS EXISTENTES EN LA COLECCION

#collection.insert_many([product_one,product_two]) #insertamos de nuevo


#collection.update_one({"nombre": "Monitor"}, {"$set": {"nombre":"Laptop HP","Precio": 300,}})#actualizamos 

#collection.update_one({"nombre": "Laptop HP"}, {"$inc": {"Precio": 60}})#con $inc incrementamos el valor del campo (Precio + 60 ), el campo estaba en 300 y ahora le sumamos 60 valor del campo es = 360

cantidad_documentos=collection.count_documents({})# contar cantidad de documentos en una collection
print(cantidad_documentos)# imprimir la cantidad de documentos

