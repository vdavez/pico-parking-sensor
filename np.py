import machine, neopixel

ONE_THIRD = 1.0 / 3.0
ONE_SIXTH = 1.0 / 6.0
TWO_THIRD = 2.0 / 3.0

class NP(neopixel.NeoPixel):
    def __init__(self, n, p):
        super().__init__(machine.Pin(p), n)

    def clear(self):
        for i in range(self.n):
            self[i] = (0, 0, 0)
        self.write()

    def set_color(self, r, g, b):
        for i in range(self.n):
            self[i] = (r, g, b)
        self.write()

    def set_hls_color(self, h, l, s):
        """Converts HLS to RGB values
        Modified from https://github.com/python/cpython/blob/3.10/Lib/colorsys.py 
        :param float h: The hue of the color to convert
        :param float l: The lightness of the color to convert
        :param float s: The saturation of the color to convert
        """

        def _v(m1, m2, hue):
            hue = hue % 1.0
            if hue < ONE_SIXTH:
                return m1 + (m2-m1)*hue*6.0
            if hue < 0.5:
                return m2
            if hue < TWO_THIRD:
                return m1 + (m2-m1)*(TWO_THIRD-hue)*6.0
            return m1

        if s == 0.0:
            self.set_color(int(l*255), int(l*255), int(l*255))
        if l <= 0.5:
            m2 = l * (1.0+s)
        else:
            m2 = l+s-(l*s)
        m1 = 2.0*l - m2
        self.set_color(
            int(_v(m1, m2, h+ONE_THIRD)*255), 
            int(_v(m1, m2, h)*255), 
            int(_v(m1, m2, h-ONE_THIRD)*255)
        )