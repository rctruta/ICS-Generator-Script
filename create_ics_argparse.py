import argparse
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

def create_ics_file(start_date, start_time, duration, frequency, end_date, meet_link):
    # Define timezone
    mountain = pytz.timezone('America/Denver')

    # Parse start date and time
    start_datetime = mountain.localize(datetime.strptime(f'{start_date} {start_time}', '%Y-%m-%d %H:%M'))

    # Parse end date
    end_datetime = mountain.localize(datetime.strptime(end_date, '%Y-%m-%d'))

    # Create calendar
    cal = Calendar()

    # Event frequency
    frequency_delta = timedelta(weeks=frequency)

    # Create events
    current_event_date = start_datetime
    while current_event_date <= end_datetime:
        event = Event()
        event.add('summary', 'Bi-Weekly Meeting')
        event.add('dtstart', current_event_date)
        event.add('dtend', current_event_date + timedelta(hours=duration))
        event.add('dtstamp', datetime.now(tz=pytz.utc))
        event.add('location', meet_link)
        event.add('description', f'Join the meeting using this Google Meet link: {meet_link}')
        cal.add_component(event)
        current_event_date += frequency_delta

    # Write to .ics file
    with open('meetings.ics', 'wb') as f:
        f.write(cal.to_ical())

    print("ICS file created successfully as 'meetings.ics'")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate an .ics file for a series of meetings.')
    parser.add_argument('--start_date', required=True, help='Start date in YYYY-MM-DD format.')
    parser.add_argument('--start_time', required=True, help='Start time in HH:MM format (24-hour).')
    parser.add_argument('--duration', type=float, default=1, help='Duration of the meeting in hours.')
    parser.add_argument('--frequency', type=int, default=2, help='Frequency of the meetings in weeks.')
    parser.add_argument('--end_date', required=True, help='End date in YYYY-MM-DD format.')
    parser.add_argument('--meet_link', required=True, help='Google Meet link for the meetings.')

    args = parser.parse_args()

    # Call function with parsed arguments
    create_ics_file(
        start_date=args.start_date,
        start_time=args.start_time,
        duration=args.duration,
        frequency=args.frequency,
        end_date=args.end_date,
        meet_link=args.meet_link
    )
