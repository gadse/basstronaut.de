import logging
import os
import os.path as path
from AdvancedHTMLParser import AdvancedHTMLParser

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

SRC_PATH = "./src"
REFERENCES_PATH = "./references"
HEADER_FILE_NAME = "header.html"
FOOTER_FILE_NAME = "footer.html"


def get_body(filename):
    parser = AdvancedHTMLParser()
    p = path.join(".", filename)
    parser.parseFile(p)
    body = parser.body
    return str(body.text.strip())


def read_header():
    return get_body("/".join((SRC_PATH, HEADER_FILE_NAME)))


def read_footer():
    return get_body("/".join((SRC_PATH, FOOTER_FILE_NAME)))


def list_all_build_files() -> list[str]:
    return os.listdir(SRC_PATH)


def enrich(content, header="", footer=""):
    return "\n".join([header, content, footer])


def build_website():
    def list_content_files():
        return [
            filename
            for filename in all_build_files
            if filename != HEADER_FILE_NAME and filename != FOOTER_FILE_NAME
        ]

    all_build_files = list_all_build_files()
    content_files = list_content_files()
    header = read_header()
    footer = read_footer()

    log.info(f"*** BUILD DIR ***********\n{all_build_files}")
    log.info(f"*** HEADER CONTENT ******\n{header}")
    log.info(f"*** FOOTER CONTENT ******\n{footer}")
    log.info(f"*** CONTENT FILES ******\n{content_files}")

    for filename in content_files:
        body_content = get_body(path.join(SRC_PATH, filename))
        enriched = enrich(body_content, header, footer)
        log.info(f"Processed {filename}\n{enriched}")

    log.info("*************************")


if __name__ == "__main__":
    build_website()
