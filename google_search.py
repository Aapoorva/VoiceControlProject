# imports
import webbrowser
import tts
import SpeechRego as sr

#------------------------------------------------------------------------------------
# search gogle function
def search_google(filtered_query):
    result = 0
    # keywords to remove
    remv_keywords = ['search','google','on','about','the','find','ok']
    # final list of words to be searched
    final_key=[]
    # append words other than remv_keywords to final_key
    for word in filtered_query:
        if word in remv_keywords:
            pass
        else:
            final_key.append(word)
    # if no keyword given ask for keyword
    if final_key == [] :
        tts.convert_text_n_speak("What should i search")
        user_input = sr.get_audio_to_text()
        user_input = user_input.lower().strip().split()
        result  = search_google(user_input)
    # to avoid ruuning 2 times
    if result == 0 :
        # string of search words
        search_words=str()
        for word in final_key:
            search_words = search_words + ' ' + word
        print('searching for '+search_words)
        webbrowser.open_new_tab('https://www.google.com/search?q='+search_words)
        tts.convert_text_n_speak("Search results ready")
        result = 1
        return result
