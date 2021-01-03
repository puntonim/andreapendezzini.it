from bs4 import BeautifulSoup

import parse_index
import utils


class ParseTerapiaDesktop(parse_index.ParseIndexDesktop):
    KEYWORD = "terapia"
    TITLE = "Terapia"

    def fix_internal_links_in_menu(self):
        # Menu bar: Ambiti di Intervento.
        self.soup = utils.replace_id(
            "comp-j6w85rn2", "ambiti-intervento", self.soup, self.MAIN_CSS
        )
        self.soup = utils.replace_href_in_li_a(
            "comp-j6htgi843", "#ambiti-intervento", self.soup
        )
        # Menu bar: Orientamento terapeutico.
        self.soup = utils.replace_href_in_li_a(
            "comp-j6htgi842", "./terapia.html", self.soup
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
        self.fix_links_in_menu()
        self.fix_internal_links_in_menu()
        self.replace_remote_images_with_local()
        self.add_mobile_redirection()
        self.save_html()


if __name__ == "__main__":
    parser_desktop = ParseTerapiaDesktop()
    parser_desktop.parse()
