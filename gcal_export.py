from calendar_parser import CalendarParser

ics_feed = "https://www.google.com/calendar/ical/4rc1vqnpc2r7nqpaboi037vf1k%40group.calendar.google.com/public/basic.ics"

cal = CalendarParser(ics_url=ics_feed)
time_hl = 'textbf'
location_hl = 'textit'

def tex_event(event):
  strg = "  if (equals=" + str(event.start_time.date()) + ") [observance="
  if not event.all_day:
    strg += " \\" + time_hl + "{" + str(event.start_time.time())[:5] + "} "
  strg +=  event.name
  if 'location' in event.keys():
    strg += " \\" + location_hl + "{" + event.location + "}"
  print strg + "]"

for event in cal.parse_calendar():
  tex_event(event)
