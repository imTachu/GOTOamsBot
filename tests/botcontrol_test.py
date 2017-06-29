import botcontrol


def test_about_talk_all_talks():
    for talk in botcontrol.fetch_talks():
        botcontrol.about_talk(intent_request_mock('AboutTalk', {'talk': talk}))


def test_who_is_the_speaker_from_intent():
    for speaker in botcontrol.fetch_speakers():
        botcontrol.who_is_the_speaker(intent_request_mock('WhoIsTheSpeaker', {'speaker': speaker}))


def test_who_is_the_speaker_from_session_attributes():
    for speaker in botcontrol.fetch_speakers():
        botcontrol.who_is_the_speaker(intent_request_mock('WhoIsTheSpeaker', {'speaker': None}))


def test_about_talk_no_talk_found():
    botcontrol.about_talk(intent_request_mock('AboutTalk', {'talk': 'salamanca'}))


def test_about_talk_one_talk_one_speaker():
    botcontrol.about_talk(intent_request_mock('AboutTalk', {'talk': 'The Scribe\'s Oath'}))


def test_about_talk_one_talk_multiple_speakers():
    botcontrol.about_talk(intent_request_mock('AboutTalk', {'talk': 'Ethics'}))


def test_about_talk_multiple_talks_one_speaker():
    botcontrol.about_talk(intent_request_mock('AboutTalk', {'talk': 'Javascript'}))


def test_about_talk_multiple_talks_multiple_speakers():
    botcontrol.about_talk(intent_request_mock('AboutTalk', {'talk': 'Machine Learning'}))


def test_about_talk_with_tag_not_in_talk_name():
    botcontrol.about_talk(intent_request_mock('AboutTalk', {'talk': 'ml'}))


def test_find_talks_by_track_single_track():
    botcontrol.find_talks_by_track('Cats')


def test_find_talks_by_track_multiple_tracks():
    botcontrol.find_talks_by_track('Solutions')


def test_find_tracks_by_location():
    for location in botcontrol.fetch_locations():
        botcontrol.find_tracks_by_location(location)


def intent_request_mock(intent_name, slot):
    return {u'currentIntent': {u'slots': slot, u'name': intent_name, u'confirmationStatus': u'None'},
            u'bot': {u'alias': None, u'version': u'$LATEST', u'name': u'GOTOamsBot'},
            u'userId': u'dq64axgllu3znz8j663b23rh7nohadni', u'inputTranscript': u'about any',
            u'invocationSource': u'DialogCodeHook', u'outputDialogMode': u'Text', u'messageVersion': u'1.0', u'sessionAttributes': None}
