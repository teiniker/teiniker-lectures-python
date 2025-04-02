-- One to Many Relationship

CREATE TABLE users (
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE mails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    address TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


-- Insert into users
INSERT INTO users (username, password) VALUES ('homer', ')jh%6Zgur5)r');
INSERT INTO users (username, password) VALUES ('marge', 'bobk8(76G#1');
SELECT * FROM users;
1|homer|)jh%6Zgur5)r
2|marge|bobk8(76G#1

-- Insert mails for homer (assuming id=1)
INSERT INTO mails (user_id, address) VALUES (1, 'homer@springfield.com');
INSERT INTO mails (user_id, address) VALUES (1, 'homer@powerplant.com');

-- Insert mails for marge (assuming id=2)
INSERT INTO mails (user_id, address) VALUES (2, 'marge@springfield.com');
SELECT * FROM mails;
1|1|homer@springfield.com
2|1|homer@powerplant.com
3|2|marge@springfield.com


-- Get all mails with usernames
SELECT 
    users.username, 
    mails.address 
FROM 
    users
JOIN 
    mails ON users.id = mails.user_id;

homer|homer@springfield.com
homer|homer@powerplant.com
marge|marge@springfield.com


-- Get mails for user 'homer'
SELECT 
    mails.address 
FROM 
    mails
JOIN 
    users ON users.id = mails.user_id
WHERE 
    users.username = 'homer';

homer@springfield.com
homer@powerplant.com

