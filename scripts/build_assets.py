#!/usr/bin/env python3
"""Rebuild the profile's self-contained SVG artwork using Python's standard library."""
from html import escape
from math import cos, sin, pi
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
INK, PAPER, MUTED, LIME, LILAC = '#111216', '#f5f3ea', '#b1b0bd', '#d5ff70', '#baa4ff'

def text(x, y, value, size=16, color=PAPER, weight=400, family='Arial, Helvetica, sans-serif', extra=''):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>'

def mono(x, y, value, size=12, color=MUTED):
    return text(x, y, value, size, color, family='monospace')

def star(x, y, radius=20, color=LIME):
    points = []
    for i in range(16):
        a, r = i * pi / 8, radius if i % 2 == 0 else radius * .28
        points.append(f'{x + cos(a) * r:.2f},{y + sin(a) * r:.2f}')
    return f'<polygon points="{" ".join(points)}" fill="{color}"/>'

def svg(name, width, height, title, body, desc='', defs=''):
    output = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>
<defs>{defs}</defs>
{body}
</svg>
'''
    (ASSETS / name).write_text(output)

def hero():
    defs = '''
<radialGradient id="halo"><stop stop-color="#8063dc" stop-opacity=".27"/><stop offset="1" stop-color="#111216" stop-opacity="0"/></radialGradient>
<linearGradient id="chrome" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#e8e2ff"/><stop offset=".2" stop-color="#857b9b"/><stop offset=".36" stop-color="#fff"/><stop offset=".5" stop-color="#554c68"/><stop offset=".68" stop-color="#e3dcf6"/><stop offset=".85" stop-color="#80748f"/><stop offset="1" stop-color="#f3f0ff"/></linearGradient>
<linearGradient id="orbit" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#68509b"/><stop offset=".45" stop-color="#e0cdff"/><stop offset="1" stop-color="#8461ce"/></linearGradient>
<radialGradient id="planet" cx=".3" cy=".2"><stop stop-color="#e8dcff"/><stop offset=".45" stop-color="#bea5ff"/><stop offset="1" stop-color="#55416e"/></radialGradient>
<pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse"><path d="M48 0H0V48" fill="none" stroke="#fff" stroke-opacity=".035"/></pattern>
<clipPath id="frame"><rect width="1200" height="590" rx="20"/></clipPath>
'''
    body = f'''<style>
.float{{animation:float 8s ease-in-out infinite;transform-origin:900px 280px}}
.satellite{{animation:orbit 28s linear infinite;transform-origin:900px 280px}}
@keyframes float{{0%,100%{{transform:translateY(0) rotate(-4deg)}}50%{{transform:translateY(-12px) rotate(4deg)}}}}
@keyframes orbit{{to{{transform:rotate(360deg)}}}}
@media(prefers-reduced-motion:reduce){{.float,.satellite{{animation:none}}}}
</style><g clip-path="url(#frame)">
<path fill="{INK}" d="M0 0h1200v590H0z"/><path fill="url(#grid)" d="M0 0h1200v590H0z"/>
<ellipse cx="925" cy="270" rx="380" ry="320" fill="url(#halo)"/>
<path d="M38 76H1162" stroke="#393740"/>
{mono(40, 46, 'RG / FIELD NOTES', 15, PAPER)}{mono(824, 46, 'TORONTO, CA  /  43.65 N', 14)}
{text(42, 216, 'RITVIK', 155, PAPER, 900, extra='letter-spacing="-9"')}
{text(42, 363, 'GOYAL', 155, LILAC, 900, extra='letter-spacing="-9"')}{star(633, 319, 36)}
{text(48, 424, 'A little curiosity.', 30)}{text(48, 464, 'A lot of possibility.', 30)}
<g class="float">
<ellipse cx="900" cy="280" rx="188" ry="186" fill="none" stroke="url(#orbit)" stroke-width="33" transform="rotate(-30 900 280)"/>
<ellipse cx="900" cy="280" rx="145" ry="142" fill="none" stroke="{LIME}" stroke-opacity=".65"/>
<ellipse cx="900" cy="280" rx="238" ry="68" fill="none" stroke="#a49cae" stroke-width="1.5" transform="rotate(-38 900 280)"/>
<ellipse cx="900" cy="280" rx="238" ry="68" fill="none" stroke="#655b79" transform="rotate(54 900 280)"/>
<path d="M900 157 Q917 245 1023 280 Q918 299 900 403 Q881 301 777 280 Q880 260 900 157Z" fill="url(#chrome)" stroke="#f4edff" stroke-opacity=".35"/>
<path d="M900 157L900 403M777 280H1023" stroke="#fff" stroke-opacity=".26"/>
<circle cx="1070" cy="145" r="29" fill="url(#planet)"/><circle cx="718" cy="373" r="13" fill="url(#chrome)"/>
</g><g class="satellite"><circle cx="900" cy="58" r="8" fill="{LIME}"/></g>
{mono(797, 500, 'FOLLOW THE CURIOSITY ↗', 14, LILAC)}
<path d="M0 539H1200V590H0z" fill="{LIME}"/>
{mono(40, 571, 'SOFTWARE. HACKATHONS. SIDE QUESTS.', 17, INK)}
{mono(850, 571, 'ALWAYS A WORK IN PROGRESS', 13, INK)}</g>'''
    svg('hero.svg', 1200, 590, 'Ritvik Goyal — a little curiosity, a lot of possibility.', body,
        'Violet orbital rings surround a chrome star. Software, hackathons, and side quests. Based in Toronto.', defs)

def card(name, title, category, accent, art, subtitle):
    body = f'''<rect width="600" height="340" rx="14" fill="{INK}"/>
<rect x=".5" y=".5" width="599" height="339" rx="14" stroke="#35333e" fill="none"/>
{mono(28, 34, category, 12, accent)}{mono(543, 34, '↗', 18)}
{text(26, 94, title, 49, PAPER, 700, extra='letter-spacing="-2"')}{text(28, 125, subtitle, 19, MUTED)}{art}'''
    svg(name, 600, 340, title, body, f'{category}. {subtitle}')

def projects():
    dealify = f'''<rect x="28" y="158" width="544" height="154" rx="10" fill="#201c2b"/>
<path d="M288 186H330M288 244H330" stroke="#645474" stroke-dasharray="4 5"/>
<rect x="48" y="178" width="240" height="44" rx="10" fill="#3b2f54"/>{text(64, 206, '“Can you do $80?”', 21)}
<rect x="90" y="236" width="198" height="44" rx="10" fill="{LILAC}"/>{text(106, 264, '“Let’s make a deal.”', 18, INK, 700)}
<rect x="330" y="178" width="222" height="102" rx="8" fill="{INK}" stroke="#76638d"/>
{mono(346, 203, 'THE PRICING ENGINE', 12, LILAC)}{text(346, 233, 'AI talks.', 23, PAPER, 700)}{text(346, 261, 'Code sets the limits.', 18, LIME)}
{mono(48, 299, 'HACK THE NORTH 2026 · CATEGORY WINNER', 11, LILAC)}'''
    card('dealify.svg', 'Dealify', '01 / COMMERCE + AI', LILAC, dealify, 'Name your price. The shop can counter.')
    wealth = f'''<rect x="28" y="158" width="544" height="154" rx="10" fill="#1c2621"/>
<g transform="translate(52 176) rotate(-6 60 60)"><path d="M0 0H126V120L115 113L104 120L93 113L82 120L71 113L60 120L49 113L38 120L27 113L16 120L0 113Z" fill="#e9f0dc"/>
{mono(16, 25, 'RECEIPT', 13, INK)}<path d="M16 40H109M16 56H80M16 72H96" stroke="#b5bfad"/>{text(16, 101, '$42.80', 23, INK, 700)}</g>
<path d="M205 236H249M241 229L249 236L241 243" stroke="{LIME}" fill="none"/>
{mono(282, 195, 'THE BIGGER PICTURE', 12, LIME)}
<path d="M282 275V218M331 275V239M380 275V208M429 275V225M478 275V200M527 275V216" stroke="#6f9672" stroke-width="21"/>
<path d="M282 244L331 250L380 231L429 239L478 215L527 222" fill="none" stroke="{LIME}" stroke-width="3"/>
{mono(282, 298, 'SCAN → REVIEW → UNDERSTAND', 11, LIME)}'''
    card('wealthsnaps.svg', 'WealthSnaps', '02 / MOBILE + MONEY', LIME, wealth, 'Small receipts. A bigger picture.')
    study = f'''<rect x="28" y="158" width="544" height="154" rx="10" fill="#1e2130"/>
<circle cx="120" cy="235" r="56" fill="none" stroke="#3b4057" stroke-width="8"/>
<circle cx="120" cy="235" r="56" fill="none" stroke="#a6baff" stroke-width="8" stroke-dasharray="264 352" transform="rotate(-90 120 235)"/>
{text(79, 245, '25:00', 29, PAPER, 700)}{mono(217, 196, 'MAKE ROOM FOR FOCUS', 12, '#a6baff')}
<rect x="217" y="213" width="20" height="20" rx="5" fill="#a6baff"/><path d="M222 222L227 227L233 218" stroke="{INK}" fill="none" stroke-width="2"/>
{text(249, 230, 'One goal.', 21)}<rect x="217" y="249" width="20" height="20" rx="5" stroke="#707a9c" fill="none"/>
{text(249, 266, 'One good session.', 21)}{mono(217, 298, 'PLAN → FOCUS → REFLECT', 11, '#a6baff')}'''
    card('studyflow.svg', 'StudyFlow', '03 / LEARNING + FOCUS', '#a6baff', study, 'A plan that actually meets you at the desk.')
    panther = f'''<rect x="28" y="158" width="544" height="154" rx="10" fill="#28221e"/>
<g transform="translate(53 176)"><rect width="493" height="119" rx="2" fill="#eee4d3"/>
{text(15, 29, 'THE PANTHER PRESS', 25, '#342820', 700, family='Georgia, serif')}{mono(410, 27, 'VOL. 01', 10, '#66554a')}
<path d="M15 39H478" stroke="#342820"/><rect x="15" y="51" width="100" height="52" fill="#bb987a"/>
<path d="M15 103L46 66L69 87L87 75L115 103" fill="#6e594c"/>{text(130, 69, 'A place for student voices.', 18, '#342820', 700, family='Georgia, serif')}
<path d="M130 83H391M130 92H385M130 101H350M418 54H478M418 64H473M418 74H478M418 84H463M418 94H478M418 104H455" stroke="#b2a08c"/></g>'''
    card('panther-press.svg', 'Panther Press', '04 / EDITORIAL + COMMUNITY', '#e9b891', panther, 'Student stories, with a home of their own.')

def footer():
    body = f'''<rect width="1200" height="168" rx="16" fill="{LIME}"/>{mono(34, 37, 'THE NEXT SIDE QUEST', 14, INK)}
{text(30, 112, 'What if we built it?', 67, INK, 700, extra='letter-spacing="-3"')}
<path d="M1072 111L1140 43M1083 43H1140V100" fill="none" stroke="{INK}" stroke-width="6"/>{star(969, 84, 29, INK)}'''
    svg('footer.svg', 1200, 168, 'The next side quest: What if we built it?', body)

if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    hero()
    projects()
    footer()
    print('Built 6 self-contained SVG assets.')
