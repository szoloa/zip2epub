from .zip2epub import main
import sys

def cli():
    main(sys.argv[1:])