# f1_config.py
import os
import fastf1

# Cache directory
CACHE_DIR = 'cache_data'
os.makedirs(CACHE_DIR, exist_ok=True)

# Enable FastF1 cache
fastf1.Cache.enable_cache(CACHE_DIR)
