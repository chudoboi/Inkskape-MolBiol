#!/usr/bin/python
import sys, copy
sys.path.append('/Applications/Inkscape.app/Contents/Resources/extensions')
import inkex, simpletransform
import json

def convert_to_cairo(num):
    bits8 = int('11111111', base=2)
    alpha = ((num) & bits8 )
    blue = ((num >> 8) & bits8)
    green = ((num >> 16) & bits8)
    red = ((num >> 24) & bits8)
    return "{}@{}@{}@{}".format(red, green, blue, alpha)


class Protein(inkex.Effect):
    def __init__(self, settings_path="settings.json"):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('--tab')
        self.OptionParser.add_option('--name')
        self.OptionParser.add_option('--width', action = 'store', type = 'int', dest = 'width', default = 200)
        self.OptionParser.add_option('--height', action = 'store', type = 'int', dest = 'height', default = 150)
        self.OptionParser.add_option('--line_width', action = 'store', type = 'float', dest = 'line_width', default = 10)
        self.OptionParser.add_option('--line_color', action = 'store', type = 'int', dest = 'line_color', default = 0)
        self.OptionParser.add_option('--fill_color', action = 'store', type = 'int', dest = 'fill_color', default = 0)

    def effect(self):
        import os
        import subprocess
        from lxml import etree

        with open("settings.json") as inp:
            settings = json.load(inp)

        python3_path = settings['python3_path']
        tempfilename = 'protein.svg'

        vals = [os.path.abspath(python3_path), os.path.abspath("dirty_hack.py"), tempfilename]
        for key, value in self.options.__dict__.items():
            if "color" in key:
                value = convert_to_cairo(value)
            if key in ("selected_nodes", "ids", "tab", "name"):
                continue
            vals.append("--{}".format(key))
            vals.append(str(value))

        inkex.debug(" ".join(vals))
        subprocess.check_call(vals)

        t = etree.parse(tempfilename)

        self.document.getroot().append(t.getroot())
        os.remove(tempfilename)

class Oval(inkex.Effect):
    def __init__(self, settings_path="settings.json"):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('--tab')
        self.OptionParser.add_option('--name')
        self.OptionParser.add_option('--width', action = 'store', type = 'int', dest = 'width', default = 200)
        self.OptionParser.add_option('--height', action = 'store', type = 'int', dest = 'height', default = 150)
        self.OptionParser.add_option('--line_width', action = 'store', type = 'float', dest = 'line_width', default = 10)
        self.OptionParser.add_option('--line_color', action = 'store', type = 'int', dest = 'line_color', default = 0)
        self.OptionParser.add_option('--fill_color', action = 'store', type = 'int', dest = 'fill_color', default = 0)


if __name__ == "__main__":
    effect = Protein()
    effect.affect()
