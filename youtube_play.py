import urllib.request
import urllib.parse
import re
import webbrowser

def play_youtube(user_query):
    video_keywords = user_query.split(' ')
    final_key = []
    remv_keywords = ['Youtube','youtube','from','of','for','video','play','Play','Video','For','Of']
    for word in video_keywords:
        if word.lower() in remv_keywords:
            pass
        else:
            final_key.append(word)
    search_words=str()
    for word in final_key:
        search_words = search_words + ' ' + word
    query_string = urllib.parse.urlencode({"search_query" : search_words})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    webbrowser.open_new_tab("http://www.youtube.com/watch?v=" + search_results[0])
    return
