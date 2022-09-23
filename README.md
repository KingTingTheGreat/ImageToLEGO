# PNGtoLEGO
takes an input .png file and displays it as a "legofied" image. this means it's pixelated to use LEGO studs and only uses colors that LEGO studs are made in.

uses the PIL Image module to open images
uses the turtle library to display the "legofied" image

Explanation of the processing types:
all of the processing types divide the image into appropriately sized pieces depending on the resolution of the image and the desired/inputted dimensions.
Type 1: crops each piece to a single pixel(the top left pixel) then matches that color the its closest LEGO counterpart
Type2: for each piece, it goes through all the pixels and finds the most commonly occuring color. the piece is assigned the most common color's closest LEGO counterpart
Type 3: for each piece, it goes through all the pixels and finds each pixels' closest LEGO counterpart. the piece is assigned the most commong LEGO counterpart

Mustafar.io is a file that can be opened in the Studio 2.0 application and shows the "legofied" image of mustafar.png uses Type 3 processing. Studio 2.0 is used to create LEGO models and can easily be exported to BrickLink to purchase pieces.
Studio 2.0 can be downloaded from BrickLink here: https://www.bricklink.com/v3/studio/download.page 
