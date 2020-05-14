import sys, copy
sys.path.append('/Applications/Inkscape.app/Contents/Resources/extensions')
import inkex, simpletransform
import json

import os
import subprocess
from lxml import etree

def convert_to_cairo(num):
    bits8 = int('11111111', base=2)
    alpha = ((num) & bits8 )
    blue = ((num >> 8) & bits8)
    green = ((num >> 16) & bits8)
    red = ((num >> 24) & bits8)
    return "{}@{}@{}@{}".format(red, green, blue, alpha)

def convert_to_hex(rgba_list):
    r = hex(rgba_list[0])[2:]
    g = hex(rgba_list[1])[2:]
    b = hex(rgba_list[2])[2:]
    a = rgba_list[3]
    if (len(r) == 1):
        r = "0" + r
    if (len(g) == 1):
        g = "0" + g
    if (len(b) == 1):
        b = "0" + b
    hex_rgb = '#' + r + g + b
    opacity = int(a)/255
    return hex_rgb, opacity

class Mouse(inkex.Effect):
    def __init__(self, settings_path="settings.json"):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('--tab')
        self.OptionParser.add_option('--body_color', action = 'store', type = 'int', dest = 'body_color', default = -1208000513)

    def effect(self):
        ink_color = self.options.body_color
        with open('mice_log.txt', 'a') as out:
            out.write(str(ink_color)+'\n')

        rgba_color = convert_to_cairo(ink_color)
        rgba_list = [int(x) for x in rgba_color.split("@")]
        hex_body = convert_to_hex(rgba_list)

        #highlights
        rgba_light = [0,0,0,0]
        x = max(rgba_list[:3])
        if x + 30 > 255:
            for i in range(len(rgba_list)-1):
                rgba_light[i] = rgba_list[i] + 255 - x
        else:
            for i in range(len(rgba_list)-1):
                rgba_light[i] = rgba_list[i] + 30
        rgba_light[3] = rgba_list[3]
        hex_light = convert_to_hex(rgba_light)

        #shadows
        rgba_dark = [0,0,0,0]
        x = min(rgba_list[:3])
        if x < 30:
            for i in range(len(rgba_list)-1):
                rgba_dark[i] = rgba_list[i] - x
        else:
            for i in range(len(rgba_list)-1):
                rgba_dark[i] = rgba_list[i] - 30
        rgba_dark[3] = rgba_list[3]
        hex_dark = convert_to_hex(rgba_dark)

        with open('mice_log.txt', 'a') as out:
            out.write(str(hex_body)+'\n'+str(hex_light)+'\n'+str(hex_dark)+'\n\n')

        source = open('MolBiol_templates/wiki_mouse.svg', 'rt')
        target = open('MolBiol_templates/tmp_mouse.svg', 'wt')

        for line in source:
            if (line.find('.st65{fill:#C0DCEB;') != -1) or (line.find('.st99{fill:#C0DCEB;') != -1):
                line = line.replace('.st65{fill:#C0DCEB;',  '.st65{fill:'+'{};fill-opacity:{};'.format(hex_body[0], hex_body[1]))
                line = line.replace('.st99{fill:#C0DCEB;',  '.st99{fill:'+'{};fill-opacity:{};'.format(hex_body[0], hex_body[1]))
                target.write(line)
            elif (line.find('.st49{fill:#DAEDF7;') != -1) or (line.find('.st66{fill:#E8F4FA;') != -1):
                line = line.replace('.st49{fill:#DAEDF7;', '.st49{fill:'+'{};fill-opacity:{};'.format(hex_light[0], hex_light[1]))
                line = line.replace('.st66{fill:#E8F4FA;', '.st66{fill:'+'{};fill-opacity:{};'.format(hex_light[0], hex_light[1]))
                target.write(line)
            elif line.find('.st80{fill:#ADC4D9;') != -1:
                line = line.replace('.st80{fill:#ADC4D9;', '.st80{fill:'+'{};fill-opacity:{};'.format(hex_dark[0], hex_dark[1]))
                target.write(line)
            else:
                target.write(line)

        source.close()
        target.close()

        tree = etree.parse('MolBiol_templates/tmp_mouse.svg')
        root = tree.getroot()
        self.current_layer.extend(root)
        os.remove('MolBiol_templates/tmp_mouse.svg')


if __name__ == "__main__":
    effect = Mouse()
    effect.affect()
