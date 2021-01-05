import re
from pathlib import Path

import cssutils
import requests
from bs4 import BeautifulSoup, Comment

DO_USE_CSSUTILS = False
HTML_SOURCE_DIR = Path().resolve() / "html"
DOCS_DIR = Path().resolve().parent / "docs"
MOBILE_MENU = HTML_SOURCE_DIR / "mobile-menu.html"


def get_raw_head(title=None, description=None, dots_to_root="."):
    if title is None:
        title = ""
    else:
        title += " | "
    if description is None:
        description = "Psicoanalista di formazione junghiana, socio dell'Istituto di Milano e dell'Italia Settentrionale del Centro Italiano di Psicologia Analitica (CIPA) . Riceve privatamente in studio a Milano e a Bergamo , per analisi individuali, percorsi psicoterapeutici e supporto psicologico. Lavora con adolescenti, giovani e adulti."

    raw_head = f"""
      <meta charset="utf-8">
      <title>{title}dott. Andrea Pendezzini</title>
      <meta name="description" content="{description}">
      <meta name="viewport" content="width=device-width, initial-scale=1">
    
      <meta property="og:title" content="{title}dott. Andrea Pendezzini">
      <meta property="og:description" content="{description}">
      <meta property="og:type" content="website">
      <meta property="og:url" content="andreapendezzini.it">
      <meta property="og:image" content="https://andreapendezzini.it/assets/img/index/IMG-5622.webp">
    
      <link rel="manifest" href="{dots_to_root}/site.webmanifest">
      <link rel="icon" href="{dots_to_root}/assets/img/favicon/favicon.ico">
      <link rel="apple-touch-icon" href="{dots_to_root}/assets/img/favicon/apple-touch-icon.png">
    
      <meta name="theme-color" content="#d5e1df">
      
      <script
          src="https://code.jquery.com/jquery-3.5.1.min.js"
          integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
          crossorigin="anonymous">
      </script>    
    """
    return raw_head


def read_file(path):
    with open(path) as fin:
        return fin.read()


def write_file(path, content, is_binary=False):
    mode = "w"
    if is_binary:
        mode = "wb+"
    with open(path, mode) as fout:
        fout.write(content)


def remove_all_comments(soup):
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()
    return soup


def remove_all_scripts(soup):
    return _remove_all_elements("script", soup)


def _remove_all_elements(el_name, soup):
    for el in soup.find_all(el_name):
        el.decompose()
    return soup


def move_out_css(new_css_file_path, soup):
    all_css = ""
    for style in soup.find_all("style"):
        if DO_USE_CSSUTILS:
            css = cssutils.parseString(style.encode_contents(), validate=False)
            all_css += css.cssText.decode("utf8") + "\n"
        else:
            all_css += style.encode_contents().decode("utf8")
        style.decompose()

    all_css = all_css.replace(
        "//static.parastorage.com", "https://static.parastorage.com"
    )

    write_file(new_css_file_path, all_css)
    return soup


def replace_head(raw_content, soup):
    head = soup.find("head")
    head.clear()
    head.append(BeautifulSoup(raw_content, "html.parser"))
    return soup


def replace_copyright(soup):
    els = soup.find_all(text=re.compile("© 2020"))
    for el in els:
        new_el = el.replace("© 2020", "© 2021")
        el.replace_with(new_el)
    return soup


def replace_id(old_id, new_id, soup, css_file_path):
    # Replace in soup.
    el = soup.find(id=old_id)
    el["id"] = new_id
    # And replace in the css file.
    _replace_string_in_css(css_file_path, old_id, new_id)
    return soup


def _replace_string_in_css(css_file_path, old_string, new_string):
    all_css = read_file(css_file_path)
    all_css = all_css.replace(old_string, new_string)
    write_file(css_file_path, all_css)


def replace_href_in_a_data_anchor(data_anchor, href, soup):
    el = soup.find("a", {"data-anchor": data_anchor})
    el["href"] = href
    return soup


def replace_href_in_li_a(li_id, href, soup):
    el = soup.find("li", {"id": li_id})
    a = el.find("a")
    a["href"] = href
    return soup


def replace_href_in_a(a_id, href, soup):
    a = soup.find("a", {"id": a_id})
    a["href"] = href
    return soup


def replace_remote_images_with_local(img_dir, soup, dots_to_root="."):
    imgs = soup.find_all("img")
    for img in imgs:
        path = _download_file(img["src"], img_dir)
        rel_path = dots_to_root + "/assets/" + str(path).split("/assets/")[1]
        img["src"] = rel_path
    return soup


def _download_file(url, dir):
    file_name = url.split("/")[-1]
    local_file_path = dir / file_name
    if not local_file_path.is_file():
        r = requests.get(url, timeout=30)
        write_file(local_file_path, r.content, is_binary=True)
    return local_file_path
