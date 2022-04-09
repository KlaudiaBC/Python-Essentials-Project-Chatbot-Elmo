# Python Essentials: "Chatbot Elmo" Portfolio Project
## Welcome!

<p id="welcome"></p>

## This is my Portfolio 3 Project regarding the Code Institute's Diploma in Software Development (E-commerce Applications).
It is a customized ChatBot built using Python.

<p align="center">
  <img src="" alt="">
</p>

## Table of contents
- <a href="#content">Content</a>
- <a href="#uj">User journey</a>
- <a href="#fe">Features</a>
- <a href="#data">Data model</a>
- <a href="#ip">Implementation process</a>
- <a href="#tu">Technologies used</a>
- <a href="#ack">Acknowledgement</a>
- <a href="#deploy">Deployment</a>
- <a href="#test">Testing</a>

<p id="content"></p>

## Content

ChatBot Elmo is a customised chatbot which allows the Users to sign up for the activities of their choice. Thanks to the automation process and connection with a google spreadsheet, it is possible to easily adjust the list of available activities and their timeline.
Elmo is a friendly AI bot equipped with a capability of small talk, providing the information about the activities and making jokes.
This type of ChatBot could be useful for schools or any institutions providing some type of services, which require previous registration with no need for sensitive information.
Because the desired audience is relatively young, the Bot is customised as a friendly or even cheeky talker rather than a professional agent. Its vocabulary is adjusted to the level of a child, it responds with easy sentences and requires basic knowledge of English.

The name:
Elmo is a red Muppet, iconic character from the children's television show called "Sesame Street".
The details of "Happy kids" school, which Elmo represents are connected with the theme of the show.

<p align="center">***</p>

There are many different approaches of building chatbots. The choice depends mostly on role the ChatBot should play.ChatBot can provide for user a specyfic information, navigate the page, set the appointments, make bank transactions and many more.

During preparation of this project I have tried several ways to create a chatbot, including:
1. Chatbot based on the build-in python libraries, designed for chatbots (like chatterbot)
As you can see on the example below, this simple and short code can already provide User with a back-to-back conversation, but the bot is missing logic and some answers do not match the question, therefore it is a great way to start but it does require further implementations/ Example

2. Chatbot trained to search for the words converted into a binary system and stored in bag of words. Matching process is based on the percentage of repeated matches. I believe this bot could be very powerful once the intents and all vocabulary is prepared in a logical and complex way/ Example

3. Currently it is also very common to use the Chatbot Platforms, which does not require any knowledge of coding and are already stocked with a great range of vocabulary. The most popular ones include:
- <a href="https://cloud.google.com/dialogflow" target="_blank">Dialogflow by Google Clouds</a>
- <a href="https://wotnot.io/" target="_blank">Wotnot</a>
- <a href="https://chatfuel.com/" target="_blank">Chatfuel</a>
- <a href="https://mobilemonkey.com/" target="_blank">MobileMonkey</a>

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="uj"></p>

## User journey

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="fe"></p>

## Features

### Excisting features

### Future features

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="data"></p>

## Data model

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="ip"></p>

## Implementation process

### Setting the sign up process:
I created a new project on the Google Cloud Platform and called it "Elmo activities".
To access spreadsheet located in my google account I had to enable two API's:
- Google Drive: credentials allows to securely access the google files
- Google Sheets

In order to connect my API I had to generate credentials which provide proof to Google Drive that my Python project has permission to access the account.
Once the credentials were set, I received a unique email address and created a key of credentials in .json format.
I added this file into my repository and called it: "creds.json". Then I copied the client email address stored in this file, and used it in the "Give access" section in my Google Sheets file.
Then I added the creds.json into my gitignore file to make sure, this document will not be committed at any point into my repository as it does contain sensitive information which should be hidden.

### Installing libraries:
At first, I added the required libraries to my run.py file:
- google-auth - used to set up the authentication needed to access Google Cloud project
- gspread - library of code needed to access and update data in the spreadsheet

Once the API connections were set, I created an if/else statement for the main conversation (register the User for chosen activities).
Next I moved into creating a function get_activities() which requests the data from the connected spreadsheet, processes it into a string and displays it for the user.
With the data tree, my statement became very complicated therefore I decided to split some parts of the statement into independent functions and call each function when it is needed.

Next function I build is responsible for requesting data from a spreadsheet, then assigning each value from row one with a value from row two and displaying the desired date in the terminal.
Furthermore I built the function which pushes the data into a spreadsheet once the User confirms his desire to be signed on the list.

At this stage I had a customised ChatBot able to provide a full basic conversation with the User and request information needed to sign up for chosen activities as well as able to save the data in the compatible spreadsheet.

<p align="center">***</p>

### Adding a personality:
In order to make my ChatBot more human-like, I had to introduce a few new functions into my python file.
To avoid storing the large amounts of data in my main code, I created a json file, which contains predefined patterns, responses and tags.

I installed the libraries needed for further development:
- sys - library with access to some variables used or maintained by the interpreter or strongly with it connected (function used in the project: sys.exit)
- nltk -  leading platform for building Python programs to work with human language data ( Natural Language Toolkit)
- WordNetLemmatizer - lexical database for the English language, used to establish structured semantic relationships between words
- nltk.stem - Interfaces used to remove morphological affixes from words, leaving only the word stem
- json - needed to read the json file
- numpy -   library supporting processing multi-dimensional arrays and matrices
- random -  Returns a random element from the given sequence
- spacy - software library for advanced natural language processing

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="tu"></p>

## Technologies used:
- <a href="https://www.python.org/" target="_blank">Python</a> - programming language
- <a hrerf = "https://www.lucidchart.com/pages/" target="_blank>Lucidchart</a> - for the diagrams
- <a href="http://pep8online.com/" target="_blank">Python</a> - check the code for PEP8 requirements
- <a href="https://www.python.org/" target="_blank">Python</a> - programming language


<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="ack"></p>

## Acknowledgements

In this place I would like to thank everyone, who added an knowledge and value to this project:
- <a href="https://codeinstitute.net/" target="_blank">Code Institute</a> course materials and walkthroughs
- lead and support of my Code Institute Mentor - Guido Cecilio
- Code Institute Slack Community
- <a href="https://www.w3schools.com/" target="_blank">W3schools</a>
- <a href="https://stackoverflow.com/" target="_blank">Stack Overflow</a>
- <a href="https://m.youtube.com/watch?v=c_gXrw1RoKo" target="_blank">"Build your own chatbot using Python" by Great Learning</a>
- <a href="https://www.freecodecamp.org/news/how-to-build-an-end-to-end-conversational-ai-system-using-behavior-trees-658a7122e794/" target="_blank">"How to Build an End-to-End Conversational AI System using Behavior Trees" by freeCodeCamp</a>
- <a href="https://stackoverflow.com/" target="_blank">"How to Make a Chatbot in Python Step By Step" by upGrad</a>
- <a href="https://m.youtube.com/watch?v=wypVcNIH6D4&list=PLzMcBGfZo4-ndH9FoC4YWHGXG5RZekt-Q&index=1&t=30s" target="_blank">"Python ChatBot Tutorial" by Tech With Tim</a>
- <a href="https://data-flair.training/blogs/python-chatbot-project/amp/" target="_blank">"Python Chatbot Project – Learn to build your first chatbot using NLTK & Keras by DataFlair"</a>
- <a href="https://www.datacamp.com/community/tutorials/decision-tree-classification-python" target="_blank">"Decision Tree Classification in Python" by datacamp</a>
- <a href="https://www.comm100.com/blog/journey-mapping-chatbot-decision-tree-from-scratch.html/" target="_blank">"Journey Mapping for Chatbots" by Comm100</a>
- <a href="https://www.youtube.com/watch?v=6GLFcm7dGiY" target="_blank>"Build a chatbot from scratch-Ultimate Chatbot Tutorial" by Tech With Sach</a>

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="deploy"></p>

## Deployment

1. Add a new line character at the end of the text inside the input method in order to make sure that my input method will work correctly in the deployed mock terminal.
2. Create a list of requirements for the project to run (which will include all external files/libraries) in order to make sure the project will run correctly on Heroku. In order to do so, create a new txt file in your workspace and use the command: "" in the GIT. The list of requirements will update automatically. Commit the changes.
3. Log into Heroku App.
4. Create a new application via button "Create app".
5. Update the settings: config vars - (also known as environment variables", stores the confident data):
- create a config var, where the KEY is "CREDS", as a VALUE paste the entire creds copied from the creds file and click "Add"
- create a config var called "PORT" and give it a value of 8000
6. Add the buildpacks into the application: click add buildpack and choose from the list:
- python - click save button,
- node.js - click save btn.
7. Go to the deploy section: select "GitHub" and confirm on the bottom of the page that you want to connect to Github.
8. Search for your repository name and click "Connect" button.
9. Scroll down to the bottom of the page and choose one of the options: automatically or manually deploy the project. Click the button "Deploy branch" which will change the branch from the main to the master.
10. You will receive the message that the project was deployed, containing the link to the live page.

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="test"></p>

## Testing

<p align="right"><a href="#welcome">Bact to top</a></p>
