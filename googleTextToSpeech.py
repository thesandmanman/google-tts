from gtts import gTTS
import subprocess

def text_to_audio(text):
    audio = gTTS(text)
    text = text.split()
    '''

     you can join the text with any symbol
     so that we can call it with subprocess module
     because subprocess can not call a file with space separarted name.

    '''
    a = '-'.join(text) 
    audio.save(a+'.mp3')
    subprocess.call('start {}.mp3'.format(a),shell=True)


text = input('Enter text = ')
text_to_audio(text)
