import json, requests

cabeceras = {
	'Title' : 'Titulo',
	'Year' : 'Año',
	'Rated' : 'Clasificación',
	'Released' : 'Publicado',
	'Runtime' : 'Duración',
	'Genre' : 'Genero',
	'Director' : 'Director',
	'Writer' : 'Escritor',
	'Actors' : 'Actores',
	'Plot' : 'Sinopsis',
	'Language' : 'Lenguaje',
	'Country' : 'Pais',
	'Awards' : 'Premios',
	'Poster' : 'Cartel',
	'Ratings' : 'Calificaciones',
	'Metascore' : 'Metascore',
	'imdbRating' : 'Ratings (imdb)',
	'imdbVotes' : 'Votos (imdb)',
	'imdbID' : 'imdbID',
	'Type' : 'Tipo',
	'DVD' : 'DVD',
	'BoxOffice' : 'Taquilla',
	'Production' : 'Producción',
	'Website' : 'Sitio web'
}
apikey = 'bb840ead'

#Send all data requests to:
url = 'http://www.omdbapi.com/'

#Poster API requests:
url_poster = 'http://img.omdbapi.com/'

# parameters = dict(
#     apikey=[yourkey]
#	  s='' # Trae varios resultados
# 	  i='', #A valid IMDb ID (e.g. tt1285016)
#     t='lost', #Movie title to search for.
#     type='', #Type of result to return. --> # movie, series, episode
#     y='', #Year of release.
#     plot='short', #Return short or full plot. --> # short, full --> default: short
#     r='json', #The data type to return. --> json, xml --> default: json
#     callback='', #JSONP callback name.
#     v='1', #API version (reserved for future use). --> default: 1
# )
parameters = dict(
	apikey=apikey,
    s='lost' #Movie title to search for.
)

resp = requests.get(url=url, params=parameters)
print(resp.text)
data = json.loads(resp.text)
print("="*20)
for x in data:
	c = cabeceras[x] if (x in cabeceras) else x
	print(c +' = '+ str(data[x]))

# print(data['Title'])