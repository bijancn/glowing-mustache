from calendar_parser import CalendarParser
import datetime as dt
# todo: Yearly reoccurring birthdays are not captured :(

ics_feed = "https://www.google.com/calendar/ical/4rc1vqnpc2r7nqpaboi037vf1k%40group.calendar.google.com/public/basic.ics"
cal = CalendarParser(ics_url=ics_feed)
time_hl = 'textbf'
location_hl = 'textit'
print_KW = False
event_name_cutoff = 30
f = open('templates/gcal_out.tex', 'w')

# returns the event as LaTeX formatted string, suitable for our template
def tex_event(event, eventtime):
  strg = "  if (equals=" + str(eventtime.date()) + ") [observance={"
  looks_all_day = event.end_time.time() == event.start_time.time() 
  if not (event.all_day or looks_all_day):
    strg += "\\" + time_hl + "{" + str(eventtime.time())[:5] + "} "
  if len(event.name) > event_name_cutoff:
    strg +=  event.name[:event_name_cutoff] + '..'
  else:
    strg +=  event.name
  if 'location' in event.keys():
    strg += ", \\" + location_hl + "{" + event.location + "}"
  strg += "}]\n"
  return strg

a_day = dt.timedelta(days=1)

# Some events span over multiple days. Do we want the label on each day like
# this or something like begin: and end: ?
def all_event(event):
  strg = tex_event(event, event.start_time)
  if (event.end_time.date() - event.start_time.date() > a_day):
    for i in range(1, (event.end_time.date() - event.start_time.date()).days):
      strg += tex_event(event, event.start_time + i * a_day)
  return strg

# todo: play with these options for improved look
def preamble(startdate, enddate):
  strg  = '\\begin{tikzpicture}[thick] \n'
  strg += '  \calendar[dates=' + str(startdate) + ' to ' + str(enddate) + ',\n'
  strg += '            week list,\n'
  strg += '            month label above centered,\n'
  strg += '            month text=\\textsc{\%mt \%y0},\n'
  strg += '            day headings={font=\small},\n'
  strg += '            day letter headings]\n'
  strg += '  if (Sunday) [red]\n'
  if print_KW:
    strg += '  if(Monday,equals=01-01,equals=02-01,equals=03-01,equals=04-01,\n'
    strg += '            equals=05-01,equals=06-01,equals=07-01,equals=08-01,\n'
    strg += '            equals=09-01,equals=10-01,equals=11-01,equals=12-01)\n'
    strg += '    [week number]\n'
  return strg

def tex_escape(strg):
  strg = strg.replace('&','\&')
  strg = strg.replace('->','$\\to$')
  strg = strg.replace('>','$>$')
  strg = strg.replace('<','$<$')
  return strg
 
year = 2013
months = range(1,13)
for month in months:
  startdate = dt.date(year, month, 1)
  print "Processing " + str(startdate)
  if month + 1 <= 12:
    enddate = dt.date(year, month + 1, 1) - dt.timedelta(days=1)
  else:
    enddate = dt.date(year + 1, 1, 1) - dt.timedelta(days=1)
  f.write(preamble(startdate, enddate)) 
  # todo: This is highly ineffective. One shouldn't call/test all events for
  # every month. Maybe gather all events first and sort them. I want multiple
  # calendars as well (e.g. private and holidays)
  for event in cal.parse_calendar():
    if startdate < event.start_time.date() < enddate:
      f.write(tex_escape(all_event(event)).encode('utf-8'))
  f.write(';\n\end{tikzpicture}\n')
f.close()
