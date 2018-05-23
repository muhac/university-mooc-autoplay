import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def driver_actions(url):
    """Login in Chrome."""
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    username = 'username'
    password = 'password' + '\n'

    while True:
        try:
            browser.find_element_by_class_name('icon-user')
        except:
            pass
        else:
            time.sleep(1.5)
            break

    # Log in actions.
    log = ActionChains(browser)
    element = browser.find_element_by_class_name('icon-user')
    log.move_to_element_with_offset(element, -20, 0)
    log.click()
    log.send_keys(username)
    element = browser.find_element_by_class_name('icon-lock')
    log.move_to_element_with_offset(element, -20, 0)
    log.click()
    log.send_keys(password)
    log.perform()

    await, interval, count = input("Press 'Enter' to start watching -> "), 10, 1
    browser.switch_to.window(browser.window_handles[-1])

    if not await:
        section = input("start from (1.1.1):")
        if not section:
            a, b, c = 1, 1, 1
        else:
            [a, b, c, *_] = section.split('.')

        while True:
            browser.find_elements_by_partial_link_text(f"第{a}章")[0].click()
            time.sleep(3)
            unit = f"{a}.{b}.{c}"
            try:
                browser.find_elements_by_partial_link_text(unit)[0]
            except:
                break
            else:
                while True:
                    unit = f"{a}.{b}.{c}"
                    try:
                        browser.find_elements_by_partial_link_text(unit)[0]
                    except:
                        c = 1
                        b = 1
                        a += 1
                        break
                    else:
                        while True:
                            unit = f"{a}.{b}.{c}"
                            try:
                                current = browser.find_elements_by_partial_link_text(unit)[0]
                            except:
                                c = 1
                                b += 1
                                break
                            else:
                                current.click()
                                while True:
                                    try:
                                        time.sleep(7)
                                        browser.find_element_by_class_name("xt_video_player_play_btn").click()
                                    except:
                                        continue
                                    else:
                                        break
                                total = browser.find_element_by_xpath(
                                    "//*[@class='xt_video_player_current_time_display fl']/span[2]").text
                                print(unit, total)
                                while True:
                                    watched = browser.find_element_by_xpath(
                                        "//*[@class='xt_video_player_current_time_display fl']/span").text
                                    total = browser.find_element_by_xpath(
                                        "//*[@class='xt_video_player_current_time_display fl']/span[2]").text

                                    if not total:
                                        time.sleep(1)
                                        bar = browser.find_element_by_css_selector('.xt_video_player_controls.cf')
                                        browser.execute_script(
                                            "arguments[0].setAttribute('class', "
                                            "'xt_video_player_controls cf xt_video_player_controls_show')", bar)
                                    elif watched == total != '0:00':
                                        c += 1
                                        break
                                time.sleep(1)
                                c += 1

    input("Press 'Enter' to exit -> ")
    browser.quit()


def login():
    website = 'http://hitsz.xuetangx.com/newcloud/dashboard#/mycredit'
    driver_actions(website)


login()
