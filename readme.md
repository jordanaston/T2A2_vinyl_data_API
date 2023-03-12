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

## **R4: Functionalities and Benefits of an ORM**

## **R5: API Endpoints**

## **R7: Third Party Services**

## **R6 / R9: Explanation of ERD and Database Relations Implementation**

## **R8: Project Models and their Relationships with each other**

## **R10: Planning and Tracking of Tasks**

## **References:**

shoyei (2019). Vinyl DJ’s - how do you organize your collection? [online] Available at: https://www.reddit.com/r/DJs/comments/bcimyk/vinyl_djs_how_do_you_organize_your_collection/ [Accessed 12 Mar. 2023].

ceeroSVK (2022). Vinyl djs: Do you catalogize BPM for your tunes somehow? [online] Available at: https://www.reddit.com/r/Beatmatch/comments/vwmhgz/vinyl_djs_do_you_catalogize_bpm_for_your_tunes/ [Accessed 12 Mar. 2023].
