#!/usr/bin/python
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



class Plasmid_brick(inkex.Effect):
    def __init__(self, settings_path="settings.json"):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('--tab')
        self.OptionParser.add_option('--name')
        self.OptionParser.add_option('--brick_type', action = 'store', type = 'int', dest = 'brick_type', default = 0)
        self.OptionParser.add_option('--bb_radius', action = 'store', type = 'int', dest = 'bb_radius', default = 200)
        self.OptionParser.add_option('--brick_width', action = 'store', type = 'float', dest = 'brick_width', default = 20)
        self.OptionParser.add_option('--brick_share', action = 'store', type = 'int', dest = 'brick_share', default = 10)
        self.OptionParser.add_option('--brick_color', action = 'store', type = 'int', dest = 'brick_color', default = 0)

    def effect(self):

        with open("settings.json") as inp:
            settings = json.load(inp)

        python3_path = settings['python3_path']
        tempfilename = 'plasmid_brick.svg'


        vals = [python3_path, "dirty_hack.py", tempfilename]
        for key, value in self.options.__dict__.items():
            if "color" in key:
                value = convert_to_cairo(value)
            if key in ("selected_nodes", "ids", "tab", "name"):
                continue
            vals.append("--{}".format(key))
            vals.append(str(value))
        subprocess.check_call(vals)


        t = etree.parse(tempfilename)

        self.document.getroot().append(t.getroot())
        os.remove(tempfilename)

if __name__ == "__main__":
    effect = Plasmid_brick()
    effect.affect()