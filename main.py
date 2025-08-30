import os
import pygame
import time

user_input = input("Type in quit: ")

song_path = os.path.join("Filepath to outro_song.mp3")

if user_input.lower() == "quit":
    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    shutdown_set = False

    while pygame.mixer.music.get_busy():
        song_position = int(pygame.mixer.music.get_pos() /1000)
        
        if song_position == 0 and not shutdown_set:
            os.system("shutdown /s /f /t 60")
            print("Music is playing")

            time.sleep(53.0)
            print("System will be shut down")
            time.sleep(1.0)
            print("5")
            time.sleep(1.0)
            print("4")
            time.sleep(1.0)
            print("3")
            time.sleep(1.0)
            print("2")
            time.sleep(1.0)
            print("1")
            time.sleep(1.0)
            print("Good bye!!!")

            os.system("taskkill /IM code.exe /F")
            os.system("taskkill /IM powershell.exe /F")
            os.system("taskkill /IM explorer.exe /F")
            os.system("taskkill /IM cmd.exe /F")
            break