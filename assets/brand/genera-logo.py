# -*- coding: utf-8 -*-
"""Genere le systeme d'identite Titanio Vero : lettres dessinees en vectoriel,
aucune police externe, donc aucun probleme de licence."""
import os

SW   = 15.0   # graisse du trait
H    = 100.0  # hauteur de capitale
TR   = 18.0   # approche entre lettres
h    = SW / 2

# ---- alphabet geometrique, construit au trait -------------------------------
def glyph(ch):
    if ch == "T":
        return 74, "M {a},{h} H {b} M {m},{h} V {v}".format(a=h, b=74-h, m=37, h=h, v=H-h)
    if ch == "I":
        return 15, "M {h},{h} V {v}".format(h=h, v=H-h)
    if ch == "A":
        y  = 62.0
        t  = (y - h) / (H - h - h)
        xl = 43 - (43 - h) * t
        xr = 43 + (43 - h) * t
        return 86, ("M {h},{v} L 43,{h} L {r},{v} M {xl},{y} H {xr}"
                    .format(h=h, v=H-h, r=86-h, xl=round(xl,2), xr=round(xr,2), y=y))
    if ch == "N":
        return 88, "M {h},{v} V {h} L {r},{v} V {h}".format(h=h, v=H-h, r=88-h)
    if ch == "O":
        rx, ry, cx = 38.0, 42.5, 45.5
        return 91, ("M {l},50 A {rx},{ry} 0 1 1 {r},50 A {rx},{ry} 0 1 1 {l},50 Z"
                    .format(l=cx-rx, r=cx+rx, rx=rx, ry=ry))
    if ch == "V":
        return 86, "M {h},{h} L 43,{v} L {r},{h}".format(h=h, v=H-h, r=86-h)
    if ch == "E":
        return 72, ("M {r},{h} H {h} M {h},{h} V {v} M {h},{v} H {r} M {h},50 H {mid}"
                    .format(h=h, v=H-h, r=72-h, mid=54))
    if ch == "R":
        return 80, ("M {h},{v} V {h} H 45 A 22.25,22.25 0 0 1 45,52 H {h} M 41,52 L {r},{v}"
                    .format(h=h, v=H-h, r=80-h))
    if ch == "i":                      # bas de casse, pour le poincon Ti
        return 15, "M {h},38 V {v} M {h},9.5 V 24.5".format(h=h, v=H-h)
    raise KeyError(ch)

def word(txt, track=TR):
    """Retourne (largeur, liste de (dx, path))."""
    out, x = [], 0.0
    for i, ch in enumerate(txt):
        w, d = glyph(ch)
        out.append((x, d))
        x += w + (track if i < len(txt) - 1 else 0)
    return x, out

def draw(txt, track=TR, dx=0.0, dy=0.0, scale=1.0):
    w, parts = word(txt, track)
    body = "".join(
        '<path d="{d}" transform="translate({x} 0)"/>'.format(d=d, x=round(px, 2))
        for px, d in parts)
    g = ('<g transform="translate({dx} {dy}) scale({s})">{b}</g>'
         .format(dx=round(dx, 2), dy=round(dy, 2), s=scale, b=body))
    return w * scale, g

# ---- le poincon -------------------------------------------------------------
PUNCH_W, CUT = 240.0, 42.0
def punch(stroke=17.0):
    o = stroke / 2
    a, b = o, PUNCH_W - o
    d = ("M {c},{a} H {bc} L {b},{c} V {bc2} L {bc},{b} H {c} L {a},{bc2} V {c} Z"
         .format(a=a, b=b, c=a + CUT, bc=b - CUT, bc2=b - CUT))
    shape = '<path d="{d}" stroke-width="{s}"/>'.format(d=d, s=stroke)
    # "Ti" centre dans le poincon
    s = 0.60
    tw, _ = word("Ti")
    tx = (PUNCH_W - tw * s) / 2
    ty = (PUNCH_W - H * s) / 2
    _, ti = draw("Ti", dx=tx, dy=ty, scale=s)
    return shape + ti

# ---- assemblage -------------------------------------------------------------
LINE1, LINE2 = "TITANIO", "VERO"
W1, _ = word(LINE1)
W2n, _ = word(LINE2)
TRACK2 = TR + (W1 - W2n) / (len(LINE2) - 1)      # VERO etire a la largeur de TITANIO

def wordmark(scale=1.0, gap=48.0):
    _, g1 = draw(LINE1, dx=0, dy=0, scale=1.0)
    _, g2 = draw(LINE2, track=TRACK2, dx=0, dy=H + gap, scale=1.0)
    return W1, H * 2 + gap, '<g transform="scale({s})">{a}{b}</g>'.format(s=scale, a=g1, b=g2)

def svg(w, h_, body, fg, bg=None, sw=SW):
    bgr = '<rect width="{w}" height="{h}" fill="{c}"/>'.format(w=w, h=h_, c=bg) if bg else ""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            'width="{w}" height="{h}" fill="none" stroke="{fg}" stroke-width="{sw}" '
            'stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="2.2">'
            '{bg}{body}</svg>').format(w=round(w,1), h=round(h_,1), fg=fg, sw=sw, bg=bgr, body=body)

BRONZE, VERDE, CREMA, BIANCO = "#B57C46", "#002418", "#F5F0E8", "#FFFFFF"
OUT = "/home/user/run.css/assets/brand"
os.makedirs(OUT, exist_ok=True)

def principale(fg, bg=None):
    ww, wh, wm = wordmark()
    gap = 62.0
    total_w = PUNCH_W + gap + ww
    dy = (wh - PUNCH_W) / 2
    body = ('<g transform="translate(0 {dy})">{p}</g>'
            '<g transform="translate({x} 0)">{w}</g>'
            .format(dy=round(dy,1), p=punch(), x=PUNCH_W + gap, w=wm))
    return svg(total_w, wh, body, fg, bg)

def verticale(fg, bg=None):
    ww, wh, wm = wordmark()
    gap = 66.0
    total_h = PUNCH_W + gap + wh
    body = ('<g transform="translate({px} 0)">{p}</g>'
            '<g transform="translate(0 {y})">{w}</g>'
            .format(px=round((ww - PUNCH_W)/2, 1), p=punch(), y=PUNCH_W + gap, w=wm))
    return svg(ww, total_h, body, fg, bg)

def lineare(fg, bg=None):
    w1, g1 = draw(LINE1, dx=0, dy=0)
    w2, g2 = draw(LINE2, dx=w1 + 62, dy=0)
    total = w1 + 62 + w2
    return svg(total, H, g1 + g2, fg, bg)

def marchio(fg, bg=None):
    return svg(PUNCH_W, PUNCH_W, punch(), fg, bg)

def marchio_pieno(fg, bg):
    """Poincon plein : la seule version lisible en dessous de 32 px."""
    a, b, c = 0.0, PUNCH_W, CUT
    d = ("M {c},{a} H {bc} L {b},{c} V {bc} L {bc},{b} H {c} L {a},{bc} V {c} Z"
         .format(a=a, b=b, c=c, bc=b - c))
    plein = '<path d="{d}" fill="{f}" stroke="none"/>'.format(d=d, f=bg)
    s = 0.66
    tw, _ = word("Ti")
    _, ti = draw("Ti", dx=(PUNCH_W - tw * s) / 2, dy=(PUNCH_W - H * s) / 2, scale=s)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {w}" width="{w}" '
            'height="{w}" fill="none" stroke="{fg}" stroke-width="{sw}" stroke-linecap="butt" '
            'stroke-linejoin="miter" stroke-miterlimit="2.2">{p}{t}</svg>'
            .format(w=PUNCH_W, fg=fg, sw=SW, p=plein, t=ti))

files = {
    "logo-principale.svg":        principale(BRONZE),
    "logo-principale-bianco.svg": principale(BIANCO),
    "logo-principale-verde.svg":  principale(VERDE),
    "logo-verticale.svg":         verticale(BRONZE),
    "logo-verticale-bianco.svg":  verticale(BIANCO),
    "logotipo-lineare.svg":       lineare(BRONZE),
    "logotipo-lineare-bianco.svg":lineare(BIANCO),
    "marchio.svg":                marchio(BRONZE),
    "marchio-bianco.svg":         marchio(BIANCO),
    "favicon.svg":                marchio_pieno(CREMA, VERDE),
    "favicon-bronzo.svg":         marchio_pieno(CREMA, BRONZE),
}
for name, content in files.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("%-30s %6d o" % (name, len(content)))
