import datetime
import time
import aircv as ac
import os
import random
import logging
from logging import handlers


class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射
    def __init__(self,filename,level='info',when='M',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)


# 主函数
def main():

    # 对比两张图，找到坐标。
    def matchImg(imgsrc, imgobj):  # imgsrc=原始图像，imgobj=待查找的图片
        imsrc = ac.imread(imgsrc)
        imobj = ac.imread(imgobj)
        match_result = ac.find_template(imsrc, imobj,
                                        0.9)  # 0.9、confidence是精度，越小对比的精度就越低 {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
        if match_result is not None:
            match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
        return match_result

    # 返回好多次，保证能完全退出软件。
    def backback():
        # 返回
        log.logger.info("返回backback")
        r = os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        log.logger.info(r)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)

    def manyclick():
        # 这里是在点击屏幕固定区域采集能量
        for myx in range(229, 804, 50):
            for myy in range(400, 736, 50):
                myxstr = str(myx)
                myystr = str(myy)
                os.popen('adb -s 66819679 shell input tap ' + myxstr + ' ' + myystr, 'r', 1)
                # log.logger.info(myxstr +' , '+myystr)
                time.sleep(0.1)
        log.logger.info("get g")
        # 点击左下一点
        os.popen('adb -s 66819679 shell input tap 259 946', 'r', 1)
        time.sleep(0.2)
        # 点击右下一点
        os.popen('adb -s 66819679 shell input tap 883 774', 'r', 1)
        time.sleep(0.2)
        # 点击右下一点
        os.popen('adb -s 66819679 shell input tap 883 890', 'r', 1)
        time.sleep(0.2)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(2)

    # 打开支付宝蚂蚁森林操作
    def openalipay():
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 去点击
        os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
        time.sleep(2)
        # 打开alipay
        os.popen('adb -s 66819679 shell input tap 135 250', 'r', 1)
        time.sleep(2)
        # 首页
        os.popen('adb -s 66819679 shell input tap 108 2222', 'r', 1)
        time.sleep(2)
        # 向下滑动
        os.popen('adb -s 66819679 shell input swipe 520 300 520 1000')
        time.sleep(2)
        # 打开蚂蚁

        # 打开蚂蚁
        # 截图
        screencap()
        try:
            # alipay_friend
            if matchImg('phoneScreencap.png', 'antIcon.png') is not None:
                print("antIcon！" + str(
                    matchImg('phoneScreencap.png', 'antIcon.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'antIcon.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'antIcon.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'antIcon.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(4)
                # 采集
                manyclick()
                print("打开蚂蚁")
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(4)

        except Exception as e:
            print(e)
            print("这里有个异常")

    # 截图
    def screencap():
        try:
            # 截图
            os.popen('adb -s 66819679 shell screencap -p /storage/emulated/0/Documents/phoneScreencap.png')
            time.sleep(2)
            # 发送到电脑
            os.popen('adb -s 66819679 pull /storage/emulated/0/Documents/phoneScreencap.png')
            time.sleep(2)
        except Exception as e:
            log.logger.info(e)
            log.logger.info("这里有个异常adb -s 66819679 shell screencap")

    def doit():
        # 截图
        screencap()
        try:
            # alipay_friend
            if matchImg('phoneScreencap.png', 'alipay_friend.png') != None:
                log.logger.info("alipay_friend！" + str(
                    matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(4)
                log.logger.info("manyclick")
                manyclick()
            elif matchImg('phoneScreencap.png', 'install.png') != None:
                log.logger.info("install！" + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'install.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'install.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)
                return

            # alipay_help
            if matchImg('phoneScreencap.png', 'alipay_help.png') != None:
                log.logger.info("alipay_help！" + str(
                    matchImg('phoneScreencap.png', 'alipay_help.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_help.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'alipay_help.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'alipay_help.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(4)
                log.logger.info("manyclick,alipay_help")
                manyclick()

            mytime = datetime.datetime.now()
            if (mytime.hour == 6 and mytime.minute <= 30):
                # 截图
                screencap()
                # alipay_hui给特定的好友浇水，根据头像判断
                if matchImg('phoneScreencap.png', 'alipay_hui.png') != None:
                    log.logger.info("alipay_hui！" + str(
                        matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'alipay_hui.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(4)
                    log.logger.info("water")
                    os.popen('adb -s 66819679 shell input tap 1000 1500', 'r', 1)
                    time.sleep(4)
                    # 返回
                    os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                    time.sleep(3)

            # alipay_lookForMoreFriends查找更多好友
            if matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png') != None:
                log.logger.info("alipay_lookForMoreFriends！" + str(
                    matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'alipay_lookForMoreFriends.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(2)
                # 截图
                screencap()
                # alipay_friend
                if matchImg('phoneScreencap.png', 'alipay_friend.png') != None:
                    log.logger.info("alipay_friend！" + str(
                        matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'alipay_friend.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(4)
                    # 截图
                    screencap()

                    # 返回
                    os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                    time.sleep(3)

            # 滑动
            os.popen('adb -s 66819679 shell input swipe  520 1300 520 200')
            time.sleep(0.3)

            # alipay_nomore到底部了，得从头开始
            if matchImg('phoneScreencap.png', 'alipay_nomore.png') != None:
                log.logger.info("alipay_nomore！" + str(
                    matchImg('phoneScreencap.png', 'alipay_nomore.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_nomore.png')['result'][1]))
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                openalipay()

            # alipay_love因为网络等问题，如果出现这alipay_love图标就得从头再来。
            if matchImg('phoneScreencap.png', 'alipay_love.png') != None:
                log.logger.info("alipay_love！" + str(
                    matchImg('phoneScreencap.png', 'alipay_love.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'alipay_love.png')['result'][1]))
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(0.7)
                openalipay()
        except Exception as e:
            log.logger.info(e)
            log.logger.info("这里有个异常")

    def shuabao():
        os.popen('adb -s 66819679 shell input tap 100 2222', 'r', 1)
        mytime = random.uniform(5.0, 15.0)
        log.logger.info("see time : " + str(mytime))
        time.sleep(mytime)
        # 截图
        screencap()
        try:
            # 窗口1
            if matchImg('phoneScreencap.png', 'fuli1.png') != None:
                log.logger.info("fuli1！" + str(
                    matchImg('phoneScreencap.png', 'fuli1.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'fuli1.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'fuli1.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'fuli1.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(9)
                log.logger.info("fuli1")
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'close1.png') != None:
                    log.logger.info("close1！" + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close1.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close1.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    log.logger.info("close1")
                if matchImg('phoneScreencap.png', 'close2.png') != None:
                    log.logger.info("close2！" + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close2.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    log.logger.info("close2")

            if matchImg('phoneScreencap.png', 'install.png') != None:
                log.logger.info("install！" + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'install.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'install.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)
                return
            # 窗口2
            if matchImg('phoneScreencap.png', 'fuli2.png') != None:
                log.logger.info("fuli2！" + str(
                    matchImg('phoneScreencap.png', 'fuli2.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'fuli2.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'fuli2.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'fuli2.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(9)
                log.logger.info("fuli2")
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'close1.png') != None:
                    log.logger.info("close1！" + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close1.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close1.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    log.logger.info("close1")
                if matchImg('phoneScreencap.png', 'close2.png') != None:
                    log.logger.info("close2！" + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close2.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    log.logger.info("close2")

            if matchImg('phoneScreencap.png', 'fuli3.png') != None:
                log.logger.info("fuli3！" + str(
                    matchImg('phoneScreencap.png', 'fuli3.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'fuli3.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'fuli3.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'fuli3.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(9)
                log.logger.info("fuli3")
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'close1.png') != None:
                    log.logger.info("close1！" + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close1.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close1.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    log.logger.info("close1")
                if matchImg('phoneScreencap.png', 'close2.png') != None:
                    log.logger.info("close2！" + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close2.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    log.logger.info("close2")

            if matchImg('phoneScreencap.png', 'fuli4.png') != None:
                log.logger.info("fuli4！" + str(
                    matchImg('phoneScreencap.png', 'fuli4.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'fuli4.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'fuli4.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'fuli4.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(9)
                log.logger.info("fuli4")
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'close1.png') != None:
                    log.logger.info("close1！" + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close1.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close1.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    log.logger.info("close1")
                if matchImg('phoneScreencap.png', 'close2.png') != None:
                    log.logger.info("close2！" + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close2.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    log.logger.info("close2")

            if matchImg('phoneScreencap.png', 'fuli5.png') != None:
                log.logger.info("fuli5！" + str(
                    matchImg('phoneScreencap.png', 'fuli5.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'fuli5.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'fuli5.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'fuli5.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(9)
                log.logger.info("fuli5")
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'close1.png') != None:
                    log.logger.info("close1！" + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close1.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close1.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close1.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    log.logger.info("close1")
                if matchImg('phoneScreencap.png', 'close2.png') != None:
                    log.logger.info("close2！" + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'close2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'close2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'close2.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(9)
                    log.logger.info("close2")

        except Exception as e:
            log.logger.info(e)
            log.logger.info("这里有个异常")


    # 淘新闻
    def taonews():
        #点击左下角的刷新按钮
        os.popen('adb -s 66819679 shell input tap 107 2222', 'r', 1)
        log.logger.info("淘新闻_点击左下角的刷新按钮")
        time.sleep(3)
        # 截图
        screencap()
        log.logger.info("淘新闻_截图")
        try:
            # 点击分钟前，能进去看
            if matchImg('phoneScreencap.png', 'taonews_min.png') != None:
                log.logger.info("淘新闻_点taonews_min进去看资讯！" + str(
                    matchImg('phoneScreencap.png', 'taonews_min.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'taonews_min.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'taonews_min.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'taonews_min.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 向下滑动
                for i in range(1, 9, 1):
                    i = i + 1
                    time.sleep(random.uniform(1.0, 2.0))
                    # 向下滑动
                    os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
                    mytime = datetime.datetime.now()
                    log.logger.info("淘新闻_已经滚动" + str(i) + "次。" + str(mytime) + "")

                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                log.logger.info("淘新闻_返回")
                time.sleep(1)
            elif matchImg('phoneScreencap.png', 'install.png') != None:
                log.logger.info("install！" + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'install.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'install.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)

            elif matchImg('phoneScreencap.png', 'taonews_hour.png') != None:
                # 点击小时前，能进去看
                    log.logger.info("淘新闻_点taonews_hour进去看资讯！" + str(
                        matchImg('phoneScreencap.png', 'taonews_hour.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'taonews_hour.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'taonews_hour.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'taonews_hour.png')['result'][1])
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(3)
                    # 向下滑动
                    for i in range(1, 9, 1):
                        i = i + 1
                        time.sleep(random.uniform(1.0, 2.0))
                        # 向下滑动
                        os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
                        mytime = datetime.datetime.now()
                        log.logger.info("淘新闻_已经滚动" + str(i) + "次。" + str(mytime) + "")

                    # 返回
                    os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                    log.logger.info("淘新闻_返回")
                    time.sleep(1)

            # 关闭无聊的弹窗
            if matchImg('phoneScreencap.png', 'abandon.png') != None:
                log.logger.info("淘新闻_点abandon！" + str(
                    matchImg('phoneScreencap.png', 'abandon.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'abandon.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'abandon.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'abandon.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
        except Exception as e:
            log.logger.info(e)
            log.logger.info("这里有个异常")

        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        log.logger.info("淘新闻_返回")
        time.sleep(0.5)


    # 快看点
    def kuaikandian():
        #点击左下角的刷新按钮
        os.popen('adb -s 66819679 shell input tap 107 2222', 'r', 1)
        log.logger.info("快看点_点击左下角的刷新按钮")
        time.sleep(3)
        # 截图
        screencap()
        log.logger.info("快看点_截图")
        try:
            # 点击分钟前，能进去看
            if matchImg('phoneScreencap.png', 'kuaikandian_min.png') != None:
                log.logger.info("淘新闻_点kuaikandian进去看资讯！" + str(
                    matchImg('phoneScreencap.png', 'kuaikandian_min.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'kuaikandian_min.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'kuaikandian_min.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'kuaikandian_min.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 向下滑动
                for i in range(1, 15, 1):
                    i = i + 1
                    time.sleep(random.uniform(1.0, 2.0))
                    # 向下滑动
                    os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
                    mytime = datetime.datetime.now()
                    log.logger.info("kuaikandian_已经滚动" + str(i) + "次。" + str(mytime) + "")

                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                log.logger.info("kuaikandian_返回")
                time.sleep(2)
            # 点击评论，能进去看
            elif matchImg('phoneScreencap.png', 'kuaikandian_comment.png') != None:
                log.logger.info("kuaikandian_comment！" + str(
                    matchImg('phoneScreencap.png', 'kuaikandian_comment.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'kuaikandian_comment.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'kuaikandian_comment.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'kuaikandian_comment.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 向下滑动
                for i in range(1, 15, 1):
                    i = i + 1
                    time.sleep(random.uniform(1.0, 2.0))
                    # 向下滑动
                    os.popen('adb -s 66819679 shell input swipe 520 1000 520 300 ')
                    mytime = datetime.datetime.now()
                    log.logger.info("kuaikandian__已经滚动" + str(i) + "次。" + str(mytime) + "")

                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                log.logger.info("kuaikandian_返回")
                time.sleep(2)
            elif matchImg('phoneScreencap.png', 'install.png') != None:
                log.logger.info("install！" + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'install.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'install.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'install.png')['result'][1])
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(3)
                # 返回
                os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
                time.sleep(3)

        except Exception as e:
            log.logger.info(e)
            log.logger.info("这里有个异常")
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(1)


    def douyin():
        os.popen('adb -s 66819679 shell input tap 100 2222', 'r', 1)
        mytime = random.uniform(5.0, 15.0)
        log.logger.info("see time : " + str(mytime))
        time.sleep(mytime)

    # 打开微博
    def openWeibo():
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 返回
        os.popen('adb -s 66819679 shell input keyevent 4', 'r', 1)
        time.sleep(0.5)
        # 去点击
        os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
        time.sleep(2)
        # 打开weibo
        os.popen('adb -s 66819679 shell input tap 125 607', 'r', 1)
        time.sleep(7)
        # 点击发现
        os.popen('adb -s 66819679 shell input tap 552 2212', 'r', 1)
        time.sleep(4)
        # 再一次点击发现
        os.popen('adb -s 66819679 shell input tap 552 2212', 'r', 1)
        time.sleep(4)
        # 点击搜索框
        os.popen('adb -s 66819679 shell input tap 552 155', 'r', 1)
        time.sleep(2)
        # 点击最近的一次搜索文字
        os.popen('adb -s 66819679 shell input tap 552 311', 'r', 1)
        time.sleep(5)
        # 点击实时
        os.popen('adb -s 66819679 shell input tap 406 286', 'r', 1)
        time.sleep(5)

    # 微博点赞
    def Weibo_zan():

        mytime = random.uniform(1.0, 3.0)
        log.logger.info("-------zan函数被调用: " + str(mytime))
        time.sleep(mytime)
        # 截图
        screencap()
        try:
            # 窗口1
            if matchImg('phoneScreencap.png', 'zan.png') != None:
                log.logger.info("找到zan！" + str(
                    matchImg('phoneScreencap.png', 'zan.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'zan.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'zan.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'zan.png')['result'][1])
                log.logger.info("我来点击：点赞")
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(1)
        except Exception as e:
            log.logger.info(e)
            log.logger.info("这里有个异常")

        try:
            # 窗口1
            if matchImg('phoneScreencap.png', 'comment.png') != None:
                log.logger.info("找到评论！" + str(
                    matchImg('phoneScreencap.png', 'comment.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'comment.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'comment.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'comment.png')['result'][1])
                log.logger.info("我来点击：评论")
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(4)
                # 截图
                screencap()
                if matchImg('phoneScreencap.png', 'baidulogo.png') != None:
                    log.logger.info("找到baidulogo！" + str(
                        matchImg('phoneScreencap.png', 'baidulogo.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'baidulogo.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'baidulogo.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'baidulogo.png')['result'][1])
                    log.logger.info("我来点击：baidulogo")
                    os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                    time.sleep(2)
                    # 百度输入法 -- 懒人短语
                    os.popen('adb -s 66819679 shell input tap 680 1663', 'r', 1)
                    time.sleep(1)
                    # 百度输入法 -- 懒人短语 -- 点击我的话
                    os.popen('adb -s 66819679 shell input tap 428 1713', 'r', 1)
                    time.sleep(2)
                    # 百度输入法 -- 键盘随便一个字母
                    myxstr = str(random.randint(203, 841))
                    myystr = str(random.randint(1600, 1960))
                    os.popen('adb -s 66819679 shell input tap ' + myxstr + ' ' + myystr, 'r', 1)
                    print(myxstr + myystr)
                    time.sleep(2)
                    # 百度输入法 -- 回车
                    os.popen('adb -s 66819679 shell input tap 974 2150', 'r', 1)
                    time.sleep(1)
                    # 百度输入法 -- 懒人短语 -- 发送
                    os.popen('adb -s 66819679 shell input tap 988 1253', 'r', 1)
                    time.sleep(2)
                    # goback()
                elif matchImg('phoneScreencap.png', 'comment2.png') != None:
                    log.logger.info("找到评论comment2！" + str(
                        matchImg('phoneScreencap.png', 'comment2.png')['result'][0]) + ',' + str(
                        matchImg('phoneScreencap.png', 'comment2.png')['result'][1]))
                    myx = str(matchImg('phoneScreencap.png', 'comment2.png')['result'][0])
                    myy = str(matchImg('phoneScreencap.png', 'comment2.png')['result'][1])
                    log.logger.info("评论comment2：")
                    # 点击底部的评论按钮
                    os.popen('adb -s 66819679 shell input tap 513 2212', 'r', 1)
                    time.sleep(3)
                    # 百度输入法
                    os.popen('adb -s 66819679 shell input tap 87 1463', 'r', 1)
                    time.sleep(2)
                    # 百度输入法 -- 懒人短语
                    os.popen('adb -s 66819679 shell input tap 680 1663', 'r', 1)
                    time.sleep(1)
                    # 百度输入法 -- 懒人短语 -- 点击我的话
                    os.popen('adb -s 66819679 shell input tap 428 1713', 'r', 1)
                    time.sleep(1)
                    # 百度输入法 -- 键盘随便一个字母
                    myxstr = str(random.randint(203, 841))
                    myystr = str(random.randint(1600, 1960))
                    os.popen('adb -s 66819679 shell input tap ' + myxstr + ' ' + myystr, 'r', 1)
                    print(myxstr + myystr)
                    time.sleep(2)
                    # 百度输入法 -- 回车
                    os.popen('adb -s 66819679 shell input tap 974 2150', 'r', 1)
                    time.sleep(1)
                    # 百度输入法 -- 懒人短语 -- 发送
                    os.popen('adb -s 66819679 shell input tap 988 1253', 'r', 1)
                    time.sleep(2)
                    goback()
        except Exception as e:
            log.logger.info(e)
            log.logger.info("这里有个异常")


        for i in range(1, 4):
            # 截图
            time.sleep(2)
            screencap()

            if matchImg('phoneScreencap.png', 'search.png') != None:
                log.logger.info("找到search！" + str(
                    matchImg('phoneScreencap.png', 'search.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'search.png')['result'][1]))
                # myx = str(matchImg('phoneScreencap.png', 'search.png')['result'][0])
                # myy = str(matchImg('phoneScreencap.png', 'search.png')['result'][1])
                # 向下滑动
                log.logger.info("向下滑动")
                os.popen('adb -s 66819679 shell input swipe 361 1700 361 1400')
                time.sleep(2)
            else:
                print('不是预计的界面，要返回了')
                goback()
                time.sleep(2)

        # 向下滑动
        log.logger.info("向下滑动")
        os.popen('adb -s 66819679 shell input swipe 361 1700 361 1000')
        time.sleep(2)

    # 模拟滑动
    def initlocal():
        time.sleep(2)  # 滑动前休息2秒，避免网络不好
        os.system('adb -s 66819679 shell input swipe 900 1200 900 500')  # 模拟从下往上滑动
        time.sleep(2)  # 滑动后休息2秒，避免开始计时延迟

    # 返回上一页面
    def goback():
        os.system('adb -s 66819679 shell input keyevent KEYCODE_BACK')  # 返回
        print('返回')

    # 浏览双十一主会场
    def see3():
        # 截图
        screencap()
        try:
            # 窗口1
            if matchImg('phoneScreencap.png', 'comein.png') != None:
                log.logger.info("comein！" + str(
                    matchImg('phoneScreencap.png', 'comein.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'comein.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'comein.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'comein.png')['result'][1])
                log.logger.info("进入逛店")
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(1)
                initlocal()
                print('进入店铺，浏览中，请等待 16 秒')
                time.sleep(16)
                goback()
                time.sleep(5)
            # 窗口1
            elif matchImg('phoneScreencap.png', 'comein2.png') != None:
                log.logger.info("comein2！" + str(
                    matchImg('phoneScreencap.png', 'comein2.png')['result'][0]) + ',' + str(
                    matchImg('phoneScreencap.png', 'comein2.png')['result'][1]))
                myx = str(matchImg('phoneScreencap.png', 'comein2.png')['result'][0])
                myy = str(matchImg('phoneScreencap.png', 'comein2.png')['result'][1])
                log.logger.info("进入逛店2")
                os.popen('adb -s 66819679 shell input tap ' + myx + ' ' + myy, 'r', 1)
                time.sleep(1)
                initlocal()
                print('进入店铺2，浏览中，请等待 16 秒')
                time.sleep(16)
                goback()
                time.sleep(5)
        except Exception as e:
            log.logger.info(e)
            log.logger.info("这里有个异常")

                # os.system('adb -s 66819679 shell input tap 900 1950')  # 进入逛店

        print('已完成逛店任务')

    i = 0
    while 1 == 1:

        log = Logger('log/all.log', level='debug')
        log.logger.debug('debug')
        log.logger.info('info')
        log.logger.warning('警告')
        log.logger.error('报错')
        log.logger.critical('严重')
        Logger('log/error.log', level='error').logger.error('error')

        mytime = datetime.datetime.now()
        log.logger.info("现在时间（）："+ str(mytime))

        # 22
        if (mytime.hour == 19):
            for i in range(1, 50):
                print('===== 3逛*****店({}/20) ======'.format(i))
                # 返回好多次
                backback()
                # home
                os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
                time.sleep(3)
                log.logger.info("开始")

                os.system('adb -s 66819679 shell input tap 346 614')
                print('打开淘宝')
                if(i==1):
                    time.sleep(10)
                    print('第一次打开淘宝，等待多10s')
                time.sleep(5)
                os.system('adb -s 66819679 shell input tap 908 157')
                print('打开20亿')
                time.sleep(5)
                os.system('adb -s 66819679 shell input tap 900 1700')  # 点击领喵币，弹出任务菜单
                print('点击领喵币，弹出任务菜单')
                time.sleep(2)
                # 浏览双十一主会场
                # see1()
                see3()

                # 返回好多次
                backback()
                # home
                os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
                time.sleep(3)
                # time.sleep(2)
                # os.system('adb -s 66819679 shell input tap 908 157')
                # print('打开20亿')
                # time.sleep(6)

                # see4()

            print('全部任务已完成')
        mytime = datetime.datetime.now()

        # 抖音极速版s
        if (mytime.hour == 0 ) or ( mytime.hour == 1)  :
            log.logger.info("抖音极速版开始")
            i = 0
            # 返回好多次
            backback()
            # 打开抖音极速版
            os.popen('adb -s 66819679 shell input tap 538 275', 'r', 1)
            time.sleep(5)
            for myy in range(1, 20, 1):
                i = i + 1
                douyin()
                mytime = datetime.datetime.now()
                log.logger.info("douyin" + str(i) + "次。" + str(mytime))
                # if myy == 1 :
                #     shuabao_comment()
                #     log.logger.info("shuabao_comment")
            time.sleep(1)
            # 返回好多次
            backback()
            # home
            os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
            time.sleep(3)
        mytime = datetime.datetime.now()

        # 刷宝
        if (mytime.hour == 2 ) or ( mytime.hour == 3)   or ( mytime.hour == 23) :
            log.logger.info("刷宝开始")
            i = 0
            # 返回好多次
            backback()
            # 打开刷宝
            os.popen('adb -s 66819679 shell input tap 337 267', 'r', 1)
            time.sleep(10)
            for myy in range(1, 20, 1):
                i = i + 1
                shuabao()
                mytime = datetime.datetime.now()
                log.logger.info("shuabao" + str(i) + "次。" + str(mytime))
                # if myy == 1 :
                #     shuabao_comment()
                #     log.logger.info("shuabao_comment")
            time.sleep(1)
            # 返回好多次
            backback()
            # home
            os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
            time.sleep(3)
        mytime = datetime.datetime.now()

        # 淘新闻
        if (mytime.hour == 4):
            log.logger.info("淘新闻开始")
            i = 0
            # 返回好多次
            backback()
            # 打开淘新闻
            os.popen('adb -s 66819679 shell input tap 751 257', 'r', 1)
            time.sleep(10)
            for myy in range(1, 15, 1):
                i = i + 1
                taonews()
                mytime = datetime.datetime.now()
                log.logger.info("淘新闻" + str(i) + "次。" + str(mytime))

            # 返回好多次
            backback()
            # home
            os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
            time.sleep(3)
        mytime = datetime.datetime.now()

        # 快看点
        if (mytime.hour == 5 )  :
            log.logger.info("快看点开始")
            i = 0
            # 返回
            log.logger.info("返回" +  str(mytime))
            # 返回好多次
            backback()
            # 打开快看点
            os.popen('adb -s 66819679 shell input tap 957 260', 'r', 1)
            time.sleep(10)
            for myy in range(1, 20, 1):
                i = i + 1
                kuaikandian()
                mytime = datetime.datetime.now()
                log.logger.info("快看点" + str(i) + "次。" + str(mytime))
            # 返回好多次
            backback()
            # home
            os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
            time.sleep(3)
        mytime = datetime.datetime.now()

        # 支付宝
        if ( mytime.hour == 6) or ( mytime.hour == 7) or ( mytime.hour == 8) or ( mytime.hour == 8 ) or ( mytime.hour < 0):
            i = 0
            # 返回好多次
            backback()
            openalipay()
            for myy in range(1, 50, 1):
                i = i + 1
                time.sleep(0.2)
                doit()
                mytime = datetime.datetime.now()
                log.logger.info("已经滚动" + str(i) + "次。" + str(mytime))
            # 返回好多次
            backback()
            # home
            os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
            time.sleep(3)
        mytime = datetime.datetime.now()

        # 手机微博点赞
        myinttime = 10
        myinttime2 = 11
        if  ( mytime.hour == myinttime) or ( mytime.hour == myinttime2) :
            mytime = datetime.datetime.now()
            i = 0
            # 返回好多次

            backback()

            openWeibo()
            for myy in range(1, 10000, 1):
                log.logger.info("for循环内")
                mytime = datetime.datetime.now()
                if  ( mytime.hour == myinttime)  or  ( mytime.hour == myinttime2) :
                    Weibo_zan()
                    log.logger.info("是这个时间段")
                else:
                    log.logger.info("不是这个时间段")
                    break

            # home
            os.popen('adb -s 66819679 shell input keyevent 3', 'r', 1)
            time.sleep(3)



main()