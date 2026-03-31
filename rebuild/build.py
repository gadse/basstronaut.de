import logging
import os
import os.path as path
from AdvancedHTMLParser import AdvancedHTMLParser

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


SRC_PATH = "./src"
REFERENCES_PATH = "./references"
HEADER_FILE_NAME = "./header.html"
FOOTER_FILE_NAME = "footer.html"


def get_body(filename):
    parser = AdvancedHTMLParser()
    parser.parseFile(path.join(SRC_PATH, filename))
    body = parser.body
    return str(body.text.strip())


def read_header():
    return get_body(HEADER_FILE_NAME)


def read_footer():
    return get_body(FOOTER_FILE_NAME)


def list_content_files():
    return [
        filename
        for filename in all_build_files
        if filename != HEADER_FILE_NAME and filename != FOOTER_FILE_NAME
    ]


def list_all_build_files() -> list[str]:
    return os.listdir(SRC_PATH)

if __name__ == "__main__":
    all_build_files = list_all_build_files()
    content_files = list_content_files()
    header_file_content = read_header()
    footer_file_content = read_footer()

    log.info(f"*** BUILD DIR ***********\n{all_build_files}")
    log.info(f"*** HEADER CONTENT ******\n{header_file_content}")
    log.info(f"*** FOOTER CONTENT ******\n{footer_file_content}")
    log.info(f"*** CONTENT FILES ******\n{content_files}")

    for filename in content_files:
        log.info(f"Processing {filename}")
        body_content = get_body(filename)
        log.info(f"*** PURE CONTENT ****** \n{body_content}")

    log.info("*************************")
