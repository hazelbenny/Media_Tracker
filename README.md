# Media_Tracker
Media Tracker
A simple Python command-line application to track books, movies, TV shows, anime, webtoons, and more that you're reading or watching.
Features

Add Items - Track any media with title, category, and status
Update Status - Mark items as watching/reading, on hold, dropped, or completed
Rate & Comment - Add ratings (1-10) and personal comments to items
Filter by Status - View items by their current status
Statistics - See your progress with detailed stats including:

Total items tracked
Breakdown by status (completed, watching, on hold, etc.)
Category distribution
Average rating


Persistent Storage - All data saved automatically to JSON file

Categories Supported

Books
Movies
TV Shows
Anime
Webtoons
Fanfics

Installation

Clone this repository:

bashgit clone https://github.com/hazelbenny/Media_Tracker.git
cd Media_Tracker

Make sure you have Python 3 installed:

bashpython --version
Usage
Run the program:
bashpython media_tracker_fixed.py
Main Menu Options

Add New Item - Add a new book, movie, show, etc.
View All Items - See your complete media list
View by Status - Filter items by status
Update Item - Change status, add ratings, or write comments
Delete Item - Remove items from your list
View Statistics - See your tracking stats
Exit - Close the program

Example Workflow

Add a new show you're watching
Update its status as you progress
When finished, mark it as completed and add a rating
View your stats to see your progress!

Data Storage
All your data is saved in media_data.json in the same folder as the program. This file is created automatically when you add your first item.
Future Improvements
Potential features to add:

Web interface using Flask
Search functionality
Tags/genres
Export to CSV
Progress tracking (e.g., episode numbers, page numbers)

Author
Created as a beginner Python learning project
License
Free to use and modify!
