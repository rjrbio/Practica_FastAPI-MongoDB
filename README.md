# Practica FastAPI + MongoDB
##### Para virtualizar con docker:
```docker
  - Localizar el directorio donde se encuentra el programa
  - Levantar el contenedor:
      docker-compose up
 # Para usar MongoDB desde consola:
  - En nueva terminal, comprobar el nombre del contenedor:
      docker ps
  - Ejecutar el programa:
      docker exec -it nombre-del-contenedor bash
  - Entrar en MongoDB:
      mongosh -username nombre-de-usuario
```
## Práctica dockerizada FastAPI con MongoDB (probando EndPoints)
En esta práctica usamos **Docker** para virtualizar la api FastAPI y el gestor de base de datos MongoDB con la finalidad de aprender el uso de los EndPoints.

##### Crear base de datos
Comenzando por crear la base de datos "videojuegos" en la que vamos a ingresar varios juegos en la tabla "juegos":

![bdd](https://github.com/user-attachments/assets/91e9a9ec-47e2-4c3b-a377-61eeaa86b464)

#### Agregar juego
Siguiendo por ingresar un primer juego:

![bdd2](https://github.com/user-attachments/assets/3db12c3c-c6e3-4913-a66e-f7ae63f9976c)

#### Uso de EndPoints
Y a partir de aquí ya podemos empezar a usar todos los Endpoints creados.

Como *Listar*

![listjuego](https://github.com/user-attachments/assets/20154888-947c-41e9-828c-fe1a6a4c8795)

*Obtener datos de un juego*

![verjuego](https://github.com/user-attachments/assets/3fa943ac-47af-4533-9696-376312dcd6d4)

*Agregar nuevo juego*

![postjuego](https://github.com/user-attachments/assets/e888a6f2-faf3-48d3-8c3e-b3af46195e2d)

*Eliminar juego*

![borrajuego](https://github.com/user-attachments/assets/559b419d-0fe9-4ef9-996e-6180b0b6a062)

O *Actualizar juego*

![putjuego](https://github.com/user-attachments/assets/c630ecda-afdb-4de2-8449-1e494a8193d7)

Exactamente igual que lo haría mediante comandos en consola:

![bdd3](https://github.com/user-attachments/assets/54d3aef7-3fb4-4ae3-8b63-49f78fa3d9ec)
