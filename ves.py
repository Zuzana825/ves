from PIL import Image, ImageDraw

def render_ves(ves: str) -> Image.Image:
    def parse_hex_color(hex_color: str):
        hex_color = hex_color.strip().lstrip('#')
        if len(hex_color) != 6:
            
            return (0, 0, 0)
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r, g, b)

    width, height = 640, 400

    obrazok = Image.new("RGB", (width, height), (255, 255, 255))
    kresba = ImageDraw.Draw(obrazok)

    lines = ves.strip().splitlines()
    for line in lines:
        parts = line.split()
        if not parts:
            continue 

        cmd = parts[0].upper()  
        try:
            if cmd == "VES":
                if len(parts) >= 4:
                    new_width = int(parts[2])
                    new_height = int(parts[3])
                    width, height = new_width, new_height
                    obrazok = Image.new("RGB", (width, height), (255, 255, 255))
                    kresba = ImageDraw.Draw(obrazok)

            elif cmd == "CLEAR":
                if len(parts) >= 2:
                    color = parse_hex_color(parts[1])
                    kresba.rectangle((0, 0, width, height), fill=color)

            elif cmd == "FILL_TRIANGLE":
                if len(parts) == 8:
                    x1, y1, x2, y2, x3, y3 = map(int, parts[1:7])
                    color = parse_hex_color(parts[7])
                    kresba.polygon((x1, y1, x2, y2, x3, y3), fill=color)

            elif cmd == "FILL_CIRCLE":
                if len(parts) == 5:
                    x, y, r = map(int, parts[1:4])
                    color = parse_hex_color(parts[4])
                    kresba.ellipse((x - r, y - r, x + r, y + r), fill=color)

            elif cmd == "FILL_REC":
                if len(parts) == 6:
                    x1, y1, x2, y2 = map(int, parts[1:5])
                    color = parse_hex_color(parts[5])
                    kresba.rectangle((x1, y1, x2, y2), fill=color)

            elif cmd == "CIRCLE":
                if len(parts) == 6:
                    x, y, r, hrubka = map(int, parts[1:5])
                    color = parse_hex_color(parts[5])
                    kresba.ellipse((x - r, y - r, x + r, y + r),
                                   outline=color, width=hrubka)

            elif cmd == "TRIANGLE":
                if len(parts) == 9:
                    x1, y1, x2, y2, x3, y3, hrubka = map(int, parts[1:8])
                    color = parse_hex_color(parts[8])
                    kresba.line((x1, y1, x2, y2), fill=color, width=hrubka)
                    kresba.line((x2, y2, x3, y3), fill=color, width=hrubka)
                    kresba.line((x3, y3, x1, y1), fill=color, width=hrubka)

            elif cmd == "RECT":
                if len(parts) == 7:
                    x1, y1, x2, y2, hrubka = map(int, parts[1:6])
                    color = parse_hex_color(parts[6])
                    kresba.rectangle((x1, y1, x2, y2), outline=color, width=hrubka)

            elif cmd == "LINE":
                if len(parts) == 7:
                    x1, y1, x2, y2, hrubka = map(int, parts[1:6])
                    color = parse_hex_color(parts[6])
                    kresba.line((x1, y1, x2, y2), fill=color, width=hrubka)

        except Exception as e:
            print(f"Chyba pri spracovaní riadku '{line}': {e}")

    return obrazok
