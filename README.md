# Meetup Auto-RSVP

A Python script which automatically confirms your attendance in your [Meetup](https://meetup.com) groups' upcoming events.

# Prerequisites

- Make sure to have a valid [Chrome WebDriver](https://chromedriver.chromium.org/) installed.
- Make sure to have [selenium](https://pypi.org/project/selenium/) installed.

# Instructions

- Clone and navigate into the repository directory:

```bash
git clone https://github.com/akshansh2000/meetup-auto-rsvp.git
cd meetup-auto-rsvp/
```

- Create a `config.json` file containing your **email** and **password**. A sample `config.json` is given:

```json
{
  "email": "<YOUR EMAIL ID>",
  "password": "<YOUR PASSWORD>"
}
```

A `config.json` file has been included in the repository for testing. Feel free to edit it.

- Run the script:

```bash
python3 main.py
```

The script will check for any new event in your joined groups every *30 minutes*, and automatically confirm your attendance for that event. It **will** notify you upon any confirmation, and also if no upcoming events are found.
