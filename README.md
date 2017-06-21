# GOTOams Bot

This bot was created from a sample bot version given for the [GOTO Amazon Chatbot Challenge.][hackathon-main]


The objective of the competition is to take this sample bot and make a complete chatbot to navigate conference schedules, ask information about the speakers, rooms, tracks etc. You can improve it in various ways: making it respond to voice commands, build a mobile app, integrate with SMS, email, facebook, slack. Also new ideas are welcome!


## Usage

//You can ask the bot by a talk exact name
Q: I want to know about Real World Java 9​ talk
A: Real World Java 9 belongs to the Programming Languages track and will be presented by Trisha Gee at Administratiezaal on Wednesday 14 of June from 11:10 to 12:00.

//Or you can ask the bot by a talk partial name
Q: I want to know about oath talk
A: The Scribe's Oath belongs to the Keynotes track and will be presented by Robert C. Martin at Effectenbeurszaal on Wednesday 14 of June from 17:10 to 18:00.

//Or you can even ask the bot by some keywords that are not contained in any talk name (but that I found relevant)
Q: Talks about ml
A: I've found 3 talks matching your interest: 
How Do You Apply Machine Learning to Deliver New Functionality For a Complex Application Given Limited Time? belongs to the Solutions Wednesday track and will be presented by Attila Houtkooper and Torec Luik at Keurzaal on Wednesday 14 of June from 11:10 to 12:00. 
Machine Learning, Your First Steps belongs to the Solutions Wednesday track and will be presented by David Stibbe at Keurzaal on Wednesday 14 of June from 10:10 to 11:00.
Machine Learning with TensorFlow belongs to the Machine Learning without a PhD track and will be presented by Robert Saxby and Rokesh Jankie at Veilingzaal on Tuesday 13 of June from 15:00 to 15:50.



Q: Who is the speaker?
A: Inventor



## Development considerations

* The datasource for this chatbot can be found in the [resources](resources) folder in this repository. I didn't create a database because didn't think it interesting for this exercise.  
* Custom slot types _talks, speakers and tracks_ values are generated from the datasource itself. See [lex_helper](lex_helper.py)  
* Besides setting up AWS credentials, this project relies on AWS Account ID, this is set via the environment variable `ACCOUNT_ID` _see_ [setup.py, line 4](setup.py)
* I included another [deployment script](deploy.sh) because I needed to rapidly deploy my AWS Lambda function without touching anything in AWS Lex

### Package contents
----------------

This package contains a sample bot to get you started quickly. The sample bot consists of:

1 - An Amazon API gateway, so that your bot is accessible via a simple REST HTTP API. See app.py.
2 - An Amazon Lambda function invoked by the API gateway. This function passes the HTTP request contents to Amazon Lex, which does the natural language processing. Here you can add some more logic before or after Lex runs. See app.py.
3 - An Amazon Lex bot. You can ask which talks are happening at a certain time and details about the speaker. See setup.py.
4 - Another Amazon Lambda function, invoked by Lex for control and validation of results of the Lex bot. See botcontrol.py.
5 - A script (setup.py) that will setup the components above in your AWS account, so you can start hacking quickly! 

Setup steps
-----------

1 - Configure your AWS access key and secret key according to https://github.com/awslabs/chalice#credentials . DO NOT publish your access key and secret key to public sites such as github!
2 - Create a virtual env for your bot with "virtualenv .". The examples below assume you are inside the virtualenv. See http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/ for more details. 
3 - Configure your AWS account id in setup.py
4 - Run: "source bin/activate"
5 - Run: "pip install -r requirements.txt"
6 - Run: "python setup.py"

How to use the bot
------------------

For most of your testing, you can use the Lex console. There is a chat window in the bot page where you can quickly test.
You can also use httpie or postman for simple tests of your API gateway. The URL for your API is output by the setup.py script.
Example with httpie:

http POST https://h0sx8hm04l.execute-api.us-east-1.amazonaws.com/dev usertext="What is on at 9 am?" (replace the URL with the one output by setup.py)

http POST https://h0sx8hm04l.execute-api.us-east-1.amazonaws.com/dev usertext="Who is the speaker?"

How to develop the bot
----------------------

The setup.py, app.py and botcontrol.py are the sourcecode for the entire bot. If you modify them, you can run setup.py again to upload them to AWS.
However, if you modify the Lambda or Lex functions directly in the AWS console, be aware that running setup.py will overwrite your changes with the contents on the files.


[hackathon-main]: http://www.amazondcn.com/challenge/index.html