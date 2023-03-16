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

<p style="text-align: center;"> Reddit screenshot 1: </p>
<p align="center"><img src="./docs/reddit-screenshot.png" width = 80%></p>
<p style="text-align: center;">(shoyei, 2019)</p>
<br>

<p style="text-align: center;"> Reddit screenshot 2: </p>
<p align="center"><img src="./docs/reddit-screenshot-2.png" width = 80%></p>
<p style="text-align: center;">(ceeroSVK, 2022)</p>
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

```
select * from "records" where id = 1;
```
The code returns data bout the record (with id = 1) stored in the database. In this example, the data will include record_id, album_title, rpm and user_id. Whereas, a tool in ORM can perform the same query in a different format. 

```
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

## **R6 / R9: Explanation of ERD and Database Relations Implementation**

## **R8: Project Models and their Relationships with each other**

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

<p style="text-align: center;"> Card Priority Badges looked like this outside the card: </p>
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
