# Movie Watchlist

<p>A full stack flask application that allows a user to track directors and movies<p>

## Contents
<hr>
<p>Technologies</p>
<p>Brief</p> 
<p>Installation</p> 
<br>

## Technologies
<hr>
<p>These are the main technologies we used to contruct the project.</P>
<br>
<p>Python</p>
<p>Flask</p>
<p>Jinja</p>
<p>HTML5</p>
<p>CSS3</p>
<br>

## Brief
<hr>
<br>
After 4 weeks at CodeClan we undertook our first project. Working independently we were to create a flask application that allows a user to perform simple CRUD actions. I decided to create a movie watchlist, following this brief.
<br><br>

### MVP
<br>
<p>- [x] Adapted from the Country Bucket List. A user should be able to...</p>
<p>- [x] The app should allow the  user to track directors and movies they want to watch and those they have watched.</p>
<p>- [x] The user should be able to create and edit directors.</p>
<p>- [x] Each director should have one or more movies to watch.</p>
<p>- [x] The user should be able to create and delete entries for movies.</p>
<p>- [x] The app should allow the user to mark movies as watched or still to see.</p><br>

### Extensions:
<p>Have separate pages for all movies and movies on the watchlist.</p>
<p>Have individual pages for directors and movies</p>
<p>Have user rating option.</p>
<p>The user can write reviews for movies.</p>
<br>

I may or may not develop this app any further. Purely to keep a record of my progress during my coding journey. This is the result of 4 weeks with CodeClan.
<br><br>

## Installation
<hr>
<br>

<p>You'll need python3, postgreSQL and flask installed to run this.<p>
<br>

<p>To build the database structure and seed with starter data run the following in your CLI<p>

```
createdb movies
psql -d movies -f db/movies.sql
python3 console.py
```
Then to run the app:
```
flask run
```

<br>
<p>Then visit http://127.0.0.1:4999/ to view the app.</p>
<br>
<p>Some directors and movies have been added. These can be deleted and more added.</p>
