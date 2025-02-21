import telebot
import datetime
import sqlite3
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
BASE_DIR = CURRENT_FILE.parent
SQL_BASE = BASE_DIR / 'sleep_base.db'