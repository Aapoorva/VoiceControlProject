# IMPORTS
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
    all_services.pop(0)

    #----------------------------------------------------------------------------------------------------------------------
    # for each service available
    for serv in all_services:

        #-----------------------------------------------------------------------------------------------------------------------------------
        # if apache is found in query
        if 'apache' in user_query:
            # for each mode in modes
            for mode in modes:
                # if mode is in query
                if mode in user_query:
                    # execute command in mode found
                    proc  = sp.Popen(['service','apache2',mode],stdout=sp.PIPE,stderr=sp.PIPE)
                    # for start and restart
                    if mode=='start' or mode=='restart':
                        tts.convert_text_n_speak('apache started')
                        return
                    # for stopping service
                    elif mode=='stop':
                        tts.convert_text_n_speak('apache stopped')
                        return
                    # for status of serice
                    else:
                        (out,err)=proc.communicate()
                        # get where is string active running
                        msg = out.decode().find('active (running)')
                        # if active runn is found speak
                        if msg>0:
                            tts.convert_text_n_speak('apache is active running now')
                            return
                        # if not found service inactive --> give option to start
                        else:
                            tts.convert_text_n_speak("apache is inactive")
                            tts.convert_text_n_speak("do you wish to start the service")
                        # get a reply
                        reply = sr.get_audio_to_text()
                        # if negative answer
                        if 'no' in reply:
                            return
                        # if affirmative
                        else:
                            tts.convert_text_n_speak('apache service started')
                            # start the service
                            proc  = sp.Popen(['service','apache2','start'],stdout=sp.PIPE,stderr=sp.PIPE)
                            return
                # if there isn't any mode in the query
                else:
                    pass

        #-------------------------------------------------------------------------------------------------------------------------------
        # FOR TELNET OR XIN
        # if telnet in user query
        elif 'telnet' in user_query:
            # for each mode in modes check if it is present in query
            for mode in modes:
                if mode in user_query:
                    # if mode found in query exceute the mode for that service i.e telnet
                    proc  = sp.Popen(['service','xinetd',mode],stdout=sp.PIPE,stderr=sp.PIPE)
                    if mode=='start' or mode=='restart':
                        tts.convert_text_n_speak('telnet started')
                        return
                        tts.convert_text_n_speak('telnet stopped')
                        return
                    else:
                        (out,err)=proc.communicate()
                        msg = out.decode().find('active (running)')
                        if msg>0:
                            tts.convert_text_n_speak('telnet is active running now')
                            return
                        else:
                            tts.convert_text_n_speak("telnet is inactive")
                            tts.convert_text_n_speak("do you wish to start the service")
                        reply = sr.get_audio_to_text()
                        if 'no' in reply:
                            return
                        else:
                            tts.convert_text_n_speak('telnet service started')
                            proc  = sp.Popen(['service','xinetd','start'],stdout=sp.PIPE,stderr=sp.PIPE)
                            return
                else:
                    pass
        #------------------------------------------------------------------------------------------------------------------------------
        elif 'nfs' in user_query:
            for mode in modes:
                if mode in user_query:
                    proc  = sp.Popen(['service','nfs-kernel-server',mode],stdout=sp.PIPE,stderr=sp.PIPE)
                    if mode=='start' or mode=='restart':
                        tts.convert_text_n_speak('nfs started')
                        return
                    elif mode=='stop':
                        tts.convert_text_n_speak('nfs stopped')
                        return
                    else:
                        (out,err)=proc.communicate()
                        msg = out.decode().find('active (running)')
                        if msg>0:
                            tts.convert_text_n_speak('nfs is active running now')
                            return
                        else:
                            tts.convert_text_n_speak("nfs is inactive")
                            tts.convert_text_n_speak("do you wish to start the service")
                        reply = sr.get_audio_to_text()
                        if 'no' in reply:
                            return
                        else:
                            tts.convert_text_n_speak('nfs service started')
                            proc  = sp.Popen(['service','nfs-kernel-server','start'],stdout=sp.PIPE,stderr=sp.PIPE)
                            return
                else:
                    pass

        #--------------------------------------------------------------------------------------------------------------------
        # a service is found in user query
        elif serv in user_query:
            # modes checked if t is in user query
            for mode in modes:
                if mode in user_query:
                     # apply mode on service
                    proc  = sp.Popen(['service',serv,mode],stdout=sp.PIPE,stderr=sp.PIPE)
                    # for strat and restart
                    if mode=='start' or mode=='restart':
                        tts.convert_text_n_speak(serv+' started')
                        return
                    # for stop
                    elif mode=='stop':
                        tts.convert_text_n_speak(serv+' stopped')
                        return
                    else:
                        # for status
                        (out,err)=proc.communicate()
                        # find if active running in result i.e out
                        msg = out.decode().find('active (running)')
                        # if active running found in out
                        if msg>0:
                            tts.convert_text_n_speak(serv+' is active running now')
                            return
                        # if not found, service is inactive
                        else:
                            tts.convert_text_n_speak(serv+" is inactive")
                            tts.convert_text_n_speak("do you wish to start the service")
                        # get answer if user wants to start service or not
                        reply = sr.get_audio_to_text()
                        if 'no' in reply:
                            return
                        else:
                            tts.convert_text_n_speak(serv+' service started')
                            proc  = sp.Popen(['service',serv,'start'],stdout=sp.PIPE,stderr=sp.PIPE)
                            return
                else:
                    pass
        # if service is not found in user query
        elif serv not in user_query:
            # if we have reached the last element of all_services and no match in user query
            if serv==all_services[-1]:
                # service not found
                tts.convert_text_n_speak('Sorry, this service is not installed')
                return
            # if we are not at the last element then continue    
            else:
                continue;
