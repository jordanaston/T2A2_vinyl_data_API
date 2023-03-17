# **Vinyl Data API Web Server Documentation**

## [GitHub Repo](https://github.com/jordanaston/T2A2_vinyl_data_API)

## [Trello Board](https://trello.com/b/WqqMcM6S/t2a2-vinyl-data-api)

## [ERD](https://lucid.app/lucidchart/d8cb7ec3-cc3f-4a87-9c4e-fb1cdca5ede5/edit?beaconFlowId=7667C101FE8BEC9D&invitationId=inv_67be62fc-84b6-48ff-a61c-5fddeeebbc8a&page=0_0#)


<br>

## *Table of Contents*

<br>

## **Installation and Setup**

## **R1 / R2: Problem Identification and Justification**

The problem that this app is trying to solve lies with people who have large collections of vinyl records. Whether they are vinyl collectors who simply love to listen to records at home, or vinyl DJs who cart around many crates full of records to use in their live performances. As you can imagine, digital music is already catalogued by applications such as iTunes, Spotify or Rekordbox and users of the apps can easily create playlists and group their albums/tracks in many different ways for listening and performing. Obviously, vinyl listeners don’t have this luxury and are forced to dig through their hefty collections to find what they’re looking for and manually manage/sort their records on the shelf and in their crates to create some sort of system of grouping and searching for records with similar attributes. 

For Vinyl DJs in particular; a lot of the time, the vinyl (particularly the older vinyl) will not provide all of the information on the record sleeve that the DJ needs in order to mix the record into the set effectively. This information includes: 

1. Tempo or BPM of each track - eg: 132BPM
2. 33, 45 or 78 RPM (rotations per minute)
3. Key (eg: A Minor)

As a listener of vinyl records, you probably aren’t as fussed about the BPM and key of the tracks as the vinyl DJs are (although some might be), but having a comprehensive and easily accessible database full of the names/ artists/ tracks and especially RPM (rotations per minute) would be a very helpful tool to have to organize the data of your record collection. I would imagine that people with very large collections would not only find it difficult to locate an album in their collection but to even remember which records they have collected, to begin with.

The following images are screenshots taken from Reddit, showing the need for this type of vinyl data organization:

<p align="center"> Reddit screenshot 1: </p>
<p align="center"><img src="./docs/reddit-screenshot.png" width = 70%></p>
<p align="center">(shoyei, 2019)</p>
<br>

<p align="center"> Reddit screenshot 2: </p>
<p align="center"><img src="./docs/reddit-screenshot-2.png" width = 70%></p>
<p align="center">(ceeroSVK, 2022)</p>
<br>

This API is designed to assist **vinyl DJs** when performing live in the following ways:

- The DJ will not have to pull out vinyl from the crates and try and read the sleeve for information about the records or specific tracks on the records before using them to mix.
- Each vinyl will have an ID that the user can search via the database in order to retrieve the data on the records/ tracks before digging through the crates (which can often be in a dark space).
- The user will be able to update their record collection with full CRUD capabilities: create, read, update and delete records and tracks. 
- The database will be filled with the user's specific vinyl collection without the need to sift through any records/tracks that aren’t in their own collection. (Eg: if you were to use the internet or Rekordbox to retrieve this information).

This API is designed to assist **vinyl collectors/listeners** in the following ways:

- The user will not have to flick through their extensive collection, whether it’s a shelf in their living room full of vinyl or a box sitting in the garage. 
- The user will be able to locate any records with a specific attribute, for example: any records with an RPM of 45 and so on..
- The user can easily see a list of their entire collection if they simply wanted to browse for anything non-specific.
- The user might be thinking of the name of a track they want to listen to but can’t remember which album it’s on or even if they own the record. 

In summary, the objective of this project is to help users of any kind store and manage their vinyl record data and to create a way for anyone with large vinyl collections to search for specific attributes on their records. I imagine people running record stores would use some sort of software similar to this to track the records kept in their stores, but for the sake of the project, it's aimed at private users with large collections.

## **R3: Justification of the Database System**

There are a wide variety of database management systems that exist, each possessing unique pros and cons that cater to a diverse range of scenarios. In order to guarantee the selection of the most suitable database management system for this project, an evaluation was performed on alternative options.

PostgreSQL is a popular relational database management system that stores data in tables with predefined relationships. In contrast, a popular non-relational database management system like MongoDB stores data in collections with flexible schemas.

Benefits of PostgreSQL as a relational database management system include:

- ACID compliance, ensuring consistency and reliability of data.
- Powerful query capabilities with support for advanced data types like arrays, JSON, and XML.
- Ability to handle large volumes of data with efficient indexing and partitioning.
- Postgres allows you to create custom functions and operators, which makes it far easier to add new features and functionality to the database.

Some potential drawbacks of PostgreSQL include:

- Limited scalability due to its reliance on predefined relationships between tables.
- Higher maintenance requirements for ensuring optimal performance.

Benefits of MongoDB as a non-relational database management system include:

- Flexibility in schema design, allowing for easier adaptation to changing data requirements.
- Scalability for handling large amounts of unstructured or semi-structured data.
- Support for distributed databases for increased fault tolerance and performance.

Some potential drawbacks of MongoDB include:

- No ACID compliance, meaning that data consistency and reliability may not be guaranteed in all scenarios.
- Less powerful query capabilities compared to PostgreSQL for complex queries and analysis.

An RDMS simplifies the process of categorizing data into distinct entities and establishing relationships between them in an efficient manner. This allows for the structured organization of data and enables users to perform complex queries on the database with ease and speed.

Because of the size and nature of this application, PostgreSQL (a Relational Database Management System or RDMS) was chosen for a number of reasons which include:

ACID compliance. The term "ACID" represents four principles;  Atomicity, Consistency, Isolation, and Durability. The principles are there to ensure the reliability of transactions within a database. 

*“The presence of four properties — atomicity, consistency, isolation and durability — can ensure that a database transaction is completed in a timely manner. When databases possess these properties, they are said to be ACID-compliant.”* (MariaDB, 2018)

For example, if a user adds a new vinyl record to their collection, an ACID-compliant database will ensure that the data is stored completely and accurately, without any errors or inconsistencies. Similarly, if a user updates or deletes a record, an ACID-compliant database will ensure that the changes are processed correctly and that no data is lost or corrupted. This is crucial for the longevity of this application.

As mentioned, other database systems such as MongoDB allow for extensive scalability whereas postgres has limited scalability options due to its reliance on predefined relationships between tables. This is ok here, because the relationships have been carefully considered before the production of the application and are planned to stay the way they are.

In this particular application, the use of an RDMS provides several advantages over non-relational databases. Since the data being stored has consistent attributes, the more rigid schema of an RDMS helps ensure domain integrity. Although non-relational databases offer greater flexibility, this advantage is not critical in this case, as the overall structure of the data across all tables in the database is not likely to change significantly over time.

## **R4: Functionalities and Benefits of an ORM**

ORM, or Object-Relational Mapping, is a programming technique that establishes a connection between object-oriented programs and relational databases, typically through a bridge mechanism. In other words, an ORM can be thought of as that layer that links OOP (object-oriented programming) to the relational database. 

In OOP languages, when working with databases, there are four primary operations that are performed to manipulate data. They are: create, read, update, and delete (CRUD). These operations are typically carried out in relational databases using SQL, as per its design.

Typically, queries using SQL are made to perform these actions on the data in a database. While this is perfectly acceptable and even required, ORM and ORM tools are there to facilitate an alternate method of interacting between the database and various OOP languages such as Python for a number of reasons. 

*“With ORM tools in place to manage the data interface, developers don’t need to worry about building the perfect database schema beforehand.”* (Contributor, 2022)

To give an idea of how an ORM such as SQLAlchemy can be used to streamline queries and make them easier for a developer to implement, we’ll take a look at an example from the code of this project.

The following is an example of SQL code that “gets” data about a record (vinyl record) from the database:

```python
select * from "records" where id = 1;
```
The code returns data bout the record (with id = 1) stored in the database. In this example, the data will include record_id, album_title, rpm and user_id. Whereas, a tool in ORM can perform the same query in a different format. 

```python
Record.query.filter_by(id=id).first()
```
This allows for a few things. You can define an object to this line of code and return the “jsonified” version of this object to the browser or a tool such as Postman or Insomnia. You can build a function around this object and create a route that includes a GET method and takes the record_id as a parameter so that when searching for the specific record in the browser (or Postman/ Insomnia) you can filter out the other records in the table in order to retrieve the one you are looking for.

This way of working applies to all of the CRUD functionalities and will be implemented in all routes that are created in the controllers. To break that down, The ORM provides a high-level query language that enables developers to retrieve data from the database using object-oriented concepts. This query language typically translates to SQL statements that are executed against the database.

ORM also maps database tables to classes and objects in the programming language used. This mapping is often defined using metadata, such as annotations or configuration files. Mapping enables developers to work with the database using familiar object-oriented programming concepts.

*“ORMs create a model of the object-oriented program with a high-level of abstraction. In other words, it makes a level of logic without the underlying details of the code. Mapping describes the relationship between an object and the data without knowing how the data is structured.”* (Liang, 2021)

ORM also provides mechanisms for modelling relationships between objects, such as one-to-one, one-to-many, and many-to-many relationships. It provides mechanisms for validating objects before they are persisted to the database. This can involve checking that objects meet certain criteria, such as having valid values for required fields, and that they do not violate any constraints or business rules.

The ORM also provides tools for managing the database schema, such as creating tables, modifying columns, and generating schema migrations. This simplifies the process of making changes to the database schema and ensures that the application's data model remains in sync with the database.

**Benefits of using on ORM:**

An ORM abstracts the underlying database operations, allowing developers to work with objects and classes in the programming language of their choice rather than writing SQL queries directly. This makes it easier to write and maintain code, especially for developers who are not as familiar with SQL or the specific database being used.

*“Object-relational mapping tools help developers automate object-to-table and table-to-object data conversion while connecting a database to an application with minimum SQL knowledge. O/R mapping allows developers to overcome the challenges of writing and interpreting SQL code and instead focus on generating business logic to ensure higher productivity with lower development and maintenance costs.”* (Contributor, 2022)

Since an ORM provides a layer of abstraction between the application and the database, it makes the application platform-independent. This means that the application can be ported to a different database system with minimal changes to the code.

ORM tools can significantly reduce the amount of boilerplate code that developers have to write when working with databases, allowing them to focus on writing business logic instead. This can lead to faster development times and increased productivity.

*“Manually writing data-access code is massively tedious work taking up much of developers’ valuable time without adding much value to an application’s functionality. Leveraging an O/R mapping tool helps developers significantly reduce development time by automatically generating the code.”* (Contributor, 2022)

ORMs can help prevent SQL injection attacks, a common type of attack where malicious SQL statements are inserted into user input. By using parameterized queries, an ORM can prevent these attacks and help ensure the security of the application.

*“An effective ORM tool also ensures security for applications by shielding them from SQL injection attacks. The O/R mapping framework helps to filter the data to ensure robust safety for the developed applications.”* (Contributor, 2022)

Since an ORM provides a high-level interface to the database, it can make code more maintainable by reducing the amount of low-level SQL code that developers have to manage. This can make it easier to refactor the code as needed and make changes to the database schema.


## **R5: API Endpoints**

## **R7: Third Party Services**

The foundation of this RESTful API is built in Flask, a web application framework designed for basic routing, request handling, and response generation. The framework offers a development server and a suite of high-level components that work together to create a powerful and scalable solution. Flask is a lightweight and flexible "micro" framework that enables developers to extend its functionality using various packages, ensuring the API remains fast and adaptable to changing requirements.

The following are the third-party packages that have been used to build this project. The "requirements.txt" file contains a comprehensive list of all the dependencies and requirements needed for the project.

**SQLAlchemy**

SQLAlchemy is a popular Object-Relational Mapping (ORM) tool used in the development of Python-based applications. It allows developers to work with relational databases in a more Pythonic manner, by representing database tables as Python classes, and rows within those tables as instances of those classes. In the app, SQLAlchemy is used to manage the interactions with the database. It provides an abstraction layer between the Python code and the underlying database, allowing the focus to remain on the business logic of the application, rather than the details of how data is stored and retrieved. 

*“SQLAlchemy as an ORM means it exposes a model-based API atop database tables so that you don't need to think about the database at all most of the times but to focus on your business logic.”* (enqueuezero.com, n.d.)

By defining classes that represent the database tables, SQLAlchemy generates the SQL code needed to perform various operations, such as querying the database, inserting new records, and updating existing ones. It also provides support for database migrations, which can help to ensure the database schema stays in sync with changes made to the application over time.

**Psycopg2**

Psycopg2 is a PostgreSQL database adapter for Python that allows developers to interact with PostgreSQL databases using Python code. It provides a set of Python modules and methods that allow applications to connect to a PostgreSQL database, execute SQL queries, and retrieve results. 

In the app, Psycopg2 is used to connect to the PostgreSQL database and perform CRUD (Create, Read, Update, Delete) operations on the database tables. It allows the Python code to interact with the database using SQL commands, such as SELECT, INSERT, UPDATE, and DELETE. 

By using Psycopg2, the app can easily communicate with the PostgreSQL database and retrieve data from the various tables, which are Users, Collections, Artists, Records, and Tracks. 

**Flask-Marshmallow**

Flask-Marshmallow is a Flask extension that provides integration between Flask and Marshmallow, a popular Python library for object serialization and deserialization. It simplifies the process of converting Python objects to and from JSON data, which is a common format used in RESTful APIs. In the app, Flask-Marshmallow is used to serialize and deserialize data when communicating with the API endpoints. 

*“Flask-Marshmallow is a thin integration layer for Flask (a Python web framework) and marshmallow (an object serialization/deserialization library) that adds additional features to marshmallow”* (flask-marshmallow.readthedocs.io, n.d.)

It allows the Python code to easily convert the data from the database tables, into JSON format that can be returned by the API endpoints. By defining schema classes that map to the database tables, Flask-Marshmallow generates the JSON data that is returned by the API endpoints. This allows the API to provide a consistent and well-defined data format that can be consumed by other applications and services.

**Python-Dotenv**

Python-Dotenv is a Python library that allows developers to load environment variables from a .env file in the project directory. This library simplifies the process of managing environment variables by allowing developers to keep sensitive information separate from their code, and to easily switch between different environment configurations. 

*“When a Python process is created, the available environment variables populate the os.environ object which acts like a Python dictionary.”* (www.doppler.com, n.d.)

Python-Dotenv is used in conjunction with Flask's config object, which provides a way to manage application-wide configuration variables. The config object can be used to set default values for configuration variables, and to load values from environment variables or configuration files such as .env.

**Flask-Bcrypt**

Flask-Bcrypt is a package that provides password hashing and verification functionality for Flask applications. It is used to securely store and manage user passwords in the app's database. In the app, Flask-Bcrypt is used to encrypt and store user passwords when they create an account or update their password. When a user logs in, their password is verified by comparing the stored encrypted password with the hashed version of the password they entered during login.

*“Password hashing is the process of turning a password into alphanumeric letters using specific algorithms. Some popular algorithms for password hashing include bcrypt and SHA.”* (Patel, 2022)

Using Flask-Bcrypt to hash and verify passwords adds an extra layer of security to the app, making it more difficult for attackers to gain access to user accounts even if they manage to obtain the password hashes from the database.


**Flask-JWT-Extended**

Flask-JWT-Extended is a package that provides JSON Web Token (JWT) functionality for Flask applications. It is used to provide authentication and access control to the API endpoints. In the app, Flask-JWT-Extended is used to generate JWTs when users are successfully authenticated and include the token in subsequent requests to protected endpoints. 

*“To access a jwt_required protected view you need to send in the JWT with each request. By default, this is done with an authorization header.”* (flask-jwt-extended.readthedocs.io, n.d.)

The JWT contains encoded information about the user's identity and permissions. When a user makes a request to a protected endpoint, Flask-JWT-Extended checks the JWT for validity and authenticity. If the token is valid and has not expired, the user is granted access to the endpoint. Flask-JWT-Extended can also be used to control access to specific endpoints based on the user's permissions.


## **R6 / R9: Explanation of ERD and Database Relations Implementation**

Presented below is an Entity Relationship Diagram (ERD) that illustrates the connections between the tables within the relational database implemented in this project. Each table is depicted as an entity in the diagram, with the attributes or fields of the database table being represented as corresponding elements in the ERD. The primary key, which serves as the unique identifier for each table, is included in every entity. The third column of each entity in the ERD shows the attribute's datatype and indicates if it is mandatory for the database table entry (NOT NULL). Additionally, foreign keys are present in some tables, signifying a connection between two tables. This relationship is also shown through the crow's foot notation utilized in the diagram.

<p align="center"> ERD </p>
<p align="center"><img src="./docs/ERD.png" width = 100%></p>

## **Entities**

**User**

The “user” table retains details regarding users who intend to store information about their vinyl record collection in the database. The attributes contained in the table are user_id (allowing them to access the system) user_name (a self-selected username for the application), email (utilized for user identification), password (used for authentication purposes), and admin, which stores a boolean value that authenticates and authorizes users. The relationship between the user and record table is many to many, as many users can own many records and many records can belong to many users. Because of this a new entity titled “collection” was created to represent this relationship between user and records.

**Collection**

Since the many to many relationship between user and record was handled by the creation of this table, we now have a 1 to many relationship between user and collection. The attributes included in this entity are collection_id, user_id and record_id. With the former being the primary key and the others, foreign keys. The purpose of this table, is to create a unique identifier (PK) that points to each collection in the database (relationship between user and record). It’s not a table that needs to be accessed by regular users, but rather a “background” table doing the job of handling a many to many relationship in the database. 

**Record / Artist** 

The record table acts as a kind of centre point to the application. Because it is linked to users through collections and has a dependent table (tracks). The PK in this table is record_id, which is a unique identifier for every album (record) entered into the database. The attributes of this table include album_title (name of the album), RPM (rotations per minute eg: 30 or 45) and artist_id (FK), which is the PK from the artist table. 

Originally, the artist_id was included as an attribute in this table but was later moved out to create a table of its own. This was done to help normalise the database as you might find the same artist many times in this table. We also now have a 1 to many relationship between the artist and record tables because 1 artist can have many records, but each record belongs to a single artist. The artist table was kept simple and only includes the artist_id and artist_name as it was moved out for the purpose of normalization. Since we have a 1 to many relationship here, we can think of the record table as being dependent on the artist table. In order for a record to exist, there must be an artist.

**Track**

The track table lies at the end of the chain so to speak. Because no tables depend on the track table, if a track was to be deleted from the database, no other data should be affected. The track table includes a track_id (identified each unique track), track_title (name of the track), BPM (beats per minute or tempo eg: 120bpm), key (eg: A Minor), and record_id, which represents the 1 to many relationship between the record and track tables. This relationship is one to many because 1 record can have many tracks but each track belongs to only 1 record. 

As you can see from the ERD, not every attribute was made nullable. The ones that are nullable, are attributes that without an entry, would not effect the relationship between the entities in the database, helping normalize and strengthen the database structure. 

**Relationships again:**

- Many to Many between the user and record tables: creating a collection table.
- 1 to Many between the artist and record tables.
- 1 to Many between the record and track tables.



## **R8: Project Models and their Relationships with each other**

The models in this project are implemented using SQLAlchemy ORM for handling database operations. There are five main classes in the code representing the tables in the database: User, Collection, Record, Artist, and Track. Each class inherits from db.Model, which is a base class for all models in SQLAlchemy.

**User class: Represents a user in the system**

- **__ tablename __:** Sets the name of the table in the database to "users".
id: Primary key column with auto-incrementing integer values.
- **user_name, email, password, and admin:** Additional attributes with various constraints (e.g., nullable=False means the attribute must have a value, and unique=True means the attribute value must be unique across all users).
- **collections:** One-to-many relationship between User and Collection. When a user is deleted, all associated collections will also be deleted due to the "cascade" parameter.

**Collection class: Represents a collection of records owned by a user**

- **__ tablename __:** Sets the table name to "collections".
- **id:** Primary key column.
- **user_id:** Foreign key column referencing the 'users.id' column, establishing a relationship with the User table.
- **record_id:** Foreign key column referencing the 'records.id' column, establishing a relationship with the Record table.

**Record class: Represents a vinyl record (album)**

- **__ tablename __:** Sets the table name to "records".
- **id:** Primary key column.
- **album_title, rpm, and artist_id:** Additional attributes, with 'artist_id' being a foreign key referencing the 'artists.id' column.
- **collections:** One-to-many relationship with Collection. When a record is deleted, all associated collections will also be deleted due to the "cascade" parameter.
- **tracks:** One-to-many relationship with Track. When a record is deleted, all associated tracks will also be deleted due to the "cascade" parameter.

**Artist class: Represents a music artist**

- **__ tablename __:** Sets the table name to "artists".
- **id:** Primary key column.
- **artist_name:** Additional attribute.
- **records:** One-to-many relationship with Record. When an artist is deleted, all associated records will also be deleted due to the "cascade" parameter.

**Track class: Represents a track in a record (album)**

- **__ tablename __:** Sets the table name to "tracks".
- **id:** Primary key column.
- **track_title, bpm, key, and record_id:** Additional attributes, with 'record_id' being a foreign key referencing the 'records.id' column.

**Associations between the models:**

- A User can have multiple Collections.
- A Collection is associated with one User and one Record.
- An Artist can have multiple Records.
- A Record is associated with one Artist and can have multiple Tracks and Collections.
- A Track is associated with one Record.

The code uses SQLAlchemy's relationship() function to establish these associations. The backref parameter creates a reverse relationship, making it easy to navigate from one side of the relationship to the other (e.g. from Record to Artist, and vice versa). The cascade parameter ensures that when a parent record is deleted, all related child records are deleted as well.

To elborate further on the code:

**User and Collection:**

```python
collections = db.relationship(
    "Collection",
    backref="user",
    cascade="all, delete"
)
```

This line establishes that one user can have multiple collections. The backref parameter creates a reverse relationship, allowing you to access the User model from the Collection model using the "user" attribute.

In the Collection class, there are foreign key columns for both user_id and record_id:

```python
user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
record_id = db.Column(db.Integer, db.ForeignKey('records.id'), nullable=False)
These columns reference the primary keys of the User and Record tables, respectively, to create the associations between these models.
```

**Artist and Record:**

```python
records = db.relationship(
    "Record",
    backref="artist",
    cascade="all, delete"
)
```

This line establishes that one artist can have multiple records. The backref parameter creates a reverse relationship, allowing you to access the Artist model from the Record model using the "artist" attribute.

In the Record class, the artist_id column is a foreign key referencing the 'artists.id' column:

```python
artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
This column creates the association between the Record and Artist models.
```

**Record and Track:**

```python
tracks = db.relationship(
    "Track",
    backref="record",
    cascade="all, delete"
)
```

This line establishes that one record can have multiple tracks. The backref parameter creates a reverse relationship, allowing you to access the Record model from the Track model using the "record" attribute.

In the Track class, the record_id column is a foreign key referencing the 'records.id' column:

```python
record_id = db.Column(db.Integer, db.ForeignKey('records.id'), nullable=False)
```

This column creates the association between the Track and Record models.

**Collection and Record:**

As mentioned earlier, the Collection class has a foreign key column record_id, which references the primary key of the Record table:

```python
record_id = db.Column(db.Integer, db.ForeignKey('records.id'), nullable=False)
```
```python
collections = db.relationship(
    "Collection",
    backref="record",
    cascade="all, delete"
)
```

This line establishes that one record can be part of multiple collections. The backref parameter creates a reverse relationship, allowing you to access the Record model from the Collection model using the "record" attribute.



## **R10: Planning and Tracking of Tasks**

**Trello Board: T2A2 - Vinyl Data API**

Trello was chosen as the tool to plan and track tasks for this project. This allowed for small portions of work to be defined as checklists inside cards that represent the larger concept. 

The Trello workspace was separated into 3 main parts:

**To Do:** An organized schedule of tasks that have been arranged in order of importance and are prepared for implementation.

**Doing:** Tasks that are currently being worked on. This is the section that was revisited the most, especially to view the questions/reminders card. This card was extremely useful as a one-stop place for any ideas that popped up during production. Questions that needed answers, reminders or instructions on how to do something later.

**Done:** When cards were completed, they would be sent to this list.

Each card was given a cover with a certain colour to represent the kind of work that needed to be done. This was used as an eye-catcher and helped to quickly identify what “type” of work was left to do. Red represented rubric questions, yellow represented the core modules of the code in terms of MVC, purple was for authorization and authentication, dark green was for questions/ reminders and blue was generally for anything to do with the readme.md file. This exact pattern had exceptions, eg: when the Trello board was initially created, there were some blue and green cards made for tasks to do with starting the project and working on the ERD. Because they were done so soon, they were left the way they were. Colour coding was also added as labels inside the cards.

When a card is opened there are certain attributes that helped define how urgent or important a task was. A power-up was installed called Card Priority Badge. The power-up meant that you could assign each card a level of importance (essentially from 1-4) which included an icon that would be shown on the outside of the card so they could be easily seen when scanning through the Trello board.

<p align="center"> Card Priority Badges looked like this inside the card: </p>
<p align="center"><img src="./docs/card-priority-screenshot.png" width = 60%></p>

<p align="center"> Card Priority Badges looked like this outside the card: </p>
<p align="center"><img src="./docs/priority-badge-screenshot.png" width = 40%></p>

A due date reminder was also set to each card that was designed to that 1 day before each card was due, I would receive a notification via email to prompt me to view the card and read over the checklist. As the tasks were completed, the checklist was gradually ticked off until the card was complete.

Below are screenshots capturing the gradual completion of tasks within the cards:

<p align="center"><img src="./docs/trello-1.png" width = 80%></p>
<p align="center"><img src="./docs/trello-2.png" width = 80%></p>
<p align="center"><img src="./docs/trello-3.png" width = 80%></p>
<p align="center"><img src="./docs/trello-4.png" width = 80%></p>
<p align="center"><img src="./docs/trello-5.png" width = 80%></p>
<p align="center"><img src="./docs/trello-6.png" width = 80%></p>
<p align="center"><img src="./docs/trello-7.png" width = 80%></p>
<p align="center"><img src="./docs/trello-8.png" width = 80%></p>
<p align="center"><img src="./docs/trello-9.png" width = 80%></p>
<p align="center"><img src="./docs/trello-10.png" width = 80%></p>
<p align="center"><img src="./docs/trello-11.png" width = 80%></p>
<p align="center"><img src="./docs/trello-12.png" width = 80%></p>
<p align="center"><img src="./docs/trello-13.png" width = 80%></p>

## **References:**

shoyei (2019). Vinyl DJ’s - how do you organize your collection? [online] Available at: https://www.reddit.com/r/DJs/comments/bcimyk/vinyl_djs_how_do_you_organize_your_collection/ [Accessed 12 Mar. 2023].

ceeroSVK (2022). Vinyl djs: Do you catalogize BPM for your tunes somehow? [online] Available at: https://www.reddit.com/r/Beatmatch/comments/vwmhgz/vinyl_djs_do_you_catalogize_bpm_for_your_tunes/ [Accessed 12 Mar. 2023].

MariaDB (2018). ACID Compliance: What It Means and Why You Should Care. [online] MariaDB. Available at: https://mariadb.com/resources/blog/acid-compliance-what-it-means-and-why-you-should-care/.

Contributor, S. (2022). Why Do We Need Object-Relational Mapping? [online] Software Reviews, Opinions, and Tips - DNSstuff. Available at: https://www.dnsstuff.com/why-do-we-need-object-relational-mapping [Accessed 12 Mar. 2023].

Liang, M. (2021). Understanding Object-Relational Mapping: Pros, Cons, and Types. [online] AltexSoft. Available at: https://www.altexsoft.com/blog/object-relational-mapping/.

enqueuezero.com. (n.d.). The Architecture of SQLAlchemy | Enqueue Zero. [online] Available at: https://enqueuezero.com/architecture/sqlalchemy.html#overview [Accessed 16 Mar. 2023].

flask-marshmallow.readthedocs.io. (n.d.). Flask-Marshmallow: Flask + marshmallow for beautiful APIs — Flask-Marshmallow 0.14.0 documentation. [online] Available at: https://flask-marshmallow.readthedocs.io/en/latest/.

www.doppler.com. (n.d.). Using Environment Variables in Python for App Configuration and Secrets. [online] Available at: https://www.doppler.com/blog/environment-variables-in-python [Accessed 16 Mar. 2023].

Patel, H. (2022). Password hashing in Node.js with bcrypt. [online] LogRocket Blog. Available at: https://blog.logrocket.com/password-hashing-node-js-bcrypt/#:~:text=Bcrypt%20is%20a%20library%20to [Accessed 16 Mar. 2023].

flask-jwt-extended.readthedocs.io. (n.d.). Basic Usage — flask-jwt-extended 4.4.4 documentation. [online] Available at: https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage/.
