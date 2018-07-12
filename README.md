# Project 1

Web Programming with Python and JavaScript

## Project Summary
For this project, I relied a lot on two major resources. I reused most of my the html and css from https://github.com/manvillej/project0 and I also heavily relied on Miguel Grinberg's FlaskMega tutorial https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world. I really like Grinberg's tutorial because it is highly digestable, isn't a toy example, and attempts to be scalable and well structured from the beginning. I was able to adapt many parts of it to my project and fill in the gaps from documentation, stack overflow, and reddit (r/python and r/flask)

### Top Level Directory:

/app/ - Most of the application

/migrations/ - db migration files

.gitignore

README.md

/config.py - holds the CONFIG object and site_config namedtuple for branding

/import.py - import py for loading zips.csv into location table

/application.py - application

/requirements.txt - I use my laptop and Anaconda. so this file is anaconda's output

/zips.csv


### /app/ Directory
./templates/ - where html files are stored

./static/ - where my scss and css files are stored

./\_\_init\_\_.py - defines the base importable stuff, app, some login properties, some db stuff

./routes.py - defines the routes in the application. It also has some utility functions that routes use. This isn't the most sustainable practice and in the future, I think I would have another directory with a file for each route and its utility functions that gets imported into routes.py

./forms.py - WTForms are defined here

./models.py - DB models are defined here

./siteConfig.py - SiteConfig named tuple is defined here for import.


## Possible Future Enhancements:
-	Styling the form inputs as Bootstrap form inputs. There is an interesting package called Flask-Bootstrap that works with Flask-WTForms, but I want to become more familiar with several other packages before adding another layer of abstraction. It also isn't terribly active right now https://pythonhosted.org/Flask-Bootstrap/forms.html P2
-	Replace Weather button clickable rows. I read up on this in stackoverflow and it requires doing some jquery. I wasn’t sure how to structure that cleanly in the app, so I decided against it. P4
-	Convert Import.py into a CLI. Flask has done a nice integration with Click. I think having a click command that takes a filename would be helpful for populating the location table. I think good CLIs really help Operations to support Production apps.  http://flask.pocoo.org/docs/1.0/cli/#custom-commands P3
-	Adding Flask Logging. Flask uses the python Logger package for logging. I’d like to add that and create a Dev and Production logger configurations. It would be extremely useful for error handling. http://flask.pocoo.org/docs/1.0/logging/ P2
-	Redo the Location Profile page. The generated paragraph was good enough for the requirements, but I would ideally like to make it a better by adding a more visual dashboard of information rather than a text paragraph and change the time formats. I’m not familiar with datetime formatting, so it would be a good thing to learn. P3
- add auth to /api/<zipcode> route. Currently it isn't set up to handle basic auth. I'd like to fix that. P1
- ImportError Handling for site_config, so there is always a fallback. P1
- Rate limiting APIs using a custom decorator. http://exploreflask.com/en/latest/views.html#custom-decorators
- Move Config.py into package directory, add documentation for environment variables to handle configurations

I should put these in the issues, but I don't know if I'll ever really need to work with this project again.


## Lessons Learned:
### Creating New Route-Form-Model-Page process
This needs more thought, but I found that this process seemed to work really well for adding a new form page like the search page.
My own experience has led me to try really hard to only change or add one supporting part at a time. I feel like this fits really well with the TDD.

1. create the route with placeholder template and get only. no dynamic jinja
2. replace template with basic form with placeholder data
3. create model, test with flask shell
4. create form, integrate into template/route, flash results
5. add logic for each case beyond the standard GET vs POST separation (ex. POST success, Post fail, etc.) flash case
6. add database interaction (data retreival/creation (POST)) to route, flash results
7. add dynamic jinja for each case
8. add security (Login for now)
9. add custom styling

In this process, step 1 makes sure the route is actually retrievable. Step 2 makes sure the form is renderable. step 3 makes sure the database interactions work correctly. Step 4 makes sure the form is receiving data correctly. Step 5 makes sure the route can handle each situation its meant to. Step 6 makes sure the database interactions in the route are succesful. Step 7 makes sure the customer receives the data in a meaningful manner. Step 8 makes sure the system is secure. Step 9 makes sure it is all pretty.

#### Thoughts
I feel walking through this process (and trying to vocalize it) really helped me understand what I need to consider when creating an application. It also made me thing how I would scale the development model for this. I would ideally like to clean up the template directory to separate top level html, form html/custom html, and base html. In an operational sense, I would separate the API design into its own application ontop of the same database and use something like Nginx to handle requests for the two. With the Creating New Route... Process, and segmenting the app into specific purposes (routes.py, models.py, /templates/, etc.) Multiple developers could work side by side and merging the work together would lead to fewer collisions unless they work working on the same route or depending on another's work. 

### Lessons from Grinberg:
I based my app file structure off of his because I could easily turn it into an installable package by adding a setup.py. I used Flask-Migrate from his examples to help with database creation and modification. I made several mistakes when creating and modifying the database and it was extremely helpful in rolling back those mistakes. I also liked using the 'flask shell' feature to test the data model layer. 

### Final Thoughts
I really really really liked this project. It was my second time trying to build a flask app (I had been working on the FlaskMega tutorial before, but it was mostly wrote copy-pasta and trying to understand it) and I feel that I really do understand a lot of how it should be put together. There's obviously a ton more to learn in any of these spaces; I think I will open a new github project for tracking these areas I would like to learn more about as we go through the courses. We are moving too fast to really dig much deeper than the project immediately in front of us. I can maybe compile some external resources into it and, at the end of the course, I can share it as a __Deeper Down The Rabbit Hole__ resource.  

While I did enjoy this project, I feel there is a lot more I could have done with just the tools we have been taught and the possibile enhancements I could try. It left me satisfied that I met the requirements, but not satisified that I did everything I could up to my current abilities. 
