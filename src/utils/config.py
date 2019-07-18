import os

TIME_PUNCHER_DIR_NAME = '.time-puncher'
BACKUP_DIR_NAME = 'backups'

TIME_PUNCHER_DIR = os.path.join(os.environ['HOME'], TIME_PUNCHER_DIR_NAME)
BACKUP_DIR = os.path.join(TIME_PUNCHER_DIR, BACKUP_DIR_NAME)