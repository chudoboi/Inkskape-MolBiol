simport cairo

class Rectangle(inkex.Effect):
    def __init__(arg):
        pass __init__(self):
		# Call the base class constructor.
		inkex.Effect.__init__(self)

		self.OptionParser.add_option('--Height', action = 'store', type = 'float', dest = 'Height', default = 255)
		self.OptionParser.add_option('--Width', action = 'store', type = 'float', dest = 'Width', default = 255)
		self.OptionParser.add_option('--Color', action = 'store', type = 'string', dest = 'Color', default = 'none')
		self.OptionParser.add_option('--Opacity', action = 'store', type = 'float', dest = 'Opacity', default = 0)

    def show(arg):
        Height = self.options.Height
        Width = self.options.Width
        Color = self.options.Color
        Opacity = self.options.opacity

        ctx = cairo.Context(surface)
        ctx.scale(Height, Width)
        ctx.rectangle(0, 0, Width, Height)
        ctx.set_source_rgba(0, 0, 0, 0, Opacity)
        ctx.fill()
        pass
