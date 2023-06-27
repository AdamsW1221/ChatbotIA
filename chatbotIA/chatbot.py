import openai
from colorama import Fore
import sys, time

 
class inteligencia_artificial():
    def __init__(self, nombre):
        
        self.api_key = openai.api_key = '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'
        self.nombre = nombre
        self.conversacion = ''
        
    def configuracionIA(self):
        self.respuesta = openai.Completion.create(
            model='gpt-3.5-turbo',
            prompt= self.conversacion,
            temperature = 0.5,
            max_tokens = 60,
            top_p = 0.3,
            frequency_penalty = 0.5,
            presence_penalty = 0.0
        )
    
    def estilo_chat(self, estilo, color, cambios):
        cambiar_estilo = estilo, color + cambios 
        
        for recorrer in cambiar_estilo:
            sys.stdout.flush()
            print(recorrer, end='')
            time.sleep(0.001)
        
    
    def config_respuestas(self):
        while True:
            dialogo_humano = input(Fore.BLUE + f'{self.nombre}: ')
            self.conversacion += f'\n{self.nombre}: '+ dialogo_humano + '\n Athena:'
            self.configuracionIA()
            respuesta_IA = self.respuesta.choices[0].text.strip()
            self.conversacion +=respuesta_IA
            probando = Fore.MAGENTA+'Athena: '+Fore.GREEN + respuesta_IA +'\n'
            print(probando)

nombre = input('como te llamas?: ')

clase_IA = inteligencia_artificial(nombre)

clase_IA.config_respuestas()