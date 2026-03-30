import logging
import os
import os.path as path

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


SRC_PATH = "./src"
REFERENCES_PATH = "./references"

HEADER_FILE_NAME = "header.html"
FOOTER_FILE_NAME = "footer.html"


all_build_files = os.listdir(SRC_PATH)
with open(path.join(SRC_PATH, HEADER_FILE_NAME)) as header_file:
    header_file_content = header_file.read()
with open(path.join(SRC_PATH, FOOTER_FILE_NAME)) as footer_file:
    footer_file_content = footer_file.read()

log.info("*** BUILD DIR ***********")
log.info(all_build_files);
log.info(f"*** HEADER CONTENT ****** \n{header_file_content}")
log.info(f"*** FOOTER CONTENT ****** \n{footer_file_content}")


content_files = [
    filename for filename
    in all_build_files
    if filename != HEADER_FILE_NAME and filename != FOOTER_FILE_NAME
]
log.info(f"*** CONTENT FILES ****** \n{content_files}")

for filename in content_files:
    with open(path.join(SRC_PATH, filename)) as f:
        log.info(f"Processing {filename}")
        content = f.readlines()
        body_start = content.index("<body>\n")
        body_end = content.index("</body>\n")
        body_content = "\n".join(content[body_start + 1 : body_end])
        log.info(f"*** PURE CONTENT ****** \n{body_content}")

log.info("*************************")