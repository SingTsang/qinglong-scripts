#   --------------------------------注释区--------------------------------
#记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名
#   入口http://tig.juyangwangluo.cn/invite/436182
#   抓取cookie填入环境变量yuanshen_db
#   多号@分割   每日0.3自己提现     记得实名
#记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名
#记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名
#记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名
#记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名记得实名
#source:huaji


#   --------------------------------代码区--------------------------------
import requests
import time
import os
import re
def version():
    print('入口：http://tig.juyangwangluo.cn/invite/436182')

class yuanshen:
    def __init__(self,cookie) -> None:
        self.cookie = cookie
        self.header = {
    "Host": "m.juyangwangluo.cn",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/36.363636)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "X-Requested-With": "w2a.W2Am.juyangwangluo.cn",
    "Referer": "http://m.juyangwangluo.cn/mobile/my/index",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": f"{self.cookie}"
}
        self.header_={
    "Host": "m.juyangwangluo.cn",
    "Connection": "keep-alive",
    "Content-Length": "7",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/36.363636)",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://m.juyangwangluo.cn",
    "Referer": "http://m.juyangwangluo.cn/mobile/abonus/index/?xapp-target=blank",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": f"{self.cookie}"
}
    
    def main_task(self):
        url = "http://m.juyangwangluo.cn/mobile/abonus/index/?xapp-target=blank"
        r = requests.get(url,headers=self.header).text
        pattern = r"var uid = '(\d+)';"
        match = re.search(pattern, r)
        if match:
            result = match.group(1)
            print("🎉️匹配到uid:", result)
            self.uid = result
            url = "http://m.juyangwangluo.cn/mobile/abonus/fen"
            data = {
                "id": self.uid,
            }
            r = requests.post(url, headers=self.header_, data=data).json()
            if r['code'] == 1:
                print("🎉️领取分红成功")
            else:
                print(f"⛔️领取分红失败[{r['msg']}]")
        else:
            print("⛔️未找到匹配uid")


if __name__ == '__main__':
    version()
    cookie = ''
    if not cookie:
      
        cookie = os.getenv("yuanshen_db")
        if not cookie:
            print("请设置环境变量:yuanshen_db")
            exit()
    cookies = cookie.split("@")
    print(f"一共获取到{len(cookies)}个账号")
    print("记得实名 记得实名 记得实名 记得实名 记得实名 记得实名 记得实名 记得实名 记得实名 记得实名 记得实名 记得实名 记得实名")
    i = 1
    for cookie in cookies:
        print(f"\n--------开始第{i}个账号--------")
        main = yuanshen(cookie)
        main.main_task()
        print(f"--------第{i}个账号执行完毕--------")
        time.sleep(20)
        i += 1
