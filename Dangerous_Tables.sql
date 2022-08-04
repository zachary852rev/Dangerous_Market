CREATE DATABASE p1;

USE p1;

CREATE TABLE Inventory (
	invID int auto_increment,
	invName varchar(255),
    invPrice int,
    invRare varchar(255),
    invDesc varchar(255),
    PRIMARY KEY (invID)
);
    
INSERT INTO Inventory (invName, invPrice, invRare, invDesc) VALUES
	("Rotten Fruit", 25, "★", "Is this merchant really selling rotten fruit?"),
    ("Questionable Cheese", 50, "★", "If you scrape the fuzzy stuff off, it should be fine."),
    ("Green Liquid", 75, "★", "I'm sure the skull on the vial is just for decoration."),
    ("Nail Bread", 100, "★", "It appears to be a slice of bread with a nail poking out the top."),
    ("Neon Jelly", 125, "★", "Meant to be eaten on toast, might cause a tingling, burning sensation."),
    ("Chunky Ooze", 150, "★★", "It's as chunky as it is opaque. Purpose: Unknown"),
    ("Hound Tooth", 175, "★★", "I hear eating teeth will make your own stronger (maybe)."),
    ("Cursed Amulet", 200, "★★", "Wear this and you too can know the joy of curses!"),
    ("Midas Glove", 225, "★★★", "Turns anything it touches into gold. ANYTHING."),
    ("Mystery Meat", 250, "★★★", "More legs means more flavor."),
    ("New Dagger", 275, "★★★", "If you ignore the bloody fingerprints it's like new!"),
    ("Supersonic Hypercube", 300, "★★★★", "With a name like that, how could it be bad?");

SELECT * FROM Inventory;

CREATE TABLE Customers (
	cusID int auto_increment,
    cusName varchar(255),
    cusDesc varchar(255),
    PRIMARY KEY (cusID)
);

INSERT INTO Customers (cusName, cusDesc) VALUES
	("Stinkus Savagetooth", "A mischevious, thieving gobin with a penchant for the fradulent. Tried to bite me once."),
    ("Vorvath Netherboy", "A young vampire with piercings rarely seen outside their room, they enjoy loud music and complaining."),
    ("Brinepaw Dustfang", "A distinguished, elder werewolf who enjoys conversation and a spot of tea by the fire."),
    ("Mongrath Snagglesnare", "A vine monster ﻿that spreads itself over giant swaths of land. Tips nicely."),
    ("Duskmoore Tanglewood", "﻿An ancient forest spirit taking the form of a small, funny-looking man with a beard.");
    
SELECT * FROM Customers;

CREATE TABLE Orders (
	saleID int auto_increment,
    cusID int,
    itemID int,
    PRIMARY KEY (saleID),
    FOREIGN KEY (cusID) REFERENCES Customers(cusID),
    FOREIGN KEY (itemID) REFERENCES Inventory(itemID)
);

INSERT INTO Orders (cusID, itemID) VALUES
	(1, 1),
    (1, 2),
    (1, 4),
    (2, 4),
    (2, 7),
    (2, 11),
    (3, 5),
    (3, 7),
    (3, 8),
    (4, 3),
    (4, 8),
    (4, 12),
    (5, 6),
    (5, 9),
    (5, 10);
    
SELECT * FROM Orders;
SELECT saleID, itemName, itemPrice, cusName FROM Orders, Inventory, Customers;