# DBAutomator

**DBAutomator** is a simple and automated database backup and restore script written in Python. It allows you to easily create backups of your SQLite database and restore them when needed.

## Features
- 📌 **Automated Backup**: Creates timestamped backups of your SQLite database.
- 🔄 **Restore Functionality**: Restore your database from a previous backup.
- 📝 **Logging**: Logs all operations for troubleshooting.
- 📂 **Backup Management**: Lists all available backups for restoration.
- ⏳ **Scheduled Backups**: Supports **cron** for automatic periodic backups.

## Installation

### 1. Clone the repository
```sh
git clone https://github.com/mahmoud-s-Khedr/DBAutomator.git
cd DBAutomator/src
```

### 2. Install Dependencies
DBAutomator runs on **Python 3** and requires no external dependencies.

### 3. Configure Paths
in Directory `/etc/dbautomator` create a file named `.env` and add the following:
```sh
DB_PATH=/path/to/your/database.db  # optional
BACKUP_DIR=/var/backups
LOG_FILE=/var/log/DBAutomator.log
```

## Usage

### **Manually Backup the Database**
Usage:
```
main.py [--backup | --restore] [--file <backup_file>]
```

```sh
python DBAutomator.py --backup
```
Creates a timestamped backup in `/var/backups/`.

### **Restore a Database**
```sh
python DBAutomator.py --restore
```
Lists all available backups and prompts you to select one.

### **Example Run**
```sh
python DBAutomator.py --backup
# Backup created successfully: backup_2025-03-18_14-30-00.db
```

```sh
python DBAutomator.py --restore
# Available backup files:
# 1. backup_2025-03-18_14-30-00.db
# Enter the backup file name: backup_2025-03-18_14-30-00.db
# Database restored successfully
```

## Automating Backups with Cron

You can schedule automatic backups using **cron** on Linux.

### **1. Open the Crontab**
```sh
crontab -e
```

### **2. Add a Cron Job**
To schedule a backup **every day at 2 AM**, add this line:
```sh
0 2 * * * /usr/bin/python3 /path/to/DBAutomator.py --backup
```
🔹 **Explanation of Cron Format:**  
```
Minute  Hour  Day  Month  DayOfWeek  Command
0       2     *    *      *         /usr/bin/python3 /path/to/DBAutomator.py --backup
```
- `0 2 * * *` → Runs at **2:00 AM** every day.
- `/usr/bin/python3` → Full path to Python 3.
- `/path/to/DBAutomator.py` → Replace with the actual path to your script.

### **3. Verify Cron Job**
To check if your cron job is added, run:
```sh
crontab -l
```

### **4. Check Logs**
Cron jobs do not print output to the terminal. You can check logs using:
```sh
cat /var/log/DBAutomator.log
```

### **Example: Running Backups Every 6 Hours**
```sh
0 */6 * * * /usr/bin/python3 /path/to/DBAutomator.py --backup
```
This will execute the backup **every 6 hours**.

## Logging
All operations are logged in `/var/log/DBAutomator.log`.

## License
This project is licensed under the **MIT License**. See `LICENSE` for details.
