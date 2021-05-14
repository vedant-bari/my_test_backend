What technologies would you use to build out this platform? Please tell us the
languages, databases, tools / servers you would use to build out the above platform.

-->
Python's Django rest framework for building Api's, Postgres as a database , gunicorn and docker container
for scaling , nginx for serving static files and Angular as frontend, websocket to send notifications to other user about tweet.

////
Write the schema of your database that is going to store the data. We want to see this in
detail to see where the all the different information will be stored

firstly, A User model to store all user's basic information (Inherited abstractUser)
provision to make a user admin/superuser 

Tweet app
Model for Userfollowers where ine user can have multiple followers
Model for tweet time of creation,text and the user who created id .


////
Main Pages- 
Login page - http://localhost:8000/login
registration - http://localhost:8000/register
dashboard - http://localhost:8000/profile



///For detail front-end code visit https://github.com/vedant-bari/twiiter_app/tree/master
