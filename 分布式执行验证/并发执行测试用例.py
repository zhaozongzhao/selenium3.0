from  multiprocessing import Pool
from multiprocessing import Manager,current_process
import os,time
from selenium import webdriver
def node_task(name,lock,arg,successTestCases,failTestCases):
    #获取当前进程名
    procname = current_process()
    print(procname)
    time.sleep(1.2)
    print(arg['node'])
    # print(arg['browerName'])

    driver = webdriver.Remote(
        command_executor="{}".format(arg['node']),
        desired_capabilities={
            "browserName": "chrome",
            "version": '75.0.3770.100',
            "video": "true",
            "platform": "WINDDOWS",
            'javascriptEnable': True
        }

    )
    # driver = webdriver.Remote(
    #     command_executor='http://192.168.0.104:6655/wd/hub',
    #     desired_capabilities={
    #         "browserName": "chrome",
    #         "version": '75.0.3770.100',
    #         "video": "true",
    #         "platform": "WINDDOWS",
    #         'javascriptEnable': True
    #     }
    #
    # )
    try:
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://smart.sqbj.com/portal/login')
        time.sleep(5)
        assert '智社区' in driver.title
        print('done')
        #请求共享资源锁
        lock.acquire()
        #向进程共享列表successTestCases中添加成功的测试用例名
        successTestCases.append('TestCase' + str(name))
        #释放资源锁
        lock.release()
        print('testcase'+ str(name)+'done')
    except AssertionError as e:
        print(e)
        driver.save_screenshot('F:\gitstorehouse\selenium3.0\分布式执行验证\\'+str(name)+".png")
        # 请求共享资源锁
        lock.acquire()
        # 向进程共享列表successTestCases中添加失败的测试用例名
        failTestCases.append('TestCase' + str(name))
        # 释放资源锁
        lock.release()
        print('执行失败')
    finally:
        driver.quit()
        print(time.time())

def run(nodeSeq):
    #创建一个多进程manage实例
    manage = Manager()
    #定义一个共享资源列表
    successTestCases = manage.list([])
    # 定义一个共享资源列表
    failTestCases = manage.list([])
    #创建一个锁
    lock= manage.Lock()
    #打印主进程ID
    print('主进程ID{}'.format(os.getpid()))
    #创建一个进程池3
    p = Pool(processes=3)
    #nodeSeq 节点列表
    testCaseNumber = len(nodeSeq)
    for i in range(testCaseNumber):
        #循环创建子进程，并将需要的数据传入子进程
        p.apply_async(node_task,args=(i+1,lock,nodeSeq[i],successTestCases,failTestCases))
    print('等待所有子进程退出')
    #关闭进程池
    p.close()
    #阻塞进程
    p.join()
    return successTestCases,failTestCases

if __name__ == '__main__':
    nodeLIist = [
        {'node':'http://192.168.0.104:6655/wd/hub'},
        {'node': 'http://192.168.0.104:6666/wd/hub'}
    ]
    testCaseNumber = len(nodeLIist)
    succTest,failtest = run(nodeLIist)
