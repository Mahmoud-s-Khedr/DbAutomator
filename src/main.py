#!/usr/bin/env python3

import os
import shutil
import datetime
import logging
import argparse
from pathlib import Path
    

# Configuration
DB_PATH = Path('/path/to/your/database.db')# Path to your SQLite database
BACKUP_DIR = Path('/var/backups')
LOG_FILE = Path('/var/log/DBAutomator.log')

def initialize():
    if not BACKUP_DIR.exists():
        BACKUP_DIR.mkdir()

    if not LOG_FILE.exists():
        with open(LOG_FILE, 'w'):
            pass


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
    

def backup_database():
    try:
        if not DB_PATH.exists():
            raise FileNotFoundError(f"Database file not found: {DB_PATH}")
            
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        backup_file = f"backup_{timestamp}.db"
        backup_path = BACKUP_DIR / backup_file
        
        shutil.copy2(DB_PATH, backup_path)
        logging.info(f"Backup created successfully: {backup_file}")
    
        return True
    except Exception as e:
        logging.error(f"Backup failed: {str(e)}")
        return False

def restore_database(backup_file):
    try:
        backup_path = BACKUP_DIR / backup_file
        

        if DB_PATH.exists():
            logging.warning("Overwriting existing database")
        
        shutil.copy2(backup_path, DB_PATH)
            
        logging.info(f"Database restored successfully from: {backup_file}")
        return True
    except Exception as e:
        logging.error(f"Restore failed: {str(e)}")
        return False

def list_backup_files():
    backup_files = [f for f in os.listdir(BACKUP_DIR) if f.startswith("backup_")]
    print("Available backup files:")
    for i, f in enumerate(backup_files, 1):
        print(f"{i}. {f}")

if __name__ == "__main__":
    initialize()
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--backup", action="store_true", help="Create a backup")
    parser.add_argument("--restore", action="store_true", help="Restore a backup file")
    args = parser.parse_args()
    
    if args.backup:
        backup_database()
    elif args.restore:
        list_backup_files()
        backup_file = input("Enter the backup file name: ")
        if restore_database(backup_file):
            print("Database restored successfully")
        else:
            print("Database restore failed")
    else:
        print("Please specify either --backup or --restore")
    