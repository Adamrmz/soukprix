from PIL import Image, ImageDraw

BG = (47, 143, 91, 255)      # --accent green
FG = (255, 255, 255, 255)    # white glyph

def rounded_square(size, radius_pct=0.225):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = int(size * radius_pct)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=BG)
    return img, d

def draw_cart(d, size):
    s = size / 24.0
    def pt(x, y):
        return (x * s, y * s)
    lw = max(1, round(1.8 * s))
    # basket body (open trapezoid, like the nav cart icon)
    d.line([pt(4.2, 7), pt(19, 7)], fill=FG, width=lw, joint="curve")
    d.line([pt(19, 7), pt(17, 15.5)], fill=FG, width=lw, joint="curve")
    d.line([pt(17, 15.5), pt(7.3, 15.5)], fill=FG, width=lw, joint="curve")
    d.line([pt(7.3, 15.5), pt(4.2, 7)], fill=FG, width=lw, joint="curve")
    # handle
    d.line([pt(4.2, 7), pt(2.2, 3.2)], fill=FG, width=lw, joint="curve")
    # wheels
    wr = 1.35 * s
    for cx in (8.3, 15.8):
        cy = 19.2 * s
        d.ellipse([cx * s - wr, cy - wr, cx * s + wr, cy + wr], fill=FG)

def build(size, out):
    img, d = rounded_square(size)
    draw_cart(d, size)
    img.save(out)

build(192, "icons/icon-192.png")
build(512, "icons/icon-512.png")
build(180, "icons/apple-touch-icon.png")
build(32, "icons/favicon-32.png")
print("done")
