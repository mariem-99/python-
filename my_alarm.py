# Python alarm clock 
import time
import datetime
import pygame #if you don't have it do in the terminal pip insall pygame 

def set_alarm(alarm_time,sound_file,sound2_file):
    print(f"alarm set for {alarm_time}")
    is_running=True
    pygame.mixer.init() #initialize pygame mixer once 
    
    #start countdown music in a loop
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1) # loop indefinitely until alarm rings  
    
    
    while is_running:
        current_time= datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time) #or to just keep updating the time in same line do , end='\r'
        
        
        if current_time == alarm_time:
            print("\n⏰ WAKE UP!! ⏰")
            
            pygame.mixer.music.stop()#stop the countdown music  
            pygame.mixer.music.load(sound2_file)# load alarm music 
            pygame.mixer.music.play() #play alarm music 
            
            while pygame.mixer.music.get_busy():#wait until finishes 
                time.sleep(1)
                
                
                
            is_running = False #exit loop after alarm rings
            
            
            
        time.sleep(1) #check every second 
        
        
        
if __name__=='__main__':
    alarm_time= input("enter the alarm time (HH:MM:SS): ")
    
    sound_file="my_music.mp3"
    sound2_file="alarm.mp3"
    set_alarm(alarm_time,sound_file,sound2_file)
    