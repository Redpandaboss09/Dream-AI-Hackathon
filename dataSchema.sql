-- Clean table from previous connection
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

-- Table which holds the following on a user:
-- id, username, and a password
CREATE TABLE user (
    -- an id col: a unique int that increments upon user addition
  id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- a username col: text which is unique, and cannot be empty
  username TEXT UNIQUE NOT NULL,
    -- a password col: must be text, and not empty
  password TEXT NOT NULL
);

-- Table which holds the following on a post:
---- a id [int]
---- an author_id [int]
---- a created [Date and time]
---- a title [str]
---- a body [str]
CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

-- Now, that the schema has been created, need to actually run these sql commans in db.py