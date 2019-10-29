#!/usr/bin/python
import sys, copy
sys.path.append('/Applications/Inkscape.app/Contents/Resources/extensions')
import inkex, simpletransform
import json

class DNA(inkex.Effect):
    def __init__(self, settings_path="settings.json"):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('--width', action = 'store', type = 'float', dest = 'width', default = 200)
        self.OptionParser.add_option('--num_of_coils', action = 'store', type = 'int', dest = 'num_of_coils', default = 3)
        self.OptionParser.add_option('--color1', action = 'store', type = 'string', dest = 'color1')
        self.OptionParser.add_option('--color2', action = 'store', type = 'string', dest = 'color2')
        self.OptionParser.add_option('--line_width', action = 'store', type = 'float', dest = 'line_width')


    def effect(self):
        import os
        import subprocess
        from lxml import etree

        with open("settings.json") as inp:
            settings = json.load(inp)

        python3_path = settings['python3_path']
        tempfilename = 'dna.svg'

        vals = [python3_path, "dirty_hack.py", "--name", tempfilename]
        for key, value in self.options.__dict__.items():
            if key == "selected_nodes" or key == "ids":
                continue
            vals.append("--{}".format(key))
            vals.append(str(value))
        subprocess.call(vals)


        t = etree.parse(tempfilename)

        self.document.getroot().append(t.getroot())
        os.remove(tempfilename)

if __name__ == "__main__":
    effect = DNA()
    effect.affect()
