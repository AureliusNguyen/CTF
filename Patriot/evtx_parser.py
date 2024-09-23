from Evtx import *

# Open a file to write the output
with open('sus.txt', 'w') as outfile:
    # Open and parse the EVTX file
    with Evtx.Evtx('suspicious.evtx') as log:
        for record in log.records():
            outfile.write(record.xml() + '\n')  # Write each event log entry to the file
