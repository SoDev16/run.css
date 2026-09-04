# -*- coding: utf-8 -*-
"""Titanio Vero — logotype dessine en vectoriel, sans police externe.

Ligne haute : capitales grasses a terminaisons biseautees, A en chevron.
Un filet. Ligne basse : le second mot, leger et tres espace.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
H = 100.0          # hauteur de capitale
W_STEM = 20.0      # graisse de la ligne haute
CH = 8.0           # profondeur du biseau


# ------------------------------------------------- ligne haute : glyphes pleins
def heavy(ch):
    """Retourne (avance, path rempli). Terminaisons coupees en diagonale."""
    w, c = W_STEM, CH
    if ch == "T":
        W = 78.0
        m0, m1 = (W - w) / 2, (W + w) / 2
        pts = [(0,0),(W,0),(W,w-c),(W-c,w),(m1,w),(m1,H),(m0,H),(m0,w),(c,w),(0,w-c)]
    elif ch == "I":
        W = w
        pts = [(0,0),(W,0),(W,H),(0,H)]
    elif ch == "A":
        W, lw, top = 86.0, 25.0, 18.0
        ax0, ax1 = (W - top) / 2, (W + top) / 2
        u = (ax1 - ax0 - 0.0)
        run = ax0                                   # deport horizontal d'une jambe
        k = (2 * run - (2 * run - top)) # place-holder, calcul explicite ci-dessous
        # sommet interieur : intersection des deux aretes internes
        uu = (W / 2 - lw - (W / 2 - run - lw)) # inutilise, garde la lisibilite
        t = (W - 2 * lw) / (2 * run) if run else 0
        yn = H * (1 - ((W / 2 - lw) - (W / 2 - run)) / run) if run else H
        # resolution directe : x_gauche(y) = lw + run*(H-y)/H ; x_droite(y) = W-lw-run*(H-y)/H
        uu = (W - 2 * lw) / (2 * run)
        yn = H * (1 - uu)
        pts = [(0,H),(ax0,0),(ax1,0),(W,H),(W-lw,H),(W/2,yn),(lw,H)]
    elif ch == "N":
        W, d = 88.0, 68.0
        pts = [(0,0),(w,0),(d,d),(d,0),(W,0),(W,H),(d,H),(w,H-d),(w,H),(0,H)]
    elif ch == "O":
        W, rx, ry = 90.0, 45.0, 50.0
        ix, iy = rx - w, ry - w
        return W, ("M 0,{cy} A {rx},{ry} 0 1 0 {w},{cy} A {rx},{ry} 0 1 0 0,{cy} Z "
                   "M {a},{cy} A {ix},{iy} 0 1 1 {b},{cy} A {ix},{iy} 0 1 1 {a},{cy} Z"
                   .format(cy=ry, rx=rx, ry=ry, w=W, ix=ix, iy=iy, a=w, b=W - w))
    elif ch == "V":
        W, lw, top = 86.0, 25.0, 18.0
        run = (W - top) / 2
        uu = (W - 2 * lw) / (2 * run)
        yn = H * uu
        pts = [(0,0),(lw,0),(W/2,yn),(W-lw,0),(W,0),((W+top)/2,H),((W-top)/2,H)]
    elif ch == "E":
        W = 72.0
        my0, my1 = (H - w) / 2, (H + w) / 2
        pts = [(0,0),(W,0),(W-c,w),(w,w),(w,my0),(W-14,my0),(W-14-c,my1),(w,my1),
               (w,H-w),(W-c,H-w),(W,H),(0,H)]
    elif ch == "R":
        W, bw = 80.0, 52.0
        pts = None
        d = ("M 0,0 H {bw} A {r},{r} 0 0 1 {bw},{by} H {inx} L {W},{H} H {lx} L {ix},{iy} "
             "H {w} V {H} H 0 Z M {w},{w} V {ry} H {bw2} A {r2},{r2} 0 0 0 {bw2},{w} Z"
             .format(bw=bw, r=27.0, by=54.0, inx=42.0, W=W, H=H, lx=W - 22,
                     ix=40.0, iy=54.0, w=w, ry=34.0, bw2=bw - 8, r2=17.0))
        return W, d
    else:
        raise KeyError(ch)
    return (max(p[0] for p in pts),
            "M " + " L ".join("{0},{1}".format(round(x, 2), round(y, 2)) for x, y in pts) + " Z")


# ------------------------------------------- ligne basse : glyphes au trait fin
DW = {"T": 59, "I": 0, "A": 71, "N": 73, "O": 76, "V": 71, "E": 57, "R": 65, "U": 73, "M": 87}


def light(ch, sw):
    h, d = sw / 2.0, DW[ch]
    top, bot, left, right = h, H - h, h, d + h
    if ch == "T":
        return d + sw, "M {l},{t} H {r} M {m},{t} V {b}".format(l=left, r=right, m=(left+right)/2, t=top, b=bot)
    if ch == "I":
        return d + sw, "M {l},{t} V {b}".format(l=left, t=top, b=bot)
    if ch == "A":
        apex = (left + right) / 2
        y = top + (bot - top) * 0.64
        k = (y - top) / (bot - top)
        return d + sw, ("M {l},{b} L {a},{t} L {r},{b} M {xl},{y} H {xr}"
                        .format(l=left, a=apex, r=right, t=top, b=bot, y=round(y,2),
                                xl=round(apex-(apex-left)*k,2), xr=round(apex+(right-apex)*k,2)))
    if ch == "N":
        return d + sw, "M {l},{b} V {t} L {r},{b} V {t}".format(l=left, r=right, t=top, b=bot)
    if ch == "O":
        rx, ry, cx = d/2.0, (H-sw)/2.0, (left+right)/2
        return d + sw, ("M {a},50 A {rx},{ry} 0 1 1 {b},50 A {rx},{ry} 0 1 1 {a},50 Z"
                        .format(a=round(cx-rx,2), b=round(cx+rx,2), rx=round(rx,2), ry=round(ry,2)))
    if ch == "V":
        return d + sw, "M {l},{t} L {a},{b} L {r},{t}".format(l=left, a=(left+right)/2, r=right, t=top, b=bot)
    if ch == "E":
        return d + sw, ("M {r},{t} H {l} M {l},{t} V {b} M {l},{b} H {r} M {l},{my} H {m}"
                        .format(l=left, r=right, t=top, b=bot,
                                my=round(top+(bot-top)*0.46,2), m=round(left+d*0.82,2)))
    if ch == "R":
        by, bx, rr = top+(bot-top)*0.52, left+d*0.58, (top+(bot-top)*0.52-top)/2
        return d + sw, ("M {l},{b} V {t} H {bx} A {rr},{rr} 0 0 1 {bx},{by} H {l} M {lg},{by} L {r},{b}"
                        .format(l=left, r=right, t=top, b=bot, bx=round(bx,2), by=round(by,2),
                                rr=round(rr,2), lg=round(left+d*0.52,2)))
    raise KeyError(ch)


def heavy_line(txt, track):
    x, parts = 0.0, []
    for i, ch in enumerate(txt):
        adv, p = heavy(ch)
        parts.append('<path d="{d}" transform="translate({x} 0)"/>'.format(d=p, x=round(x, 2)))
        x += adv + (track if i < len(txt) - 1 else 0)
    return x, '<g fill-rule="evenodd">{0}</g>'.format("".join(parts))


def light_line(txt, sw, track):
    x, parts = 0.0, []
    for i, ch in enumerate(txt):
        adv, p = light(ch, sw)
        parts.append('<path d="{d}" transform="translate({x} 0)"/>'.format(d=p, x=round(x, 2)))
        x += adv + (track if i < len(txt) - 1 else 0)
    return x, '<g fill="none" stroke-width="{0}">{1}</g>'.format(sw, "".join(parts))


# ------------------------------------------------------------------ composition
TRACK1   = 30.0     # approche de la ligne haute
CAP2     = 0.46     # hauteur de capitale de la ligne basse
SW2      = 12.0     # graisse de la ligne basse
RULE     = 6.0
GAP_RULE = 30.0
GAP_L2   = 26.0
W2_RATIO = 0.62


def logotipo(w1_txt, w2_txt, fg, bg=None, tm=False, track=TRACK1):
    w1, g1 = heavy_line(w1_txt, track)
    nat = sum(DW[c] + SW2 for c in w2_txt)
    t2 = max(0.0, ((w1 * W2_RATIO) / CAP2 - nat) / (len(w2_txt) - 1))
    w2, g2 = light_line(w2_txt, SW2, t2)
    w2 *= CAP2

    y_rule = H + GAP_RULE
    y_l2 = y_rule + RULE + GAP_L2
    total_h = y_l2 + H * CAP2

    body = g1
    body += '<rect x="0" y="{y}" width="{w}" height="{r}"/>'.format(y=round(y_rule,2), w=round(w1,2), r=RULE)
    body += ('<g transform="translate({x} {y}) scale({s})" stroke="{fg}">{g}</g>'
             .format(x=round((w1-w2)/2,2), y=round(y_l2,2), s=CAP2, fg=fg, g=g2))
    if tm:
        body += ('<g transform="translate({x} -6) scale(0.26)" fill="none" stroke="{fg}" '
                 'stroke-width="13"><path d="M 6,8 H 76 M 41,8 V 66 M 98,66 V 8 L 126,46 '
                 'L 154,8 V 66"/></g>'.format(x=round(w1+18,2), fg=fg))

    pad = 44.0
    vx, vy = (-pad, -pad) if bg else (0, -4)
    vw = w1 + (2*pad if bg else (76 if tm else 4))
    vh = total_h + (2*pad if bg else 8)
    rect = ('<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'
            .format(x=vx, y=vy, w=round(vw,2), h=round(vh,2), c=bg)) if bg else ""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" width="{w}" '
            'height="{h}" fill="{fg}" stroke="none" stroke-linecap="butt" '
            'stroke-linejoin="miter" stroke-miterlimit="2.4">{r}{b}</svg>'
            .format(x=vx, y=round(vy,2), w=round(vw,1), h=round(vh,1), fg=fg, r=rect, b=body))


def monogramma(fg, bg=None, letters="TV", pad=48.0, radius=0.18):
    x, parts = 0.0, []
    for i, ch in enumerate(letters):
        adv, p = heavy(ch)
        parts.append('<path d="{d}" transform="translate({x} 0)"/>'.format(d=p, x=round(x,2)))
        x += adv + (22.0 if i < len(letters)-1 else 0)
    side = max(x, H) + pad*2
    body = ('<rect width="{s}" height="{s}" rx="{r}" fill="{c}"/>'
            .format(s=round(side,2), r=round(side*radius,2), c=bg)) if bg else ""
    body += ('<g fill="{fg}" fill-rule="evenodd" transform="translate({dx} {dy})">{p}</g>'
             .format(fg=fg, dx=round((side-x)/2,2), dy=round((side-H)/2,2), p="".join(parts)))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" width="{s}" '
            'height="{s}" stroke="none">{b}</svg>'.format(s=round(side,2), b=body))


BRONZE, VERDE, CREMA, BIANCO = "#B57C46", "#002418", "#F5F0E8", "#FFFFFF"

if __name__ == "__main__":
    files = {
        "logo-principale.svg":        logotipo("TITANIO", "VERO", BRONZE),
        "logo-principale-bianco.svg": logotipo("TITANIO", "VERO", BIANCO),
        "logo-principale-verde.svg":  logotipo("TITANIO", "VERO", VERDE),
        "logo-su-verde.svg":          logotipo("TITANIO", "VERO", BIANCO, bg=VERDE),
        "logo-tm.svg":                logotipo("TITANIO", "VERO", BRONZE, tm=True),
        "logo-tm-bianco.svg":         logotipo("TITANIO", "VERO", BIANCO, tm=True),
        "monogramma.svg":             monogramma(BRONZE),
        "monogramma-bianco.svg":      monogramma(BIANCO),
        "favicon.svg":                monogramma(CREMA, VERDE),
        "favicon-bronzo.svg":         monogramma(CREMA, BRONZE),
    }
    for n, c in sorted(files.items()):
        open(os.path.join(OUT, n), "w", encoding="utf-8").write(c)
        print("%-30s %5d o" % (n, len(c)))
