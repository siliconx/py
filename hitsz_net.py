#!/usr/bin/python3

# driver download from https://npm.taobao.org/

import time
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

home_url = 'http://10.248.98.2/srun_portal_pc?ac_id=1&theme=basic2'

def init():
    print('running...')

    chrome_options = Options()

    # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('--no-sandbox')
    # 指定浏览器分辨率
    chrome_options.add_argument('window-size=1920x1080')
    # 谷歌文档提到需要加上这个属性来避免出bug
    chrome_options.add_argument('--disable-gpu')
    # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('--hide-scrollbars')
    # 不加载图片, 提升加载速度
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # 关闭浏览器图形界面, 无GUI的操作系统不加这条会启动失败
    chrome_options.add_argument('--headless')
    # 忽略非错误日志
    chrome_options.add_argument('--log-level=3')


    global driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(home_url)

    # 等待页面加载
    time.sleep(1)


def login():
    '''登陆.'''
    # 检查登录状态
    config = driver.execute_script("return window.CONFIG;")

    if config and config.get('page') == 'success':
        print("already online")
        return
    
    # 获取用户名输入框
    username_input = driver.find_element(By.ID, 'username')
    # 获取密码输入框
    pwd_input = driver.find_element(By.ID, 'password')
    # 填入用户名和密码
    username_input.send_keys(username)
    pwd_input.send_keys(password)
    # 登陆按钮
    button = driver.find_element(By.ID, 'login-account')
    button.click()
    # 等待页面加载
    time.sleep(2)

    config = driver.execute_script("return window.CONFIG;")

    # 检查 'page' 属性是否为 'success'
    if config and config.get('page') == 'success':
        msg = 'Login success'
    else:
        msg = 'Login failed'
        
    print(msg)


def logout():
    '''注销.'''

    # 检查注销状态
    config = driver.execute_script("return window.CONFIG;")

    if config and config.get('page') == 'account':
        print("already offline")
        return
    
    # 注销按钮
    button = driver.find_element(By.ID, 'logout')
    button.click()
    # 等待页面加载
    time.sleep(1)

    # 确认注销按钮
    button = driver.find_element(By.CLASS_NAME, 'btn-confirm')
    button.click()


if __name__ == '__main__':
    # 可直接填入账号密码，免输入登陆注销
    username = ''
    password = ''
    if not (username and password):
        username = input('Enter username: ')
        password = getpass.getpass('Enter password: ')

    init()
    config = driver.execute_script("return window.CONFIG;")

    # 检查 'page' 属性是否为 'success'
    if config and config.get('page') == 'success':
        print('Currently logged in')
    else:
        print('Currently not logged in')

    action = input('1-login\n2-logout\n')
    if action == '1':
        login()
    elif action == '2':
        logout()

driver.close()
