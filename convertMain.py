file_object = open("calendarTest.ics", "w")#change calendar test to SchoolScheduleSemesterYear



file_object.write("BEGIN:VCALENDAR\n"
                  "PRODID:-//Google Inc//Google Calendar 70.9054//EN\n"
                  "VERSION:2.0 CALSCALE:GREGORIAN METHOD:PUBLISH X-WR-CALNAME:RANDOMIZE\n"
                  "X-WR-TIMEZONE:America/Chicago\n"
                  "BEGIN:VTIMEZONE\n"
                  "TZID:Etc/UTC\n"
                  "X-LIC-LOCATION:Etc/UTC\n"
                  "BEGIN:STANDARD\n"
                  "TZOFFSETFROM:+0000\n"
                  "TZOFFSETTO:+0000\n"
                  "TZNAME:GMT\n"
                  "DTSTART:19700101T000000\n"
                  "END:STANDARD\n"
                  "END:VTIMEZONE\n"
                  "BEGIN:VTIMEZONE\n"
                  "TZID:America/Chicago\n"
                  "X-LIC-LOCATION:America/Chicago\n"
                  "BEGIN:DAYLIGHT\n"
                  "TZOFFSETFROM:-0600\n"
                  "TZOFFSETTO:-0500\n"
                  "TZNAME:CDT\n"
                  "DTSTART:19700308T020000\n"
                  "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU\n"
                  "END:DAYLIGHT\n"
                  "BEGIN:STANDARD\n"
                  "TZOFFSETFROM:-0500\n"
                  "TZOFFSETTO:-0600\n"
                  "TZNAME:CST\n"
                  "DTSTART:19701101T020000\n"
                  "RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU\n"
                  "END:STANDARD\n"
                  "END:VTIMEZONE\n")

#here we have the for loop
name = "Don Vogel"
time = "8:30 - 9:45"
time2 = "0"
if time[1] == ':':
    time2+=time

if len(time2) == 12:
    time2 = time2.replace(' - ', '0')

time2 = time2.replace(' - ', '')
time2 = time2.replace(':', '')
startTime = time2[0:4]
endTime = time2[4:8]
location = "location"
classDays = "Tuesday & Thursday"

classDays = classDays.replace(' & ', ',')
classDays = classDays.replace('Sunday', 'SU')
classDays = classDays.replace('Monday', 'MO')
classDays = classDays.replace('Tuesday', 'TU')
classDays = classDays.replace('Wednesday', 'WE')
classDays = classDays.replace('Thursday', 'TH')
classDays = classDays.replace('Friday', 'FR')
classDays = classDays.replace('Saturday', 'SA')

print(classDays)
file_object.write("BEGIN:VEVENT\n"
                  "DTSTART:20180822T"+startTime+"00\n"#when the event starts
                  "DTEND:20180822T"+endTime+"00\n"#when the event ends
                  "RRULE:FREQ=WEEKLY;UNTIL=20181207T055959Z;BYDAY="+classDays+"\n"#here you insert the end time and days the classes go
                  "DESCRIPTION:"+name+"\n"#here is the professor
                  "LOCATION:"+location+"\n"
                  "SEQUENCE:1\n"#this probably means repetition, so use this one
                  "STATUS:TENTATIVE\n"
                  "SUMMARY:<class name>\n"
                  "TRANSP:OPAQUE\n"
                  "END:VEVENT\n")
#loop ends here

file_object.write("END:VCALENDAR\n")

file_object.close()