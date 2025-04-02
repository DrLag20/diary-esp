import speech_recognition as speech_recog

def speech():
    """
    Función que utiliza el micrófono para capturar audio y convertirlo a texto.
    """
    mic = speech_recog.Microphone()  # Crear una instancia del micrófono
    recog = speech_recog.Recognizer()  # Crear una instancia del reconocedor de voz

    with mic as audio_file:  # Usar el micrófono como fuente de audio
        recog.adjust_for_ambient_noise(audio_file)  # Ajustar para el ruido ambiental
        audio = recog.listen(audio_file)  # Escuchar y capturar el audio del micrófono
        return recog.recognize_google(audio, language="es-ES")  # Convertir el audio a texto usando Google Speech API
    
    