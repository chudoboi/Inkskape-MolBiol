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


class Circ_na(inkex.Effect):
    def __init__(self, settings_path="settings.json"):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('--tab')
        self.OptionParser.add_option('--name')
        self.OptionParser.add_option('--radius_out', action = 'store', type = 'int', dest = 'radius_out', default = 200)
        self.OptionParser.add_option('--radius_in', action = 'store', type = 'int', dest = 'radius_in', default = 190)
        self.OptionParser.add_option('--line_width', action = 'store', type = 'float', dest = 'line_width', default = 5.00)
        self.OptionParser.add_option('--color', action = 'store', type = 'int', dest = 'color', default = 0)
        self.OptionParser.add_option('--base_width', action = 'store', type = 'float', dest = 'base_width', default = 0.00)
        self.OptionParser.add_option('--num', action = 'store', type = 'int', dest = 'num', default = 0)

    def effect(self):

        with open("settings.json") as inp:
            settings = json.load(inp)

        python3_path = settings['python3_path']
        tempfilename = 'circ_na.svg'

        vals = [python3_path, "dirty_hack.py", tempfilename]
        for key, value in self.options.__dict__.items():
            if "color" in key:
                value = convert_to_cairo(value)
            if key in ("selected_nodes", "ids", "tab", "name"):
                continue
            vals.append("--{}".format(key))
            vals.append(str(value))

        with open(u"C:/Users/user/AppData/Roaming/inkscape/extensions/log.txt", "a") as out:
            out.write('Running\n')
            subprocess.check_call(['C:\\Users\\user\\Anaconda3\\condabin\\activate.bat', 'base', '&'] + vals, stderr=out, shell=True)  # draw figure


        t = etree.parse(tempfilename)
        self.current_layer.extend(t.getroot())
        os.remove(tempfilename)


if __name__ == "__main__":
    effect = Circ_na()
    effect.affect()
