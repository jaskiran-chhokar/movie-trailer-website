import fresh_tomatoes
import media


# create movie objects by passing required attributes
the_imitation_game = media.Movie("The Imitation Game",
                        "During World War II, the English mathematical genius Alan Turing tries to crack the German Enigma code with help from fellow mathematicians.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQQ5vi9xgRkP0nk5aRn8tcGEGRnOQyM-aAS1ldqfQSi_69V1yfU",
                        "https://www.youtube.com/watch?v=S5CjKEFb-sM")

titanic = media.Movie("Titanic",
                     "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                     "http://www.movienewsletters.net/photos/008672R1.jpg",
                     "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

harry_potter = media.Movie("The Prisoner of Azkaban",
                           "It's Harry's third year at Hogwarts; not only does he have a new Defense Against the Dark Arts teacher, but there is also trouble brewing. Convicted murderer Sirius Black has escaped the Wizards' Prison and is coming after Harry.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY4NTIwODg0N15BMl5BanBnXkFtZTcwOTc0MjEzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=_MKyGj6ZU10")


forrest_grump = media.Movie("Forrest Grump",
                            "Forrest Gump is a 1994 film starring Tom Hanks and directed by Robert Zemeckis. It is based on the 1986 novel of the same name by Winston Groom.",
                            "http://www.movienewsletters.net/photos/000014R1.jpg",
                            "https://www.youtube.com/watch?v=uPIEn0M8su0")

the_theory_of_everything = media.Movie("The Theory of Everything",
                                       "The Theory of Everything is the extraordinary true story of one of the world's greatest living minds, the renowned astrophysicist Stephen Hawking, who falls deeply in love with fellow Cambridge student Jane Wilde.",
                                       "http://t0.gstatic.com/images?q=tbn:ANd9GcSgW7hpezP5xtikV7WqwwqFm37kqMeJeFEGpYcO30CDcchn9g8m",
                                       "https://www.youtube.com/watch?v=Salz7uGp72c")

a_beautiful_mind = media.Movie("A Beautiful Mind",
                               "After John Nash, a brilliant but asocial mathematician, accepts secret work in cryptography, his life takes a turn for the nightmarish.",
                               "http://www.gstatic.com/tv/thumb/movieposters/28869/p28869_p_v8_ad.jpg",
                               "https://www.youtube.com/watch?v=a4KdpA59GOo")


#create and call movie object array
movie_objects = [the_imitation_game, titanic, harry_potter, forrest_grump, the_theory_of_everything, a_beautiful_mind] 
fresh_tomatoes.open_movies_page(movie_objects)
