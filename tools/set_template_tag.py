#!/usr/bin/env python3
"""Point this book's index.html at another tag of the quiz template.

    python3 tools/set_template_tag.py 2.2.0

index.html loads its code from one tagged copy of
eckko/recall-quiz-site-template on jsDelivr. Use an exact tag such as
2.2.0, never a branch: a tag never changes, so the site never changes
under you. Commit the changed index.html afterwards.
"""

import re
import sys
from pathlib import Path

INDEX_FILE = Path(__file__).resolve().parent.parent / "index.html"
VERSION_PATTERN = re.compile(r"^\d+(\.\d+){0,2}$")
TAG_IN_ADDRESS = re.compile(r"(recall-quiz-site-template)@[^/\"]+")
TAG_IN_COMMENT = re.compile(r"(CDN at tag )[^\s.]+(?:\.[^\s.]+)*")


def new_page(page, version):
    """The page text with every template tag replaced by `version`."""
    page = TAG_IN_ADDRESS.sub(rf"\1@{version}", page)
    return TAG_IN_COMMENT.sub(rf"\g<1>{version}", page)


def main():
    """Rewrite index.html for the tag given on the command line."""
    if len(sys.argv) != 2 or not VERSION_PATTERN.match(sys.argv[1]):
        sys.exit("Usage: python3 tools/set_template_tag.py 2.2.0 "
                 "(an exact tag, not a branch)")
    page = INDEX_FILE.read_text(encoding="utf-8")
    if "recall-quiz-site-template@" not in page:
        sys.exit("index.html does not load the template from a CDN tag.")
    INDEX_FILE.write_text(new_page(page, sys.argv[1]), encoding="utf-8")
    print(f"index.html now loads the template at tag {sys.argv[1]}")


if __name__ == "__main__":
    main()
