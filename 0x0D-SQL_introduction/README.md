# SQL - Introduction

>  Oh MYSQL!!! I've gained solid knowledge on:
- Writing SQL scripts to interact with a MySQL server.
- Creating and managing databases and tables.
- Querying databases using SQL commands.
- Filtering, sorting, and aggregating data.
- Modifying database records and structures.
- Understanding character sets and collations.
- Working with real-world data and applying SQL to solve various problems.

## Mandatory
<details>
  <summary> <code>0-list_databases.sql</code> - Write a script that lists all databases of your MySQL server.</summary>
</details>


<details>
  <summary> <code>1-create_database_if_missing.sql</code> - Write a script that creates the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>If the database hbtn_0c_0 already exists, your script should not fail</li>
    <li>You are not allowed to use the SELECT or SHOW statements</li>
  </ul>
</details>

<details>
  <summary> <code>2-remove_database.sql</code> - Write a script that deletes the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>If the database hbtn_0c_0 doesn’t exist, your script should not fail</li>
    <li>You are not allowed to use the SELECT or SHOW statements</li>
  </ul>
</details>


<details>
  <summary> <code>3-list_tables.sql</code> - Write a script that lists all the tables of a database in your MySQL server.</summary>
  <ul>
    <li>The database name will be passed as an argument of the mysql command (in the following example: mysql is the name of the database)</li>
</ul>
</details>

<details>
  <summary> <code>4-first_table.sql</code> - Write a script that creates a table called first_table in the current database in your MySQL server.</summary>
  <ul>
    <li>first_table description:</li>
    <ul>
      <li>id INT</li>
      <li>name VARCHAR(256)</li>
    </ul>
    <li>The database name will be passed as an argument of the mysql command</li>
    <li>If the table first_table already exists, your script should not fail</li>
    <li>You are not allowed to use the SELECT or SHOW statements</li>
  </ul>
</details>


<details>
  <summary> <code>5-full_table.sql</code> - Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>The database name will be passed as an argument of the mysql command</li>
    <li>You are not allowed to use the DESCRIBE or EXPLAIN statements</li>
  </ul>
</details>

<details>
  <summary> <code>6-list_values.sql</code> - Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>All fields should be printed</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>7-insert_values.sql</code> - Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.</summary>
  <ul>
    <li>New row:</li>
    <ul>
      <li>id = 89</li>
      <li>name = Best School</li>
    </ul>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>8-count_89.sql</code> - Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>9-full_creation.sql</code> - Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and adds multiple rows.</summary>
  <ul>
    <li>second_table description:</li>
    <ul>
      <li>id INT</li>
      <li>name VARCHAR(256)</li>
      <li>score INT</li>
    </ul>
    <li>The database name will be passed as an argument to the mysql command</li>
    <li>If the table second_table already exists, your script should not fail</li>
    <li>You are not allowed to use the SELECT and SHOW statements</li>
    <li>Your script should create these records:</li>
    <ul>
      <li>id = 1, name = “John”, score = 10</li>
      <li>id = 2, name = “Alex”, score = 3</li>
      <li>id = 3, name = “Bob”, score = 14</li>
      <li>id = 4, name = “George”, score = 8</li>
    </ul>
  </ul>
</details>

<details>
  <summary> <code>10-top_score.sql</code> - Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>Results should display both the score and the name (in this order)</li>
    <li>Records should be ordered by score (top first)</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>11-best_score.sql</code> - Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>Results should display both the score and the name (in this order)</li>
    <li>Records should be ordered by score (top first)</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>


<details>
  <summary> <code>12-no_cheating.sql</code> - Write a script that updates the score of Bob to 10 in the table second_table.</summary>
  <ul>
    <li>You are not allowed to use Bob’s id value, only the name field</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>13-change_class.sql</code> - Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>14-average.sql</code> - Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>The result column name should be average</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>15-groups.sql</code> - Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>The result should display:</li>
    <ul>
      <li>the score</li>
      <li>the number of records for this score with the label number</li>
    </ul>
    <li>The list should be sorted by the number of records (descending)</li>
    <li>The database name will be passed as an argument to the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>16-no_link.sql</code> - Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.</summary>
  <ul>
    <li>Don’t list rows without a name value</li>
    <li>Results should display the score and the name (in this order)</li>
    <li>Records should be listed by descending score</li>
    <li>The database name will be passed as an argument to the mysql command</li>
    <li>In this example, new data have been added to the table second_table.</li>
  </ul>
</details>

## Advanced
<details>
  <summary> <code>100-move_to_utf8.sql</code> - Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.</summary>
  <ul>
    <li>You need to convert all of the following to UTF8:</li>
    <ul>
      <li>Database hbtn_0c_0</li>
      <li>Table first_table</li>
      <li>Field name in first_table</li>
    </ul>
  </ul>
</details>



`101-avg_temperatures.sql` - Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

<details>
  <summary> <code>102-top_city.sql</code> - Write a script that displays the top 3 cities' temperature during July and August ordered by temperature (descending).</summary>
  <ul>
    <li>The result should display the city and the average temperature (avg_temp).</li>
  </ul>
</details>


<details>
  <summary> <code>103-max_state.sql</code> - Write a script that displays the max temperature of each state, ordered by State name.</summary>
  <ul>
    <li>The result should display the state and the maximum temperature (max_temp).</li>
  </ul>
</details>
