import requests
import json

import media
import fresh_tomatoes

# Getting movie data by making requests to themoviedb.org API using
# personal API key.
try:
    matrix = requests.get(
        "https://api.themoviedb.org/3/movie/"
        "603?api_key=da2bb8468c2a728673dc669aaaec512a").json()
# in case the request fails, skipping and executing the code further
except Exception as e:
    pass

# Extracting necessary data from json object which was returned after API
# request.
matrix_title = matrix['title']
matrix_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + \
    matrix['poster_path']
matrix_overview = matrix['overview']

# Since themoviedb.org API does not contain movie trailers, id and trailer
# url are taken from youtube.com.
matrix_youtube_id = 'm8e-FF8MsqU'
matrix_trailer = 'https://www.youtube.com/watch?v=m8e-FF8MsqU'

# Getting movie data by making requests to themoviedb.org API using
# personal API key.
try:
    arrival = requests.get(
        "https://api.themoviedb.org/3/movie/"
        "329865?api_key=da2bb8468c2a728673dc669aaaec512a").json()
# in case the request fails, skipping and executing the code further
except Exception as e:
    pass

# Extracting necessary data from json object which was returned after API
# request.
arrival_title = arrival['title']
arrival_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + \
    arrival['poster_path']
arrival_overview = arrival['overview']

# Since themoviedb.org API does not contain movie trailers, id and trailer
# url are taken from youtube.com.
arrival_youtube_id = 'FMo3UJ4B4g'
arrival_trailer = 'https://www.youtube.com/watch?v=tFMo3UJ4B4g'

# Getting movie data by making requests to themoviedb.org API using
# personal API key.
try:
    godfather = requests.get(
        "https://api.themoviedb.org/3/movie/"
        "238?api_key=da2bb8468c2a728673dc669aaaec512a").json()
# in case the request fails, skipping and executing the code further
except Exception as e:
    pass

# Extracting necessary data from json object which was returned after API
# request.
godfather_title = godfather['title']
godfather_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + \
    godfather['poster_path']
godfather_overview = godfather['overview']

# Since themoviedb.org API does not contain movie trailers, id and trailer
# url are taken from youtube.com.
godfather_youtube_id = 'sY1S34973zA'
godfather_trailer = 'https://www.youtube.com/watch?v=sY1S34973zA'

# Getting movie data by making requests to themoviedb.org API using
# personal API key.
try:
    holyMotors = requests.get(
        "https://api.themoviedb.org/3/movie/"
        "103328?api_key=da2bb8468c2a728673dc669aaaec512a").json()
# in case the request fails, skipping and executing the code further
except Exception as e:
    pass

# Extracting necessary data from json object which was returned after API
# request.
holyMotors_title = holyMotors['title']
holyMotors_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + \
    holyMotors['poster_path']
holyMotors_overview = holyMotors['overview']

# Since themoviedb.org API does not contain movie trailers, id and trailer
# url are taken from youtube.com
holyMotors_youtube_id = 'NWu9WjEcdbk'
holyMotors_trailer = 'https://www.youtube.com/watch?v=NWu9WjEcdbk'

# Getting movie data by making requests to themoviedb.org API using
# personal API key.
try:
    clockworkOrange = requests.get(
        "https://api.themoviedb.org/3/movie/"
        "185?api_key=da2bb8468c2a728673dc669aaaec512a").json()
# in case the request fails, skipping and executing the code further
except Exception as e:
    pass

# Extracting necessary data from json object which was returned after API
# request
clockworkOrange_title = clockworkOrange['title']
clockworkOrange_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + \
    clockworkOrange['poster_path']
clockworkOrange_overview = clockworkOrange['overview']

# Since themoviedb.org API does not contain movie trailers, id and trailer
# url are taken from youtube.com
clockworkOrange_youtube_id = 'SPRzm8ibDQ8'
clockworkOrange_trailer = 'https://www.youtube.com/watch?v=SPRzm8ibDQ8'

# Getting movie data by making requests to themoviedb.org API using
# personal API key.
try:
    oneFlew = requests.get(
        "https://api.themoviedb.org/3/movie/"
        "510?api_key=da2bb8468c2a728673dc669aaaec512a").json()
# in case the request fails, skipping and executing the code further
except Exception as e:
    pass

# Extracting necessary data from json object which was returned after API
# request
oneFlew_title = oneFlew['title']
oneFlew_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + \
    oneFlew['poster_path']
oneFlew_overview = oneFlew['overview']

# Since themoviedb.org API does not contain movie trailers, id and trailer
# url are taken from youtube.com.
oneFlew_youtube_id = 'OXrcDonY-B8&t=2s'
oneFlew_trailer = 'https://www.youtube.com/watch?v=OXrcDonY-B8&t=2s'

# Creating class Movie objects which will be members of
# list_of_favourite_movies array.
matrix = media.Movie(matrix_title, matrix_poster,
                     matrix_overview, matrix_youtube_id, matrix_trailer)
arrival = media.Movie(arrival_title, arrival_poster,
                      arrival_overview, arrival_youtube_id, arrival_trailer)
godfather = media.Movie(
    godfather_title,
    godfather_poster,
    godfather_overview,
    godfather_youtube_id,
    godfather_trailer)
holyMotors = media.Movie(
    holyMotors_title,
    holyMotors_poster,
    holyMotors_overview,
    holyMotors_youtube_id,
    holyMotors_trailer)
clockworkOrange = media.Movie(
    clockworkOrange_title,
    clockworkOrange_poster,
    clockworkOrange_overview,
    clockworkOrange_youtube_id,
    clockworkOrange_trailer)
oneFlew = media.Movie(oneFlew_title, oneFlew_poster,
                      oneFlew_overview, oneFlew_youtube_id, oneFlew_trailer)

# Creating array containing class Movie objects.
list_of_favourite_movies = [matrix, arrival,
                            godfather, holyMotors, clockworkOrange, oneFlew]

# Using open_movies_page function with list_of_favourite_movies array to
# generate html displaying movies list.
fresh_tomatoes.open_movies_page(list_of_favourite_movies)
