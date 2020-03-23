import time
import functions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def driver_actions(url):
    """Login in Chrome."""
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    username = 'username'
    password = 'password' + '\n'

    # Log in
    while True:
        browser.find_element_by_id('lUsername').send_keys(username)
        browser.find_element_by_id('lPassword').send_keys(password)

        try:
            time.sleep(2)
            browser.find_element_by_id('course_studying').click()
        except:
            browser.delete_all_cookies()
            browser.get(url)
        else:
            break

    interval, count = 10, 1
    if not input('Enter to start watching -> '):
        browser.switch_to.window(browser.window_handles[-1])
        while True:
            total_time = browser.find_element_by_class_name('current_play').find_element_by_css_selector('.time.fl')
            print(f' %3d : {total_time.text}' % count)
            for _ in range(300):     # 50 minutes at least in case of unexpected stop
                time.sleep(interval)
                try:
                    # Pop out questions
                    log = ActionChains(browser)
                    element = browser.find_element_by_class_name('popboxes_main')
                    log.move_to_element_with_offset(element, 200, 500)
                    log.click()
                    log.move_to_element_with_offset(element, 200, 300)
                    log.click()
                    log.move_to_element_with_offset(element, 200, 150)
                    log.click()
                    log.perform()
                    time.sleep(0.5)
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
                elif '给力加载中' in percentage:
                    browser.refresh()
            else:
                browser.refresh()
                continue

            # Go to next
            try:
                browser.find_element_by_css_selector('.next_lesson_bg.tm_next_lesson').click()
            except:
                break   # the last one
            else:
                count += 1
                time.sleep(2)

    input("Press 'Enter' to Exit.")
    browser.quit()


def login():
    website = 'https://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/'
    functions.ping("online.zhihuishu.com")
    driver_actions(website)


try:
    login()
except EOFError:
    print('你中止了进程。')
