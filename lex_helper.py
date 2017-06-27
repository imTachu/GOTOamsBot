import botcontrol


def build_talks_slot():
    return build_enum_dictionary(botcontrol.fetch_talks() | botcontrol.fetch_tags())


def build_speakers_slot():
    return build_enum_dictionary(botcontrol.fetch_speakers())


def build_tracks_slot():
    return build_enum_dictionary(botcontrol.fetch_tracks())


def build_locations_slot():
    return build_enum_dictionary(botcontrol.fetch_locations())


def build_enum_dictionary(value_list):
    content = []
    for i in value_list:
        d = {unicode('value'): unicode(i)}
        content.append(d)
    return content
