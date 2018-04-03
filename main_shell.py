import media
import fresh_tomatoes
import requests, json

matrix = requests.get("https://api.themoviedb.org/3/movie/603?api_key=da2bb8468c2a728673dc669aaaec512a").json()

matrix_title = matrix['title']
matrix_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + matrix['poster_path']
matrix_overview = matrix['overview']
matrix_youtube_id = 'm8e-FF8MsqU'
matrix_trailer = 'https://www.youtube.com/watch?v=m8e-FF8MsqU'


arrival = requests.get("https://api.themoviedb.org/3/movie/329865?api_key=da2bb8468c2a728673dc669aaaec512a").json()

arrival_title = arrival['title']
arrival_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + arrival['poster_path']
arrival_overview = arrival['overview']
arrival_youtube_id = 'FMo3UJ4B4g'
arrival_trailer = 'https://www.youtube.com/watch?v=tFMo3UJ4B4g'


godfather = requests.get("https://api.themoviedb.org/3/movie/238?api_key=da2bb8468c2a728673dc669aaaec512a").json()

godfather_title = godfather['title']
godfather_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + godfather['poster_path']
godfather_overview = godfather['overview']
godfather_youtube_id = 'sY1S34973zA'
godfather_trailer = 'https://www.youtube.com/watch?v=sY1S34973zA'


holyMotors = requests.get("https://api.themoviedb.org/3/movie/103328?api_key=da2bb8468c2a728673dc669aaaec512a").json()

holyMotors_title = holyMotors['title']
holyMotors_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + holyMotors['poster_path']
holyMotors_overview = holyMotors['overview']
holyMotors_youtube_id = 'NWu9WjEcdbk'
holyMotors_trailer = 'https://www.youtube.com/watch?v=NWu9WjEcdbk'

clockworkOrange = requests.get("https://api.themoviedb.org/3/movie/185?api_key=da2bb8468c2a728673dc669aaaec512a").json()

clockworkOrange_title = clockworkOrange['title']
clockworkOrange_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + clockworkOrange['poster_path']
clockworkOrange_overview = clockworkOrange['overview']
clockworkOrange_youtube_id = 'SPRzm8ibDQ8'
clockworkOrange_trailer = 'https://www.youtube.com/watch?v=SPRzm8ibDQ8'

oneFlew = requests.get("https://api.themoviedb.org/3/movie/510?api_key=da2bb8468c2a728673dc669aaaec512a").json()

oneFlew_title = oneFlew['title']
oneFlew_poster = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2/' + oneFlew['poster_path']
oneFlew_overview = oneFlew['overview']
oneFlew_youtube_id = 'OXrcDonY-B8&t=2s'
oneFlew_trailer = 'https://www.youtube.com/watch?v=OXrcDonY-B8&t=2s'


matrix = media.Movie(matrix_title, matrix_poster, matrix_overview, matrix_youtube_id, matrix_trailer)

arrival = media.Movie(arrival_title, arrival_poster, arrival_overview, arrival_youtube_id, arrival_trailer)

godfather = media.Movie(godfather_title, godfather_poster, godfather_overview, godfather_youtube_id, godfather_trailer)

holyMotors = media.Movie(holyMotors_title, holyMotors_poster, holyMotors_overview, holyMotors_youtube_id, holyMotors_trailer)

clockworkOrange = media.Movie(clockworkOrange_title, clockworkOrange_poster, clockworkOrange_overview, clockworkOrange_youtube_id, clockworkOrange_trailer)

oneFlew = media.Movie(oneFlew_title, oneFlew_poster, oneFlew_overview, oneFlew_youtube_id, oneFlew_trailer)


list_of_favourite_movies = [matrix, arrival, godfather, holyMotors, clockworkOrange, oneFlew]

fresh_tomatoes.open_movies_page(list_of_favourite_movies)
