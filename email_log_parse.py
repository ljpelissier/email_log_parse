"""
Redact Student last names from Google Vault metadata.xml file

The script expects an xml and a csv in the current directory.
Student information csv must have column with last name and a header LastName

Match filenames in the first two variables of the script.

The script asks for confirmation as some words may show a match to a name
by coincidence. ex) last name Grant and grant as in $ awarded.

"""
import pandas as pd

# make sure file names match
ORIGINAL_EMAIL_LOG_FILE = "BD_Log-metadata.xml"

studentInformation = pd.read_csv("//192.168.10.10/NewAccounts/StudentComputerAccountCheck.csv")

lastNames = studentInformation.LastName
REDACTED_EMAIL_LOG_FILE = "redactedStudentNames_" + ORIGINAL_EMAIL_LOG_FILE
logFile = open(ORIGINAL_EMAIL_LOG_FILE, encoding="utf-8")
redactedFile = open(REDACTED_EMAIL_LOG_FILE, "wt", encoding="utf-8")
for line in logFile:
    if "TagName='#Subject'" in line:
        for name in lastNames:
            name = name + ' '
            if name in line:
                print(line)
                print(name)
                deletIt = input("Do you want to redact " + name
                                + "from this line?(y/n)")
                if deletIt.lower() == 'y':
                    redactedFile.write(line.replace(name,"***StudentNameRedacted***"))
                else:
                    redactedFile.write(line)
    else:
        redactedFile.write(line)
logFile.close()
redactedFile.close()
