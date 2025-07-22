# Starting the code for the SQLite database
from datetime import datetime
import sqlite3

# click: some beautifying of command line terminal
import click

# current_app: points to the flask application making request
from flask import current_app
# g:  is unique for each request. Used to store data that might be accessed by multiple functions during a request. 
# The connection is stored and reused instead of creating a new connection if get_db is called a second time in the same request.
from flask import g as data_getter

# purpose: create the connection to the sqlite database
def get_db():
    # have to check if connection has been made
    if "db" not in data_getter:
        # make the connection
         data_getter.db = sqlite3.connect(
            # DATABASE: the configuration key
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.Row: returns connection in form of dicts to access data by column name
        data_getter.db.row_factory = sqlite3.Row
    
    return data_getter.db        

# purpose: close the connection
def close_db(e=None):
    # just closes the database connection if there even is a database connection made in the first place
    db = data_getter.pop('db', None)

    if not db:
        db.close()

# initialize the database using the commands from the dataSchema.sql
def init_db():
    db = get_db()

    with current_app.open_resource('dataSchema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# now to make the initialization work in the command line 
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# getting the timestamp in a human readable form
sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

# Now need to be registered to the application instance
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command) # can now register this database in the command line with the flask command
