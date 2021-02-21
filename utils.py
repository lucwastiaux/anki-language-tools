import re
import logging
import aqt
import anki.template
import anki.sound
from . import constants

def get_green_stylesheet():
    night_mode = aqt.mw.pm.night_mode()
    if night_mode:
        return constants.GREEN_STYLESHEET_NIGHTMODE
    return constants.GREEN_STYLESHEET

def get_red_stylesheet():
    night_mode = aqt.mw.pm.night_mode()
    if night_mode:
        return constants.RED_STYLESHEET_NIGHTMODE
    return constants.RED_STYLESHEET

def play_anki_sound_tag(text):
    out = aqt.mw.col.backend.extract_av_tags(text=text, question_side=True)
    file_list = [
        x.filename
        for x in anki.template.av_tags_to_native(out.av_tags)
        if isinstance(x, anki.sound.SoundOrVideoTag)
    ]   
    if len(file_list) >= 1:
        filename = file_list[0]
        aqt.sound.av_player.play_file(filename)
