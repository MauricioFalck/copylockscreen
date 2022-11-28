from os import path, environ
from datetime import datetime


def log(message, level=1, dbg_level=False):
    """
    Logs a message to a log file

    Args:
        message: The message to be logged
        level: The debug level (0 for INFO, 1 for DEBUG)
        dbg_level: The debug level to be considered. 
        If dbg_level is 0 (INFO), a message with level = 1 (DEBUG) is not printed

    """
    # Construct the full path of the log file
    log_file = path.join(environ.get('TEMP'), 'log_cp_spotlight.txt')

    with open(log_file, 'a') as file:
        # Create a timestamp string
        timestamp = datetime.now().strftime("<%d/%m/%Y@%H:%M> ")
        # Defines the initial message
        if message == 'INIT':
            file.write('\n\n' + timestamp + ' STARTING EXECUTION: \n')
        # Format and prints the message
        else:
            msg_type = ''
            if (level == 0):
                msg_type = '[INFO]'
            elif (level == 1):
                msg_type = '[DEBUG]'
            if (level == 1 and dbg_level) or level == 0:
                file.write(msg_type + ' ' + timestamp + ' ' + message + '\n')
        file.close()
