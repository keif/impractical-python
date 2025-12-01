"""Profile the palingrams find_palingrams function."""

import cProfile
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPT_DIR.parent))

import main  # noqa: E402

cProfile.run(f"{main.__name__}.find_palingrams({main.__name__}.WORD_LIST)")
