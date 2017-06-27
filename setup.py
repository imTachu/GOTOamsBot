import boto3
import lex_helper
import os
import time
from zipfile import ZipFile

from botocore.exceptions import ClientError

ACCOUNT_ID = os.environ['AWS_ACCOUNT_ID']


with ZipFile('lambda-package.zip', 'w') as myzip:
    myzip.write('botcontrol.py')
    myzip.write('resources/__init__.py')
    myzip.write('resources/speakers.py')
    myzip.write('resources/talks.py')

""" Initial Lex configuration """

botcontrol_function = {
    u'Code': {u'ZipFile': open('lambda-package.zip').read()},
    u'Description': u'Function doing advanced control of your bot, called by Lex',
    u'FunctionName': u'botcontrol',
    u'Handler': u'botcontrol.lambda_handler',
    u'MemorySize': 128,
    u'Role': u'arn:aws:iam::{}:role/samplebot-dev'.format(ACCOUNT_ID),
    u'Runtime': u'python2.7',
    u'Timeout': 10,
    u'TracingConfig': {u'Mode': u'PassThrough'},
    u'Publish': True,
}

permission = {
    u'FunctionName': u'botcontrol',
    u'StatementId': u'AuthorizeLex',
    u'Action': u'lambda:InvokeFunction',
    u'Principal': u'lex.amazonaws.com',
    u'SourceArn': "arn:aws:lex:us-east-1:{}:intent:*:*".format(ACCOUNT_ID),
}

""" Intents """

about_talk_intent = {
    u'dialogCodeHook': {u'messageVersion': u'1.0',
                        u'uri': u'arn:aws:lambda:us-east-1:{}:function:botcontrol'.format(ACCOUNT_ID)},
    u'fulfillmentActivity': {u'codeHook': {u'messageVersion': u'1.0',
                                           u'uri': u'arn:aws:lambda:us-east-1:{}:function:botcontrol'.format(
                                               ACCOUNT_ID)},
                             u'type': u'CodeHook'},
    u'name': u'AboutTalk',
    u'sampleUtterances': [u'About {talk}', u'Tell me about {talk} talk', u'I wanna know about {talk} talk',
                          u'I want to know about {talk} talk', u'What talks are about {talk}', u'Talks about {talk}', u'About that talk', u'About a talk'],
    u'slots': [{u'name': u'talk',
                u'priority': 1,
                u'sampleUtterances': [],
                u'slotConstraint': u'Required',
                u'slotType': u'Talks',
                u'slotTypeVersion': u'$LATEST',
                u'valueElicitationPrompt': {u'maxAttempts': 2,
                                            u'messages': [{u'content': u'What talk? You don\'t have to tell me the full name, maybe just a keyword. For example, cloud, LEGO, ml.', u'contentType': u'PlainText'}]}}],
}

who_is_the_speaker_intent = {
    u'dialogCodeHook': {u'messageVersion': u'1.0',
                        u'uri': u'arn:aws:lambda:us-east-1:{}:function:botcontrol'.format(ACCOUNT_ID)},
    u'fulfillmentActivity': {u'codeHook': {u'messageVersion': u'1.0',
                                           u'uri': u'arn:aws:lambda:us-east-1:{}:function:botcontrol'.format(ACCOUNT_ID)},
                             u'type': u'CodeHook'},
    u'name': u'WhoIsTheSpeaker',
    u'sampleUtterances': [u'Who is the speaker', u'Who are the speakers', u'Who is him', u'Who is her'],
    u'slots': [{u'name': u'speaker',
                u'priority': 1,
                u'sampleUtterances': [],
                u'slotConstraint': u'Required',
                u'slotType': u'Speakers',
                u'slotTypeVersion': u'$LATEST',
                u'valueElicitationPrompt': {u'maxAttempts': 2,
                                            u'messages': [{u'content': u'What is the first/last name of the speaker?',
                                                           u'contentType': u'PlainText'}]}}],
}

whats_the_schedule_intent = {
    u'dialogCodeHook': {u'messageVersion': u'1.0',
                        u'uri': u'arn:aws:lambda:us-east-1:{}:function:botcontrol'.format(ACCOUNT_ID)},
    u'fulfillmentActivity': {u'codeHook': {u'messageVersion': u'1.0', u'uri': u'arn:aws:lambda:us-east-1:{}:function:botcontrol'.format(ACCOUNT_ID)}, u'type': u'CodeHook'},
    u'name': u'WhatsTheSchedule',
    u'sampleUtterances': [u'What\'s the conference is the schedule', u'What is the schedule', u'What is the timetable', u'Timetable', u'Schedule', u'What is the schedule on {when}'],
    u'slots': [{u'name': u'when',
                u'priority': 1,
                u'sampleUtterances': [],
                u'slotConstraint': u'Required',
                u'slotType': u'AMAZON.TIME',
                u'valueElicitationPrompt': {u'maxAttempts': 2,
                                            u'messages': [{u'content': u'When?', u'contentType': u'PlainText'}]}}],
}

about_tracks_intent = {
    u'dialogCodeHook': {u'messageVersion': u'1.0',
                        u'uri': u'arn:aws:lambda:us-east-1:{}:function:botcontrol'.format(ACCOUNT_ID)},
    u'fulfillmentActivity': {u'codeHook': {u'messageVersion': u'1.0', u'uri': u'arn:aws:lambda:us-east-1:{}:function:botcontrol'.format(ACCOUNT_ID)}, u'type': u'CodeHook'},
    u'name': u'AboutTracks',
    u'sampleUtterances': [u'{track} track', u'Track {track}'],
    u'slots': [{u'name': u'track',
                u'priority': 1,
                u'sampleUtterances': [],
                u'slotConstraint': u'Required',
                u'slotType': u'Tracks',
                u'slotTypeVersion': u'$LATEST',
                u'valueElicitationPrompt': {u'maxAttempts': 2, u'messages': [{u'content': u'What track?', u'contentType': u'PlainText'}]}}],
}

about_locations_intent = {
    u'dialogCodeHook': {u'messageVersion': u'1.0',
                        u'uri': u'arn:aws:lambda:us-east-1:{}:function:botcontrol'.format(ACCOUNT_ID)},
    u'fulfillmentActivity': {u'codeHook': {u'messageVersion': u'1.0', u'uri': u'arn:aws:lambda:us-east-1:{}:function:botcontrol'.format(ACCOUNT_ID)}, u'type': u'CodeHook'},
    u'name': u'AboutLocations',
    u'sampleUtterances': [u'{location} room', u'Room {location}', u'What will be presented in {location}', u'What will be presented'],
    u'slots': [{u'name': u'location',
                u'priority': 1,
                u'sampleUtterances': [],
                u'slotConstraint': u'Required',
                u'slotType': u'Locations',
                u'slotTypeVersion': u'$LATEST',
                u'valueElicitationPrompt': {u'maxAttempts': 2, u'messages': [{u'content': u'In what room??', u'contentType': u'PlainText'}]}}],
}

""" Custom slot types """

speakers_slot_type = {
    u'description': u'All speakers from the conference',
    u'enumerationValues': lex_helper.build_speakers_slot(),
    u'name': u'Speakers',
}

talks_slot_type = {
    u'description': u'All talks from the conference',
    u'enumerationValues': lex_helper.build_talks_slot(),
    u'name': u'Talks',
}

tracks_slot_type = {
    u'description': u'All tracks from the conference',
    u'enumerationValues': lex_helper.build_tracks_slot(),
    u'name': u'Tracks',
}

locations_slot_type = {
    u'description': u'All locations in the conference venue',
    u'enumerationValues': lex_helper.build_locations_slot(),
    u'name': u'Locations',
}

bot = {
    u'abortStatement': {u'messages': [{u'content': u'Sorry, I could not understand. Goodbye.',
                                       u'contentType': u'PlainText'}]},
    u'childDirected': False,
    u'clarificationPrompt': {u'maxAttempts': 5,
                             u'messages': [{u'content': u'Sorry, can you please repeat that?',
                                            u'contentType': u'PlainText'}]},
    u'intents': [{u'intentName': u'WhoIsTheSpeaker', u'intentVersion': u'$LATEST'},
                 {u'intentName': u'WhatsTheSchedule', u'intentVersion': u'$LATEST'},
                 {u'intentName': u'AboutTracks', u'intentVersion': u'$LATEST'},
                 {u'intentName': u'AboutLocations', u'intentVersion': u'$LATEST'},
                 {u'intentName': u'AboutTalk', u'intentVersion': u'$LATEST'}],
    u'locale': u'en-US',
    u'name': u'GOTOamsBot',
    u'processBehavior': 'BUILD',
    u'voiceId': u'0'}

bot_alias = {
    u'name': u'GOTOamsBot',
    u'botVersion': u'$LATEST',
    u'botName': u'GOTOamsBot',
}

# Bot parameters end here

# Setup code

os.system('chalice deploy')

lex = boto3.client('lex-models', region_name='us-east-1')
lambd = boto3.client('lambda', region_name='us-east-1')


def wait(secs):
    time.sleep(secs)


# delete everything

try:
    lambd.delete_function(FunctionName='botcontrol')
    print 'Deleted botcontrol lambda function'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'ResourceNotFoundException':
        raise

try:
    lex.delete_bot_alias(name='GOTOamsBot', botName='GOTOamsBot')
    print 'Deleted alias GOTOamsBot'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

try:
    lex.delete_bot(name='GOTOamsBot')
    print 'Deleted GOTOamsBot'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

try:
    lex.delete_intent(name='WhoIsTheSpeaker')
    print 'Deleted intent WhoIsTheSpeaker'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

try:
    lex.delete_intent(name='AboutTalk')
    print 'Deleted intent AboutTalk'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

try:
    lex.delete_intent(name='AboutTracks')
    print 'Deleted intent AboutTracks'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

try:
    lex.delete_intent(name='AboutLocations')
    print 'Deleted intent AboutLocations'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

try:
    lex.delete_intent(name='WhatsTheSchedule')
    print 'Deleted intent WhatsTheSchedule'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

try:
    lex.delete_slot_type(name='Speakers')
    print 'Deleted slot type Speakers'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

try:
    lex.delete_slot_type(name='Talks')
    print 'Deleted slot type Talks'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

try:
    lex.delete_slot_type(name='Tracks')
    print 'Deleted slot type Tracks'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

try:
    lex.delete_slot_type(name='Locations')
    print 'Deleted slot type Locations'
    wait(3)
except ClientError, e:
    if e.response['Error']['Code'] != 'NotFoundException':
        raise

lambd.create_function(**botcontrol_function)
print 'Created lambda function botcontrol'
wait(3)

lambd.add_permission(**permission)
wait(3)
print 'Assigned permissions authorizing Lex to call botcontrol'

lex.put_slot_type(**speakers_slot_type)
print 'Created slot type Speakers'
wait(3)

lex.put_slot_type(**talks_slot_type)
print 'Created slot type Talks'
wait(3)

lex.put_slot_type(**tracks_slot_type)
print 'Created slot type Tracks'
wait(3)

lex.put_slot_type(**locations_slot_type)
print 'Created slot type Locations'
wait(3)

lex.put_intent(**about_talk_intent)
wait(3)
print 'Created AboutTalk intent'

lex.put_intent(**about_tracks_intent)
wait(3)
print 'Created AboutTracks intent'

lex.put_intent(**about_locations_intent)
wait(3)
print 'Created AboutLocations intent'

lex.put_intent(**who_is_the_speaker_intent)
wait(3)
print 'Created WhoIsTheSpeaker intent'

lex.put_intent(**whats_the_schedule_intent)
wait(3)
print 'Created WhatsTheSchedule intent'

lex.put_bot(**bot)
wait(3)
print 'Created bot'

lex.put_bot_alias(**bot_alias)
print 'Created bot alias'
wait(5)

os.unlink('lambda-package.zip')

print 'All done, exiting...'
