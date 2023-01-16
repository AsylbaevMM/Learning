-- create
CREATE TABLE GROUPMATES (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO GROUPMATES (name, age, address) VALUES ('Ivan', 17, 'Moscow');
INSERT INTO GROUPMATES (name, age, address) VALUES ('Tagir', 25, 'Kazan');
INSERT INTO GROUPMATES (name, age, address) VALUES ('Vlad', 30, 'Moscow');
INSERT INTO GROUPMATES (name, age, address) VALUES ('Petr', 24, 'Murom');
INSERT INTO GROUPMATES (name, age, address) VALUES ('Stas', 21, 'Moscow');
INSERT INTO GROUPMATES (name, age, address) VALUES ('Rowshan', 22, 'Moscow');
INSERT INTO GROUPMATES (name, age, address) VALUES ('Rafis', 26, 'Kazan');
INSERT INTO GROUPMATES (name, age, address) VALUES ('Hanz', 20, 'Berlin');
INSERT INTO GROUPMATES (name, age, address) VALUES ('Erkin', 36, 'Ufa');
INSERT INTO GROUPMATES (name, age, address) VALUES ('Nurzhan', 41, 'Astana');
INSERT INTO GROUPMATES (name, age, address) VALUES ('John', 15, 'London');

-- fetch 
SELECT name FROM GROUPMATES WHERE address = 'Moscow' and age >= 18 and age < 30;