import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("tutorial").sheet1          # hook up finishes here, code start below

data = sheet.get_all_records()


existing_cust_names = sheet.col_values(1)
existing_cust_emails = sheet.col_values(2)
existing_cust_phones = sheet.col_values(3)     # formatting error on sheet
existing_cust_addresses = sheet.col_values(4)

new_cust_names = sheet.col_values(7)             # column G
new_cust_emails = sheet.col_values(8)            # column H
new_cust_phones = sheet.col_values(9)          # column I  # formatting error on sheet
new_cust_addresses = sheet.col_values(10)         # column J

status_col = sheet.col_values(13)               # status, column M



def primary_search():
    counter1 = 0
    for item in new_cust_emails:
        counter1 += 1
        current_row = str(counter1)
        if item in existing_cust_emails:
            sheet.update('m' + current_row, 'existing customer')
        else:
            pass                                # redundant ?

primary_search()



def secondary_search():
    counter2 = 0
    for item in new_cust_addresses:
        counter2 += 1
        current_row = str(counter2)
        if item in existing_cust_addresses:
            sheet.update('m' + current_row, 'Existing customer')
        else:

            sheet.update('m' + current_row, 'New customer')

secondary_search()

# change 'i' for 'item' causes error?

#TODO Look up how many requests you are able to do in a minute
# After each request you add a sleep then. Sleep is a simple command that lets your programm wait for a given time.
# sleep is included in the time library.
# or Use a try-except block. In try you update the cell.
# When it throws an error you loop with while inside the except block until the cell is successfully updated.