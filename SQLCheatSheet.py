"""
SQL Cheat Sheet
This Cheat Sheet is based on the tutorial of WebDevSimplified
https://www.youtube.com/watch?v=p3qvj9hO_Bo&ab_channel=WebDevSimplified
"""

# CREATE DATABASE databaseName;  # Creating a database
# DROP DATABASE databaseName;  # Destroying a database
# USE databaseName; # Directs further commands to the database we refer to.

"""
CREATE TABLE tableName(
   test_col  DATATYPE (i.e INT, STRING, VARCHAR(LengthOfStringThatWePermit) etc),
   test_col2 DATATYPE
);
""" # Creates a table in the database that we USE.

# -Table column ATTRIBUTES-
# NOT NULL  # Prevents the cells in the COLUMN from being empty.
# AUTO_INCREMENT  # Filling each row of the column with an incrementing value automatically
# PRIMARY KEY (colName)  # Defines the column that distinguishes all rows in the TABLE.
# FOREIGN KEY(colName) REFERENCES tableName(colNameInTheReferencedTable)  # Linking two tables by a col.

# ALTER TABLE tableName  # Set a pointer to a table that we wish to modify. DO NOT USE ';', do all the modifications
# in the table first!
# ADD anotherColName DATATYPE;  # Adds another column to the table that we ALTER.

# DROP TABLE tableName  # Destroying a table.

# INSERT INTO tableName(colName1, colName2,...)
# VALUES(value1ForColName1, value1ForColName2...), (value2ForColName1, value2ForColName2...);  # Inserting data to table.

# SELECT colName FROM tableName;  # Applies further commands to the column selected from the table selected.
# SELECT * FROM tableName;  # Applies further commands to ALL column selected from the table selected.
# SELECT colName FROM tableName LIMIT integer;  # Applies further commands to the first integer rows of
# column selected from the table selected.

# SELECT colName1 AS 'newName1', colName2 AS 'newName2',... FROM tableName;  # Renames cols.
# SELECT * FROM tableName ORDER BY colName;  # Reorders the rows of the table in alphabetical order of the col referred.
# - SELECT ATTRIBUTES-
# SELECT * FROM tableName ORDER BY colName ASC;  # Reorders in an alphabetical order. (Redundant)
# SELECT * FROM tableName ORDER BY colName DESC;  # Reorders in a reversed order. (Z to A) instead of (A to Z)
# SELECT DISTINCT colName FROM tableName;  # Returns only unique rows from the table.

# SELECT * FROM tableName
# WHERE someCol1 = someValue1 OR/AND
# someCol2 = someValue2...;  # Shows all rows from a TABLE that fulfill a set of rules.

# SELECT * FROM tableName
# WHERE someCol1 BETWEEN lowBound AND HighBound;  # Returns all rows that are in a given range

# SELECT * FROM tableName
# WHERE colName LIKE '%!%';  # Shows all rows from a TABLE that fulfill a set of rules by regular expression.
# -LIKE ATTRIBUTES-
# % Wild Card: you can replace the % with ANY NUMBER of ANY characters

# UPDATE tableName
# SET colName = newValue
# WHERE someKEYCol = someValue;  # Update all table rows with new value, where this row fulfills a rule.

# DELETE FROM tableName WHERE someKEYcol = someValue;  # Deletes rows that fulfill the set of rules.

# -INNER JOIN-
# SELECT * FROM tableName1  # <- tableName1 is the LEFT table and tableName2 is the RIGHT table.
# JOIN tableName2 ON tableName1.someCol1 = tableName2.someCol2;  # Returns a new merged table that fulfills the set of rules.

# -LEFT JOIN-
# SELECT * FROM  bands
# LEFT JOIN albums ON bands.id = albums.band_id;  # Unlike INNER JOIN, LEFT JOIN includes ALL ROWS at the LEFT table,
# regardless if they are also appear at the RIGHT table.

# -RIGHT JOIN-
# SELECT * FROM  albums
# LEFT JOIN bands ON bands.id = albums.band_id;  # Unlike INNER JOIN, RIGHT JOIN includes ALL ROWS at the RIGHT table,
# regardless if they are also appear at the LEFT table.

# SELECT AVG(colName) FROM tableName;  #  Returns the average value of all entries in the col.
# SELECT MAX(colName) FROM tableName;  #  Returns the max value of all entries in the col.
# SELECT MIN(colName) FROM tableName;  #  Returns the min value of all entries in the col.
# SELECT SUM(colName) FROM tableName;  #  Returns the sum value of all entries in the col.
# SELECT COUNT(colName) FROM tableName;  #  Returns the number entries in the col.

# SELECT colName, COUNT(colName) FROM tableName GROUP BY colName;  # Returns the frequency of each value in colName in the table.


