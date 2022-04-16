# Asana To Task Warrior

## Simple steps to dump Asana For Task Warrior
Won't go into the details of [Task Warrior](https://taskwarrior.org/), if you're here then likely already aware.

### Converting Asana to TaskWarrior tasks
1. Export Asana tasks as CSV
   1.  Browser Only:
       1. Select All Items
       2. Grab the PullDown
       3. Export to CSV
   2.  Sidenote Gotcha:
       - Something I ran into was the [**BOM** *(\ufeff)](https://en.wikipedia.org/wiki/Byte_order_mark) string was in the beginning of the csv
       - Must have been inserted when saving from LibreOffice, who knows
       - Remove that by using vi ```:set nobomb``` and save file
3. convert to json (see cjParse.py)
4. Run through [jq](https://stedolan.github.io/jq/manual/)
5. Run through sed and awk and capture
6. Edit the capture *script* accordingly
7. Happy with it?  Run it.

$ cat ~/Documents/BrainDump.json | jq -r '.[1,2]'
