"""
Copyright (c) Cutleast
"""

import sys
from argparse import ArgumentParser
from dynamic_interface_patcher.app import App

def main():
    # Parse command-line arguments
    parser = ArgumentParser()
    parser.add_argument('--debug', action='store_true', help="Enable debug mode")
    parser.add_argument('--silent', action='store_true', help="Run in silent mode")
    parser.add_argument('--repack_bsa', action='store_true', help="Repack BSA")
    parser.add_argument('--output_path', type=str, help="Path for output files")
    parser.add_argument('--patchpath', type=str, help="Path to the patch")
    parser.add_argument('--originalpath', type=str, help="Path to the original files")
    args = parser.parse_args()

    # Initialize and run GUI
    app = App(args)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
