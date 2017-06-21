import botcontrol

# def test_getSpeaker():
#     print botcontrol.getSpeaker("Cockcroft")
#     assert botcontrol.getSpeaker("Adrian") == botcontrol.getSpeaker("Cockcroft")

# def test_dictionary():
#     assert about_talk({u'currentIntent': {u'slots': {u'talk': u'oath'}, u'name': u'AboutTalk', u'confirmationStatus': u'None'}, u'bot': {u'alias': None, u'version': u'$LATEST', u'name': u'GOTOamsBot'}, u'userId': u'dq64axgllu3znz8j663b23rh7nohadni', u'inputTranscript': u'about any', u'invocationSource': u'DialogCodeHook', u'outputDialogMode': u'Text', u'messageVersion': u'1.0', u'sessionAttributes': {u'speaker': u'Dr. Emmzett Brown'}}) == 13


# def test_who_is_the_speaker():
#     print botcontrol.who_is_the_speaker({u'currentIntent': {u'slots': {u'speaker': u'oath'}, u'name': u'AboutTalk', u'confirmationStatus': u'None'}, u'bot': {u'alias': None, u'version': u'$LATEST', u'name': u'GOTOamsBot'}, u'userId': u'dq64axgllu3znz8j663b23rh7nohadni', u'inputTranscript': u'about any', u'invocationSource': u'DialogCodeHook', u'outputDialogMode': u'Text', u'messageVersion': u'1.0', u'sessionAttributes': {u'speaker': u'Dr. Emmzett Brownzzz'}})
#     assert botcontrol.who_is_the_speaker({u'currentIntent': {u'slots': {u'speaker': u'oath'}, u'name': u'AboutTalk', u'confirmationStatus': u'None'}, u'bot': {u'alias': None, u'version': u'$LATEST', u'name': u'GOTOamsBot'}, u'userId': u'dq64axgllu3znz8j663b23rh7nohadni', u'inputTranscript': u'about any', u'invocationSource': u'DialogCodeHook', u'outputDialogMode': u'Text', u'messageVersion': u'1.0', u'sessionAttributes': {u'speaker': u'Dr. Emmzett Brown'}}) == 13


# def test_close_with_response_card():
#     print(botcontrol.close_with_response_card('sasf',
#                                     'Fulfilled',
#                                     {'contentType': 'PlainText',
#                                      'content': 'aaaa response'}, 'hashf', 'nananan java ',
#                                     'https://conf-assets.s3.eu-central-1.amazonaws.com/uploads/portraits/72/thumb.jpg') )
#     assert botcontrol.close_with_response_card('sgsdgggg',
#                                     'Fulfilled',
#                                     {'contentType': 'PlainText',
#                                      'content': 'aaaa response'}, 'hashf', 'nananan java ',
#                                     'https://conf-assets.s3.eu-central-1.amazonaws.com/uploads/portraits/72/thumb.jpg') == 2


def test_about_talk_no_talk_found():
    botcontrol.about_talk(about_talk_intent_request_mock('salamanca'))


def test_about_talk_one_talk_one_speaker():
    botcontrol.about_talk(about_talk_intent_request_mock('The Scribe\'s Oath'))


def test_about_talk_one_talk_multiple_speakers():
    botcontrol.about_talk(about_talk_intent_request_mock('Ethics'))


def test_about_talk_multiple_talks_one_speaker():
    botcontrol.about_talk(about_talk_intent_request_mock('Javascript'))


def test_about_talk_multiple_talks_multiple_speakers():
    botcontrol.about_talk(about_talk_intent_request_mock('Machine Learning'))


def test_about_talk_with_tag_not_in_talk_name():
    botcontrol.about_talk(about_talk_intent_request_mock('ml'))


def about_talk_intent_request_mock(talk_name):
    return {u'currentIntent': {u'slots': {u'talk': talk_name}, u'name': u'AboutTalk', u'confirmationStatus': u'None'}, u'bot': {u'alias': None, u'version': u'$LATEST', u'name': u'GOTOamsBot'}, u'userId': u'dq64axgllu3znz8j663b23rh7nohadni', u'inputTranscript': u'about any', u'invocationSource': u'DialogCodeHook', u'outputDialogMode': u'Text', u'messageVersion': u'1.0', u'sessionAttributes': {u'speaker': u'Dr. Emmzett Brown'}}