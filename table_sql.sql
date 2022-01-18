create table if not exists places (
city_id serial PRIMARY KEY,
city VARCHAR ( 50 ) NOT NULL,
region VARCHAR (200) NOT NULL,
population int,
country VARCHAR ( 50 ) not null
);