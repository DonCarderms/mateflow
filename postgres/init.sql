CREATE TABLE User (
  id SERIAL PRIMARY KEY,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(20) NOT NULL,
  email VARCHAR(50) NOT NULL,
  active BOOLEAN DEFAULT FALSE
);

CREATE TABLE Material (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES User(id),
  name VARCHAR(20) NOT NULL,
  description VARCHAR(200) NOT NULL,
  image VARCHAR(200) NOT NULL,
  active BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE Comment (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES User(id),
  material_id INTEGER REFERENCES Material(id),
  comment VARCHAR(200) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO User (username, password, email, active)
  VALUES ('john', 'password1', 'john@example.com', true),
         ('jane', 'password2', 'jane@example.com', true);

INSERT INTO Material (user_id, name, description, image, active)
  VALUES (1, 'Material 1', 'Description of material 1', 'image1.jpg', true),
         (1, 'Material 2', 'Description of material 2', 'image2.jpg', true),
         (2, 'Material 3', 'Description of material 3', 'image3.jpg', false);

INSERT INTO Comment (user_id, material_id, comment)
  VALUES (1, 1, 'This material is great!'),
         (2, 1, 'I disagree, it could be better.'),
         (1, 2, 'I like this one even more!');

