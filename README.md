[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10878172)
# final-project

The Diamondback website: dbknews.com

## Introduction

My final project takes The Diamondback's stylebook pdf and turns it into a searchable website. It includes a home page with all the style entries as well as three separate pages that include entries with specific tags — IMPORTANT, AP DEVIATION and SPORTS.

## Workable Data

I started by taking the stylebook pdf file and turning it into a useful dataset to populate my website. I first tried to do this programatically but because the pdf was formatted with two columns, I ended up manually building my dataset. I created a csv file that contains four columns: id, name, description and tags.

## Displaying Entries

Once I had a clean csv file, I started working on how to create a home page that displayed every style entry. I based this code off of our second news app and how we displayed every zip code. At first, I was stuck on how to modify the code to include not only the entry's name but also the tags and description. I solved it by removing the ```Stylebook.name``` selector from my ```all_tips``` variable in my index function. I was also getting a peewee error that said I did not have an id column when I did, so I solved it by adding a line to remove and insert the ```Stylebook.db``` every time I ran the ```setup.sh``` file. Then to have my app display each entry in one column instead of three, I removed sections from the ```index.html``` file. I also added some CSS to change the background color of the body of my ```index.html``` page and created boxes of equal width in a slightly darker color to go around each individual style entry. 

## Full Text Search

Then, I started working on implementing full text search, modeled after what we did in class. I copied the relevant code into the ```app.py``` and ```index.html``` files but kept getting an error that my ```StylebookIndex(FTSModel)``` didn't exist. I realized I skipped the step that created the index, so I added in another .py file to do that. I then added code into the ```index.html``` file that would display my search results and get rid of the irrelevant entries using conditional statements. I also added a conditional statement to the credits section in the ```index.html``` file that would show the created by section at the bottom if there were no searches or search results and display both the dear reader intro and the created by section if there were search results, because the dear reader section disappears from the top if search results are returned. 

## Scroll to Top Button

Next, I worked on creating "scroll to top" and "back to bottom" buttons. I asked ChatGPT to help me write code for this button, and it wasn't able to figure out the Javascript to have both buttons appear at once. So, I kept just the "back to top" button. 

## Tags Pages

Next, I worked on creating a dropdown button in my navigation bar that would allow a user to go to another page with entries with specific tags. I used previous classwork and Bootstrap documentation to create a navbar and dropdown button, but I couldn't figure out how to get the dropdown menu to actually open. ChatGPT kept telling me I needed to impplement different versions of Bootstrap CSS, a Bootstrap Javascript file and the Popper.js library. When none of this worked, I decided to create three separate buttons that would take you to different pages. To have the buttons take you to a new page that only had entries with the correct tags, ChatGPT told me I needed to create two functions for each page in my ```app.py``` file. When the button is clicked, one function would trigger a request to the correct route to render the right page. The second function would actually render the page. I created these two functions for each page. 

## Navigaton Bar Styling

Next, I tried various Bootstrap and ChatGPT methods to make my navigation bar look nice. I decided to create three columns within the bar to evenly space out The Diamondback logo and website name, the buttons and the search bar. 

## Testing Search Bars

I then tested my search bar in each new page and realized it was still searching through all the entries. ChatGPT helped me solve this by suggesting I add a filter into the results variable of the search function in each of my functions that would only look at entries that have the correct tags. This added code was ```where(StylebookIndex.match(search_term) & (Stylebook.tags.contains("IMPORTANT")))```. 

## The Diamondback Website Button

Finally, I added a button that links to The Diamondback's website and cleaned up some of the HTML and CSS to make things prettier on each page. 

## Deployment and Project Longevity

This project is currently deployed in Github Codespaces but when the class is over, I'd like to somehow have it deploy on Github Pages. Users are able to access all of the underlying data. In the future, I would like to add code that would allow users to update style entries right in the web page with a "date updated" line, but I didn't get to that for this project. Therefore, this website will be outdated when The Diamondback revises its stylebook or when certain entries become outdated over time. The Diamondback typically revises its stylebook every few years; this current revision was published five years after its previous iteration. 
