import argparse
import cairo
import math

#for dna.py
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

#for plasmid_bb.py
def draw_plasmid_bb(line_width, bb_radius, bb_color):
    r, g = bb_color[0]/255, bb_color[1]/255
    b, a = bb_color[2]/255, bb_color[3]/255
    height = (bb_radius+line_width)*2
    width = (bb_radius+line_width)*2

    with cairo.SVGSurface("plasmid_bb.svg", width, height)  as surface:
        context = cairo.Context(surface)

        context.set_line_width(line_width)
        context.set_source_rgba(r, g, b, a)
        context.arc(bb_radius+line_width, bb_radius+line_width, bb_radius, 0, 2*math.pi)
        context.stroke()

#for plasmid_brick.py
def draw_plasmid_brick(brick_type, brick_width, bb_radius, brick_share, brick_color):
    r, g = brick_color[0]/255, brick_color[1]/255
    b, a = brick_color[2]/255, brick_color[3]/255
    s = bb_radius + brick_width

    if brick_type == 0:
        height = (bb_radius+brick_width)*2
        width = (bb_radius+brick_width)*2
        angle = 2*math.pi * brick_share / 100
        with cairo.SVGSurface("plasmid_brick.svg", width, height)  as surface:
            context = cairo.Context(surface)

            context.set_line_width(brick_width)
            context.set_source_rgba(r, g, b, a)
            context.arc(s, s, bb_radius, 0, angle)
            context.stroke()
    if brick_type == 1:
        height = bb_radius * 2 + brick_width * 2.5
        width = bb_radius * 2 + brick_width * 2.5
        angle = -2 * math.pi * brick_share / 100
        with cairo.SVGSurface("plasmid_brick.svg", width, height)  as surface:
            context = cairo.Context(surface)

            context.set_line_width(brick_width)
            context.set_source_rgba(r, g, b, a)
            context.arc(s, s, bb_radius, angle, 0)
            context.stroke()

            context.move_to(s + bb_radius + brick_width * 0.9, s)
            context.line_to(s + bb_radius, s + brick_width / 1.5)
            context.line_to(s + bb_radius - brick_width * 0.9, s)
            context.line_to(s + bb_radius + brick_width * 0.9, s)
            context.fill()
    if brick_type == 2:
        angle = 2 * math.pi * brick_share / 100
        height = bb_radius*2 + brick_width * 2.5
        width = bb_radius*2 + brick_width * 2.5
        with cairo.SVGSurface("plasmid_brick.svg", width, height)  as surface:
            context = cairo.Context(surface)

            context.set_line_width(brick_width)
            context.set_source_rgba(r, g, b, a)
            context.arc(s, s, bb_radius, 0, angle)
            context.stroke()

            context.move_to(s + bb_radius + brick_width * 0.9, s)
            context.line_to(s + bb_radius, s - brick_width / 1.5)
            context.line_to(s + bb_radius - brick_width * 0.9, s)
            context.line_to(s + bb_radius + brick_width * 0.9, s)
            context.fill()

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

parser_pl_bb = subparsers.add_parser('plasmid_bb.svg', help='draw a plasmid backbone')
parser_pl_bb.add_argument('--line_width', type=float, required=True)
parser_pl_bb.add_argument('--bb_radius', type=int, required=True)
parser_pl_bb.add_argument('--bb_color', type=rgba_color, required=True)

parser_pl_brick = subparsers.add_parser('plasmid_brick.svg', help='draw an element of my plasmid')
parser_pl_brick.add_argument('--brick_type', type=int, required=True)
parser_pl_brick.add_argument('--bb_radius', type=int, required=True)
parser_pl_brick.add_argument('--brick_width', type=float, required=True)
parser_pl_brick.add_argument('--brick_share', type=int, required=True)
parser_pl_brick.add_argument('--brick_color', type=rgba_color, required=True)

#parser_circle = subparsers.add_parser("circle", help="draw a circle")
#parser_circle.add_argument("--radius", type=float, required=True)



args = parser.parse_args()

#if args.figure_name == "circle":
#    draw_circle(args.radius)
if args.figure_name == "dna.svg":
    draw_dna(args.width, args.num_of_coils, args.color1, args.color2, args.line_width)

elif args.figure_name == "rectangle.svg":
    draw_rectangle(args.width, args.height, args.line_width, args.line_color, args.fill_color)

elif args.figure_name == "plasmid_bb.svg":
    draw_plasmid_bb(args.line_width, args.bb_radius, args.bb_color)
elif args.figure_name == "plasmid_brick.svg":
     draw_plasmid_brick(args.brick_type, args.brick_width, args.bb_radius, args.brick_share, args.brick_color)

else:
    print("Wrong figure name")
    exit(1)
