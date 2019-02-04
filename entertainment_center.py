import media
import fresh_tomatoes
# Criação das instâncias da classe movies
toy_story = media.Movie('Toy Story', 'A story of a boy and his toys that '
                                     'come to life',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/'
                        'Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')
avatar = media.Movie('Avatar', 'A marine on an alien planet',
                     'http://upload.wikimedia.org/wikipedia/id/b/b0/'
                     'Avatar-Teaser-Poster.jpg',
                     'http://www.youtube.com/watch?v=-9ceBgWV8io')
inception = media.Movie('Inception', 'as a professional thief who '
                                     'steals information by '
                                     'infiltrating the subconscious',
                        'https://upload.wikimedia.org/wikipedia/en/2/'
                        '2e/Inception_%282010%29_theatrical_poster.jpg',
                        'https://www.youtube.com/watch?v=YoHD9XEInc0')
shutter_island = media.Movie('Shutter Island',
                             'Leonardo DiCaprio stars as U.S. Marshal '
                             'Edward "Teddy" Daniels who is investigating a '
                             'psychiatric facility on Shutter Island '
                             'after one of the patients goes missing.',
                             'https://upload.wikimedia.org/wikipedia'
                             '/en/7/76/Shutterislandposter.jpg',
                             'https://www.youtube.com/watch?v=v8yrZSkKxTA')
the_butterfly_effect = media.Movie('The butterfly effect',
                                   ' Evan finds he has the ability to '
                                   'travel back in time to inhabit '
                                   'his former self '
                                   '(that is, his adult mind inhabits '
                                   'his younger body) and to change the '
                                   'present by '
                                   'changing his past behaviors',
                                   'https://upload.wikimedia.org/wikipedia'
                                   '/en/4/43/Butterflyeffect_poster.jpg',
                                   'https://www.youtube.com/watch'
                                   '?v=B8_dgqfPXFg')
avengers = media.Movie('Avengers: Infinity War', 'Avengers against Thanos',
                       'https://upload.wikimedia.org/wikipedia/en'
                       '/4/4d/Avengers_Infinity_War_poster.jpg',
                       'https://www.youtube.com/watch?v=6ZfuNTqbHE8')

movies = [toy_story, avatar, inception,
          shutter_island, the_butterfly_effect, avengers]
fresh_tomatoes.open_movies_page(movies)
