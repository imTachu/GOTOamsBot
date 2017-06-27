import lex_helper
import botcontrol


def test_build_talks_dict():
    assert len(lex_helper.build_talks_slot()) == len(botcontrol.fetch_talks()) + len(botcontrol.fetch_tags())


def test_build_speakers_dict():
    assert len(lex_helper.build_speakers_slot()) == len(botcontrol.fetch_speakers())


def test_build_tracks_dict():
    assert len(lex_helper.build_tracks_slot()) == len(botcontrol.fetch_tracks())


def test_build_locations_dict():
    assert len(lex_helper.build_locations_slot()) == len(botcontrol.fetch_locations())
