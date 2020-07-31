## Aplicación sin Dash

1. Elegir un nombre para la aplicación. No debe tener mayusculas ni espacios.
2. Crear un directorio en "app/dashboard" con el nombre elegido.
3. Usar npconverter para convertir libreta de jupyter en script de python (saltar si no es libreta de jupyter).
4. Remover el comando "display(objeto)" del codigo (saltar si no se usa el comando).
5. Cambiar la ruta donde se guarda el html resultado a "data/nombre/nombre.html", donde nombre es el nombre de la aplicación.
6. Renombar el archivo a generate_html.py
7. Mover generate_html.py a "app/dashboard/nombre/"
8. Agregar app/dashboard/nombre/requirements.txt con los requerimientos para ejecutar la aplicación.

### Ejemplo:

1. Se tiene una aplicación que genera mapas de incidencia. El nombre será "mapa_incidencia".
2. Se crea el directorio "app/dashboard/mapa_incidencia/"
3. Se tiene una libreta llamada mapa_incidencia.ipynb con la aplicación:.
  
    Correr:
```bash
    jupyter nbconvert --to script mapa_incidencia.ipynb
```
  
    para obtener mapa_incidencia.py
 
4. El script obtenido con nbconvert usaba el comando display(), así que esas lineas son removidas.
5. La ruta donde se guarda el html resultado del script es "data/mapa_incidencia/mapa_incidencia.html" y se modifica el código.

        Si se guardaba como:
```py
    mapa.save("mapa_resultado.html")
```
        ahora se guarda como:
```py
    mapa.save("data/mapa_incidencia/mapa_incidencia.html")
```


6. Se renombra el script a generate_html.py
7. Se mueve el script dentro de "app/dashboard/mapa_incidencia/".
8. La aplicación utilizaba numpy, pandas y folium, así que creo un archivo requirements.txt y escribo esos requerimientos en el archivo y lo guardó en "app/dashboard/mapa_incidencia/"
