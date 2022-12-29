# selenium 4

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write_file(path, content):
    with open(path, "w", encoding="UTF-8") as f:
        f.write(content)
    return


def check_cookies():
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "W0wltc"))).click()
    except Exception:
        pass
    return


def search_keyword():
    # enter 'automatización' into search field, press ENTER
    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q")))
    search_field.send_keys("automatización")
    search_field.send_keys(Keys.RETURN)
    return


def launch_wiki():
    # search for 'wikipedia' website and launch it
    automat_urls = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "iUh30")))
    for automat_url in automat_urls:
        if "wikipedia.org" in automat_url.text:
            automat_url.click()
            return


def history_part_in_article():
    # search for target info in the wiki article
    history_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "mw-content-text"] / div[1] / div[8] / div / div')))
    wr_history_text = f"\nFirst Automation Process\n{history_text.text}\n"
    write_file("./data/auto_history.txt", wr_history_text)
    print(wr_history_text)
    return


def take_screenshot():
    # take screenshot of target info
    history = driver.find_element(By.ID, "Historia")
    driver.execute_script("arguments[0].scrollIntoView()", history)
    driver.save_screenshot("screenshots/auto_history.png")


def get_data_and_screenshot_from_website():
    check_cookies()
    search_keyword()
    launch_wiki()
    history_part_in_article()
    take_screenshot()
    return


if __name__ == "__main__":
    # defining driver and source website
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.es")
    get_data_and_screenshot_from_website()
    driver.close()
    print("Automation search complete!\nData and screenshot saved under 'data' and 'screenshots' folders.\n")
