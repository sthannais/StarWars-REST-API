DROP DATABASE IF EXISTS starwars;

CREATE DATABASE starwars;

use starwars;

CREATE TABLE
    users(
        id int NOT NULL AUTO_INCREMENT,
        firts_name CHAR(150) NOT NULL,
        last_name CHAR(50) NOT NULL,
        mail CHAR(50) NOT NULL,
        password CHAR(50) NOT NULL,
        PRIMARY KEY (id)
    );

CREATE TABLE
    characters(
        id int NOT NULL AUTO_INCREMENT,
        name CHAR(150) NOT NULL,
        height CHAR(50) NOT NULL,
        hair_color CHAR(50) NOT NULL,
        skin_color CHAR(50) NOT NULL,
        PRIMARY KEY (id)
    );

CREATE TABLE
    planets(
        id int NOT NULL AUTO_INCREMENT,
        name CHAR(150) NOT NULL,
        rotation_period CHAR(50) NOT NULL,
        climate CHAR(50) NOT NULL,
        terrain CHAR(50) NOT NULL,
        populations CHAR(50) NOT NULL,
        PRIMARY KEY (id)
    );

CREATE TABLE
    favorite_characters(
        id int NOT NULL AUTO_INCREMENT,
        characters_id INTEGER(50) NOT NULL,
        create_at CHAR(50) NOT NULL,
        PRIMARY KEY (id)
    );

CREATE TABLE
    favorite_planets(
        id int NOT NULL AUTO_INCREMENT,
        planets_id INTEGER(50) NOT NULL,
        create_at CHAR(50) NOT NULL,
        PRIMARY KEY (id)
    );