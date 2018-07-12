# Project 1

Web Programming with Python and JavaScript

## Project Summary

## Possible Future Enhancements:
-	Styling the form inputs as Bootstrap form inputs. There is an interesting package called Flask-Bootstrap that works with Flask-WTForms, but I want to become more familiar with several other packages before adding another layer of abstraction. It also isn't terribly active right now https://pythonhosted.org/Flask-Bootstrap/forms.html P2
-	Replace Weather button clickable rows. I read up on this in stackoverflow and it requires doing some jquery. I wasn’t sure how to structure that cleanly in the app, so I decided against it. P4
-	Convert Import.py into a CLI. Flask has done a nice integration with Click. I think having a click command that takes a filename would be helpful for populating the location table. I think good CLIs really help Operations to support Production apps.  http://flask.pocoo.org/docs/1.0/cli/#custom-commands P3
-	Adding Flask Logging. Flask uses the python Logger package for logging. I’d like to add that and create a Dev and Production logger configurations. It would be extremely useful for error handling. http://flask.pocoo.org/docs/1.0/logging/ P2
-	Redo the Location Profile page. The generated paragraph was good enough for the requirements, but I would ideally like to make it a better by adding a more visual dashboard of information rather than a text paragraph and change the time formats. I’m not familiar with datetime formatting, so it would be a good thing to learn. P3
- add auth to /api/<zipcode> route. Currently it isn't set up to handle basic auth. I'd like to fix that. P1
- ImportError Handling for site_config, so there is always a fallback. P1

I should put these in the issues, but I don't know if I'll ever really need to work with this project again.
