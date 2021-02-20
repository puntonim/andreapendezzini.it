import parse_index
import utils

IMG_DIR = utils.DOCS_DIR / "assets" / "img" / "psicosomatica"


class ParsePsicosomaticaDesktop(parse_index.ParseIndexDesktop):
    KEYWORD = "psicosomatica"
    TITLE = "Psicosomatica"

    def fix_internal_links_in_menu(self):
        pass


class ParsePsicosomaticaMobile(parse_index.ParseIndexMobile):
    KEYWORD = "psicosomatica"
    TITLE = "Psicosomatica"

    def fix_internal_links_in_menu(self):
        pass


def main():
    ParsePsicosomaticaDesktop().parse()
    ParsePsicosomaticaMobile().parse()


if __name__ == "__main__":
    main()
