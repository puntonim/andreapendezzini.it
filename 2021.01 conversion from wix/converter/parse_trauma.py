import parse_index


class ParseTraumaDesktop(parse_index.ParseIndexDesktop):
    KEYWORD = "trauma"
    TITLE = "Trauma"

    def fix_internal_links_in_menu(self):
        pass


class ParseTraumaMobile(parse_index.ParseIndexMobile):
    KEYWORD = "trauma"
    TITLE = "Trauma"

    def fix_internal_links_in_menu(self):
        pass


def main():
    ParseTraumaDesktop().parse()
    ParseTraumaMobile().parse()


if __name__ == "__main__":
    main()
