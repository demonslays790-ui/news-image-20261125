"""News-image entry runner.

Copies the pre-rendered entry.png sitting beside this script into the
grading output directory. No rendering happens here: the image was already
produced during the build, so grading only needs a faithful copy.

The script directory is resolved through the real path of this file, so the
copy still finds entry.png even when the grader invokes the script through
a symlink or from a different working directory.
"""

import os
import shutil
import sys

ENTRY_FILENAME = "entry.png"


def main() -> int:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    source = os.path.join(script_dir, ENTRY_FILENAME)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    destination = os.path.join(output_dir, ENTRY_FILENAME)
    shutil.copyfile(source, destination)
    os.chmod(destination, 0o644)

    print("Wrote {} ({} bytes)".format(destination, os.path.getsize(destination)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
