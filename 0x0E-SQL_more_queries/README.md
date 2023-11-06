# SQL - More queries

> In this project, I went even further, to learn more advanced SQL queries, which has reinforced my understanding for databases. This include:

- SQL privileges
- Create new user
- SQL table constraints
- SQL JOINS
- Calculating statistics on Joined tables
- Grouping
## Mandatory
`0-privileges.sql` - Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

<details>
  <summary> <code>1-create_user.sql</code> - Write a script that creates the MySQL server user <code>user_0d_1</code>.</summary>
  <ul>
    <li><code>user_0d_1</code> should have all privileges on your MySQL server</li>
    <li>The <code>user_0d_1</code> password should be set to <code>user_0d_1_pwd</code></li>
    <li>If the user <code>user_0d_1</code> already exists, your script should not fail</li>
  </ul>
</details>

<details>
  <summary> <code>2-create_read_user.sql</code> - Write a script that creates the database <code>hbtn_0d_2</code> and the user <code>user_0d_2</code>.</summary>
  <ul>
    <li><code>user_0d_2</code> should have only <code>SELECT</code> privilege in the database <code>hbtn_0d_2</code></li>
    <li>The <code>user_0d_2</code> password should be set to <code>user_0d_2_pwd</code></li>
    <li>If the database <code>hbtn_0d_2</code> already exists, your script should not fail</li>
    <li>If the user <code>user_0d_2</code> already exists, your script should not fail</li>
  </ul>
</details>

<details>
  <summary> <code>3-force_name.sql</code> - Write a script that creates the table <code>force_name</code> on your MySQL server.</summary>
  <ul>
    <li><code>force_name</code> description:</li>
    <ul>
      <li>id INT</li>
      <li>name VARCHAR(256) can't be null</li>
    </ul>
    <li>The database name will be passed as an argument of the mysql command</li>
    <li>If the table <code>force_name</code> already exists, your script should not fail</li>
  </ul>
</details>

<details>
  <summary> <code>4-never_empty.sql</code> - Write a script that creates the table <code>id_not_null</code> on your MySQL server.</summary>
  <ul>
    <li><code>id_not_null</code> description:</li>
    <ul>
      <li>id INT with the default value 1</li>
      <li>name VARCHAR(256)</li>
    </ul>
    <li>The database name will be passed as an argument of the mysql command</li>
    <li>If the table <code>id_not_null</code> already exists, your script should not fail</li>
  </ul>
</details>


<details>
  <summary> <code>5-unique_id.sql</code> - Write a script that creates the table <code>unique_id</code> on your MySQL server.</summary>
  <ul>
    <li><code>unique_id</code> description:</li>
    <ul>
      <li>id INT with the default value 1 and must be unique</li>
      <li>name VARCHAR(256)</li>
    </ul>
    <li>The database name will be passed as an argument of the mysql command</li>
    <li>If the table <code>unique_id</code> already exists, your script should not fail</li>
  </ul>
</details>

<details>
  <summary> <code>6-states.sql</code> - Write a script that creates the database <code>hbtn_0d_usa</code> and the table <code>states</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.</summary>
  <ul>
    <li><code>states</code> description:</li>
    <ul>
      <li>id INT unique, auto-generated, can’t be null and is a primary key</li>
      <li>name VARCHAR(256) can’t be null</li>
    </ul>
    <li>If the database <code>hbtn_0d_usa</code> already exists, your script should not fail</li>
    <li>If the table <code>states</code> already exists, your script should not fail</li>
  </ul>
</details>


<details>
  <summary> <code>7-cities.sql</code> - Write a script that creates the database <code>hbtn_0d_usa</code> and the table <code>cities</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.</summary>
  <ul>
    <li><code>cities</code> description:</li>
    <ul>
      <li>id INT unique, auto-generated, can’t be null and is a primary key</li>
      <li>state_id INT, can’t be null and must be a FOREIGN KEY that references to <code>id</code> of the <code>states</code> table</li>
      <li>name VARCHAR(256) can’t be null</li>
    </ul>
    <li>If the database <code>hbtn_0d_usa</code> already exists, your script should not fail</li>
    <li>If the table <code>cities</code> already exists, your script should not fail</li>
  </ul>
</details>

<details>
  <summary> <code>8-cities_of_california_subquery.sql</code> - Write a script that lists all the cities of California that can be found in the database <code>hbtn_0d_usa</code>.</summary>
  <ul>
    <li>The <code>states</code> table contains only one record where <code>name = California</code> (but the <code>id</code> can be different, as per the example)</li>
    <li>Results must be sorted in ascending order by <code>cities.id</code></li>
    <li>You are not allowed to use the <code>JOIN</code> keyword</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>9-cities_by_state_join.sql</code> - Write a script that lists all cities contained in the database <code>hbtn_0d_usa</code>.</summary>
  <ul>
    <li>Each record should display: <code>cities.id - cities.name - states.name</code></li>
    <li>Results must be sorted in ascending order by <code>cities.id</code></li>
    <li>You can use only one SELECT statement</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>10-genre_id_by_show.sql</code> - Write a script that lists all shows contained in <code>hbtn_0d_tvshows</code> that have at least one genre linked.</summary>
  <ul>
    <li>Each record should display: <code>tv_shows.title - tv_show_genres.genre_id</code></li>
    <li>Results must be sorted in ascending order by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code></li>
    <li>You can use only one SELECT statement</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>11-genre_id_all_shows.sql</code> - Write a script that lists all shows contained in the database <code>hbtn_0d_tvshows</code>.</summary>
  <ul>
    <li>Each record should display: <code>tv_shows.title - tv_show_genres.genre_id</code></li>
    <li>Results must be sorted in ascending order by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code></li>
    <li>If a show doesn’t have a genre, display NULL</li>
    <li>You can use only one SELECT statement</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>12-no_genre.sql</code> - Write a script that lists all shows contained in <code>hbtn_0d_tvshows</code> without a genre linked.</summary>
  <ul>
    <li>Each record should display: <code>tv_shows.title - tv_show_genres.genre_id</code></li>
    <li>Results must be sorted in ascending order by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code></li>
    <li>You can use only one SELECT statement</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>


<details>
  <summary> <code>13-count_shows_by_genre.sql</code> - Write a script that lists all genres from <code>hbtn_0d_tvshows</code> and displays the number of shows linked to each.</summary>
  <ul>
    <li>Each record should display: <code>&lt;TV Show genre&gt; - &lt;Number of shows linked to this genre&gt;</code></li>
    <li>First column must be called <code>genre</code></li>
    <li>Second column must be called <code>number_of_shows</code></li>
    <li>Don’t display a genre that doesn’t have any shows linked</li>
    <li>Results must be sorted in descending order by the number of shows linked</li>
    <li>You can use only one SELECT statement</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>14-my_genres.sql</code> - Write a script that uses the <code>hbtn_0d_tvshows</code> database to list all genres of the show Dexter.</summary>
  <ul>
    <li>The <code>tv_shows</code> table contains only one record where <code>title = Dexter</code> (but the id can be different)</li>
    <li>Each record should display: <code>tv_genres.name</code></li>
    <li>Results must be sorted in ascending order by the genre name</li>
    <li>You can use only one SELECT statement</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>15-comedy_only.sql</code> - Write a script that lists all Comedy shows in the database <code>hbtn_0d_tvshows</code>.</summary>
  <ul>
    <li>The <code>tv_genres</code> table contains only one record where <code>name = Comedy</code> (but the id can be different)</li>
    <li>Each record should display: <code>tv_shows.title</code></li>
    <li>Results must be sorted in ascending order by the show title</li>
    <li>You can use only one SELECT statement</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>16-shows_by_genre.sql</code> - Write a script that lists all shows, and all genres linked to that show, from the database <code>hbtn_0d_tvshows</code>.</summary>
  <ul>
    <li>If a show doesn’t have a genre, display NULL in the genre column</li>
    <li>Each record should display: <code>tv_shows.title - tv_genres.name</code></li>
    <li>Results must be sorted in ascending order by the show title and genre name</li>
    <li>You can use only one SELECT statement</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>


## Advanced

<details>
  <summary> <code>100-not_my_genres.sql</code> - Write a script that uses the <code>hbtn_0d_tvshows</code> database to list all genres not linked to the show Dexter.</summary>
  <ul>
    <li>The <code>tv_shows</code> table contains only one record where <code>title = Dexter</code> (but the <code>id</code> can be different)</li>
    <li>Each record should display: <code>tv_genres.name</code></li>
    <li>Results must be sorted in ascending order by the genre name</li>
    <li>You can use a maximum of two SELECT statements</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>

<details>
  <summary> <code>101-not_a_comedy.sql</code> - Write a script that lists all shows without the genre Comedy in the database <code>hbtn_0d_tvshows</code>.</summary>
  <ul>
    <li>The <code>tv_genres</code> table contains only one record where <code>name = Comedy</code> (but the <code>id</code> can be different)</li>
    <li>Each record should display: <code>tv_shows.title</code></li>
    <li>Results must be sorted in ascending order by the show title</li>
    <li>You can use a maximum of two SELECT statements</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>


<details>
  <summary> <code>102-rating_shows.sql</code> - Write a script that lists all shows from <code>hbtn_0d_tvshows_rate</code> by their rating.</summary>
  <ul>
    <li>Each record should display: <code>tv_shows.title - rating sum</code></li>
    <li>Results must be sorted in descending order by the rating</li>
    <li>You can use only one SELECT statement</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>


<details>
  <summary> <code>103-rating_genres.sql</code> - Write a script that lists all genres in the database <code>hbtn_0d_tvshows_rate</code> by their rating.</summary>
  <ul>
    <li>Each record should display: <code>tv_genres.name - rating sum</code></li>
    <li>Results must be sorted in descending order by their rating</li>
    <li>You can use only one SELECT statement</li>
    <li>The database name will be passed as an argument of the mysql command</li>
  </ul>
</details>
