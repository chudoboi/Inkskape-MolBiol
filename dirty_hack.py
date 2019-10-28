import cairo
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str, required=True)
parser.add_argument("--width", type=float, required=True)
parser.add_argument("--num_of_coils", type=int, required=True)
parser.add_argument("--color1", type=str, required=True)
parser.add_argument("--color2", type=str, required=True)
parser.add_argument("--line_width", type=str, required=True)
args = parser.parse_args()

if args.name = "dna.svg":
    width = args.width
    height = width * 1.3 / 2
    coils = args.num_of_coils
    color1 = args.color1
    color2 = args.color2
    line_width = args.line_width

    r1, r2 = color1[0]/255, color2[0]/255
    g1, g2 = color1[1]/255, color2[1]/255
    b1, b2 = color1[2]/255, color2[2]/255
    opac1, opac2 = color1[3], color2[3]

    sur_width = width + 100
    sur_height = 49/20 * height * coils + 100

    with cairo.SVGSurface(args.name,  sur_height, sur_width) as surface:
        context = cairo.Context(surface)
        x3 = 50
        while coils>0:
            x0, y0 = x3, width/2
            x1, y1 = x0 + height*11/20, y0 - width/2
            x2, y2 = x0 + height*11/20, y0 - width/2
            x3, y3 = x0 + height, y0
            context.set_source_rgb(r1, g1, b1)
            context.set_line_width(line_width)
            context.move_to(x0, y0)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()

            context.set_source_rgb(r2, g2, b2)
            x0 = x0 + height*9/20
            x1, y1 = x0 + height*9/20, y0 - width/2
            x2, y2 = x0 + height*11/20, y0 - width/2
            x3, y3 = x0 + height, y0
            context.move_to(x0, y0)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()

            x0 = x3
            x1, y1 = x0 + height*9/20, y0 + width/2
            x2, y2 = x0 + height*11/20, y0 + width/2
            x3, y3 = x0 + height, y0
            context.move_to(x0, y0)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()

            context.set_source_rgb(r1, g1, b1)
            x0 = x0 - height*9/20
            x1, y1 = x0 + height*9/20, y0 + width/2
            x2, y2 = x0 + height*11/20, y0 + width/2
            x3, y3 = x0 + height, y0
            context.move_to(x0, y0)
            context.curve_to(x1, y1, x2, y2, x3, y3)
            context.stroke()

            coils = coils - 1

if args.name = "prot_rect.svg":
    with cairo.SVGSurface(args.name, args.width, args.height) as surface:
        context = cairo.Context(surface)
        x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
        x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
        context.scale(args.width, args.height)
        context.set_line_width(0.04)
        context.move_to(x, y)
        context.curve_to(x1, y1, x2, y2, x3, y3)
        context.stroke()
        context.set_source_rgba(1, 0.2, 0.2, 0.6)
        context.set_line_width(0.02)
        context.move_to(x, y)
        context.line_to(x1, y1)
        context.move_to(x2, y2)
        context.line_to(x3, y3)
        context.stroke()
