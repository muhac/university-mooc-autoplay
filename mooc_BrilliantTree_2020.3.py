import time
import json

try:
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from cryptography.fernet import Fernet

except ModuleNotFoundError:
    print("缺少库文件的解决办法："
          "\n  pip install selenium"
          "\n  pip install cryptography")
    time.sleep(30)
    exit(1)


def get_user_info() -> (str, str):
    try:
        # 已经保存的用户信息
        with open('USER_INFO') as f_obj:
            info: dict = json.load(f_obj)

        key: bytes = info['key'].encode(encoding='utf8')
        cipher_suite = Fernet(key)

        en_username: bytes = cipher_suite.decrypt(info['username'].encode(encoding='utf8'))
        en_password: bytes = cipher_suite.decrypt(info['password'].encode(encoding='utf8'))

        username: str = en_username.decode(encoding='utf8')
        password: str = en_password.decode(encoding='utf8')

    except:
        # 重新获取用户信息
        username: str = input('username: ')
        password: str = input('password: ')

        new_key: bytes = Fernet.generate_key()
        cipher_suite = Fernet(new_key)

        new_username: bytes = cipher_suite.encrypt(username.encode(encoding='utf8'))
        new_password: bytes = cipher_suite.encrypt(password.encode(encoding='utf8'))

        info: dict = {'key': new_key.decode(encoding='utf8'),  # str
                      'username': new_username.decode(encoding='utf8'),
                      'password': new_password.decode(encoding='utf8'), }

        with open('USER_INFO', 'w') as f_obj:
            json.dump(info, f_obj)

    return username, password


def driver_actions(url):
    # 获取用户信息
    username, password = get_user_info()

    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    # 登陆界面
    for _ in range(1):  # 可以选择自动登录尝试次数
        time.sleep(3)

        # 怎么不能自动填充，会被检测出来？？？？？？？
        browser.find_element_by_id('lUsername').send_keys(username)
        browser.find_element_by_id('lPassword').send_keys(password)
        browser.find_element_by_class_name('wall-sub-btn').click()
        # TODO: 自动填充账号密码是，必出滑动验证且无法通过
        #       不知道是被检测出来了还是智慧树的脚本有问题

        try:
            time.sleep(10)  # 有概率弹出滑动验证
            browser.find_element_by_class_name('header-enter-school').click()
        except:
            browser.delete_all_cookies()
            browser.get(url)
        else:
            break

    else:
        # 自动登陆失败，采用手动登陆
        input('请手动登陆，然后按任意键继续...')
        browser.find_element_by_class_name('header-enter-school').click()

    # 播放界面
    def popout(select=0):
        # 播放过程中弹题
        browser.find_elements_by_class_name('topic-item')[select].click()
        print('    弹题', end='')

        time.sleep(1)
        browser.find_elements_by_class_name('btn')[-1].click()
        print('    已关闭', end='')

        try:
            # 未作答的题目无法关闭
            browser.find_element_by_class_name('el-message-box__close').click()
            print('    未作答', end='')
        except:
            # 弹题以后会自动暂停
            time.sleep(1)
            ac = ActionChains(browser)
            e = browser.find_element_by_class_name('videoArea')
            ac.move_to_element_with_offset(e, 100, 100)
            ac.click()
            ac.perform()
            print('    继续播放')

    if not input('进入播放界面后按回车键，程序将接管...'):
        # browser.switch_to.window(browser.window_handles[-1]) # 现在 (2020) 不弹出新页面了
        playlist = browser.find_elements_by_class_name('time_ico_half')
        for count, video in enumerate(playlist):
            print(f'{time.asctime()} : {count + 1:3d} / {len(playlist)}')

            try:
                # 这里是防止看过的部分弹出题目挡住播放列表
                # 多选连点两次会取消选择所以选最后一个选项
                popout(-1)
            except:
                pass
            finally:
                video.click()

            for _ in range(300):  # 为了防止卡关，设置50分钟上限
                time.sleep(10)
                try:
                    popout()
                except:
                    pass

                try:
                    # 读取当前进度
                    browser.find_element_by_class_name('current_play') \
                        .find_element_by_class_name('progress-num')
                except:
                    try:
                        popout(-1)
                    except:
                        pass
                    finally:
                        break  # 当播放完成时进度条消失，播放下一节

            else:
                # 万一卡住了，刷新重试
                browser.refresh()
                time.sleep(10)
                log = ActionChains(browser)
                element = browser.find_element_by_class_name('videoArea')
                log.move_to_element_with_offset(element, 100, 100)
                log.click()
                log.perform()
                continue

    input("按任意键退出...")
    browser.quit()


if __name__ == '__main__':
    print('GitHub: bugstop\n\n'
          '适用于 2020.3 智慧树更新。')

    try:
        website = 'https://passport.zhihuishu.com/login'
        driver_actions(website)
    except EOFError:
        print('你中止了进程。')
