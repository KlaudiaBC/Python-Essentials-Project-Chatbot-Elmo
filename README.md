# Python Essentials: "Chatbot Elmo" Portfolio Project
## Welcome!

<p id="welcome"></p>

## This is my Portfolio 3 Project regarding the Code Institute's Diploma in Software Development (E-commerce Applications).
It is a customized ChatBot built in Python and deployed in the Code Institute mock terminal on Heroku.

<p align="center">
  <img src="https://github.com/KlaudiaBC/Python-Essentials-Project-Chatbot-Elmo/blob/main/img/title.png?raw=true" alt="intro-page">
</p>

## Table of contents
- <a href="#content">Content</a>
- <a href="#uj">User stories</a>
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
As you can see on the example below, this simple and short code can already provide User with a back-to-back conversation, but the bot is missing logic and some answers do not match the question, therefore it is a great way to start but it does require further implementations. See example of my project in Google Colab:

<p align="center">
  <img src="https://github.com/KlaudiaBC/Python-Essentials-Project-Chatbot-Elmo/blob/main/img/simple_chatbot.png?raw=true" alt="chatterbot">
</p>

2. Chatbot trained to search for the words converted into a binary system and stored in bag of words. Matching process is based on the percentage of repeated matches. I believe this bot could be very powerful once the intents and all vocabulary is prepared in a logical and complex way.

3. Currently it is also very common to use the Chatbot Platforms, which does not require any knowledge of coding and are already stocked with a great range of vocabulary. The most popular ones include:
- <a href="https://cloud.google.com/dialogflow" target="_blank">Dialogflow by Google Clouds</a>
- <a href="https://wotnot.io/" target="_blank">Wotnot</a>
- <a href="https://chatfuel.com/" target="_blank">Chatfuel</a>
- <a href="https://mobilemonkey.com/" target="_blank">MobileMonkey</a>

Example of my Dialogflow project:

<p align="center">
  <img src="https://github.com/KlaudiaBC/Python-Essentials-Project-Chatbot-Elmo/blob/main/img/dialogflow.png?raw=true" alt="dialogflow">
</p>

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="uj"></p>

## User stories

<table>
  <tr>
    <th>User stories:</th>
    <th>Acceptance criteria:</th>
  </tr>
  <tr>
    <td>As a User I want to be led through the registration process so that I can sign up for activities of my choice.</td>
    <td>Given that I am the User I will be provided with short back-to-back conversation which will process adding my name to the desired list.</td>
  </tr>
    <tr>
    <td>As a User I want to be able to easily access information about the school so that I know the place, contact and cost.</td>
    <td>Given that I am the User I will be provided with the desired information once I type in the input field word connected with what I am looking for.</td>
  </tr>
    <tr>
    <td>As a User I want to know which activities are available.</td>
    <td>Given that I am the User I will be provided with the desired information in the beginning of the registration process.</td>
  </tr>
    <tr>
    <td>As a User I want to know what time activities take place.</td>
    <td>Given that I am the User I will be provided with the desired information in the beginning of the registration process.</td>
  </tr>
    <tr>
    <td>As a User I want to end the application once my purpose is met.</td>
    <td>Given that I am the User I will be provided with the exit option once I reach the ending point of the conversation or type: bye or exit in the input field.</td>
  </tr>
    <tr>
    <td>As a User I want to be entertained by a joke.</td>
    <td>Given that I am the User I will be provided with a random joke everytime I type word: "joke" in the terminal (in any form eg. joking, tell me jokes etc.)</td>
  </tr>
  <tr>
    <td>As a User I want my messages to be understood so that I can find what I am looking for.</td>
    <td>Given that I am the User I will be provided with multiple options of information and lead into a main purpose of the application which is registration for activities.</td>
  </tr>
  </table>
  
<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="fe"></p>

## Features

### Excisting features
- Customised customer interactions - ChatBot has multiple personalised responses for a User
- Quick registration - allows for subscribing to a selected activity list via the short and friendly conversation
- Easy deployment and messaging support - application is deployed via Herokuapp and is easy to use, all information needed for the User are provided in the top part of the terminal.
- Integrations with 3rd party applications - the chatbot is connected with Google Cloud (Google Drive and Google Sheets).
- Security and privacy of customer data - the data provided via User is stored in the authorised files with limited access.
- Random jokes - as an element of a user-friendly environment adjusted to targeted groups of recipients.
- Useful information - ChatBot provide the information about contact details, address, prices and available activities with the time schedule.

<p align="center">
  <img src="https://github.com/KlaudiaBC/Python-Essentials-Project-Chatbot-Elmo/blob/main/img/main_root_conv.png?raw=true" alt="conversation">
</p>

### Future features
Sign up process:
- Ask User for more credentials - a Bot can request and collect multiple informations like: surname, date of birth etc.
- Check availability - provide in the worksheets another row with data, containing the number of free places (for each activity). The Bot can check if this number is greater than 0 and only then allow User to register. Once registered, the Bot can subtract one from the amount of free places for particular activity and update the data.

ChatBot features:
- Allow human handover - connect with a human support once the expectations of the customer can not be met
- Add UX/UI - add design of the chat window as well as implementation of specific font, background or graphic signs (like emotions)
- Add omnichannel messaging support - the feature which provides the integrations allowing ChatBot to be launched across the channels (User do not have to provide any information manually)
- Expand the vocabulary - rule-based chatbots can often be annoying for a customer because they can't understand the actual intent of human queries. To improve User experience, the bot needs to have a great corpus and have to be equipped with the AI-training algorithms which allows it to become more intelligent and understand the User better.
- Remove punctuation and stop-words. As I have used this method in my previous version of chatbot, I haven't got time to implement it in my current project but it is indeed a very powerful feature.

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="data"></p>

## Data model

### 1. Decision tree:
I created a map of the possible outcomes of a series of related choices. My decision tree starts with a single node, which branches into two possible outcomes. Each of those outcomes leads to additional nodes, which connect with new possibilities. The end point is when the User makes a decision about exiting the terminal via typing one of exit words or confirm exit while asked an exit question. If the User will provide requested information, the outcome will be to pass the data into the desired spreadsheet. See the flowchart:
 
<p align="center">
  <img src="https://github.com/KlaudiaBC/Python-Essentials-Project-Chatbot-Elmo/blob/main/img/main_conv.png?raw=true" alt="data tree">
</p>

### 2. Nested lists:
I have declared the variable "Intents" to store a list that contains ten objects. Each object contains a nested list of three elements: tag, pattern and responses. Each element in this data structure has its name/value pair, so for name "intents" - there are six values, for name "tag" there is one value and so on.

See pic.

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="ip"></p>

## Implementation process

### Setting the sign up process and API:
I created a new project on the Google Cloud Platform and called it "Elmo activities".
To access spreadsheet located in my google account I had to enable two API's:
- Google Drive: credentials allows to securely access the google files
- Google Sheets

In order to connect my API with a Python project I had to generate credentials which provide proof to Google Drive that my Python project has permission to access the account.
Once the credentials were set, I received a unique email address and created a key of credentials in .json format.
I added this file into my repository and called it: "creds.json". Then I copied the client email address stored in this file, and used it in the "Give access" section in my Google Sheets file.
I added the creds.json into my git.ignore file to make sure, this document will not be committed at any point into my repository as it does contain sensitive information which should be hidden.

Installing libraries:
At first, I added the required libraries to my run.py file:
- google-auth - used to set up the authentication needed to access Google Cloud project
- gspread - library of code needed to access and update data in the spreadsheet

Once the API connections were set, I created an if/else statement for the main conversation (register the User for chosen activities).
Next I moved into creating a function get_date() which requests the data from the connected spreadsheet and displays it for a user in format: activity - date/time.
My statement defining the main conversation flow became very complicated therefore I decided to split some parts of the statement into independent functions and call each function when it is needed. Furthermore I built the function which pushes the data into a spreadsheet once the User confirms his desire to be signed on the list.

At this stage I had a customised ChatBot able to provide a full basic conversation with the User and request information needed to sign up for chosen activities as well as able to save the data in the compatible spreadsheet.

<p align="center">***</p>

### Adding a personality:
In order to make my ChatBot more human-like, I had to introduce a few new functions into my python file.
To avoid storing the large amounts of data in my main code, I created a json file, which contains predefined patterns, responses and tags.

I installed the libraries needed for further development:
- sys - library with access to some variables used or maintained by the interpreter or strongly with it connected (function used in the project: sys.exit)
- nltk - leading platform for building Python programs to work with human language data (Natural Language Toolkit)
- WordNetLemmatizer - lexical database for the English language, used to establish structured semantic relationships between words
- nltk.stem - Interfaces used to remove morphological affixes from words, leaving only the word stem
- json - needed to read the json file
- random - returns a random element from the given sequence
- spacy - software library for advanced natural language processing

I stored the particular parts of the data in variables in the way: pattern+tag and responses+tag. Then I created a function which will process the text from the input.
1. Tokanization - the process of converting a sequence of characters into a sequence of tokens (strings with an assigned meaning). I have used build in function provided with nltk library in order to tokenize the answers.
2. Lemmatization - the process of reducing inflection in words to their root forms - lemmas. Another way to achieve the processing of the word into its root version is called stemming. The main difference between those two ways is that the stemming removes only the last characters of the word, where lemmatization takes into consideration context so can provide better correction of words. See the lemmatization and the stemming process on picture below.

<p align="center">
  <img src="https://github.com/KlaudiaBC/Python-Essentials-Project-Chatbot-Elmo/blob/main/img/text_processing.png?raw=true" alt="word processing">
 </p>

<p align="center">
  <img src="https://github.com/KlaudiaBC/Python-Essentials-Project-Chatbot-Elmo/blob/main/img/stemm_lemma.png?raw=true" alt="stemming">
</p>

Once the answer was brought to the root word, I created a loop with a nested loops, which checks if:
- the object (word) match with any object on the patterns list
- if the tag of pattern where the object exists matches to any tag in patterns list
- if this tag matches to any tag in responses list

Finally once all mapping is done:
- choose the random response from the responses array stored on the list containing matching tag
  
<p align="center">
  <img src="https://github.com/KlaudiaBC/Python-Essentials-Project-Chatbot-Elmo/blob/main/img/patternsandresponses.png?raw=true" alt="patterns">
</p>

In other words, the function is looking for a pattern (a list of predicted words) which contains the processed word from the input and is assigned to this patterns tag. Then it looks for the same tag in the responses list and via this tag is able to display response matching to Users input.

I also added extra leading information, which Elmo will pass to the User - clues what to ask about or what User should type in the input to receive desired response.

### Integration of the root conversation with chatbot responses:
Since I have built those two parts of functionality apart, it was time to connect them. 

The main goal: root conversation- allow users to register for activities. Once User chooses yes in the first question and follows the next queries, he will be able to achieve this goal in less than 5 min with no effort.
If the User will choose "no" in the first question or in any other queries, he will be sent back into a second node question.
If User types any other word in the input field- the bot will display the answer and lead back to the top of the root- the second node question.

Once the process of registration is done, User is sent to the second node and can sign up for more activities or continue conversation (ask for information, joke, tell about feelings). The main loop of the tree is executing the root continuously until the User will confirm the desire to end the process.

After deployment, I realised that my input form has no validation therefore, once User presses enter with no input, it breaks the code and shows error. To fix this, I defined a new function responsible for checking if the input is greater than 0 characters.

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="tu"></p>

## Technologies used:
- <a href="https://www.python.org/">Python</a> - programming language
- <a href="https://id.heroku.com/login">Heroku</a> - for deployment
- <a href="https://pythontutor.com/">Python Tutor</a> - for code visualisation
- <a href="https://colab.research.google.com/">Google Colab</a> - for combining executable code 
- <a href="https://www.draw.io/">Draw.io</a> - for the diagrams
- <a href="http://pep8online.com/">Pep8 online</a> - check the code for PEP8 requirements

<p align="right"><a href="#welcome">Bact to top</a></p>
<p id="ack"></p>

## Acknowledgements

In this place I would like to thank everyone, who added an knowledge and value to this project:
- <a href="https://codeinstitute.net/" target="_blank">Code Institute</a> course materials and walkthroughs
- lead and support of my Code Institute Mentor - Guido Cecilio
- Code Institute Slack Community
- <a href="https://www.w3schools.com/" target="_blank">W3schools</a>
- <a href="https://stackoverflow.com/" target="_blank">Stack Overflow</a>
- <a href="https://m.youtube.com/watch?v=c_gXrw1RoKo" target="_blank">"Build your own chatbot using Python"</a> by Great Learning
- <a href="https://www.freecodecamp.org/news/how-to-build-an-end-to-end-conversational-ai-system-using-behavior-trees-658a7122e794/" target="_blank">"How to Build an End-to-End Conversational AI System using Behavior Trees"</a> by freeCodeCamp
- <a href="https://stackoverflow.com/" target="_blank">"How to Make a Chatbot in Python Step By Step"</a> by upGrad
- <a href="https://m.youtube.com/watch?v=wypVcNIH6D4&list=PLzMcBGfZo4-ndH9FoC4YWHGXG5RZekt-Q&index=1&t=30s" target="_blank">"Python ChatBot Tutorial"</a> by Tech With Tim
- <a href="https://data-flair.training/blogs/python-chatbot-project/amp/" target="_blank">"Python Chatbot Project – Learn to build your first chatbot using NLTK & Keras"</a> by DataFlair
- <a href="https://www.datacamp.com/community/tutorials/decision-tree-classification-python" target="_blank">"Decision Tree Classification in Python"</a> by datacamp
- <a href="https://www.comm100.com/blog/journey-mapping-chatbot-decision-tree-from-scratch.html/" target="_blank">"Journey Mapping for Chatbots"</a> by Comm100
- <a href="https://www.youtube.com/watch?v=6GLFcm7dGiY" target="_blank">"Build a chatbot from scratch-Ultimate Chatbot Tutorial"</a> by Tech With Sach

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

Continuous testing during app development was implemented via printing each individual function right after creating it to ensure expected results were met.
The features, which were taken into a testing, are listed below.

<table>
  <tr>
    <th>Element</th>
    <th>Expected result</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>Name input field</td>
    <td>The name is correctly displayed in the greeting sentence: "hello" + name from the input.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Render activities</td>
    <td>The available activities are correctly displayed for the User and are compatible with activities provided in the connected spreadsheet.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td> Registration</td>
    <td>After User confirms the desire to be signed up for a specific list of activities, the data he provided is sent and appended in a connected spreadsheet.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Display joke</td>
    <td>Once User asks for a joke via the input field, the random joke will be rendered and the app returns into the second child node query.</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Small talk</td>
    <td>The words provided by User are processed into a root word which allows the user to display correct responses out of available responses: address, contact, cost, feelings (sad, happy, bored), thank, greeting, exit.</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Exit</td>
    <td>Once the User confirms the will to exit the terminal, the terminal is shut.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Input</td>
    <td>Once the input is none and User presses "Enter", the terminal will return the question.</td>
    <td>Pass</td>
  </tr>
</table>

The code was validated through the PEP8 online and the syntax is correct.

<p align="center">
  <img src="https://github.com/KlaudiaBC/Python-Essentials-Project-Chatbot-Elmo/blob/main/img/pep8.png?raw=true" alt="pep8">
</p>

<p align="right"><a href="#welcome">Bact to top</a></p>
