### POINTS: 2
### KEY: Well done and great comments! But in general, avoid space in names for routes and everywhere else when it comes to coding. Use underscores (_) where you want spacing. 

# Intro to Django routes 2 graded classwork 

Endpoints are the most important concept when it comes to backend web services. Based on the URL you route the request to the proper piece of code to service the request and return a response.

In the Django implementation, you have a default set of endpoints, but can have specific ones for the various applications that make your overall implementation.

**Exercise 1:
Reuse your ```route66``` project from in-class lesson or re-create using:

* Create a new Django project using ```django-admin startproject route66_project```
* Add an application using ```python manage.py startapp route66```
* Import ```views``` into your base ```urls.py```


Add the following endpoints and responses:

* ```gogetthegood/``` that returns ```Here you go!``` along with with something that matters to you (e.g. ```Here you go! Matching Socks!```)
* ```happyhappyjoyjoy/``` that returns the whatever that means to you (e.g. ```Ren & Stimpy FOREVER!```)

CHALLENGE:
Add an endpoint/route that accepts a string as a parameter. Parse out the string and echo back to the User with the text ```I heard you !```




