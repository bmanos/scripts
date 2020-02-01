# Delete all mails from Public\Support_backup  folder
import os
import imaplib

# Get credentials
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')

box = imaplib.IMAP4('mail.server.gr', 143)
box.login(db_user, db_pass)
box.select('#Public.#Support.Backup_support')
typ, data = box.search(None, 'ALL')
for num in data[0].split():
   box.store(num, '+FLAGS', '\\Deleted')
box.expunge()
box.close()
box.logout()