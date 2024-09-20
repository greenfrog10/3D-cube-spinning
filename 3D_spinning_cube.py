from ursina import *                    
import random

app = Ursina()                          

window.borderless = False              
window.fullscreen = False               
window.exit_button.visible = False      
window.fps_counter.enabled = True

sky = Sky()
sky.color = color.rgb(0, 0, 0)

cube = Entity(model='cube', color=color.orange, scale=(4,4,4))

i = 0

def update():
    global i
    max_i = random.randint(10,30)  
    cube.rotation_y += 1  
    cube.rotation_z += 1  

    if i > max_i:
        cube.color = color.random_color()  
        i = 0  
    
    i += 1

# Run the application
app.run()
