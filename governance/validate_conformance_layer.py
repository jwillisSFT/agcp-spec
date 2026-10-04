#!/usr/bin/env python3
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("validate_v2_1_x_conformance_layer.py")), run_name="__main__")
