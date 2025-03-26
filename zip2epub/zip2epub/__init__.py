import os

try: 
    cacheFolder = toml.load(os.path.expanduser('~/.config/zip2epub/config.toml'))[cacheFolder]
except:
    cacheFolder = os.path.expanduser('~/.cache/zip2epub')