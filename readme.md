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



## **R5: API Endpoints**

## **R7: Third Party Services**

## **R6 / R9: Explanation of ERD and Database Relations Implementation**

## **R8: Project Models and their Relationships with each other**

## **R10: Planning and Tracking of Tasks**

## **References:**

shoyei (2019). Vinyl DJ’s - how do you organize your collection? [online] Available at: https://www.reddit.com/r/DJs/comments/bcimyk/vinyl_djs_how_do_you_organize_your_collection/ [Accessed 12 Mar. 2023].

ceeroSVK (2022). Vinyl djs: Do you catalogize BPM for your tunes somehow? [online] Available at: https://www.reddit.com/r/Beatmatch/comments/vwmhgz/vinyl_djs_do_you_catalogize_bpm_for_your_tunes/ [Accessed 12 Mar. 2023].

MariaDB (2018). ACID Compliance: What It Means and Why You Should Care. [online] MariaDB. Available at: https://mariadb.com/resources/blog/acid-compliance-what-it-means-and-why-you-should-care/.