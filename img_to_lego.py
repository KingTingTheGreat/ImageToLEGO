from PIL import Image
# import math
import turtle
from time import perf_counter
from ImageToLego import ShowLegofied

# colors from LEGO.com
# last updated 7/9/2022
LEGO = {
    "#4b9f4a": "BrightGreen",
    "#36AEBF": "MediumAzur",  # medium azure
    "#923978": "BrightReddishViolet",  # magenta
    "#352100": "DarkBrown",
    "#008F9B": "BrightBluishGreen",  # dark turquoise
    "#0055BF": "BrightBlue",  # blue
    "#AA7D55": "MediumNougat",
    "#F2CD37": "BrightYellow",  # yellow
    "#C91A09": "BrightRed",  # red
    "#E4CD9E": "BrickYellow",  # tan
    "#FFFFFF": "White",
    "#05131D": "Black",
    "#0A3463": "EarthBlue",  # dark blue
    "#FFF03A": "CoolYellow",  # bright light yellow
    "#5A93DB": "MediumBlue",
    "#DFEEA5": "SpringYellowishGreen",  # yelowish green
    "#E4ADC8": "LightPurple",  # bright pink
    "#BBE90B": "BrightYellowishGreen",  # lime
    "#6074A1": "SandBlue",
    "#958A73": "SandYellow",  # dark tan
    "#A95500": "DarkOrange",
    "#078BC9": "DarkAzur",  # dark azure
    "#9FC3E9": "LightRoyalBlue",  # bright light blue
    "#F8BB3D": "FlameYellowishOrange",  # bright light orange
    "#C870A0": "BrightPurple",  # dark pink
    "#E1D5ED": "Lavender",
    "#B3D7D1": "Aqua",
    "#FF698F": "VibrantCoral",  # coral
    "#898788": "SilverMetallic",  # flat silver
    "#AA7F2E": "WarmGold",  # pearl gold
    "#FE8A18": "BrightOrange",  # orange
    "#F6D7B3": "LightNougat",
    "#6C6E68": "DarkStoneGrey",  # dark bluish gray
    "#582A12": "ReddishBrown",
    "#720E0F": "DarkRed",
    "#A0A5A9": "MediumStoneGrey",  # light bluish gray
}

# colors from BrickLink.com
# last updated 7/9/2022
BRICKLINK = {
    "#05131D": "Black",
    "#0055BF": "Blue",
    "#4B9F4A": "BrightGreen",
    "#9FC3E9": "BrightLightBlue",
    "#F8BB3D": "BrightLightOrange",
    "#FFF03A": "BrightLightYellow",
    "#E4ADC8": "BrightPink",
    "#583927": "Brown",
    "#FF698F": "Coral",
    "#078BC9": "DarkAzure",
    "#0A3463": "DarkBlue",
    "#6C6E68": "DarkBluishGray",
    "#352100": "DarkBrown",
    "#184632": "DarkGreen",
    "#A95500": "DarkOrange",
    "#C870A0": "DarkPink",
    "#720E0F": "DarkRed",
    "#958A73": "DarkTan",
    "#008F9B": "DarkTurquoise",
    "#237841": "Green",
    "#E1D5ED": "Lavender",
    "#ADC3C0": "LightAqua",
    "#A0A5A9": "LightBluishGray",
    "#9BA19D": "LightGray",
    "#F6D7B3": "LightNougat",
    "#FECCCF": "LightPink",
    "#BBE90B": "Lime",
    "#923978": "Magenta",
    "#36AEBF": "MediumAzure",
    "#5A93DB": "MediumBlue",
    "#AC78BA": "MediumLavender",
    "#AA7D55": "MediumNougat",
    "#FFA70B": "MediumOrange",
    "#EBD800": "NeonYellow",  # vibrant yellow
    "#D09168": "Nougat",
    "#9B9A5A": "OliveGreen",
    "#FE8A18": "Orange",
    "#FC97AC": "Pink",
    "#C91A09": "Red",
    "#582A12": "ReddishBrown",
    "#6074A1": "SandBlue",
    "#E4CD9E": "Tan",
    "#FFFFFF": "White",
    "#F2CD37": "Yellow",
    "#DFEEA5": "YellowishGreen",
    "#635F52": "TransBlack",
    "#D9E4A7": "TransBrightGreen",
    "#FCFCFC": "TransClear",
    "#0020A0": "TransDarkBlue",
    "#DF6695": "TransDarkPink",
    "#84B68D": "TransGreen", 
    "#AEEFEC": "TransLightBlue",
    "#C9E788": "TransLightBrightGreen",
    "#FCB76D": "TransLightOrange",  # trans flame yellowish orange
    "#F8F184": "TransNeonGreen",
    "#FF800D": "TransNeonOrange",
    "#DAB000": "TransNeonYellow",
    "#F08F1C": "TransOrange",
    "#E4ADC8": "TransPink",
    "#A5A5CB": "TransPurple",
    "#C91A09": "TransRed",
    "#F5CD2F": "TransYellow",
    "#E0E0E0": "ChromeSilver",
    "#B48455": "FlatDarkGold",
    "#898788": "FlatSilver",
    "#575857": "PearlDarkGray",
    "#AA7F2E": "PearlGold",
    "#DCBC81": "PearlLightGold",
    "#84B68D":"SatinTransBrightGreen",
    "#FCFCFC": "SatinTransClear",  # trans clear opal
    "#0020A0": "SatinTransDarkBlue",  # trans dark blue opal
    "#68BCC5": "SatinTransLightBlue",  # trans blue opal
    "#DBAC34": "MetallicGold",
    "#D4D5C9": "GlowInDarkOpaque",
    "#D9D9D9": "GlowInDarkWhite", 
    "#FFFFFF": "GlitterTransClear", 
    "#DF6695": "GlitterTransDarkPink", 
    "#68BCC5": "GlitterTransLightBlue", 
}


def hex_to_rgb(hexcode):
    hexcode = hexcode.strip("#")
    return tuple(
        int(str(hexcode[i: i + 2]), 16) for i in (0, 2, 4)
    )  # str() is used to ensure a string is passed to int()


def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb[:3]


def color_distance(rgb1, rgb2):
    r_dist = (rgb1[0] - rgb2[0]) * (rgb1[0] - rgb2[0])
    g_dist = (rgb1[1] - rgb2[1]) * (rgb1[1] - rgb2[1])
    b_dist = (rgb1[2] - rgb2[2]) * (rgb1[2] - rgb2[2])
    return r_dist + g_dist + b_dist


def closest_color(rgb, colors):
    closest_dist = 20_000  # all distances will be less than this
    closest_color = "#FFFFFF"  # white is set to default; this will be replaced because of dist

    for hexcode in colors:
        current_rgb = hex_to_rgb(hexcode)
        current_dist = color_distance(rgb, current_rgb)
        if current_dist < closest_dist:
            closest_dist = current_dist
            closest_color = hexcode

    return closest_color


def single_pix(copy):
    copy.resize((1, 1), resample=0)
    rgb = copy.getpixel((0, 0))
    if type(rgb) == int:
        return (255 - rgb, 255 - rgb, 255 - rgb)
    return rgb


def dominant_color_post(copy):
    unique_colors_img = {}
    col, row = copy.size
    for r in range(row):
        for c in range(col):
            rgb = copy.getpixel((c, r))
            if type(rgb) == int:
                rgb = (255-rgb, 255-rgb, 255-rgb)
            if rgb in unique_colors_img:
                unique_colors_img[rgb] += 1
            else:
                unique_colors_img[rgb] = 1
    return max(unique_colors_img, key=unique_colors_img.get)    


def dominant_color_pre(copy, colors):
    unique_colors_lego = {}
    col, row = copy.size
    for r in range(row):
        for c in range(col):
            rgb = copy.getpixel((c, r))
            if type(rgb) == int:
                rgb = (255-rgb, 255-rgb, 255-rgb)
            lego_color = closest_color(rgb, colors)
            if lego_color in unique_colors_lego:
                unique_colors_lego[lego_color] += 1
            else:
                unique_colors_lego[lego_color] = 1
    return max(unique_colors_lego, key=unique_colors_lego.get)


def print_pieces(legofied, colors):
    unique_colors = {}
    for r_index, row in enumerate(legofied):
        for c_index, color in enumerate(row):
            if color in unique_colors:
                unique_colors[color] += 1
            else:
                unique_colors[color] = 1
    print(f"total number of colors: {len(unique_colors)}")
    for color in unique_colors:
        print(f"{colors[color]}: {unique_colors[color]}")


def create_legofied(length, image_name, conversion_type, colors):
    if conversion_type not in range(1, 4):
        conversion_type = 1

    image = Image.open(image_name, mode="r")
    pixels = image.load()
    col, row = image.size

    # width is the vertical dimension
    width = row * (length / col)
    width = int(width)

    l_inc = col // length
    w_inc = row // width

    legofied = [[None for x in range(length)] for y in range(width)]

    for r in range(width):
        if r % 5 == 0:
            print(f"{(r/width) * 100}% done")
        for c in range(length):
            
            copy = image.crop((c*l_inc, r*w_inc, (c*l_inc) + l_inc, (r*w_inc) + w_inc))

            if conversion_type == 3:
                lego_hex = dominant_color_pre(copy, colors)
                legofied[r][c] = lego_hex
            else:
                if conversion_type == 1:
                    current_rgb = single_pix(copy)
                elif conversion_type == 2:
                    current_rgb = dominant_color_post(copy)
                legofied[r][c] = closest_color(current_rgb, colors)

    return legofied


def show_legofied(legofied, colors):
    scr = turtle.Screen()
    scr.title("Legofied Image")
    scr.tracer(0)
    scr.bgcolor("black")

    w = len(legofied[0])
    h = len(legofied)
    scr.setup(width=(w)*10 + w*2, height=h*10 + h*2)

    print("dims in studs")
    print(f"length: {str(w)}, height: {str(h)}")

    print_pieces(legofied, colors)

    stud = turtle.Turtle()
    stud.speed(0)
    stud.penup()
    stud.shape("circle")
    stud.shapesize(0.5)

    x = -(w*10 + w)//2 + 2
    y = (h*10 + h)//2 - 2
    stud.goto(x-11, y)

    for i in range(h):
        for j in range(w):
            stud.goto(stud.xcor()+11, stud.ycor())
            # print(i, j)
            stud.color(legofied[i][j])
            stud.stamp()
        stud.goto(x-11, stud.ycor()-11)
    stud.hideturtle()
    turtle.done()


def save_to_file(legofied, filename_no_txt, use_lego):
    filename = filename_no_txt
    open(filename, 'w').close() # erase previous contents

    with open(filename, 'w') as f:
        for index_r, row in enumerate(legofied):
            for index_c, color in enumerate(row):
                f.write(f"{color}")
                if index_c != len(row) - 1:
                    f.write(',')
            if row != len(legofied) - 1:
                f.write('\n')
        if use_lego:
            f.write('l')
        else:
            f.write('b')


def load_from_file(filename):
    legofied = []
    use_lego = True
    with open(filename, 'r') as f:
        for line in f:
            if len(line) != 1:
                line = line.strip().split(',')
                legofied.append(line)
            else:
                use_lego = line.lower() == 'l'
    return (legofied, use_lego)


def get_legofied_inputs():
    length = input("length of output in studs: ")
    while length.isnumeric() == False:
            length = input("length of output in studs: ")
    length = int(length)

    conversion_type = input("processing type: ")
    while conversion_type not in ['1', '2', '3']:
        conversion_type = input("processing type: ")
    conversion_type = int(conversion_type)

    colors_from = input("use colors from LEGO or BrickLink? ").lower()
    while colors_from not in ['lego', 'bricklink', 'l', 'b']:
        colors_from = input("use colors from LEGO or BrickLink? ").lower()

    return (length, conversion_type, colors_from in ['lego', 'l'])


def main():
    """ how the user will interact with this code """
    input_file = input("filepath or file name: ")

    if input_file.endswith(".txt"):
        try:
            legofied, use_lego = load_from_file(input_file)
            colors = LEGO
            if not use_lego:
                colors = BRICKLINK
            show_legofied(legofied, colors)
        except Exception as e:
            print("an error occurred")
            print(e)

    else:
        length, conversion_type, use_lego = get_legofied_inputs()
        colors = LEGO
        if not use_lego:
            colors = BRICKLINK

        try:
            s = perf_counter()
            legofied = create_legofied(length, input_file, conversion_type, colors)
            e = perf_counter()
            print(f"time to complete: {e - s} seconds")

            save_name = input_file.split('.')[0] + str(conversion_type) + '.txt'
            save_to_file(legofied, save_name, use_lego)
            show_legofied(legofied, colors)
        except Exception as e:
            print("an error occurred")
            print(e)


if __name__ == "__main__":
    main()