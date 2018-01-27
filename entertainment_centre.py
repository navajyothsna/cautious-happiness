import fresh_tomatoes
import media

Urvi = media.Movie("Urvi",
                   "2017",
                   "151 minutes",
                   "crime drama",
                   "kannada",
                   "B.S. Pradeep Varma",
                   "Shruthi Hariharan, Shraddha Srinath, Shweta Pandit, Madhukar Niyogi, Prabhu Mundkur, Bhavani Prakash, Janvi Jyoti",
                   "Three Women unite to fight a common Antagonist.",
                   "https://mir-s3-cdn-cf.behance.net/project_modules/1400/df67db34973739.584c5ee3da36e.jpg",
                   "https://www.youtube.com/watch?v=H2T1BxCZCzk")

That_Girl_in_Yellow_Boots = media.Movie("That Girl in Yellow Boots",
                                        "2011",
                                        "99 Minutes",
                                        "thriller tracing Ruth",
                                        "Hindi, English and Kannada",
                                        "Anurag Kashyap",
                                        "Kalki Koechlin, Naseeruddin Shah",
                                        "A British Women facing challenges while attempting to locate her father in India",
                                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMGVjNGEwNWMtYTlhZS00Yjk0LWEyY2UtNDUyOTFlOGRmMmJmXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UY268_CR3,0,182,268_AL_.jpg",
                                        "https://www.youtube.com/watch?v=FRDRfQ_mZnA")

Kirik_Party = media.Movie("Kirik Party",
                          "2016",
                          "165 Minutes",
                          "Romantic comedy",
                          "Kannada",
                          "Rishab Shetty",
                          "Rakshit Shetty, Rashmika Mandanna, Samyuktha Hegde, Achyuth Kumar, Pramod Shetty",
                          "The progression of Karna and gang from being a bunch of mischief makers to responsible adults is the theme of Kirik Party. It is a fun filled film with lots of melodious songs.",
                          "https://in.bmscdn.com/iedb/movies/images/mobile/listing/xxlarge/kirik-party-et00050740-15-12-2016-05-23-26.jpg",
                          "https://www.youtube.com/watch?v=IfvnbER_6sQ")


Devdas = media.Movie("Devdas",
                          "2016",
                          "165 Minutes",
                          "Romantic comedy",
                          "Hindi",
                          "Rishab Shetty",
                          "Rakshit Shetty, Rashmika Mandanna, Samyuktha Hegde, Achyuth Kumar, Pramod Shetty",
                          "The progression of Karna and gang from being a bunch of mischief makers to responsible adults is the theme of Kirik Party. It is a fun filled film with lots of melodious songs.",
                          "https://in.bmscdn.com/iedb/movies/images/mobile/listing/xxlarge/kirik-party-et00050740-15-12-2016-05-23-26.jpg",
                          "https://www.youtube.com/watch?v=8tuHQWGMQwY")

DDLJ = media.Movie("Dilwale Dulhania Le Jayenge",
                          "1995",
                          "189 Minutes",
                          "Romantic",
                          "Hindi",
                          "Aditya Chopra",
                          "Shah Rukh Khan, Kajol",
                          "The Big-Hearted Will Take Away the Bride",
                          "https://cdn.pinkvilla.com/files/styles/contentpreview/public/dilwale-dulhania-le-jayenge_0_0_0_0.jpg?itok=TK42V-u0",
                          "https://www.youtube.com/watch?v=c25GKl5VNeY&vl=en")

Dil_chahta_Hai = media.Movie("Dil Chahta Hai",
                          "2001",
                          "184 Minutes",
                          "Comedy-drama",
                          "Hindi",
                          "Farhan Akhtar",
                          "Aamir Khan, Saif Ali Khan, Akshaye Khanna, Preity Zinta, Sonali Kulkarni, Dimple Kapadia",
                          "The movie is about three childhood friends, Akash Malhotra (Aamir Khan), Sameer Mulchandani (Saif Ali Khan), and Siddharth  Sinha (Akshaye Khanna). Akash does not believe in the concept of love and does not engage in relationships lasting more than two weeks",
                          "https://is2-ssl.mzstatic.com/image/thumb/Music60/v4/07/cf/de/07cfde84-5dca-010b-27e4-35ccd0f1b998/8902894114844_cover.jpg/1200x630bb.jpg",
                          "https://www.youtube.com/watch?gl=SG&v=m13b25V0B10&hl=en-GB")

Queen = media.Movie("Queen",
                          "2014",
                          "146 Minutes",
                          "Comedy",
                          "Hindi",
                          "Vikas Bahl",
                          "Kangana Ranaut, Rajkummar Rao, Lisa Haydon",
                          "The story is about an Under-confident young punjabi woman becomes bold and strong minded after some bad consequences happened in her life.",
                          "http://www.peneflix.com/wp-content/uploads/2014/03/Queen-Hindi-Movie.jpg",
                          "https://www.youtube.com/watch?v=KGC6vl3lzf0")
movies = [Urvi, That_Girl_in_Yellow_Boots, Kirik_Party, Devdas, DDLJ, Dil_chahta_Hai, Queen]
fresh_tomatoes.open_movies_page(movies)

