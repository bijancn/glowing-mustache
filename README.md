glowing-mustache
================

LaTeX Calender

Upcoming Milestones:
--------------------
- GitHub Repo aufsetzen (und mich einladen ;))
- Python-GoogleCalendarParser ausprobieren. Event title und termin
ausgeben lassen.
- TeX Vorlage durcharbeiten. Befehle verstehen und kommentieren.
Vereinfachen. Mir ist zB noch nicht klar, wie man jeden Monat auf ein
DIN A4 Blatt macht. Wenn man die Range bei dem TikZ erhoeht, haengt er
das einfach an das gleiche TikZ Bild dran.
- \include von ein paar Test Terminen, die man sich in ein extra File
gcal.tex schreibt.
- Erzeugung eines solchen Test file von Python aus.

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

Angenommen obiges klappt, haben wir jetzt Events als Python Objekte.
Der naechste Schritt ist, daraus Strings zu machen, die fuer TeX
lesbar sind. Im Anhang habe ich eine norwegische Vorlage fuer Tikz
Calendar, an der ich bischen rumgespielt habe. Da muss man sich auch
etwas reinarbeiten. Insbesondere sollte sie so allgemein und simpel
wie moeglich gehalten werden und die ganzen laenderspezifischen
Sachen, wie Feiertage, sollten aus Google Calendar folgen. Die
wichtige Syntax habe ich im TeX file markiert. Es scheint sowas wie
  if (equals=07-29) [observance=Olsok]
zu sein. Kenne mich aber auch noch nicht so aus. Am besten waere es
wenn man an die Stelle ein \include einfuegen kann und dann das tex
file einbindet, das man mit Python generiert. Geht aber auch anders.
