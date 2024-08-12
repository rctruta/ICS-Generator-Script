from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Define timezone
mountain = pytz.timezone('America/Denver')

# Create calendar
cal = Calendar()

# Start date
# Update the start date according to your needs (yyyy, mm, dd, hh, min, sec)
start_date = mountain.localize(datetime(2024, 8, 13, 9, 0, 0))

# Event frequency (every other Tuesday)
# Update the frequency according to your needs
frequency = timedelta(weeks=2)

# End date
# Update the end date according to your needs; here it's set for the last of the year
end_date = mountain.localize(datetime(2024, 12, 31, 23, 59, 59))

# Google Meet link
# Update this with the Google Meet link--you'll need to generate it in your own Google Calendar
meet_link = ""

# Create events
current_event_date = start_date
while current_event_date <= end_date:
    event = Event()
    event.add('summary', 'Bi-Weekly Meeting')
    event.add('dtstart', current_event_date)
    event.add('dtend', current_event_date + timedelta(hours=1))
    event.add('dtstamp', datetime.now(tz=pytz.utc))
    event.add('location', meet_link)
    event.add('description', f'Join the meeting using this Google Meet link: {meet_link}')
    cal.add_component(event)
    current_event_date += frequency

# Write to .ics file
with open('bi_weekly_meetings.ics', 'wb') as f:
    f.write(cal.to_ical())

print("ICS file created successfully as 'bi_weekly_meetings.ics'")
