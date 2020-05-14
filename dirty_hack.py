import sys

sys.path.extend([u'C:\\Users\\user\\Anaconda3\\python.exe',
'C:\\Users\\user\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe'])

import argparse
import cairo
import math
import numpy as np

with open("C:/Users/user/AppData/Roaming/inkscape/extensions/log.txt", "a") as out:
    out.write("dirty_hack opened\n")

#dna.py
def draw_dna(width, coils, color1, color2, line_width):
    height = width * 1.3 / 2

    r1, r2 = color1[0]/255, color2[0]/255
    g1, g2 = color1[1]/255, color2[1]/255
    b1, b2 = color1[2]/255, color2[2]/255
    opac1, opac2 = color1[3] / 255, color2[3] / 255

    sur_width = width + 100
    sur_height = 49/20 * height * coils + 100

    with cairo.SVGSurface("dna.svg",  sur_height, sur_width) as surface:
        context = cairo.Context(surface)
        x3 = 50 + height*9/20
        while coils>0:
            x0, y0 = x3, width/2
            x1, y1 = x0 + height*2/5, y0 - width/2
            x2, y2 = x0 + height*3/5, y0 - width/2
            x3, y3 = x0 + height, y0
            context.set_source_rgb(r1, g1, b1)
            context.set_line_width(line_width)
            context.move_to(x0, y0)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()

            context.set_source_rgb(r2, g2, b2)
            x0 = x0 - height*9/20
            x1, y1 = x0 + height*2/5, y0 - width/2
            x2, y2 = x0 + height*3/5, y0 - width/2
            x3, y3 = x0 + height, y0
            context.move_to(x0, y0)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()

            x0 = x3
            x1, y1 = x0 + height*2/5, y0 + width/2
            x2, y2 = x0 + height*3/5, y0 + width/2
            x3, y3 = x0 + height, y0
            context.move_to(x0, y0)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()

            context.set_source_rgb(r1, g1, b1)
            x0 = x0 + height*9/20
            x1, y1 = x0 + height*2/5, y0 + width/2
            x2, y2 = x0 + height*3/5, y0 + width/2
            x3, y3 = x0 + height, y0
            context.move_to(x0, y0)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()

            coils = coils - 1


#rectangle?
def draw_protein(width, height, line_width, line_color, fill_color):
    fill_r, line_r = fill_color[0] / 255, line_color[0] / 255
    fill_g, line_g = fill_color[1] / 255, line_color[1] / 255
    fill_b, line_b = fill_color[2] / 255, line_color[2] / 255
    fill_a, line_a = fill_color[3] / 255, line_color[3] / 255

    with cairo.SVGSurface("protein.svg", 4*line_width+width, 4*line_width+height) as surface:
        context = cairo.Context(surface)
        context.set_source_rgba(fill_r, fill_g, fill_b, fill_a)
        context.rectangle(line_width, line_width, line_width+width, line_width+height)
        context.fill_preserve()
        context.set_line_width(line_width)
        context.set_line_join(cairo.LINE_JOIN_ROUND)
        context.set_source_rgba(line_r,line_g, line_b, line_a)
        context.stroke()

#plasmid_bb.py
def draw_plasmid_fraction(r_type, r_share, r_width, fill_color):
    with open("C:/Users/user/AppData/Roaming/inkscape/extensions/log.txt", "a") as out:
        out.write(r_type+' '+r_share+' '+r_width+' '+fill_color)
    f_color = list(np.array(fill_color)/255)
    height = 200 + r_width*2.5
    width = 200*2 +r_width*2.5
    s = 100+r_width

    if r_type == 0:
        angle = 2*math.pi * r_share / 100
        with cairo.SVGSurface("plasmid_fraction.svg", width, height)  as surface:
            context = cairo.Context(surface)
            context.set_line_width(r_width)
            context.set_source_rgba(f_color[0], f_color[1], f_color[2], f_color[3])
            context.arc(r_width+100, 100+r_width, 100, 0, angle)
            context.stroke()

    if r_type == 1:
        angle = -2*math.pi * r_share / 100
        with cairo.SVGSurface("plasmid_fraction.svg", width, height)  as surface:
            context = cairo.Context(surface)

            context.set_line_width(r_width)
            context.set_source_rgba(r, g, b, a)
            context.arc(s, s, 100, angle, 0)
            context.stroke()

            context.move_to(s+100+r_width*0.7, s)
            context.line_to(s+100, s+r_width/2)
            context.line_to(s+100-r_width*0.7, s)
            context.line_to(s+100+r_width*0.7, s)
            context.fill()

    if r_type == 2:
        angle = 2*math.pi * r_share / 100
        with cairo.SVGSurface("plasmid_fraction.svg", width, height)  as surface:
            context = cairo.Context(surface)

            context.set_line_width(r_width)
            context.set_source_rgba(r, g, b, a)
            context.arc(s, s, 100, 0, angle)
            context.stroke()

            context.move_to(s+100+r_width*0.7, s)
            context.line_to(s+100, s-r_width/2)
            context.line_to(s+100-r_width*0.7, s)
            context.line_to(s+100+r_width*0.7, s)
            context.fill()

#circular_dna.py
def draw_circular_dna(radius_out, radius_in, line_width, color, num, base_width):
    height = (radius_out + line_width) * 2
    width = (radius_out + line_width) * 2
    center = line_width + radius_out
    r, g = color[0]/255, color[1]/255
    b, a = color[2]/255, color[3]/255

    with cairo.SVGSurface("circular_dna.svg", width, height)  as surface:
        context = cairo.Context(surface)
        context.set_line_width(line_width)
        context.set_source_rgba(r, g, b, a)
        context.arc(center, center, radius_out, 0, 2*math.pi)
        context.stroke()

        context.arc(center, center, radius_in, 0, 2*math.pi)
        context.stroke()

        context.set_line_width(base_width)
        if num != 0:
            step = 360/num
            degrees = 0
            for i in range(num):
                radians = math.radians(degrees)
                cos = math.cos(radians)
                sin = math.sin(radians)
                x_out, y_out = radius_out * cos + center, radius_out * sin + center
                x_in, y_in = radius_in * cos + center, radius_in * sin + center

                context.move_to(x_in, y_in)
                context.line_to(x_out, y_out)
                context.stroke()

                degrees += step


def rgba_color(param):
    cols = [int(x) for x in param.split("@")]
    return cols


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='figure_name')

parser_dna = subparsers.add_parser('dna.svg', help='draw a double-strand dna fragment')
parser_dna.add_argument('--width', type=int, required=True)
parser_dna.add_argument('--num_of_coils', type=int, required=True)
parser_dna.add_argument('--color1', type=rgba_color, required=True)
parser_dna.add_argument('--color2', type=rgba_color, required=True)
parser_dna.add_argument('--line_width', type=float, required=True)

parser_rectangle = subparsers.add_parser('protein.svg', help='draw a protein')
parser_rectangle.add_argument("--width", type=int, required=True)
parser_rectangle.add_argument("--height", type=int, required=True)
parser_rectangle.add_argument("--line_width", type=float, required=True)
parser_rectangle.add_argument("--line_color", type=rgba_color, required=True)
parser_rectangle.add_argument("--fill_color", type=rgba_color, required=True)

parser_pl_fract = subparsers.add_parser('plasmid_fraction.svg', help='draw a fraction of my plasmid')
parser_pl_fract.add_argument('--r_type', type=int, required=True)
parser_pl_fract.add_argument('--r_share', type=int, required=True)
parser_pl_fract.add_argument('--r_width', type=float, required=True)
parser_pl_fract.add_argument('--fill_color', type=rgba_color, required=True)

parser_circ_dna = subparsers.add_parser('circular_dna.svg', help = 'draw a circular DNA')
parser_circ_dna.add_argument('--radius_out', type=int, required=True)
parser_circ_dna.add_argument('--radius_in', type=int, required=True)
parser_circ_dna.add_argument('--line_width', type=float, required=True)
parser_circ_dna.add_argument('--color', type=rgba_color, required=True)
parser_circ_dna.add_argument('--num', type=int, required=True)
parser_circ_dna.add_argument('--base_width', type=float, required=True)

#parser_circle = subparsers.add_parser("circle", help="draw a circle")
#parser_circle.add_argument("--radius", type=float, required=True)



args = parser.parse_args()
with open("C:/Users/user/AppData/Roaming/inkscape/extensions/log.txt", "a") as out:
    out.write("Blya2\n")

#if args.figure_name == "circle":
#    draw_circle(args.radius)
if args.figure_name == "dna.svg":
    draw_dna(args.width, args.num_of_coils, args.color1, args.color2, args.line_width)

elif args.figure_name == "rectangle.svg":
    draw_rectangle(args.width, args.height, args.line_width, args.line_color, args.fill_color)

elif args.figure_name == "plasmid_fraction.svg":
    with open("C:/Users/user/AppData/Roaming/inkscape/extensions/log.txt", "a") as out:
        out.write("figure_name\n")
    draw_plasmid_fraction(args.r_type, args.r_share, args.r_width, args.fill_color)
elif args.figure_name == 'circular_dna.svg':
    draw_circular_dna(args.radius_out, args.radius_in, args.line_width, args.color, args.num, args.base_width)

else:
    with open("C:/Users/user/AppData/Roaming/inkscape/extensions/log.txt", "a") as out:
        out.write("Blya\n")
    print("Wrong figure name")
    exit(1)
