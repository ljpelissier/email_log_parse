# email_log_parse
Parse email log file to redact student names.

Redact Student last names from Google Vault metadata.xml file

The script expects an xml and a csv in the current directory.
Student information csv must have column with last name and a header LastName

Match filenames in the first two variables of the script.

The script asks for confirmation as some words may show a match to a name
by coincidence. 
      ex) last name Grant and grant as in $ awarded.
