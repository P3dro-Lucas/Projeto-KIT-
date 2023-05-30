import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit as pyw
import subprocess as sb

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'kit' in comando:
                comando = comando.replace('kit', ' ')
                #maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está ok')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()

    elif 'procure por' in comando:
        procurar = comando.replace('procure por', ' ')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'toque' in comando:
        musica = comando.replace('toque',' ')
        resultado = pyw.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()

    elif 'busque' in comando:
        busca = comando.replace('busque por', '')
        resultado = pyw.search(busca)
        maquina.say('Aguarde')
        maquina.runAndWait()#####

    elif 'bloco de notas' in comando:
        programa = 'Notepads.exe'
        arquivo = 'file.txt'
        sb.Popen([programa, arquivo])

    else:
        maquina.say("Comando não existe ou repita-o")
        comando_voz_usuario()