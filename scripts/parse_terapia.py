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


class ParseTerapiaMobile(parse_index.ParseIndexMobile):
    KEYWORD = "terapia"
    TITLE = "Terapia"

    def fix_internal_links_in_menu(self):
        # Menu bar: Ambiti di Intervento.
        self.soup = utils.replace_id(
            "comp-j6w85rn2", "ambiti-intervento", self.soup, self.MAIN_CSS
        )
        self.soup = utils.replace_href_in_a(
            "menu-link-ambiti-intervento", "#ambiti-intervento", self.soup
        )


def main():
    ParseTerapiaDesktop().parse()
    ParseTerapiaMobile().parse()


if __name__ == "__main__":
    main()
