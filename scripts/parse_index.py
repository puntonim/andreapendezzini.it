from bs4 import BeautifulSoup

import utils

IMG_DIR = utils.DOCS_DIR / "assets" / "img" / "index"


class ParseIndexDesktop:
    SOURCE_INDEX = utils.HTML_SOURCE_DIR / "index-desktop.html"
    INDEX = utils.DOCS_DIR / "index.html"
    MAIN_CSS = utils.DOCS_DIR / "assets" / "css" / "index" / "main-desktop.css"
    DOTS_TO_ROOT = "."

    def __init__(self):
        self.soup = None

    def read_html(self):
        return utils.read_file(self.SOURCE_INDEX)

    def remove_all_comments(self):
        self.soup = utils.remove_all_comments(self.soup)

    def remove_all_scripts(self):
        self.soup = utils.remove_all_scripts(self.soup)

    def move_out_css(self):
        self.soup = utils.move_out_css(self.MAIN_CSS, self.soup)

    def replace_head(self):
        raw_content = f"""
            <link href="{self.DOTS_TO_ROOT}/assets/css/index/main-desktop.css" rel="stylesheet"/>
            <link href="{self.DOTS_TO_ROOT}/assets/css/index/main-desktop-nimiq.css" rel="stylesheet"/>
        """
        self.soup = utils.replace_head(raw_content, self.soup)

    def remove_ads_bar(self):
        add_bar = self.soup.find("div", {"id": "WIX_ADS"})
        add_bar.decompose()
        return self.soup

    def replace_copyright(self):
        self.soup = utils.replace_copyright(self.soup)

    def fix_internal_anchors(self):
        # Replace "comp-j6w6mgxz" with "chi-sono".
        self.soup = utils.replace_id(
            "comp-j6w6mgxz", "chi-sono", self.soup, self.MAIN_CSS
        )
        self.soup = utils.replace_href_in_data_anchor(
            "dataItem-j6w6mgyd1", "#chi-sono", self.soup
        )

        # Replace "comp-j6w6mgyg" with "contatti".
        self.soup = utils.replace_id(
            "comp-j6w6mgyg", "contatti", self.soup, self.MAIN_CSS
        )
        self.soup = utils.replace_href_in_data_anchor(
            "dataItem-j6w6mgyf1", "#contatti", self.soup
        )

    def replace_remote_images_with_local(self):
        self.soup = utils.replace_remote_images_with_local(
            IMG_DIR, self.soup, dots_to_root=self.DOTS_TO_ROOT
        )

    def add_mobile_redirection(self):
        head = self.soup.find("head")
        raw_content = f"""
            <script type='text/javascript' src='{self.DOTS_TO_ROOT}/assets/js/redirect-mobile.js'></script>
        """
        head.insert(0, BeautifulSoup(raw_content, "html.parser"))

    def save_html(self):
        utils.write_file(self.INDEX, self.soup.prettify())

    def parse(self):
        html = self.read_html()
        self.soup = BeautifulSoup(html, "html.parser")
        self.remove_all_comments()
        self.remove_all_scripts()
        self.move_out_css()
        self.replace_head()
        self.remove_ads_bar()
        self.replace_copyright()
        self.fix_internal_anchors()
        self.replace_remote_images_with_local()
        self.add_mobile_redirection()
        self.save_html()


class ParseIndexMobile(ParseIndexDesktop):
    SOURCE_INDEX = utils.HTML_SOURCE_DIR / "index-mobile.html"
    INDEX = utils.DOCS_DIR / "m" / "index.html"
    MAIN_CSS = utils.DOCS_DIR / "assets" / "css" / "index" / "main-mobile.css"
    DOTS_TO_ROOT = ".."

    def replace_head(self):
        raw_content = f"""
            <meta content="width=320, user-scalable=yes" id="wixMobileViewport" name="viewport"/>
            <link href="{self.DOTS_TO_ROOT}/assets/css/index/main-mobile.css" rel="stylesheet"/>
            <link href="{self.DOTS_TO_ROOT}/assets/css/index/main-mobile-nimiq.css" rel="stylesheet"/>
            
            <script
                src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
                integrity="sha256-4+XzXVhsDmqanXGHaHvgh1gMQKX40OUvDEBTu8JcmNs="
                crossorigin="anonymous">
            </script>
            <script type='text/javascript' src='{self.DOTS_TO_ROOT}/assets/js/main.js'></script>
        """
        self.soup = utils.replace_head(raw_content, self.soup)

    def add_mobile_menu(self):
        site_header_wrapper = self.soup.find("header", {"id": "SITE_HEADER_WRAPPER"})
        raw_content = utils.read_file(utils.MOBILE_MENU)
        site_header_wrapper.insert_before(BeautifulSoup(raw_content, "html.parser"))

    def fix_internal_anchors(self):
        # Replace "comp-khi93rum" with "chi-sono".
        self.soup = utils.replace_id(
            "comp-khi93rum", "chi-sono", self.soup, self.MAIN_CSS
        )
        self.soup = utils.replace_href_in_data_anchor(
            "dataItem-j6w6mgyd1", "#chi-sono", self.soup
        )

        # Replace "comp-j6w6mgyg" with "contatti".
        self.soup = utils.replace_id(
            "comp-j6w6mgyg", "contatti", self.soup, self.MAIN_CSS
        )
        self.soup = utils.replace_href_in_data_anchor(
            "dataItem-j6w6mgyf1", "#contatti", self.soup
        )

    def parse(self):
        html = self.read_html()
        self.soup = BeautifulSoup(html, "html.parser")
        self.remove_all_comments()
        self.remove_all_scripts()
        self.move_out_css()
        self.replace_head()
        self.remove_ads_bar()
        self.replace_copyright()
        self.add_mobile_menu()
        self.fix_internal_anchors()
        self.replace_remote_images_with_local()
        self.add_mobile_redirection()
        self.save_html()


if __name__ == "__main__":
    parser_desktop = ParseIndexDesktop()
    parser_desktop.parse()

    parser_mobile = ParseIndexMobile()
    parser_mobile.parse()
