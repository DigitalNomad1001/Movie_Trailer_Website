import fresh_tomatoes
import media

# Stephanie's Suggested Movie Trailers
# Instance Variables = movie_title, poster_image, trailer_youtube

fireplace_for_your_home = media.Movie("Fireplace for Your Home",
                                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMzM2OTAzOTE1N15BMl5BanBnXkFtZTgwMDU4NjA2MDE@._V1_UY268_CR1,0,182,268_AL_.jpg",
                                      "https://www.youtube.com/watch?v=n3Vuwop3MGA")

avatar = media.Movie("Archer",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/5/57/Archer_S5_DVD.jpg/220px-Archer_S5_DVD.jpg",
                     "https://www.youtube.com/watch?v=zcKk22LNdJE")

doctor_strange = media.Movie("Doctor Strange",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=kNdM7b1Lm04")

the_tomorrow_people = media.Movie("The Tomorrow People",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyMDA4NjY0Nl5BMl5BanBnXkFtZTgwMDgzNDIxMDE@._V1_.jpg",
                                  "https://www.youtube.com/watch?v=vUfHbwdbPzw")

halt_and_catch_fire = media.Movie("Halt and Catch Fire",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNjAyMDg1Nl5BMl5BanBnXkFtZTgwMDQyNTA2OTE@._V1_.jpg",
                                  "https://www.youtube.com/watch?v=b35DGguOuEY")

new_girl = media.Movie("New Girl",
                       "https://upload.wikimedia.org/wikipedia/en/8/8c/New_Girl_S1_DVD.jpg",
                       "https://www.youtube.com/watch?v=D1NDNFZGY7k")

# Open movie trailer website in browser

movies = [fireplace_for_your_home, avatar, doctor_strange,
          the_tomorrow_people, halt_and_catch_fire, new_girl]

fresh_tomatoes.open_movies_page(movies)

