"""
Valentine Greeting Card
Snovi Patel
"""
from graphics import * #Importing from graphics library 
 
    
def valentine():
    #A window with title "Valentine Greeting Card"
    width = 500 # Width of the window
    height = 500 # Height of the window
    win = GraphWin("Valentine Greeting Card", width, height)
    win.setBackground("blue")# Background color to blue 
    
    # A heading in the window that says "Happy Valentine's Day"
    headingPt = Point(width/2, height/5)  
    heading = Text(headingPt, "Happy Valentine's Day")
    heading.setSize(24) # Text size
    heading.setStyle("bold") # Font 
    heading.setFill("white") # Text color 
    heading.draw(win)
    
    # A yellow-colored smiley face using a circle 
    face_right = Circle(Point(435, 56), 35)
    face_right.setOutline("yellow")
    face_right.setFill("yellow")
    face_right.draw(win)
    
    # A red-colored heart-shaped left eye of the face  
    left_eye1 = Polygon(Point(423.0, 45.0),Point(427.0, 41.0),Point(431.0, 41.0),
                        Point(431.0, 46.0),Point(427.0, 51.0),Point(423.0, 55.0),
                        Point(419.0, 53.0),Point(416.0, 50.0),Point(415.0, 45.0),
                        Point(418.0, 42.0),Point(421.0, 43.0))
    left_eye1.setOutline("red")
    left_eye1.setFill("red")
    left_eye1.draw(win)
    
    # Clone to create the right eye of the face 
    right_eye1 = left_eye1.clone()
    right_eye1.move(23, -1)  
    right_eye1.draw(win)

    # Mouth of the face (white color)
    mouth1 = Polygon(Point(422.0, 71.0),Point(425.0, 74.0),
                    Point(429.0, 76.0),Point(434.0, 77.0),
                    Point(439.0, 76.0),Point(444.0, 73.0),
                    Point(445.0, 70.0))
    mouth1.setFill("white")
    mouth1.draw(win)
   
    # Clone to create another yellow color face to the left of the window
    face_left = face_right.clone()  # Duplicating the first face  
    face_left.move(-365, 0)  # Moving the clone to the left  
    face_left.draw(win)  # Drawing the second face 

    # Cloning and moving the left eye for the second face 
    left_eye2 = left_eye1.clone()
    left_eye2.move(-365,0) # Moving it to align with the second face
    left_eye2.draw(win)
    
    # Cloning and moving the right eye for the second face 
    right_eye2 = right_eye1.clone()
    right_eye2.move(-365,0)
    right_eye2.draw(win)
    
    # Cloning and moving the mouth for the second face  
    mouth2= mouth1.clone()
    mouth2.move(-365,0)
    mouth2.draw(win)
    
    # A red heart using polygon
    heart = Polygon(Point(247.0, 198.0),Point(284.0, 160.0),Point(327.0, 143.0),Point(369.0, 153.0),
                    Point(395.0, 186.0),Point(399.0, 238.0),Point(380.0, 285.0),Point(345.0, 335.0),
                    Point(303.0, 378.0),Point(261.0, 411.0),Point(218.0, 385.0),Point(180.0, 351.0),
                    Point(147.0, 319.0),Point(114.0, 268.0),Point(101.0, 218.0),Point(118.0, 175.0),
                    Point(158.0, 160.0),Point(193.0, 166.0),Point(219.0, 181.0))
    
    heart.setOutline("red")
    heart.draw(win)
    
    # Making the heart change color between pink and red
    for i in range(5): # looping 5 times
        heart.setFill("pink")
        time.sleep(0.5) # pause before changing to another color
        heart.setFill("red")
        time.sleep(0.5)
    
    # Arrow body using line
    arrow_body = Line(Point(43, 439), Point(102, 395))
    arrow_body.setWidth(4) # thickness to 4
    arrow_body.draw(win)
    
    # Left part of arrowhead
    arrow_left = Line(Point(102, 395), Point(86, 394))
    arrow_left.setWidth(4) # thickness to 4
    arrow_left.draw(win)
    
    # Right part of arrowhead
    arrow_right = Line(Point(102, 395), Point(101, 412))
    arrow_right.setWidth(4) # thickness to 4
    arrow_right.draw(win)

    # Loop to move arrow diagonally upward
    for i in range(75): # 75 times
        arrow_left.move(2, -2)  # Moving the left arrowhead up and right  
        arrow_right.move(2, -2)  # Moving the right arrowhead up and right  
        arrow_body.move(2, -2)  # Moving the main arrow body up and right  
        time.sleep(0.01)  # Adding a small delay for smooth movement
    
    # Display a message saying "i love you"
    msg = Text(Point(250,250), "I LOVE YOU!")
    msg.setFill("white")
    msg.draw(win)
    
    # Balloon 1 to the bottom left of the window
    balloon1 = Oval(Point(40.0,337.0),Point(67.0,384.0))
    balloon1.setFill("orange") # orange color
    balloon1.setOutline("black")
    balloon1.draw(win)
    
    #String of balloon 1
    string1 = Line(Point(52.0,385.0),Point(50.0,448.0))
    string1.setWidth(2)
    string1.draw(win)
    
    # Clone to create balloon 2 to the bottom right of the window
    balloon2 = balloon1.clone()
    balloon2.move(400,0)
    balloon2.draw(win)
    balloon2.setFill("green") # color green
    
    #String of balloon 2
    string2 = string1.clone() # using clone
    string2.move(400,0)
    string2.draw(win)
    
    #Clone to create balloon 3 to the top right of the window
    balloon3 = balloon2.clone()
    balloon3.move(0,-200)
    balloon3.draw(win)
    balloon3.setFill("pink") # color pink
    
    #String of balloon 3
    string3 = string2.clone()
    string3.move(0,-200)
    string3.draw(win)
    
    # Clone to create balloon 4 to the top left of the window
    balloon4 = balloon3.clone()
    balloon4.move(-400,0)
    balloon4.draw(win)
    balloon4.setFill("red") #color red
    
    # String of balloon 4
    string4 = string3.clone()
    string4.move(-400,0)
    string4.draw(win)
    
    # Clone to create balloon 5 to the middle of the window
    balloon5 = balloon1. clone()
    balloon5.move(200,-50)
    balloon5.draw(win)
    balloon5.setFill("light blue") # light blue color
    
    #String of balloon 5
    string5 = string1.clone()
    string5.move(200, -50)
    string5.draw(win)
    
    #Loop to move all balloons upward
    for i in range(57):
        balloon1.move(0,-8)
        string1.move(0,-8)
        balloon2.move(0,-8)
        string2.move(0,-8)
        balloon3.move(0,-6)
        string3.move(0,-6)
        balloon4.move(0,-6)
        string4.move(0,-6)
        balloon5.move(0,-8)
        string5.move(0,-8)
        
 
    #a message instructing the user to close the window 
    instPt = Point(width/2, height-10)
    inst = Text(instPt,"Click anywhere to close")
    inst.setFill("white")
    inst.draw(win)
    
    # Waiting for the user to click before closing the window
    click = win.getMouse()  
    win.close()
    
valentine()

