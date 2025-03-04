import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    LEDGER_FILE = os.environ.get('LEDGER_FILE') or 'data/ledger.json' #File path for the decentralized ledger