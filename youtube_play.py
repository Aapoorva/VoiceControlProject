# Imports
import urllib.request
import urllib.parse
import re
import webbrowser
import tts
import SpeechRego as sr

# argument user_query from talkwork.py
def play_youtube(filtered_query):
    # split user_query to words
    video_keywords = filtered_query
    # final keywords to search
    final_key = []
    # keywords that won't be used for searching
    remv_keywords = ['youtube','from','of','for','video','play']

    # appending keyword to final_key list rejecting remv_keywords
    for word in video_keywords:
        if word in remv_keywords:
            pass
        else:
            final_key.append(word)

    #checking video name given or not
    if final_key == [] :
        tts.convert_text_n_speak("Which video you want to play")
        user_input = sr.get_audio_to_text()
        user_input = user_input.lower().strip().split()
        play_youtube(user_input)

    # making string of keywords to search
    search_words=str()
    for word in final_key:
        search_words = search_words + ' ' + word

    # search for a page and display
    query_string = urllib.parse.urlencode({"search_query" : search_words})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    # open link in tab webbrowser
    webbrowser.open_new_tab("http://www.youtube.com/watch?v=" + search_results[0])
    tts.convert_text_n_speak("Video Opened. Enjoy your video")
    # return