## React-Flask starter code
This project contains simple starter code I've used on various projects, including an Autograder for IU's Intro to AI course I created.

This project is a sample React.js app that is served from a Flask app. It uses GitHub OAuth for authentication and SQLAlchemy as an ORM. The GitHub OAuth service can be changed to virtually any with ease.

The front-end is a CRA React.js app, which you can find in the `client_app` directory. The back-end, found in the `server` directory, is built in Python and uses Flask w/ SQLAlchemy. 

## Running
In order to run locally, first start the React app by running `npm start` while in the `client_app` directory. Then, start the flask app by running `run.py`. Don't forget to configure settings found in `server/settings.py`. You will need to create a `.env` that contains the environment you're running the app under. See the example included for reference. The Flask app contains several comments on how it all works. I recommend starting by looking at `server/__init__.py`. 

## Publishing
The flow I use in order to publish the app on a development or production environment looks like the following: build the react-app by running `npm run build`. This puts the built files in `client_app/build`. The `site` blueprint references that directory in order to server the app to the client. Configure the environment set in the `.env` (i.e., PROD). Start the flask app however you'd like, I usually prefer [gunicorn](https://gunicorn.org/). Finally, I use a NGINX reverse-proxy that points my domain (i.e., https://example.com) to the gunicorn server (i.e., localhost:5000). 

You can do this however you'd like, refer to Flask's [deployment options](https://flask.palletsprojects.com/en/1.1.x/deploying/) documentation for more info.

## Demo Site
I currently don't have this setup anywhere, but will add a link once I do.