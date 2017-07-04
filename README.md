# GOTOams Bot


[![Build Status][travisci-badge]][travisci-builds] 

This bot was created for the [GOTO Amazon Chatbot Challenge.][hackathon-main]

## Usage

* You can ask the bot by a talk exact name:

    Q: I want to know about _Real World Java 9_​ talk

    A: Real World Java 9 belongs to the Programming Languages track and will be presented by Trisha Gee at Administratiezaal on Wednesday 14 of June from 11:10 to 12:00.

* Or you can ask the bot by a talk partial name:
    Q: I want to know about oath talk
    
    A: The Scribe's Oath belongs to the Keynotes track and will be presented by Robert C. Martin at Effectenbeurszaal on Wednesday 14 of June from 17:10 to 18:00.

* Or you can even ask the bot by some keywords that are not contained in any talk name (but that I found relevant):
    
    Q: Talks about ml
    
    A: I've found 3 talks matching your interest: 
    How Do You Apply Machine Learning to Deliver New Functionality For a Complex Application Given Limited Time? belongs to the Solutions Wednesday track and will be presented by Attila Houtkooper and Torec Luik at Keurzaal on Wednesday 14 of June from 11:10 to 12:00. 
    Machine Learning, Your First Steps belongs to the Solutions Wednesday track and will be presented by David Stibbe at Keurzaal on Wednesday 14 of June from 10:10 to 11:00.
    Machine Learning with TensorFlow belongs to the Machine Learning without a PhD track and will be presented by Robert Saxby and Rokesh Jankie at Veilingzaal on Tuesday 13 of June from 15:00 to 15:50.

----------------

* When you ask about a talk, you can then also ask for the speaker (Or if you ask for the speaker before asking for a talk, you will be prompted with the speaker name)

Q: I want to know about lego
A: REST no more - Using Actors for the Internet of (LEGO) Trains & Raspberry Pis belongs to the Cyber-Physical Systems track and will be presented by Johan Janssen at Veilingzaal on Wednesday 14 of June from 14:00 to 14:50.
Tachú

Q: Who is the speaker?
A: <Speaker picture> Johan Janssen. Twitter: johanjanssen42

----------------

There are many more questions you can ask the chatbot, I made a super flash demo [here.][demo-video]

## Development considerations

* The datasource for this chatbot can be found in the [resources](resources) folder in this repository. I didn't create a database because didn't think it was interesting for this challenge.  
* Custom slot types _talks, speakers, locations and tracks_ values are generated from the datasource itself. See [lex_helper](lex_helper.py)  
* Besides setting up AWS credentials, this project relies on AWS account ID, this is set via the environment variable `AWS_ACCOUNT_ID` _see_ [setup.py, line 4](setup.py)
* I included another [deployment script](deploy.sh) because I needed to rapidly deploy my AWS Lambda function without touching anything in AWS Lex

## Package contents
----------------

This package contains a sample bot to get you started quickly. The sample bot consists of:

1 - An Amazon Lex bot. You can ask which talks are happening at a certain time and details about the speaker. See setup.py.
2 - Another Amazon Lambda function, invoked by Lex for control and validation of results of the Lex bot. See botcontrol.py.
3 - The resources folder that contains the datasources necessary for the chatbot.
4 - A [full deployment script](setup.sh) that will setup the components above in your AWS account.
5 - A [lambda quickly deployment script](deploy.sh) because I needed to rapidly deploy my AWS Lambda function without touching anything in AWS Lex.

## Know "issues"
----------------

* There are some _small_ known things this chatbot won't handle very well: For example, if a talk has more than one speaker, I will only save in the session attributes the first one. This needs to be improved.


##How to use the bot
------------------

This bot was installed in Facebook Messenger, at the moment only the specified users in the competition can chat with it. It is available [here][messenger-chatbot]


[hackathon-main]: http://www.amazondcn.com/challenge/index.html
[travisci-badge]: https://travis-ci.com/imTachu/GOTOamsBot.svg?token=FXoqSPyhGxTJyV3aAbkJ&branch=master
[travisci-builds]: https://travis-ci.com/imTachu/GOTOamsBot
[messenger-chatbot]: https://www.messenger.com/t/244400059380375
[demo-video]: https://www.youtube.com/watch?v=moMGkIe6eH0
