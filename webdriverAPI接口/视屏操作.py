from selenium import webdriver
from time import  sleep
driver = webdriver.Firefox()
driver.get("http://www.runoob.com/try/try.php?filename=tryjsref_video_play")

# 定位播放的位置
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="iframeResult"]'))
video = driver.find_element_by_xpath('//*[@id="myVideo"]')
# video = driver.find_element_by_xpath("//*[@id='preview-player_html5_api']")


#返回文件
url= driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

#播放视频
print("start")
driver.execute_script("return arguments[0].play()",video)

#播放15秒钟
sleep(15)

#暂停视频
print("stop")
driver.execute_script("return arguments[0].pause()",video)

#暂停15秒钟
sleep(5)

#播放视频
print("start")
driver.execute_script("return arguments[0].play()",video)
#播放15秒钟
sleep(15)

driver.quit()