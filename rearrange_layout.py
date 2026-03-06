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
chi_sono_section = extract_section("CHI SONO", html)
contatti_section = extract_section("CONTATTI", html)
social_proof_section = extract_section("SOCIAL PROOF", html)
footer_section = extract_section("FOOTER", html)

header_match = re.match(r"(.*?<!-- ════+ NAVBAR)", html, re.DOTALL)
header = header_match.group(1).replace("<!-- ═══════════════════════════════════ NAVBAR", "").strip()

footer_scripts_match = re.search(r"(<!-- ════+ STICKY WHATSAPP \(Mobile\) ════+ -->.*)", html, re.DOTALL)
footer_scripts = footer_scripts_match.group(1).strip()

# Change section backgrounds to alternate clearly
# Problema: section--light
# Chi Sono: section--dark
# Metodo: section--light
# Contatti: section--dark
# Social Proof: section--light -> (this is already section--light, so we keep)

chi_sono_clean = chi_sono_section.replace('class="section section--light"', 'class="section section--dark"')
chi_sono_clean = chi_sono_clean.replace('class="section__tag"', 'class="section__tag section__tag--light"')
chi_sono_clean = chi_sono_clean.replace('class="section__title"', 'class="section__title section__title--light"')
chi_sono_clean = chi_sono_clean.replace('class="about__lead"', 'class="about__lead section__subtitle--light"')

metodo_clean = metodo_section.replace('class="section section--dark"', 'class="section section--light"')
metodo_clean = metodo_clean.replace('class="section__tag section__tag--light"', 'class="section__tag"')
metodo_clean = metodo_clean.replace('class="section__title section__title--light"', 'class="section__title"')
metodo_clean = metodo_clean.replace('class="section__subtitle section__subtitle--light"', 'class="section__subtitle"')


new_navbar_index = navbar_section.replace('<li><a href="#metodo" class="navbar__link">Il Metodo</a></li>', 
                                          '<li><a href="#chi-sono" class="navbar__link">Chi Sono</a></li>\n                <li><a href="#metodo" class="navbar__link">Il Metodo</a></li>')
new_navbar_index = new_navbar_index.replace('<li><a href="#chi-sono" class="navbar__link">Chi Sono</a></li>\n                <li><a href="#contatti" class="navbar__link">Contatti</a></li>', 
                                          '<li><a href="#contatti" class="navbar__link">Contatti</a></li>')

new_index_html = f"""{header}

    <!-- ═══════════════════════════════════ NAVBAR ═══════════════════════════════════ -->
    {new_navbar_index}

    <!-- ═══════════════════════════════════ HERO ═══════════════════════════════════ -->
    {hero_section}

    <!-- ═══════════════════════════════════ PROBLEMA ═══════════════════════════════════ -->
    {problema_section}

    <!-- ═══════════════════════════════════ CHI SONO ═══════════════════════════════════ -->
    {chi_sono_clean}

    <!-- ═══════════════════════════════════ METODO ═══════════════════════════════════ -->
    {metodo_clean}

    <!-- ═══════════════════════════════════ CONTATTI ═══════════════════════════════════ -->
    {contatti_section}

    <!-- ═══════════════════════════════════ SOCIAL PROOF ═══════════════════════════════════ -->
    {social_proof_section}

    <!-- ═══════════════════════════════════ FOOTER ═══════════════════════════════════ -->
    {footer_section}

    <!-- ═══════════════════════════════════ STICKY WHATSAPP (Mobile) ═══════════════════════════════════ -->
    {footer_scripts}
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_index_html)

print("HTML restructuring completed successfully.")
