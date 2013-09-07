glowing-mustache
================

LaTeX Calender

Upcoming Milestones:
--------------------
- TeX Vorlage weiter durcharbeiten. Befehle verstehen und kommentieren.

Die Grundlage ist Googles API
https://developers.google.com/google-apps/calendar/v2/developers_guide_protocol?hl=de&csw=1#RetrievingEvents

Prinzipiell bekommt man von Google XML, das man zB mit
http://docs.python.org/2/library/xml.etree.elementtree.html
parsen kann.

Von dort bis zur Extraktion der Events ist es allerdings noch ein
recht langer Weg, den schon andere gegangen sind. Fuer den schnellen
'Proof of Concept' wuerde ich daher eine Python Bibliothek wie
https://github.com/oblique63/Python-GoogleCalendarParser
verwenden.

Das scheint alles zu koennen, was wir erst mal brauchen, aber das muss
man sich angucken. Ich glaube man kann dem direkt die URL geben. Falls
nicht, waere das
http://blog.nguyenvq.com/backup-my-google-calendars-via-shell-and-python-scripts-and-scheduling-them-via-cron/
auch eine Moeglichkeit. Waere vielleicht sowieso nicht schlecht
Backups vom Google Calendar zu haben.
