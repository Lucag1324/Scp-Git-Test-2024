import time
from apa102_pi.driver import apa102
 
def display_clock(seconds, minutes, hours):
    clock = [0x000000, 0x000000, 0x000000, 0x000000, 0x808080] * 12 # black, black, black, black, gray
    clock[14] = clock[29] = clock[44] = clock[59] = 0xFFFFFF # white
 
    if hours > 12:
        hours = hours-12
 
    clock[hours * 5] = 0xFF0000 # Red
    clock[minutes] = 0x0000FF # Blue
    clock[seconds] = 0x00FF00 # Green
 
    # Display the clock
    strip = apa102.APA102(num_led=60)
    # Turn off all pixels (sometimes a few light up when the strip gets power)
    strip.clear_strip()
 
    # Prepare a few individual pixels
   
    for i in range(len(clock)):
        strip.set_pixel_rgb(i + 1, clock[i])
       
    # Copy the buffer to the Strip (i.e. show the prepared pixels)
    strip.show()
   
 
while True:
    # Get current time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour
    
    # Display the clock
    display_clock(seconds, minutes, hours)
   
    # Wait for one second before updating again
    time.sleep(1)