# this module arrange the entered entries with proper serial number

def serialnumber_newuser(serialnumber_column, worksheet):
        for position in range(1, worksheet.max_row+1):
                element = worksheet.cell(row = position+1, column = serialnumber_column)
                element.value = str(position)


def serialnumber_migration(serialnumber_column, worksheet, position):
    if position == worksheet.max_row:
        pass
    else:
        for updating_position in range(position, worksheet.max_row+1):
            if updating_position == worksheet.max_row:
                pass
            else:
                element = worksheet.cell(row = updating_position+1, column = serialnumber_column)
                element.value = str(updating_position-1)


def serialnumber_migration_sheetchange(serialnumber_column, worksheet):
    serialnumber_newuser(serialnumber_column, worksheet)
    



