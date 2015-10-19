import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a crazy child whos toys come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=4KPTXpQehio" )
#print(toy_story.storyline)


avatar = media.Movie("Avatar", "Some crappy 3d movie about aliens", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)


equilibrium = media.Movie("Equilibrium","In a Fascist future where all forms of feeling are illegal, a man in charge of enforcing the law rises to overthrow the system", "http://ia.media-imdb.com/images/M/MV5BMTkzMzA1OTI3N15BMl5BanBnXkFtZTYwMzUyMDg5._V1_SY317_CR0,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=raleKODYeg0")
#print("You are now watching a bad ass Equilibrium trailer")
#equilibrium.show_trailer()

darkcity = media.Movie("Dark City","A man struggles with memories of his past, including a wife he cannot remember, in a nightmarish world with no sun and run by beings with telekinetic powers who seek the souls of humans", 
  "https://upload.wikimedia.org/wikipedia/en/9/9c/Dark_City_poster.jpg", "https://www.youtube.com/watch?v=gt9HkO-cGGo")


oldboy = media.Movie("Old Boy","After being kidnapped and imprisoned for 15 years, Oh Dae-Su is released, only to find that he must find his captor in 5 days.", "http://pointofreviewpr.com/wp-content/uploads/2014/03/OldBoy.jpg", "https://www.youtube.com/watch?v=2HkjrJ6IK5E")


ran = media.Movie("Ran", "An elderly lord abdicates to his three sons, and the two corrupt ones turn against him.", "http://static1.squarespace.com/static/5342f393e4b02233d745c04f/53e9584fe4b0a24404145ef1/53e9586be4b0162bed566c8b/1407801480663/ran+poster.png", "https://www.youtube.com/watch?v=AbbfDntoRRk")





movies = [toy_story, avatar, equilibrium, darkcity, oldboy, ran]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
