import time
from selenium import webdriver


def driver_actions(url):
    """Login in Chrome."""
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    username = 'username'
    password = 'password' + '\n'

    while True:
        browser.find_element_by_id('lUsername').send_keys(username)
        browser.find_element_by_id('lPassword').send_keys(password)

        try:
            time.sleep(2)
            browser.find_element_by_id('userName').click()
            browser.switch_to.window(browser.window_handles[-1])
            browser.find_element_by_class_name('i18nSwitchBtn').click()
        except:
            browser.delete_all_cookies()
            browser.get(url)
        else:
            break
    await, interval, count = input("Press 'Enter' to start watching -> "), 10, 1
    if not await:
        browser.switch_to.window(browser.window_handles[-1])
        while True:
            total_time = browser.find_element_by_class_name('current_play').find_element_by_css_selector('.time.fl')
            print(f' %3d : {total_time.text}' % count)
            while True:
                time.sleep(interval)
                try:
                    browser.find_element_by_class_name('popbtn_cancel').click()
                except:
                    pass
                # Find current watching percentage.
                current = browser.find_element_by_class_name('current_play')
                bar = current.find_element_by_class_name('progressbar_box_tip')
                browser.execute_script("arguments[0].style = 'display: block;';", bar)
                percentage = current.find_element_by_xpath("//*[@class='progressbar_box_tip']/span").text
                if '100' in percentage:
                    break
            try:
                browser.find_element_by_css_selector('.next_lesson_bg.tm_next_lesson').click()
            except:
                break
            else:
                count += 1
                time.sleep(2)

    input("Press 'Enter' to Exit.")
    browser.quit()


def login():
    website = 'http://passport.zhihuishu.com/login'
    driver_actions(website)


login()
