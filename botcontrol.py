# coding=utf-8
from __future__ import print_function
from resources.talks import TALKS
from resources.speakers import SPEAKERS

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """


def get_slots(intent_request):
    return intent_request['currentIntent']['slots']


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message, title):
    logger.info('[elicit_slot] locals = {}', locals())
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': {
                'contentType': 'PlainText',
                'content': message
            },
            'responseCard': {'version': '0',
                             'contentType': 'application/vnd.amazonaws.card.generic',
                             'genericAttachments': [{
                                 'title': title,
                                 'buttons': [
                                     {
                                         'text': 'Tuesday June 13',
                                         'value': '2017-06-13'
                                     },
                                     {
                                         'text': 'Wednesday June 14',
                                         'value': '2017-06-14'
                                     }
                                 ]}]
                             }
        }
    }


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }
    return response


def close_with_response_card(session_attributes, fulfillment_state, message, title, subtitle, link, image_url):
    response = {'sessionAttributes': session_attributes,
                'dialogAction': {
                    'type': 'Close',
                    'fulfillmentState': fulfillment_state,
                    'message': message,
                    'responseCard': {'version': '0',
                                     'contentType': 'application/vnd.amazonaws.card.generic',
                                     'genericAttachments': [{
                                         'title': title,
                                         'subTitle': subtitle,
                                         'attachmentLinkUrl': link,
                                         'imageUrl': image_url}]}}}
    return response


def delegate(session_attributes, slots):
    logger.info('[delegate] locals = {}'.format(locals()))
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }


""" --- Helper Functions --- """


def build_validation_result(is_valid, violated_slot, message_content):
    if message_content is None:
        return {
            "isValid": is_valid,
            "violatedSlot": violated_slot,
        }

    return {
        'isValid': is_valid,
        'violatedSlot': violated_slot,
        'message': {'contentType': 'PlainText', 'content': message_content}
    }


""" --- Intents --- """


def about_talk(intent_request):
    logger.info(intent_request)

    source = intent_request['invocationSource']

    logger.info('[what_is_on_now] locals = {}'.format(locals()))

    slots = get_slots(intent_request)
    talk_slot = str(slots['talk'])

    talks = list(set([s for s in fetch_talks() if talk_slot.lower() in s.lower()]) | set(find_talks_by_tag(talk_slot.lower())))
    output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
    if len(talks) == 0:
        response = 'I\'m sorry, I couldn\'t find any talk that contains \'' + talk_slot + '\'. Please try again :)'
    elif len(talks) == 1:
        talk = TALKS[talks[0]]
        response = format_about_talk_message(talks[0], talk)
        output_session_attributes['speakers'] = talk['speakers'][0]
    else:
        response = 'I\'ve found ' + str(len(talks)) + ' talks matching your interest: \n\n'
        for t in talks:
            talk = TALKS[t]
            response += format_about_talk_message(t, talk) + '\n'
    return close(output_session_attributes,
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': response})


def about_tracks(intent_request):
    logger.info(intent_request)

    slots = get_slots(intent_request)
    track_slot = str(slots['track'])

    tracks = [s for s in fetch_tracks() if track_slot.lower() in s.lower()]
    if len(tracks) == 0:
        response = 'I\'m sorry, I couldn\'t find any track \'' + track_slot + '\'. Please try again :)'
    elif len(tracks) == 1:
        response = format_about_tracks_message(tracks[0])
    else:
        response = 'I\'ve found ' + str(len(tracks)) + ' tracks matching your interest: \n\n'
        for t in tracks:
            response += format_about_tracks_message(t) + '.\n'
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': response})


def about_locations(intent_request):
    logger.info(intent_request)

    slots = get_slots(intent_request)
    location_slot = str(slots['location'])

    locations = [s for s in fetch_locations() if location_slot.lower() == s.lower()]
    logger.info(locations)
    if len(locations) == 0:
        response = 'I\'m sorry, I couldn\'t find any location \'' + location_slot + '\'. Please try again :)'
    elif len(locations) == 1:
        response = format_about_locations_message(locations)
    else:
        response = 'I\'ve found ' + str(len(locations)) + ' locations matching your interest: \n\n'
        for l in locations:
            response += format_about_locations_message(l) + '.\n'
    print(response)
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': response})


def who_is_the_speaker(intent_request):
    source = intent_request['invocationSource']

    logger.info('[who_is_the_speaker] locals = {}'.format(locals()))

    slots = get_slots(intent_request)
    current_slots = get_slots(intent_request)
    speaker_slot = slots['speaker']

    if source == 'DialogCodeHook':
        output_session_attributes = intent_request['sessionAttributes'] if intent_request[
                                                                               'sessionAttributes'] is not None else {}
        speaker_from_context = output_session_attributes.get('speakers')
        if speaker_slot is None and speaker_from_context is None:
            return delegate(output_session_attributes, current_slots)
        elif speaker_slot is None and speaker_from_context is not None:
            logger.info('[who_is_the_speaker] got speaker {} from previous intent'.format(speaker_from_context))
            response = find_speakers_by_speaker(speaker_from_context)[0]
        elif speaker_slot is not None:
            response = find_speakers_by_sub_speaker(speaker_slot)[0]
    return close_with_response_card(intent_request['sessionAttributes'],
                                    'Fulfilled',
                                    {'contentType': 'PlainText',
                                     'content': response}, response,
                                    SPEAKERS[response]['headline'] + '\n Twitter: @' + SPEAKERS[response][
                                        'twitter'] if 'twitter' in SPEAKERS[response] else SPEAKERS[response][
                                        'headline'],
                                    None, SPEAKERS[response]['photo'])


def whats_the_schedule(intent_request):
    slots = get_slots(intent_request)
    when_slot = slots['when']
    logger.info(when_slot)
    if when_slot is None:
        return elicit_slot(intent_request['sessionAttributes'],
                           intent_request['currentIntent']['name'],
                           slots, 'when', 'I have the schedules for both tuesday 13 and wednesday 14 of june',
                           'For what day you\'d like to see the schedule?')

    if when_slot == '2017-06-13':
        image = 'https://s3.amazonaws.com/gotoams2017challenge/june_13.jpg'
        day = 'Tuesday june 13th'
    else:
        image = 'https://s3.amazonaws.com/gotoams2017challenge/june_14.jpg'
        day = 'Tuesday june 14th'
    return close_with_response_card(intent_request['sessionAttributes'],
                                    'Fulfilled',
                                    {'contentType': 'PlainText',
                                     'content': 'Here, this is the schedule that you requested'}, 'GOTOams Schedule',
                                    day, image, image)


def request_photos(intent_request):
    logger.info(intent_request)
    return close_with_response_card(intent_request['sessionAttributes'],
                                    'Fulfilled',
                                    {'contentType': 'PlainText',
                                     'content': 'Absolutely! Here are the conference pictures '},
                                    'GOTO Conference Flickr', 'GOTOams 2017 album',
                                    'https://www.flickr.com/photos/26420411@N02/sets/72157682225251443',
                                    'https://goo.gl/txkQxW')


def when_conference(intent_request):
    logger.info(intent_request)
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'Bummer! This year\'s conference has happened. Save the date for June 18–20, 2018! :D'})


def contact(intent_request):
    logger.info(intent_request)
    return {'sessionAttributes': intent_request['sessionAttributes'],
            'dialogAction': {
                'type': 'Close',
                'fulfillmentState': 'Fulfilled',
                'message': {'contentType': 'PlainText',
                            'content': 'Here is the conference social media. Keep in touch! ;)'},
                'responseCard': {'version': '0',
                                 'contentType': 'application/vnd.amazonaws.card.generic',
                                 'genericAttachments': [{
                                     'title': 'info@amsterdam.gotocon.com',
                                     'subTitle': 'https://twitter.com/gotoamst\nhttps://www.facebook.com/GOTOConference'
                                 }]}}}


""" --- Dictionary Helpers --- """


def format_about_talk_message(talk_name, talk):
    return talk_name + ' belongs to the ' + talk['track'] + ' track and will be presented by ' + ' and '.join(
        talk['speakers']) + ' at ' + talk['location'] + ' on ' + talk['start'].strftime('%A %d of %B') + ' from ' + \
           talk['start'].strftime('%H:%M') + ' to ' + talk['end'].strftime('%H:%M') + '.'


def format_about_tracks_message(track_name):
    talks = find_talks_by_track(track_name)
    talk = TALKS[talks[0]]
    return track_name + ' will be presented at ' + talk['location'] + ' on ' + talk['start'].strftime(
        '%A %d of %B') + '.\nIts talks are: \n* ' + ',\n* '.join(talks)


def format_about_locations_message(location):
    tracks = find_tracks_by_location(location[0])
    print(tracks)
    return location[0] + ' room will host tracks: \n* ' + ',\n* '.join(tracks)


def fetch_tags():
    response = []
    for talk in TALKS:
        response.extend(TALKS[talk]['tags'])
    return set(response)


def fetch_talks():
    return set(TALKS.keys())


def fetch_speakers():
    return set(SPEAKERS.keys())


def fetch_tracks():
    response = []
    for talk in TALKS:
        response.append(TALKS[talk]['track'])
    return set(response)


def fetch_locations():
    response = []
    for talk in TALKS:
        response.append(TALKS[talk]['location'])
    return set(response)


def find_speakers_by_sub_speaker(sp):
    return [s for s in fetch_speakers() if sp.lower() in s.lower()]


def find_speakers_by_speaker(sp):
    return [s for s in fetch_speakers() if sp.lower() == s.lower()]


def find_talks_by_tag(tag):
    response = []
    for talk in TALKS:
        if any(t == tag for t in TALKS[talk]['tags']):
            response.append(talk)
    return set(response)


def find_talks_by_track(track):
    response = []
    for talk in TALKS:
        if TALKS[talk]['track'] == track:
            response.append(talk)
    return list(set(response))


def find_tracks_by_location(location):
    response = []
    for talk in TALKS:
        if TALKS[talk]['location'] == location:
            response.append(TALKS[talk]['track'])
    return list(set(response))


""" --- Intents Handling --- """


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug(
        'dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    if intent_name == 'AboutTalk':
        return about_talk(intent_request)
    elif intent_name == 'WhoIsTheSpeaker':
        return who_is_the_speaker(intent_request)
    elif intent_name == 'WhatsTheSchedule':
        return whats_the_schedule(intent_request)
    elif intent_name == 'AboutTracks':
        return about_tracks(intent_request)
    elif intent_name == 'AboutLocations':
        return about_locations(intent_request)
    elif intent_name == 'RequestPhotos':
        return request_photos(intent_request)
    elif intent_name == 'WhenConference':
        return when_conference(intent_request)
    elif intent_name == 'Contact':
        return contact(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    logger.debug('event = {}'.format(event))

    return dispatch(event)
