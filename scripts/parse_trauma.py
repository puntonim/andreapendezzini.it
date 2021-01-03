from bs4 import BeautifulSoup

import parse_index
import utils


class ParseTraumaDesktop(parse_index.ParseIndexDesktop):
    KEYWORD = "trauma"
    TITLE = "Trauma"

    def fix_internal_links_in_menu(self):
        pass

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
    parser_desktop = ParseTraumaDesktop()
    parser_desktop.parse()
