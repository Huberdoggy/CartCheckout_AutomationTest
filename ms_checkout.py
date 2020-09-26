from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys

# Import my pass from secrets
from secrets import pw

opts = Options()
opts.add_argument("--no-sandbox")

# Init a variable to hold the chrome driver methods
browser = webdriver.Chrome(ChromeDriverManager().install())


# Open my target URL
browser.get('https://www.microsoft.com/en-us/p/xbox-series-x/8wj714n3rbtl')
sleep(5)
# Close Popup if present..
no_popup = browser.find_element_by_xpath(
    "//*[@id='email-newsletter-dialog']/div[3]/div[1]")
no_popup.click()

# declare var for username, and click the login button. Proceed with first screen
user_name = "huberdoggy@gmail.com"
browser.find_element_by_id("mectrl_headerPicture").click()
sleep(2)
username_input = browser.find_element_by_id("i0116")
username_input.send_keys(user_name)
submit_btn = browser.find_element_by_id("idSIButton9").click()

# store submit button in a var and click
sleep(8)
password_input = browser.find_element_by_id("i0118")
password_input.send_keys(pw)

submit_btn = browser.find_element_by_id("idSIButton9")
sleep(2)
submit_btn.click()

# At the next prompt, choose "No don't stay signed in"
sleep(5)
no_stayLogin = browser.find_element_by_xpath("//*[@id='idBtn_Back']")
no_stayLogin.click()

# Go to the cart
sleep(5)
go_to_cart = browser.find_element_by_xpath("//*[@id='uhf-shopping-cart']")
go_to_cart.click()
