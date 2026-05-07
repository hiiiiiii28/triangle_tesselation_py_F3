import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""
    
    # Fill the background
    sg.fill_background("white")
    
    # make some variables available
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    
    triangle_height = height/5
    triangle_width = width / 3
    
    # Draw the tesselation
    # code for red triangles
    sg.set_fill_color(colors[0])
    
    for i in range(5):
        sg.fill_triangle(2*triangle_width, i*triangle_height, 3*triangle_width, i*triangle_height, 3*triangle_width, (i+1)*triangle_height) 
        
    
    # code for blue triangles
    
    
    # code for yellow triangles
   
   
    # code for green triangles
 
 
    # code for magenta triangles
    
    
    # code for cyan triangles
    
    
    

if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)