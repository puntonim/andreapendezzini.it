from pathlib import Path

from bs4 import BeautifulSoup

import utils

HTML_FILE_PATHS = [
    Path().resolve().parent / "docs" / "index.html",
    Path().resolve().parent / "docs" / "psicosomatica.html",
    Path().resolve().parent / "docs" / "terapia.html",
    Path().resolve().parent / "docs" / "trauma.html",
    Path().resolve().parent / "docs" / "m" / "index.html",
    Path().resolve().parent / "docs" / "m" / "psicosomatica.html",
    Path().resolve().parent / "docs" / "m" / "terapia.html",
    Path().resolve().parent / "docs" / "m" / "trauma.html",
]


class AddGoogleAnalyticsScript:
    def __init__(self, path):
        self.soup = None
        self.path = path

    def read_html(self):
        return utils.read_file(self.path)

    def save_html(self):
        utils.write_file(self.path, self.soup.prettify())

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

    def add_google_analytics_script(self):
        head = self.soup.find("head")
        data_id = "google-gtag"
        for el in head.find_all("script", {"data-id": data_id}):
            el.decompose()
        # Notice that I am using `data-id` to make this fn idempotent.
        raw_content = f"""
        <script async data-id="{data_id}" src="https://www.googletagmanager.com/gtag/js?id=UA-163439271-2">
          // Global site tag (gtag.js) - Google Analytics part 1/2
        </script>
        <script data-id="{data_id}">
          // Global site tag (gtag.js) - Google Analytics part 2/2
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', 'UA-163439271-2');
        </script>
        """
        head.insert(0, BeautifulSoup(raw_content, "html.parser"))

    def run(self):
        html = self.read_html()
        self.soup = BeautifulSoup(html, "html.parser")
        self.add_google_analytics_script()
        self.save_html()


def add_google_script_to_all_pages():
    for path in HTML_FILE_PATHS:
        task = AddGoogleAnalyticsScript(path)
        task.run()


if __name__ == "__main__":
    print("START")
    add_google_script_to_all_pages()
    print("DONE")
