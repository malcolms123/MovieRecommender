import requests, json
from movie import Movie

url = 'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc'

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzODljMDY2MTEwZTg0NDA2ZGM5NjY2OGM4NmU5MzA4NSIsInN1YiI6IjVlZmZjZmU5NTFjMDFmMDAzODM5ODllNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._dMqcptsJMBMy90dNp9Amj7EoPkNiL67dcNgN66f_cY"
}

response = requests.get(url, headers=headers)
results = response.json()['results']

# packaging into movies
movies = []
for result in results:
    movies.append(Movie(result))


# displaying data
for movie in movies:
    print(movie.title)
