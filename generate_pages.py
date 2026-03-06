import re
import os

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Exact matching using capturing groups to keep delimiters
pattern = r"(<!-- ════+ .+? ════+ -->)"
parts = re.split(pattern, html)

# parts will have 21 elements:
# 0: header
# 1: comment NAVBAR
# 2: content NAVBAR
# 3: comment HERO
# 4: content HERO
# 5: comment PROBLEMA
# 6: content PROBLEMA
# 7: comment METODO
# 8: content METODO
# 9: comment SOCIAL PROOF
# 10: content SOCIAL PROOF
# 11: comment TRATTAMENTI
# 12: content TRATTAMENTI
# 13: comment CHI SONO
# 14: content CHI SONO
# 15: comment CONTATTI
# 16: content CONTATTI
# 17: comment FOOTER
# 18: content FOOTER
# 19: comment STICKY
# 20: content STICKY + footer close

header = parts[0]
nav_c = parts[1]
nav_v = parts[2]
hero_c = parts[3]
hero_v = parts[4]
prob_c = parts[5]
prob_v = parts[6]
meto_c = parts[7]
meto_v = parts[8]
soc_c = parts[9]
soc_v = parts[10]
trat_c = parts[11]
trat_v = parts[12]
chi_c = parts[13]
chi_v = parts[14]
cont_c = parts[15]
cont_v = parts[16]
foot_c = parts[17]
foot_v = parts[18]
stick_c = parts[19]
stick_v = parts[20]

# --- MODIFICATIONS FOR INDEX ---

# 1. Navbar index links
nav_v_idx = nav_v.replace('href="#trattamenti"', 'href="trattamenti.html"')
nav_v_idx = nav_v_idx.replace('<li><a href="#metodo" class="navbar__link">Il Metodo</a></li>', 
                              '<li><a href="#chi-sono" class="navbar__link">Chi Sono</a></li>\n                <li><a href="#metodo" class="navbar__link">Il Metodo</a></li>')
nav_v_idx = nav_v_idx.replace('<li><a href="#chi-sono" class="navbar__link">Chi Sono</a></li>\n                <li><a href="#contatti" class="navbar__link">Contatti</a></li>', 
                              '<li><a href="#contatti" class="navbar__link">Contatti</a></li>')

# 2. Chi Sono background to match dark instead of light
chi_v_idx = chi_v.replace('class="section section--light"', 'class="section section--dark"')
chi_v_idx = chi_v_idx.replace('class="section__tag"', 'class="section__tag section__tag--light"')
chi_v_idx = chi_v_idx.replace('class="section__title"', 'class="section__title section__title--light"')
chi_v_idx = chi_v_idx.replace('class="about__lead"', 'class="about__lead section__subtitle--light"')

# 3. Metodo background to match light instead of dark
meto_v_idx = meto_v.replace('class="section section--dark"', 'class="section section--light"')
meto_v_idx = meto_v_idx.replace('class="section__tag section__tag--light"', 'class="section__tag"')
meto_v_idx = meto_v_idx.replace('class="section__title section__title--light"', 'class="section__title"')
meto_v_idx = meto_v_idx.replace('class="section__subtitle section__subtitle--light"', 'class="section__subtitle"')

# 4. Footer links
foot_v_idx = foot_v.replace('href="#trattamenti"', 'href="trattamenti.html"')

# Order: Hero, Problema, Chi Sono, Metodo, Contatti, Social Proof
index_html = (
    header +
    nav_c + nav_v_idx +
    hero_c + hero_v +
    prob_c + prob_v +
    chi_c + chi_v_idx +
    meto_c + meto_v_idx +
    cont_c + cont_v +
    soc_c + soc_v +
    foot_c + foot_v_idx +
    stick_c + stick_v
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)


# --- MODIFICATIONS FOR TRATTAMENTI ---

header_tratt = header.replace('<title>Fisioproject — Fisioterapista a Prato | Dott. Valentino Alessi</title>', '<title>Trattamenti | Fisioproject</title>')

nav_v_trt = nav_v.replace('href="#problema"', 'href="index.html#problema"')
nav_v_trt = nav_v_trt.replace('href="#metodo"', 'href="index.html#metodo"')
nav_v_trt = nav_v_trt.replace('href="#recensioni"', 'href="index.html#recensioni"')
nav_v_trt = nav_v_trt.replace('href="#trattamenti"', 'href="#"')
nav_v_trt = nav_v_trt.replace('href="#chi-sono"', 'href="index.html#chi-sono"')
nav_v_trt = nav_v_trt.replace('href="#contatti"', 'href="index.html#contatti"')
nav_v_trt = nav_v_trt.replace('href="#hero"', 'href="index.html"')

trat_v_trt = trat_v.replace('class="section section--gradient"', 'class="section section--gradient" style="padding-top: 180px; min-height: 80vh;"')

foot_v_trt = foot_v.replace('href="#problema"', 'href="index.html#problema"')
foot_v_trt = foot_v_trt.replace('href="#metodo"', 'href="index.html#metodo"')
foot_v_trt = foot_v_trt.replace('href="#trattamenti"', 'href="#"')
foot_v_trt = foot_v_trt.replace('href="#chi-sono"', 'href="index.html#chi-sono"')
foot_v_trt = foot_v_trt.replace('href="#contatti"', 'href="index.html#contatti"')

tratt_html = (
    header_tratt +
    nav_c + nav_v_trt +
    trat_c + trat_v_trt +
    foot_c + foot_v_trt +
    stick_c + stick_v
)

with open("trattamenti.html", "w", encoding="utf-8") as f:
    f.write(tratt_html)

print("HTML generated successfully! lengths: index=", len(index_html.split('\\n')), "trattamenti=", len(tratt_html.split('\\n')))
