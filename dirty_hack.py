import argparse
import cairo

def draw_dna(width, coils, color1, color2, line_width):
    height = width * 1.3 / 2

    r1, r2 = color1[0]/255, color2[0]/255
    g1, g2 = color1[1]/255, color2[1]/255
    b1, b2 = color1[2]/255, color2[2]/255
    opac1, opac2 = color1[3], color2[3]

    sur_width = width + 100
    sur_height = 49/20 * height * coils + 100

    with cairo.SVGSurface("dna.svg",  sur_height, sur_width) as surface:
        context = cairo.Context(surface)
        x3 = 50
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
            x0 = x0 + height*9/20
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
            x0 = x0 - height*9/20
            x1, y1 = x0 + height*2/5, y0 + width/2
            x2, y2 = x0 + height*3/5, y0 + width/2
            x3, y3 = x0 + height, y0
            context.move_to(x0, y0)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()

            coils = coils - 1


def draw_rectangle(width, height, color):
    with cairo.SVGSurface("rectangle.svg", width, height) as surface:
        context = cairo.Context(surface)
        context.set_line_width(9)
        context.set_line_join(cairo.LINE_JOIN_BEVEL)
        context.set_source_rgba(0, 1, 1)
        context.rectangle(50, 50, 100, 200)
        context.stroke_preserve()
        context.set_source_rgba()
        context.fill()

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='figure_name')

parser_dna = subparsers.add_parser('dna.svg', help='draw a double-strand dna fragment')
parser_dna.add_argument('--width', type=int, required=True)
parser_dna.add_argument('--num_of_coils', type=int, required=True)
parser_dna.add_argument('--color1', type=str, required=True)
parser_dna.add_argument('--color2', type=str, required=True)
parser_dna.add_argument('--line_width', type=float, required=True)

parser_rectangle = subparsers.add_parser('rectangle', help='draw a rectangle')
parser_rectangle.add_argument("--rec_width", type=float, required=True)
parser_rectangle.add_argument("--rec_height", type=float, required=True)
parser_rectangle.add_argument("--rec_color", type=str, required=True)


#parser_circle = subparsers.add_parser("circle", help="draw a circle")
#parser_circle.add_argument("--radius", type=float, required=True)



args = parser.parse_args()

#if args.figure_name == "circle":
#    draw_circle(args.radius)
if args.figure_name == "rectangle":
    draw_rectangle(args.height, args.width)
elif args.figure_name == "dna.svg":
    draw_dna(args.width, args.num_of_coils, args.color1, args.color2, color.line_width)
else:
    print("Wrong figure name")
    exit(1)
