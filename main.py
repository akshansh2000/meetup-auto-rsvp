from selenium import webdriver
import sys
import json
import datetime
import time


def initialize():
    try:
        with open("config.json", 'r') as config:
            config = json.load(config)

            if not {"email", "password"}.issubset(set(config.keys())):
                raise Exception()

            email = config["email"]
            password = config["password"]

        print("config: valid")
        print("Trying to log in...")
    except:
        print(
            "Please create a valid config file in order to log in.\n" +
            "Read the README for more instructions.\n" +
            "Exiting..."
        )
        sys.exit(1)

    options = webdriver.ChromeOptions()
    options.headless = True

    driver = webdriver.Chrome(options=options)

    authenticate(driver, email, password)


def authenticate(driver, email, password):
    driver.get("https://meetup.com/login")

    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("password").send_keys(password)

    driver.find_element_by_id("loginFormSubmit").click()

    check_if_logged_in(driver)


def check_if_logged_in(driver):
    try:
        error_element = None
        error_element = driver.find_element_by_xpath(
            "//div[@class='docBox  error ']"
        )

        print("Incorrect Email ID or Password\nExiting...")
        sys.exit(1)
    except:
        if error_element is None:
            print("Logged In Successfully")
        else:
            sys.exit(1)

    while True:
        print("Gathering event links...")
        gather_event_links(driver)
        time.sleep(1800)


def gather_event_links(driver):
    driver.get("https://www.meetup.com/find/?events=true&eventFilter=my")

    event_links = [
        href.get_attribute("href") for href in driver.find_elements_by_xpath(
            "//a[@class='resetLink big event wrapNice omnCamp omngj_sj7emga omnrv_fe1mga ']"
        )
    ]

    if not event_links:
        print(f"No upcoming events at {datetime.datetime.now()}")

    iterate_events(driver, event_links)


def iterate_events(driver, event_links):
    already_rsvped = True
    for event_link in event_links:
        driver.get(event_link)
        already_rsvped &= rsvp_event(driver)

    if already_rsvped:
        print(f"No upcoming events at {datetime.datetime.now()}")


def rsvp_event(driver):
    try:
        driver.find_element_by_xpath(
            "//span[@class='text--body inverted']//span"
        )

        return True
    except:
        pass

    event_name = driver.find_element_by_xpath(
        "//h1[@class='pageHead-headline text--pageTitle']"
    ).text
    event_date = driver.find_element_by_xpath(
        "//time[@class='eventStatusLabel']//span"
    ).text

    driver.find_element_by_class_name("gtmEventFooter--attend-btn").click()
    print(f"You're attending the {event_name} event on {event_date}!")

    return False


if __name__ == "__main__":
    initialize()
