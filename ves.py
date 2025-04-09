from PIL import Image, ImageDraw

def render_ves(ves: str, width: int = 600, height: int = 400) -> Image.Image:
    obrazok = Image.new("RGB", (width, height), (255, 255, 255))
    kresba = ImageDraw.Draw(obrazok)
    riadky = ves.strip().splitlines()

    def line(x1, y1, x2, y2, hrubka, farba):
        kresba.line((x1, y1, x2, y2), fill=farba, width=hrubka)

    def fill_circle(sx, sy, r, hrubka, farba):
        kresba.ellipse((sx - r, sy - r, sx + r, sy + r), fill=farba, outline=farba, width=hrubka)

    def circle(s1, s2, r, hrubka, farba):
        for t in range(hrubka):
            r_s_hrubkou = r + t
            for x in range(r_s_hrubkou + 1):
                y = int((r_s_hrubkou**2 - x**2)**0.5)
                for dx, dy in [(x, y), (y, x), (-x, y), (-y, x), (-x, -y), (-y, -x), (x, -y), (y, -x)]:
                    px, py = s1 + dx, s2 + dy
                    if 0 <= px < width and 0 <= py < height:
                        obrazok.putpixel((px, py), farba)

    def rectangle(x1, y1, x2, y2, hrubka, farba):
        kresba.rectangle((x1, y1, x2, y2), outline=farba, width=hrubka)

    def fill_rectangle(x1, y1, x2, y2, hrubka, farba):
        kresba.rectangle((x1, y1, x2, y2), fill=farba, outline=farba, width=hrubka)

    def triangle(x1, y1, x2, y2, x3, y3, hrubka, farba):
        kresba.line((x1, y1, x2, y2), fill=farba, width=hrubka)
        kresba.line((x2, y2, x3, y3), fill=farba, width=hrubka)
        kresba.line((x3, y3, x1, y1), fill=farba, width=hrubka)

    def fill_triangle(x1, y1, x2, y2, x3, y3, farba):
        kresba.polygon((x1, y1, x2, y2, x3, y3), fill=farba)

    for riadok in riadky:
        prvky = riadok.split()
        if not prvky:
            continue
        typ = prvky[0].upper()

        try:
            if typ == "LINE":
                x1, y1, x2, y2 = map(int, prvky[1:5])
                hrubka = int(prvky[5])
                farba = tuple(map(int, prvky[6:9]))
                line(x1, y1, x2, y2, hrubka, farba)

            elif typ == "FILL_CIRCLE":
                sx, sy, r = map(int, prvky[1:4])
                hrubka = int(prvky[4])
                farba = tuple(map(int, prvky[5:8]))
                fill_circle(sx, sy, r, hrubka, farba)

            elif typ == "CIRCLE":
                s1, s2, r = map(int, prvky[1:4])
                hrubka = int(prvky[4])
                farba = tuple(map(int, prvky[5:8]))
                circle(s1, s2, r, hrubka, farba)

            elif typ == "REC":
                x1, y1, x2, y2 = map(int, prvky[1:5])
                hrubka = int(prvky[5])
                farba = tuple(map(int, prvky[6:9]))
                rectangle(x1, y1, x2, y2, hrubka, farba)

            elif typ == "FILL_REC":
                x1, y1, x2, y2 = map(int, prvky[1:5])
                hrubka = int(prvky[5])
                farba = tuple(map(int, prvky[6:9]))
                fill_rectangle(x1, y1, x2, y2, hrubka, farba)

            elif typ == "TRIANGLE":
                x1, y1, x2, y2, x3, y3 = map(int, prvky[1:7])
                hrubka = int(prvky[7])
                farba = tuple(map(int, prvky[8:11]))
                triangle(x1, y1, x2, y2, x3, y3, hrubka, farba)

            elif typ == "FILL_TRIANGLE":
                x1, y1, x2, y2, x3, y3 = map(int, prvky[1:7])
                farba = tuple(map(int, prvky[7:10]))
                fill_triangle(x1, y1, x2, y2, x3, y3, farba)

            elif typ == "CLEAR":
                fill_rectangle(0, 0, width, height, 0, (255, 255, 255))

        except Exception as e:
            print(f"Chyba pri spracovaní riadku: {riadok}, chyba: {e}")

    return obrazok
