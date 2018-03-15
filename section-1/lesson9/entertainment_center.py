import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://goo.gl/images/tnnRAf",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

empire_strikes_back = media.Movie("Empire Strikes Back",
								  "In an attempt to convert Luke to the dark side, Darth Vader lures young Skywalker into a trap in the Cloud City",
								  "https://t1.gstatic.com/images?q=tbn:ANd9GcTtXwQAEDxEY3E9Nn78H96VZCjlV6hZWPlDd5IpVNyeuzO2vT17",
								  "https://www.youtube.com/watch?v=JNwNXF9Y6kY")


movies = [toy_story, avatar, empire_strikes_back]
fresh_tomatoes.open_movies_page(movies)