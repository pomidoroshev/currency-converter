import os

REDIS_DSN = os.getenv('REDIS_DSN', 'redis://localhost')
STORAGE_NAME = os.getenv('STORAGE_NAME', 'rates')
