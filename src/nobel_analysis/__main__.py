"""!
@file __main__.py
@brief Entry point of `python -m nobel_analysis`.
"""

import sys

from nobel_analysis.presentation.cli import main

if __name__ == "__main__":
    sys.exit(main())
