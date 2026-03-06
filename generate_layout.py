import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Split the file by the specific comments to get the big blocks
def extract_section(name, html):
    pattern = rf"(<!-- ════+ {name} ════+ -->.*?)(?=\n\s*<!-- ════+ \w+(?: \w+)* \(?(?:Mobile)?\)? *════+ -->|\n\s*</body)"
    match = re.search(pattern, html, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

navbar_section = extract_section("NAVBAR", html)
hero_section = extract_section("HERO", html)
problema_section = extract_section("PROBLEMA", html)
metodo_section = extract_section("METODO", html)
social_proof_section = extract_section("SOCIAL PROOF", html)
trattamenti_section = extract_section("TRATTAMENTI", html)
chi_sono_section = extract_section("CHI SONO", html)
contatti_section = extract_section("CONTATTI", html)
footer_section = extract_section("FOOTER", html)

# We need to manually construct index.html since we are moving things around.
header_match = re.match(r"(.*?<!-- ════+ NAVBAR)", html, re.DOTALL)
header = header_match.group(1).replace("<!-- ═══════════════════════════════════ NAVBAR", "").strip()

footer_scripts_match = re.search(r"(<!-- ════+ STICKY WHATSAPP \(Mobile\) ════+ -->.*)", html, re.DOTALL)
footer_scripts = footer_scripts_match.group(1).strip()

# Modify navbar links in index.html
new_navbar_index = navbar_section.replace('href="#trattamenti"', 'href="trattamenti.html"')
new_footer_index = footer_section.replace('href="#trattamenti"', 'href="trattamenti.html"')

new_index_html = f"""{header}

    <!-- ═══════════════════════════════════ NAVBAR ═══════════════════════════════════ -->
    {new_navbar_index}

    <!-- ═══════════════════════════════════ HERO ═══════════════════════════════════ -->
    {hero_section}

    <!-- ═══════════════════════════════════ PROBLEMA ═══════════════════════════════════ -->
    {problema_section}

    <!-- ═══════════════════════════════════ METODO ═══════════════════════════════════ -->
    {metodo_section}

    <!-- ═══════════════════════════════════ CHI SONO ═══════════════════════════════════ -->
    {chi_sono_section}

    <!-- ═══════════════════════════════════ CONTATTI ═══════════════════════════════════ -->
    {contatti_section}

    <!-- ═══════════════════════════════════ SOCIAL PROOF ═══════════════════════════════════ -->
    {social_proof_section}

    <!-- ═══════════════════════════════════ FOOTER ═══════════════════════════════════ -->
    {new_footer_index}

    <!-- ═══════════════════════════════════ STICKY WHATSAPP (Mobile) ═══════════════════════════════════ -->
    {footer_scripts}
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_index_html)

# Create trattamenti.html
new_navbar_tratt = navbar_section
new_navbar_tratt = new_navbar_tratt.replace('href="#problema"', 'href="index.html#problema"')
new_navbar_tratt = new_navbar_tratt.replace('href="#metodo"', 'href="index.html#metodo"')
new_navbar_tratt = new_navbar_tratt.replace('href="#recensioni"', 'href="index.html#recensioni"')
new_navbar_tratt = new_navbar_tratt.replace('href="#trattamenti"', 'href="#"')
new_navbar_tratt = new_navbar_tratt.replace('href="#chi-sono"', 'href="index.html#chi-sono"')
new_navbar_tratt = new_navbar_tratt.replace('href="#contatti"', 'href="index.html#contatti"')
new_navbar_tratt = new_navbar_tratt.replace('href="#hero"', 'href="index.html"')

new_footer_tratt = footer_section
new_footer_tratt = new_footer_tratt.replace('href="#problema"', 'href="index.html#problema"')
new_footer_tratt = new_footer_tratt.replace('href="#metodo"', 'href="index.html#metodo"')
new_footer_tratt = new_footer_tratt.replace('href="#trattamenti"', 'href="#"')
new_footer_tratt = new_footer_tratt.replace('href="#chi-sono"', 'href="index.html#chi-sono"')
new_footer_tratt = new_footer_tratt.replace('href="#contatti"', 'href="index.html#contatti"')

# Title adjustments
tratt_header = header.replace('<title>Fisioproject — Fisioterapista a Prato | Dott. Valentino Alessi</title>', '<title>Trattamenti | Fisioproject</title>')

# For trattamenti.html we probably want additional padding for the top section because there is no hero covering the header.
modified_trattamenti = trattamenti_section.replace('class="section section--gradient"', 'class="section section--gradient" style="padding-top: 180px; min-height: 80vh;"')

new_trattamenti_html = f"""{tratt_header}

    <!-- ═══════════════════════════════════ NAVBAR ═══════════════════════════════════ -->
    {new_navbar_tratt}

    <!-- ═══════════════════════════════════ TRATTAMENTI ═══════════════════════════════════ -->
    {modified_trattamenti}

    <!-- ═══════════════════════════════════ FOOTER ═══════════════════════════════════ -->
    {new_footer_tratt}

    <!-- ═══════════════════════════════════ STICKY WHATSAPP (Mobile) ═══════════════════════════════════ -->
    {footer_scripts}
"""

with open("trattamenti.html", "w", encoding="utf-8") as f:
    f.write(new_trattamenti_html)

print("HTML restructuring completed successfully.")
