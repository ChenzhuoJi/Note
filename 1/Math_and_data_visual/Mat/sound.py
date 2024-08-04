import numpy as np 
import pygame,pygame.sndarray
'''arr=np.random.randint(-32634,32635,size=44100)

pygame.mixer.init(frequency=44100,size=-16,channels=1)
sound=pygame.sndarray.make_sound(arr)
sound.play()'''

pygame.mixer.init(frequency=44100,size=-16,channels=1)
form=np.repeat([10000,-10000],50)
arr=np.tile(form,441)
sound=pygame.sndarray.make_sound(arr)
sound.play()