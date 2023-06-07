import time 
def count_down(seconds):
    while seconds>0 :
     min = int(seconds/60)
     sec = int(seconds%60)
     timer = f'{min}:{sec}'
     print(timer, end='\r')
     time.sleep(1)
     seconds -= 1
    print('Time Up')
print('Choose 1 to enter time in minutes')
print('Choose 2 to enter time in seconds')   
option = int(input('1 or 2: '))
if(option == 1): 
   minutes = int(input('Enter the time in minutes: '))
   seconds = minutes*60
else:
   seconds = int(input('Enter the time in seconds: '))
count_down(int(seconds))    
