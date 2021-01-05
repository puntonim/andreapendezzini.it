from bs4 import BeautifulSoup

import utils


class ParseIndexDesktop:
    KEYWORD = "index"
    TITLE = "Home"

    def __init__(self):
        self.soup = None
        self.IMG_DIR = utils.DOCS_DIR / "assets" / "img" / self.KEYWORD
        self.SOURCE_PAGE = utils.HTML_SOURCE_DIR / f"{self.KEYWORD}-desktop.html"
        self.PAGE = utils.DOCS_DIR / f"{self.KEYWORD}.html"
        self.MAIN_CSS = (
            utils.DOCS_DIR
            / "assets"
            / "css"
            / self.KEYWORD
            / f"{self.KEYWORD}-desktop.css"
        )
        self.DOTS_TO_ROOT = "."

    def read_html(self):
        return utils.read_file(self.SOURCE_PAGE)

    def remove_all_comments(self):
        self.soup = utils.remove_all_comments(self.soup)

    def remove_all_scripts(self):
        self.soup = utils.remove_all_scripts(self.soup)

    def move_out_css(self):
        self.soup = utils.move_out_css(self.MAIN_CSS, self.soup)

    def replace_head(self):
        raw_content = utils.get_raw_head(
            title=self.TITLE, dots_to_root=self.DOTS_TO_ROOT
        )
        raw_content += f"""
            <link href="{self.DOTS_TO_ROOT}/assets/css/{self.KEYWORD}/{self.KEYWORD}-desktop.css" rel="stylesheet"/>
            <link href="{self.DOTS_TO_ROOT}/assets/css/desktop-nimiq.css" rel="stylesheet"/>
            
           <script type='text/javascript' src='{self.DOTS_TO_ROOT}/assets/js/main-desktop.js'></script>
        """
        self.soup = utils.replace_head(raw_content, self.soup)

    def remove_ads_bar(self):
        add_bar = self.soup.find("div", {"id": "WIX_ADS"})
        add_bar.decompose()
        return self.soup

    def replace_copyright(self):
        self.soup = utils.replace_copyright(self.soup)

    def fix_links_in_menu(self):
        # Menu bar: Home.
        self.soup = utils.replace_href_in_li_a(
            "comp-j6htgi840", "./index.html", self.soup
        )
        # Menu bar: Chi sono.
        self.soup = utils.replace_href_in_li_a(
            "comp-j6htgi841", "./index.html#chi-sono", self.soup
        )
        # Menu bar: Orientamento terapeutico.
        self.soup = utils.replace_href_in_li_a(
            "comp-j6htgi842", "./terapia.html", self.soup
        )
        # Menu bar: Ambiti di Intervento.
        self.soup = utils.replace_href_in_li_a(
            "comp-j6htgi843", "./terapia.html#ambiti-intervento", self.soup
        )
        # Menu bar: Psicosomatica.
        self.soup = utils.replace_href_in_li_a(
            "comp-j6htgi844", "./psicosomatica.html", self.soup
        )
        # Menu bar: Trauma.
        self.soup = utils.replace_href_in_li_a(
            "comp-j6htgi845", "./trauma.html", self.soup
        )
        # Menu bar: Contatti.
        self.soup = utils.replace_href_in_li_a(
            "comp-j6htgi846", "./index.html#contatti", self.soup
        )

    def fix_internal_links_in_menu(self):
        # Menu bar: Chi sono.
        self.soup = utils.replace_href_in_li_a("comp-j6htgi841", "#chi-sono", self.soup)
        # self.soup = utils.replace_id(
        #     "comp-j6w6mgxz", "chi-sono", self.soup, self.MAIN_CSS
        # )
        # Menu bar: Contatti.
        self.soup = utils.replace_href_in_li_a("comp-j6htgi846", "#contatti", self.soup)
        # self.soup = utils.replace_id(
        #     "comp-j6w6mgyg", "contatti", self.soup, self.MAIN_CSS
        # )

    def replace_remote_images_with_local(self):
        self.soup = utils.replace_remote_images_with_local(
            self.IMG_DIR, self.soup, dots_to_root=self.DOTS_TO_ROOT
        )

    def add_mobile_redirection(self):
        head = self.soup.find("head")
        raw_content = f"""
            <script type='text/javascript' src='{self.DOTS_TO_ROOT}/assets/js/redirect-mobile.js'></script>
        """
        head.insert(0, BeautifulSoup(raw_content, "html.parser"))

    def save_html(self):
        utils.write_file(self.PAGE, self.soup.prettify())

    def parse(self):
        html = self.read_html()
        self.soup = BeautifulSoup(html, "html.parser")
        self.remove_all_comments()
        self.remove_all_scripts()
        self.move_out_css()
        self.replace_head()
        self.remove_ads_bar()
        self.replace_copyright()
        self.fix_links_in_menu()
        self.fix_internal_links_in_menu()
        self.replace_remote_images_with_local()
        self.add_mobile_redirection()
        self.save_html()


class ParseIndexMobile(ParseIndexDesktop):
    KEYWORD = "index"

    def __init__(self):
        super().__init__()
        self.SOURCE_PAGE = utils.HTML_SOURCE_DIR / f"{self.KEYWORD}-mobile.html"
        self.PAGE = utils.DOCS_DIR / "m" / f"{self.KEYWORD}.html"
        self.MAIN_CSS = (
            utils.DOCS_DIR
            / "assets"
            / "css"
            / self.KEYWORD
            / f"{self.KEYWORD}-mobile.css"
        )
        self.DOTS_TO_ROOT = ".."

    def replace_head(self):
        raw_content = utils.get_raw_head(
            title=self.TITLE, dots_to_root=self.DOTS_TO_ROOT
        )
        raw_content += f"""
            <link href="{self.DOTS_TO_ROOT}/assets/css/{self.KEYWORD}/{self.KEYWORD}-mobile.css" rel="stylesheet"/>
            <link href="{self.DOTS_TO_ROOT}/assets/css/mobile-nimiq.css" rel="stylesheet"/>
            
            <script type='text/javascript' src='{self.DOTS_TO_ROOT}/assets/js/main-mobile.js'></script>
        """
        self.soup = utils.replace_head(raw_content, self.soup)

    def fix_viewport(self):
        head = self.soup.find("head")
        head.find("meta", {"name": "viewport"}).decompose()
        raw_content = """
            <meta content="width=320, user-scalable=yes" id="wixMobileViewport" name="viewport"/>
        """
        head.append(BeautifulSoup(raw_content, "html.parser"))

    def add_mobile_menu(self):
        site_header_wrapper = self.soup.find("header", {"id": "SITE_HEADER_WRAPPER"})
        raw_content = utils.read_file(utils.MOBILE_MENU)
        site_header_wrapper.insert_before(BeautifulSoup(raw_content, "html.parser"))

    def fix_internal_links_in_menu(self):
        # Menu bar: Chi sono.
        # self.soup = utils.replace_id(
        #     "comp-khi93rum", "chi-sono", self.soup, self.MAIN_CSS
        # )
        self.soup = utils.replace_href_in_a(
            "menu-link-chi-sono", "#chi-sono", self.soup
        )

        # Menu bar: Contatti.
        # self.soup = utils.replace_id(
        #     "comp-j6w6mgyg", "contatti", self.soup, self.MAIN_CSS
        # )
        self.soup = utils.replace_href_in_a(
            "menu-link-contatti", "#contatti", self.soup
        )

    def parse(self):
        html = self.read_html()
        self.soup = BeautifulSoup(html, "html.parser")
        self.remove_all_comments()
        self.remove_all_scripts()
        self.move_out_css()
        self.replace_head()
        self.fix_viewport()
        self.remove_ads_bar()
        self.replace_copyright()
        self.add_mobile_menu()
        self.fix_internal_links_in_menu()
        self.replace_remote_images_with_local()
        self.add_mobile_redirection()
        self.save_html()


def main():
    ParseIndexDesktop().parse()
    ParseIndexMobile().parse()


if __name__ == "__main__":
    main()
