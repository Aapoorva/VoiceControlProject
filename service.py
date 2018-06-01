import subprocess as sp
import tts
import SpeechRego as sr

def Service(user_query):
    print('in service module')
    # service modes
    modes = ['stop','start','restart','status']
    # execute service command to get all services present
    proc = sp.Popen(['service','--status-all'], stdout=sp.PIPE, stderr=sp.PIPE)
    # get stdout and error if occured
    (out,err) = proc.communicate()
    # get list of services from stdout
    all_services = out.decode().replace(' [ - ] ','').replace('\n','').replace(' [ + ] ','').split(' ')
    #----------------------------------------------------------------------------------------------------------------------
    # for each service available
    for serv in all_services:
        # if apache is found in query
        if 'apache' in user_query:
            # for each mode in modes
            for mode in modes:
                # if mode is in query
                if mode in user_query:
                    proc  = sp.Popen(['service','apache2',mode],stdout=sp.PIPE,stderr=sp.PIPE)
                    if mode=='start' or mode=='restart':
                        tts.convert_text_n_speak('apache started')
                        return
                    elif mode=='stop':
                        tts.convert_text_n_speak('apache stopped')
                        return
                    else:
                        (out,err)=proc.communicate()
                        msg = out.decode().find('active (running)')
                        if msg>0:
                            tts.convert_text_n_speak('apache is active running now')
                            return
                        else:
                            tts.convert_text_n_speak("apache is inactive")
                            tts.convert_text_n_speak("do you wish to start the service")
                        reply = sr.get_audio_to_text()
                        if 'no' in reply:
                            return
                        else:
                            tts.convert_text_n_speak('apache service started')
                            proc  = sp.Popen(['service','apache2','start'],stdout=sp.PIPE,stderr=sp.PIPE)
                            return
                else:
                    pass
        elif 'telnet' in user_query:
            for mode in modes:
                if mode in user_query:
                    pass
        elif 'nfs' in user_query:
            for mode in modes:
                if mode in user_query:
                    pass
        elif serv in user_query:
            for mode in modes:
                if mode in user_query:
                    pass
        else:
            tts.convert_text_n_speak('Sorry, this service is not installed')
            return
