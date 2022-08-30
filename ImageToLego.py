from PIL import Image
import math
import turtle
import time

# colors from LEGO.com pick a brick
# last updated 7/9/2022
colors1 = [("BrightGreen", "4b9f4a"), 
("MediumAzur", "36AEBF"), #medium azure
("BrightReddishViolet", "923978"), #magenta
("DarkBrown", "352100"),
("BrightBluishGreen", "008F9B"), #dark turquoise 
("BrightBlue", "0055BF"), #blue
("MediumNougat", "AA7D55"),
("BrightYellow", "F2CD37"), #yellow
("BrightRed", "C91A09"),  #red
("BrickYellow", "E4CD9E"),  #tan
("White", "FFFFFF"), 
("Black", "05131D"), 
("EarthBlue", "0A3463"),  #dark blue
("CoolYellow", "FFF03A"),  #bright light yellow
("MediumBlue", "5A93DB"), 
("SpringYellowishGreen", "DFEEA5"),  #yelowish green
("LightPurple", "E4ADC8"),  #bright pink
("BrightYellowishGreen", "BBE90B"),  #lime
("SandBlue", "6074A1"), 
("SandYellow", "958A73"),  #dark tan
("DarkOrange", "A95500"), 
("DarkAzur", "078BC9"),  #dark azure
("LightRoyalBlue", "9FC3E9"),  #bright light blue
("FlameYellowishOrange", "F8BB3D"),  #bright light orange
("BrightPurple", "C870A0"),  #dark pink
("Lavender", "E1D5ED"), 
("Aqua", "B3D7D1"), 
("VibrantCoral", "FF698F"),  #coral
("SilverMetallic", "898788"),  #flat silver
("WarmGold", "AA7F2E"),  #pearl gold
("BrightOrange", "FE8A18"),  #orange
("LightNougat", "F6D7B3"), 
("DarkStoneGrey", "6C6E68"),  #dark bluish gray
("ReddishBrown", "582A12"),
("DarkRed", "720E0F"), 
("MediumStoneGrey", "A0A5A9")]  #light bluish gray

# colors from BrickLink.com
# last updated 7/9/2022
colors2 = [("Black", "05131D"),
("Blue", "0055BF"),
("BrightGreen", "4B9F4A"),
("BrightLightBlue", "9FC3E9"),
("BrightLightOrange", "F8BB3D"),
("BrightLightYellow", "FFF03A"),
("BrightPink", "E4ADC8"),
("Brown", "583927"),
("Coral", "FF698F"),
("DarkAzure", "078BC9"),
("DarkBlue", "0A3463"),
("DarkBluishGray", "6C6E68"),
("DarkBrown", "352100"),
("DarkGreen", "184632"),
("DarkOrange", "A95500"),
("DarkPink", "C870A0"),
("DarkRed", "720E0F"),
("DarkTan", "958A73"),
("DarkTurquoise", "008F9B"),
("Green", "237841"),
("Lavender", "E1D5ED"),
("LightAqua", "ADC3C0"),
("LightBluishGray", "A0A5A9"),
("LightGray", "9BA19D"),
("LightNougat", "F6D7B3"),
("LightPink", "FECCCF"),
("Lime", "BBE90B"),
("Magenta", "923978"),
("MediumAzure", "36AEBF"),
("MediumBlue", "5A93DB"),
("MediumLavender", "AC78BA"),
("MediumNougat", "AA7D55"),
("MediumOrange", "FFA70B"),
("NeonYellow", "EBD800"), # vibrant yellow
("Nougat", "D09168"),
("OliveGreen", "9B9A5A"),
("Orange", "FE8A18"),
("Pink", "FC97AC"),
("Red", "C91A09"),
("ReddishBrown", "582A12"),
("SandBlue", "6074A1"),
("Tan", "E4CD9E"),
("White", "FFFFFF"),
("Yellow", "F2CD37"),
("YellowishGreen", "DFEEA5"),
("TransBlack", "635F52"),
("TransBrightGreen", "D9E4A7"),
("TransClear", "FCFCFC"),
("TransDarkBlue", "0020A0"),
("TransDarkPink", "DF6695"),
("TransGreen", "84B68D"),
("TransLightBlue", "AEEFEC"),
("TransLightBrightGreen", "C9E788"),
("TransLightOrange", "FCB76D"), # trans flame yellowish orange
("TransNeonGreen", "F8F184"),
("TransNeonOrange", "FF800D"),
("TransNeonYellow", "DAB000"),
("TransOrange", "F08F1C"),
("TransPink", "E4ADC8"),
("TransPurple", "A5A5CB"),
("TransRed", "C91A09"),
("TransYellow", "F5CD2F"),
("ChromeSilver", "E0E0E0"),
("FlatDarkGold", "B48455"),
("FlatSilver", "898788"),
("PearlDarkGray", "575857"),
("PearlGold", "AA7F2E"),
("PearlLightGold", "DCBC81"),
("SatinTransBrightGreen", "84B68D"),
("SatinTransClear", "FCFCFC"), # trans clear opal
("SatinTransDarkBlue", "0020A0"), # trans dark blue opal
("SatinTransLightBlue", "68BCC5"), # trans blue opal
("MetallicGold", "DBAC34"),
("GlowInDarkOpaque", "D4D5C9"),
("GlowInDarkWhite", "D9D9D9"),
("GlitterTransClear", "FFFFFF"),
("GlitterTransDarkPink", "DF6695"),
("GlitterTransLightBlue", "68BCC5")]

colors = colors1


def HexToRGB(hexcode):
    """ converts hexcode to RGB """
    return tuple(int(str(hexcode[i:i+2]), 16) for i in (0, 2, 4)) #str() is used to ensure a string is passed to int() 


def RGBToHex(rgb):
    """ convert RGB to hexcode
    https://www.educative.io/answers/how-to-convert-hex-to-rgb-and-rgb-to-hex-in-python """

    return '#%02x%02x%02x' % rgb[:3]


def FindClosestColor(rgb):
    """ returns the tuple in list colors that represents the color closest to input color """
    #find values for first color in colors
    first_rgb = HexToRGB(colors[0][1])
    first_dist = GetColorDist(rgb, first_rgb)

    closest_dist = first_dist
    closest_color = colors[0]

    for i in range(1, len(colors)):
        loop_rgb = HexToRGB(colors[i][1])
        loop_dist = GetColorDist(rgb, loop_rgb)
        if loop_dist < closest_dist:
            closest_dist = loop_dist
            closest_color = colors[i]

    return closest_color



def GetColorDist(color1, color2):
    """ color1 and color2 are rgb tuples
    returns the distance between them
    https://stackoverflow.com/questions/1847092/given-an-rgb-value-what-would-be-the-best-way-to-find-the-closest-match-in-the-d\ """

    dist = ((color1[0]-color2[0])**2 + ((color1[1]-color2[1])**2) + ((color1[2]-color2[2])**2))

    return dist
    

def ImageToLego(length, image_name, conversion_type): 
    """ width is set by input
    length is made proportional by the program 
    returns a 2-D list representing the LEGO-fied image
    https://sighack.com/post/averaging-rgb-colors-the-right-way#:~:text=The%20typical%20approach%20to%20averaging,color%2C%20sum%20their%20squares%20instead."""    
    if conversion_type not in range(1, 4):
        conversion_type = 1
    image = Image.open(image_name, mode="r")
    pixels = image.load()
    col, row = image.size
    
    # width is height of the image (vertical dimension)
    width = row * (length / col)
    width = int(width)
    
    length_increment = col // length
    width_increment = row // width

    list_rep = [[None for x in range(length)] for y in range(width)]

    for y in range(width):
        for x in range(length):

            copy = image.crop((x*length_increment, y*width_increment, (x*length_increment) + length_increment, (y*width_increment) + width_increment))

            if conversion_type == 1:
                copy.resize((1, 1), resample=0)
                current_color = copy.getpixel((0, 0))
                if type(current_color) == int:
                    current_color = (255-current_color, 255-current_color, 255-current_color)

                list_rep[y][x] = FindClosestColor(current_color)


            if conversion_type == 2:
                current_color = FindDominantColor(copy)

                list_rep[y][x] = FindClosestColor(current_color)


            if conversion_type == 3:
                hexcode = FindDominantPre(copy)
                # list_rep[y][x] = (True, hexcode) # include True to keep output data type tuple and to keep hexcode at index 1; keeps consistency with other methods
                list_rep[y][x] = HexcodeToColor(hexcode)

    return list_rep


def findColor(color):
    for tuple_color in colors1:
        if tuple_color[0] == color:
            return tuple_color


def HexcodeToColor(hexcode):
    """ returns the tuple in global list colors that contains the string hexcode """
    for i in range(len(colors)):
        if colors[i][1] == hexcode:
            return colors[i]
    return None


def FindDominantPre(image):
    """ returns the most frequent color in image 
    each color/pixel in the image is converted to its LEGO equivalent
    the most frequent of the LEGO colors is returned """
    unique_colors = [x[1] for x in colors]
    counts = [0 for i in range(36)]

    col, row = image.size

    for y in range(row):
        for x in range(col):
            current_color = image.getpixel((x, y))
            if type(current_color) == int:
                current_color = (255-current_color, 255-current_color, 255-current_color)
            lego_color = FindClosestColor(current_color)[1]

            index = FindIndex(lego_color, unique_colors)
            counts[index] += 1
    max_count = max(counts)
    max_index = FindIndex(max_count, counts)
    return unique_colors[max_index]



def FindDominantColor(image):
    """ returns the most frequent actual color in image 
    the color is then converted to its LEGO equivalent in ImageToLego() """
    unique_colors = UniqueColors(image)

    counts = [0 for i in range(len(unique_colors))]

    col, row = image.size
    for y in range(row):
        for x in range(col):
            current_color = image.getpixel((x, y))
            if type(current_color) == int:
                current_color = (255-current_color, 255-current_color, 255-current_color)
            index = FindIndex(current_color, unique_colors)
            counts[index] += 1

    max_count = max(counts)
    max_index = FindIndex(max_count, counts)

    max_color = unique_colors[max_index]

    return max_color


def UniqueColors(image):
    """ returns a list of all unique colors that appear in image """
    col, row = image.size
    num = 0
    colors = []
    for y in range(row):
        for x in range(col):
            current_color = image.getpixel((x, y))
            if current_color not in colors:
                num += 1
                if type(current_color) == int:
                    current_color = (255-current_color, 255-current_color, 255-current_color)
                colors += [current_color]
    return colors

def FindIndex(to_find, list_in):
    """ returns the first index where to_find appears in list_in 
    returns -1 if the object is not found """
    for i in range(len(list_in)):
        if list_in[i] == to_find:
            return i
    if type(to_find) == str:
        print('str not found')
    if type(to_find) == int:
        print('int not found')
    if type(to_find) == tuple:
        print('tuple not found')
    return -1


def ShowLegofied(list_rep):
    """ creates a turtle Screen and shows the input LEGO-fied image """
    scr = turtle.Screen()
    scr.title("Legofied Image")
    scr.tracer(0)
    scr.bgcolor("black")
    # this 10 means each stud is 10 pixels in diameter. that is the default size of a circle created by turtle
    w = len(list_rep[0])
    h = len(list_rep)
    scr.setup(width=(w) * 10 + w * 2, height=h * 10 + h * 2) 

    print('dimensions in studs')
    print('length:', str(len(list_rep[0])))
    print('height:', str(len(list_rep)))

    GetNumPieces(list_rep)

    stud = turtle.Turtle()
    stud.speed(0)
    stud.penup()
    stud.shape("circle")
    stud.shapesize(0.5)

    x = -(len(list_rep[0]) * 10 + len(list_rep[0]))//2 + 2
    y = (len(list_rep) * 10 + len(list_rep))//2 - 2
    stud.goto(x - 11, y)

    for i in range(len(list_rep)):
        for j in range(len(list_rep[0])):
            stud.goto(stud.xcor() + 11, stud.ycor())
            stud.color("#" + list_rep[i][j][1])
            stud.stamp()

        stud.goto(x - 11, stud.ycor() - 11)
    stud.hideturtle()
    turtle.done()
              
              
def GetNumPieces(list_rep):
    """ prints each unique color in the LEGO-fied image and the frequency of that piece """
    # find number of different colors
    num_colors = 0
    different_colors = []
    for i in range(len(list_rep)):
        for j in range(len(list_rep[0])):
            current_color = list_rep[i][j]
            if current_color not in different_colors:
                num_colors += 1
                different_colors += [current_color]
    # get totals of each color
    num_each = [0 for x in range(num_colors)]
    for index in range(len(different_colors)):
        for i in range(len(list_rep)):
            for j in range(len(list_rep[0])):
                if different_colors[index] == list_rep[i][j]:
                    num_each[index] += 1
    # print totals
    print('total number of colors:', str(num_colors))
    for i in range(num_colors):
        print(str(different_colors[i]), str(num_each[i]))


def ShowAllColors(colors):
    """ creates a turtle Screen and displays all LEGO colors for a 1x1 round tile """
    screen = turtle.Screen()
    screen.setup(400, 800)
    screen.tracer(0)
    screen.title("all colors")

    block = turtle.Turtle()
    block.speed(0)
    block.shape("square")
    block.shapesize(2)
    block.penup()
    block.goto(-180, 360)

    for i in range(len(colors)):
        block.goto(block.xcor() + 45, block.ycor())
        block.color("#" + colors[i][1])
        block.stamp()
        
        if (i + 1) % 6 == 0:
            block.goto(-180, block.ycor() - 45)
    block.hideturtle()
    screen.update()
    turtle.done()


def main():
    """ how the general user will interact with this code """
    image_name = input("filepath or file name: ")

    length = input("desired length of output in studs: ")
    while length.isnumeric() == False:
            length = input("desired width of output in studs: ")
    length = int(length)

    conversion_type = input("desired processing type: ")
    while conversion_type not in ['1', '2', '3']:
        conversion_type = input("desired processing type: ")
    conversion_type = int(conversion_type)

    colors_from = input("use colors from LEGO or BrickLink? ")
    while colors_from.lower() not in ['lego', 'bricklink', 'l', 'b']:
        colors_from = input("use colors from LEGO or BrickLink? ")

    if colors_from.lower() in ['lego', 'l']:
        colors = colors1
    else:
        colors = colors2

    try:
        start = time.time()
        legofied_image = ImageToLego(length, image_name, conversion_type)
        end = time.time()
        print('time to convert:', str(end - start))

        ShowLegofied(legofied_image)
    except Exception as e:
        print("an error occurred")
        print(e)



main()

# ShowAllColors(colors1)
# ShowAllColors(colors2)