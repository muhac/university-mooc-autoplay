from selenium import webdriver
import time


def driver_actions(url):
    """Login in Chrome."""
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    await, interval, count = input("Press 'Enter' to start watching -> "), 10, 1
    browser.switch_to.window(browser.window_handles[-1])

    if not await:
        a, b, c = 1, 1, 1
        while True:
            browser.find_elements_by_partial_link_text(f"第{a}章")[0].click()
            time.sleep(3)
            unit = f"{a}.{b}.{c}"
            try:
                current = browser.find_elements_by_partial_link_text(unit)[0]
            except:
                break
            else:
                while True:
                    unit = f"{a}.{b}.{c}"
                    try:
                        current = browser.find_elements_by_partial_link_text(unit)[0]
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
                                print(unit)
                                current.click()
                                time.sleep(10)
                                browser.find_element_by_class_name("xt_video_player_play_btn").click()
                                # while True:
                                #     watched = current.find_element_by_xpath(
                                #         "//*[@class='xt_video_player_current_time_display']/span").text.split(':')[0]
                                #     total = current.find_element_by_xpath(?????^^^^^?????).text.split(':')[0]
                                #     if watched == total:
                                #         c += 1
                                #         break
                                # 写上这段速度会快很多but高数作业ddl。。
                                time.sleep(300)
                                c += 1

    input("Press 'Enter' to exit -> ")
    browser.quit()


def login():
    website = 'http://hitsz.xuetangx.com/newcloud/dashboard#/mycredit'
    driver_actions(website)


login()
