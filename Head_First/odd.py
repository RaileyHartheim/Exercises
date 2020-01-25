from datetime import datetime

right_this_minute = datetime.today().minute

if right_this_minute % 2 == 1:
    print("This minute seems a little odd")
else:
    print("Not an odd minute.")
