# HealthBoy


**RESTful API**


* How to put username and score into DB?

	Send POST request to

	http://www.jaejoonglee.com/healthboy/score

	with

	{
		"username": username1,
		"score": 100
	}

	json format.


* How to get a score by username?

	Send GET request to

	http://www.jaejoonglee.com/healthboy/score/<username>

	E.x) if username is jaejoong then, the url will be http://www.jaejoonglee.com/healthboy/score/jaejoong

	It will return json format like this:

	{
		"username": jaejoong,
		"score": 100
	}


