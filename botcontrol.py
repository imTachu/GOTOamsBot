from __future__ import print_function
from resources.talks import TALKS
from resources.speakers import SPEAKERS

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """


def get_slots(intent_request):
    return intent_request['currentIntent']['slots']


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    logger.info('[elicit_slot] locals = {}', locals())
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
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


def close_with_response_card(session_attributes, fulfillment_state, message, title, subtitle, image_url):
    response = {'sessionAttributes': session_attributes,
                'dialogAction': {
                    'type': 'Close',
                    'fulfillmentState': fulfillment_state,
                    'message': message, 'responseCard': {'version': '0',
                                    'contentType': 'application/vnd.amazonaws.card.generic',
                                    'genericAttachments': [{
                                        'title': title,
                                        'subTitle': subtitle,
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


def validate_when(when_slot):
    logger.info('[validate_when] locals = {}'.format(locals()))
    talk = TIMETABLE.get(when_slot)
    if talk is None:
        return build_validation_result(False,
                                       'when',
                                       'There is nothing at that time! Maybe try some other time?')

    return build_validation_result(True, None, None)


""" --- Functions that control the bot's behavior --- """


def what_is_on_now(intent_request):
    """
    Performs dialog management and fulfillment
    Beyond fulfillment, the implementation of this intent demonstrates the use of the elicitSlot dialog action
    in slot validation and re-prompting.
    """

    source = intent_request['invocationSource']

    logger.info('[what_is_on_now] locals = {}'.format(locals()))

    slots = get_slots(intent_request)
    when_slot = slots['when']

    if source == 'DialogCodeHook':
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt for the first violation detected.

        validation_result = validate_when(when_slot)
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return elicit_slot(intent_request['sessionAttributes'],
                               intent_request['currentIntent']['name'],
                               slots,
                               validation_result['violatedSlot'],
                               validation_result['message'])

        output_session_attributes = intent_request['sessionAttributes'] if intent_request[
                                                                               'sessionAttributes'] is not None else {}
        talk = TIMETABLE[when_slot]
        output_session_attributes['speaker'] = talk[
            'speaker']  # store for a follow-up with the 'Who is the speaker' intent.

        return delegate(output_session_attributes, get_slots(intent_request))

    logger.info('[what_is_on_now] All parameters are filled in, responding...')
    logger.info('[what_is_on_now] locals = {}'.format(locals()))

    talk = TIMETABLE[when_slot]
    response = '{title} by {speaker}'.format(**talk)

    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': response})


def about_talk(intent_request):
    logger.info(intent_request)

    source = intent_request['invocationSource']

    logger.info('[what_is_on_now] locals = {}'.format(locals()))

    slots = get_slots(intent_request)
    talk_slot = str(slots['talk'])

    # if source == 'DialogCodeHook':
    #     # Perform basic validation on the supplied input slots.
    #     # Use the elicitSlot dialog action to re-prompt for the first violation detected.
    #
    #     validation_result = validate_when(when_slot)
    #     if not validation_result['isValid']:
    #         slots[validation_result['violatedSlot']] = None
    #         return elicit_slot(intent_request['sessionAttributes'],
    #                            intent_request['currentIntent']['name'],
    #                            slots,
    #                            validation_result['violatedSlot'],
    #                            validation_result['message'])
    #
    #     output_session_attributes = intent_request['sessionAttributes'] if intent_request[
    #                                                                            'sessionAttributes'] is not None else {}
    #     talk = TIMETABLE[when_slot]
    #     output_session_attributes['speaker'] = talk[
    #         'speaker']  # store for a follow-up with the 'Who is the speaker' intent.
    #
    #     return delegate(output_session_attributes, get_slots(intent_request))
    #
    # logger.info('[what_is_on_now] All parameters are filled in, responding...')
    # logger.info('[what_is_on_now] locals = {}'.format(locals()))
    #
    talks = list(set([s for s in fetch_talks() if talk_slot.lower() in s.lower()]) | set(find_talks_by_tag(talk_slot.lower())))
    if len(talks) == 0:
        response = 'I\'m sorry, I couldn\'t find any talk that contains \'' + talk_slot + '\'. Please try again :)'
    elif len(talks) == 1:
        talk = TALKS[talks[0]]
        response = format_about_talk_message(talks[0], talk)
    else:
        response = 'I\'ve found ' + str(len(talks)) + ' talks matching your interest: \n\n'
        for t in talks:
            talk = TALKS[t]
            response += format_about_talk_message(t, talk) + '\n'
    print(response)
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': response})


def format_about_talk_message(talk_name, talk):
    return talk_name + ' belongs to the ' + talk['track'] + ' track and will be presented by ' + ' and '.join(talk['speakers']) + ' at ' + talk['location'] + ' on ' + talk['start'].strftime('%A %d of %B') + ' from ' + talk['start'].strftime('%H:%M') + ' to ' + talk['end'].strftime('%H:%M') + '.'


def who_is_the_speaker(intent_request):
    # source = intent_request['invocationSource']
    # logger.info('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # logger.info('[who_is_the_speaker] locals = {}'.format(locals()))
    #
    #slots = get_slots(intent_request)
    #speaker_slot = slots['speaker']
    #
    # if source == 'DialogCodeHook':
    #     output_session_attributes = intent_request['sessionAttributes'] if intent_request[
    #                                                                            'sessionAttributes'] is not None else {}
    #     speaker_from_context = output_session_attributes.get('speaker')
    #     current_slots = get_slots(intent_request)
    #     current_slots['speaker'] = speaker_from_context
    #     if speaker_slot is None and speaker_from_context is not None:
    #         logger.info('[who_is_the_speaker] got speaker {} from previous intent'.format(speaker_from_context))
    #     return delegate(output_session_attributes, current_slots)
    #
    # logger.info('[who_is_the_speaker] All parameters are filled in, responding...')
    # logger.info('[who_is_the_speaker] locals = {}'.format(locals()))

    response = 'lalalalal'
    return close_with_response_card(intent_request['sessionAttributes'],
                                    'Fulfilled',
                                    {'contentType': 'PlainText',
                                     'content': response}, 'hashf', 'nananan java ',
                                    'https://conf-assets.s3.eu-central-1.amazonaws.com/uploads/portraits/72/thumb.jpg')


def whats_the_schedule(intent_request):
    return close_with_response_card(intent_request['sessionAttributes'],
                                    'Fulfilled',
                                    {'contentType': 'PlainText',
                                     'content': 'resources/schedule_jun_13.jpg'}, 'hashf', 'nananan java ',
                                    'https://conf-assets.s3.eu-central-1.amazonaws.com/uploads/portraits/72/thumb.jpg')


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


def find_talks_by_tag(tag):
    response = []
    for talk in TALKS:
        if any(t == tag for t in TALKS[talk]['tags']):
            response.append(talk)
    return set(response)

""" --- Intents --- """


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug(
        'dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'WhatIsOnNow':
        return what_is_on_now(intent_request)
    elif intent_name == 'WhoIsTheSpeaker':
        return who_is_the_speaker(intent_request)
    elif intent_name == 'AboutTalk':
        return about_talk(intent_request)
    elif intent_name == 'WhatsTheSchedule':
        return whats_the_schedule(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    logger.debug('event = {}'.format(event))

    return dispatch(event)
