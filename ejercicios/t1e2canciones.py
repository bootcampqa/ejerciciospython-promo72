#Pide a la usuaria que introduzca la siguiente información sobre su canción favorita:
cancion_fav = input("¿Cuál es el título de tu canción favorita?")

artista_fav = input("¿Cuál es el nombre del artista?")

album_fav = input("¿Cuál es el título del álbum?")

año_fav = int(input("¿Cuál es el año de lanzamiento?"))


duracion_fav = float(input("¿Cuál es la duración de la canción en segundos?"))

video_fav = input("¿Tiene videoclip? Si/No")

#Muestra la información introducida
print ("Canción favorita", cancion_fav) 
print ("Artista",artista_fav)
print ("Album",album_fav)
print ("Año",año_fav)
print ("Duración",duracion_fav)
print ("Tiene videoclip",video_fav)



#Solicita los mismos datos de la canción que menos le guste
cancion_hate = input("¿Cuál es el título de tu canción que odias?")

artista_hate = input("¿Cuál es el nombre del artista?")

album_hate = input("¿Cuál es el título del álbum?")

año_hate = int(input("¿Cuál es el año de lanzamiento?"))

duracion_hate = float(input("¿Cuál es la duración de la canción en segundos?"))

video_hate = input("¿Tiene videoclip? Si/No")

#Muestra la información introducida
print ("Canción",cancion_hate)
print ("Artista",artista_hate)
print ("Álbum",album_hate)
print ("Año",año_hate)
print ("Duración",duracion_hate)
print ("Vídeo",video_hate)