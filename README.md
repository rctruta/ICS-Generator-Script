# ICS Generator Script

This repository contains a Python script to generate `.ics` files for calendar events. Specifically, the script creates a series of bi-weekly meetings with a Google Meet link. It is designed to work seamlessly within GitHub Codespaces or your local development environment.

## Features

- Generates an `.ics` file for bi-weekly meetings.
- Allows customization of the start date, meeting frequency, and Google Meet link.
- Outputs a calendar file that can be imported into any calendar application.

## Requirements

- Python 3.6+
- `icalendar` library
- `pytz` library

If you're using GitHub Codespaces, these requirements will be pre-installed. If you're running the script locally, ensure you have the necessary dependencies installed.

## Setup

### Cloning the Repository

```bash
git clone https://github.com/yourusername/ics-generator.git
cd ics-generator
```

### Installing Dependencies

If you don't have the required libraries installed, you can install them using pip:

```bash
pip install icalendar pytz
```

### Running the Script

Once the dependencies are installed, you can run the script to generate the `.ics` file:

```bash
python create_ics.py
```

This will generate a file named `bi_weekly_meetings.ics` in the root directory of the project.

### Using GitHub Codespaces

You can run this script directly within a GitHub Codespace:

1. Open the repository in GitHub Codespaces.
2. Run the script using the built-in terminal:
   
   ```bash
   python create_ics.py
   ```

This will ensure the script works correctly in a cloud environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify the README as needed to fit your specific project details!
