from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://192.168.0.108:6655/wd/hub',
    desired_capabilities={
        'platform': 'WINDOWS',
        'browserName':'FIREFOX',
        'video':'True',
        'version':'7',
        'javascriptEnable':True
    })
print('Video:'+'http://www.baidu.com'+driver.session_id)

driver.implicitly_wait(30)
driver.maximize_window()
driver.get('http://www.baidu.com')
# import selenium
# from selenium.webdriver import Remote

# # 定义主机与浏览,放在字典里面
# lists = {
#     "http://192.168.0.108:6655/wd/hub": "firefox"
# }
# #通过不同的浏览器执行脚本
# for host, browser in lists.items():
#     print(host,browser)
#     driver = Remote(command_executor=host,
#                     desired_capabilities={ 'platform':'ANY',
#                                            'browserName':'firefox',
#                                            # 'version':'',
#                                            # 'javascriptEnable':True
#                                         }
#                     )
#     driver.get("http://www.baidu.com")
#     driver.find_element_by_id("kw").send_keys(browser)
#     driver.find_element_by_id("su").click()
#     driver.close()

# from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
# # 本地启动selenium grid
# selenium_grid_url = "http://127.0.0.1:6655/wd/hub"
#
# # 创建一个DesiredCapabilities实例
# capabilities = DesiredCapabilities.FIREFOX.copy()
# capabilities['platform'] = "WINDOWS"  # 指定操作系统
# capabilities['version'] = "7"   # 指定操作系统版本
#
# # 连接到远程服务进行自动化测试
# driver = webdriver.Remote(desired_capabilities=capabilities,
#                           command_executor=selenium_grid_url)