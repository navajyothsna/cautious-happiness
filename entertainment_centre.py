import fresh_tomatoes
import media

Urvi = media.Movie( "Urvi",
                   "151 minutes",
                   "crime drama",
                   "https://mir-s3-cdn-cf.behance.net/project_modules/1400/df67db34973739.584c5ee3da36e.jpg",
                   "https://www.youtube.com/watch?v=H2T1BxCZCzk")

That_Girl_in_Yellow_Boots = media.Movie("That Girl in Yellow Boots",
                                        "99 Minutes",
                                        "suspance thriller",
                                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMGVjNGEwNWMtYTlhZS00Yjk0LWEyY2UtNDUyOTFlOGRmMmJmXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UY268_CR3,0,182,268_AL_.jpg",
                                        "https://www.youtube.com/watch?v=FRDRfQ_mZnA")

Kirik_Party = media.Movie("Kirik Party",
                          "165 Minutes",
                          "The progression of Karna and gang from being a bunch of mischief makers to responsible adults is the theme of Kirik Party. It is a fun filled film with lots of melodious songs.",
                          "https://in.bmscdn.com/iedb/movies/images/mobile/listing/xxlarge/kirik-party-et00050740-15-12-2016-05-23-26.jpg",
                          "https://www.youtube.com/watch?v=IfvnbER_6sQ")


Devdas = media.Movie("Devdas",
                     "165 Minutes",
                     "Romantic comedy",
                     "http://www.scenetheworld.com/wp-content/uploads/2017/03/Devdas-800x500.jpg",
                     "https://www.youtube.com/watch?v=8tuHQWGMQwY")

DDLJ = media.Movie("Dilwale Dulhania Le Jayenge",
                   "189 Minutes",
                   "Romantic",
                   "https://cdn.pinkvilla.com/files/styles/contentpreview/public/dilwale-dulhania-le-jayenge_0_0_0_0.jpg?itok=TK42V-u0",
                   "https://www.youtube.com/watch?v=c25GKl5VNeY&vl=en")

Dil_chahta_Hai = media.Movie("Dil Chahta Hai",
                          "184 Minutes",
                          "Comedy-drama",
                          "https://is2-ssl.mzstatic.com/image/thumb/Music60/v4/07/cf/de/07cfde84-5dca-010b-27e4-35ccd0f1b998/8902894114844_cover.jpg/1200x630bb.jpg",
                          "https://www.youtube.com/watch?gl=SG&v=m13b25V0B10&hl=en-GB")


movies = [Urvi, That_Girl_in_Yellow_Boots, Kirik_Party, Devdas, DDLJ, Dil_chahta_Hai]
fresh_tomatoes.open_movies_page(movies)
