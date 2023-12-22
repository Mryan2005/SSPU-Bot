import pickle
from seleniumwire import webdriver
import selenium.common.exceptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from browsermobproxy import Server
import io
import settings
import sys
import time
import urllib.request
settings = settings.user
server = Server(r".\src\browsermob-proxy\bin\browsermob-proxy")
server.start()
proxy = server.create_proxy()
print('proxy', proxy.proxy)
def MakeError():
    raise Exception("如登")
ser = Service()
ser.path = 'C:\\Users\\A2564\\AppData\\Local\\Programs\\Python\\Python311\\geckodriver.exe'
firefox_options = Options()
#firefox_options.add_argument('--ignore-certificate-errors')
#firefox_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
#firefox_options.add_argument("-headless")
driver = webdriver.Firefox(options=firefox_options, service=ser)
proxy.new_har(options={
    'captureContent': True,
    'captureHeaders': True
})
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
class Post(object):
    def setTitle(self,title):
        self.title = title
    def setUrl(self,url):
        self.url = url
    def setOutline(self,outline):
        self.outline = outline
def is_word_which_i_need(chars):
    for i in chars:
        if '\u4e00' <= i <= '\u9fff':
            return True
        elif '0' <= i <= '9':
            return True
        elif '-' == i:
            return True
        else:
            return False
def get():
    res=urllib.request.urlopen('https://jwc.sspu.edu.cn/897/list.htm')
    htmlBytes=res.read()
    filr = open('website.html','wb')
    filr.write(htmlBytes)
    filr.close()
    filr = open('website.html','rb')
    filr.close()
    file = open('website.html','rb')
    file2 = open('result.txt','w')
    texts = file.readlines()
    file.close()
    text = ''
    flag = 0
    flag1 = 0
    posts = []
    for i in texts:
        if('<ul class="news_list list2">' in i.decode("utf8") and flag == 0):
            flag = 1
            print("find")
        if(flag == 1):
            if('<span class="news_title">' in i.decode("utf8")):
                for j in i.decode("utf8"):
                    if(j != '\t' and flag1 == 0):
                        text += j
                    if('<span class="news_title">' in text and flag1 == 0):
                        text = ''
                        j = ''
                        flag1 = 1
                    if(flag1 == 1):
                        if(j != '\n' and j != '\t'):
                            text += j
                            if('</span>' in text):
                                #print(text)
                                file2.write(text)
                                file2.write('\n')
                                text = ''
                                flag1 = 0                    
    file2.close()
    text = ''
    flag = 0
    k = -1
    file = open('result.txt','r')
    file1 = open("result.md",'w')
    for i in file.readlines():
        k += 1
        posts.append(Post())
        for j in i:
            if(j != ' '):
                text += j
            if('<a' == text):
                flag = 1
                text = ''
            if(flag == 1):
                if('href=' == text):
                    text = ''
                    flag = 2
            if(flag == 2):
                if(j == "'"):
                    flag = 3
                    text = ''
                    continue
            if(flag == 3):
                if(j == "'"):
                    flag = 4
                    text = text.replace("'","",1)
                    print("https://jwc.sspu.edu.cn" + text)
                    posts[k].setUrl("https://jwc.sspu.edu.cn" + text)
                    text = ''
            if(flag == 4):
                if("target='_blank'" == text):
                    text = ''
                    flag = 5
            if(flag == 5):
                if('title=' == text):
                    text = ''
                    flag = 6
            if(flag == 6):
                if(j == "'"):
                    flag = 7
                    text = ''
                    continue
            if(flag == 7):
                if(j == "'"):
                    flag = 8
                    text = text.replace("'","",1)
                    print(text)
                    posts[k].setTitle(text)
                    print('------------------')
                    text = ''
            if(flag == 8):
                flag = 0
                break
    # get the outline of the post
    count = 0
    for g in posts:
        url = g.url
        try:
            driver.get(url)
            outline = driver.find_element(By.XPATH, "//div[@class=\"WordSection1\"]")
            outline = outline.text[:200]
            g.setOutline(outline)
        except selenium.common.exceptions.NoSuchElementException:
            g.setOutline("由于网页不支持打开，请到该站点查看")
        count += 1
        print(count)
    file3 = open("./result.md","w")
    for o in posts:
        file3.write("[")
        file3.write(o.title)
        file3.write("](")
        file3.write(o.url)
        file3.write(")\n")
        file3.write(o.outline+"……")
        file3.write("\n\n")
    count -= 1
    lastpart = count
    res=urllib.request.urlopen('https://pe2016.sspu.edu.cn/342/list.htm')
    htmlBytes=res.read()
    filr = open('website.html','wb')
    filr.write(htmlBytes)
    filr.close()
    filr = open('website.html','rb')
    filr.close()
    file = open('website.html','rb')
    file2 = open('result.txt','w')
    texts = file.readlines()
    file.close()
    text = ''
    flag = 0
    flag1 = 0
    for i in texts:
        if('<div class="dht_blank1"></div>' in i.decode("utf8") and flag == 0):
            flag = 1
            print("find")
        if(flag == 1):
            if('<li>' in i.decode("utf8")):
                for j in i.decode("utf8"):
                    if(j != '\t' and flag1 == 0):
                        text += j
                    if('<li>' in text and flag1 == 0):
                        text = ''
                        j = ''
                        flag1 = 1
                    if(flag1 == 1):
                        if(j != '\n' and j != '\t'):
                            text += j
                            if('</li>' in text):
                                #print(text)
                                file2.write(text)
                                file2.write('\n')
                                text = ''
                                flag1 = 0                    
    file2.close()
    text = ''
    flag = 0
    file = open('result.txt','r')
    for i in file.readlines():
        k += 1
        posts.append(Post())
        for j in i:
            if(j != ' '):
                text += j
            if('<a' in text):
                flag = 1
                text = ''
            if(flag == 1):
                if('href=' in text):
                    text = ''
                    flag = 2
            if(flag == 2):
                if(j == '"'):
                    flag = 3
                    text = ''
                    continue
            if(flag == 3):
                if(j == '"'):
                    flag = 4
                    text = text.replace('"',"",1)
                    print("https://pe2016.sspu.edu.cn" + text)
                    posts[k].setUrl("https://pe2016.sspu.edu.cn" + text)
                    text = ''
            if(flag == 4):
                if('target="_blank"' in text):
                    text = ''
                    flag = 5
            if(flag == 5):
                if('title=' in text):
                    text = ''
                    flag = 6
            if(flag == 6):  
                if(j == '"'):
                    flag = 7
                    text = ''
                    continue
            if(flag == 7):
                if(j == '"'):
                    flag = 8
                    text = text.replace('"',"",1)
                    print(text)
                    posts[k].setTitle(text)
                    print('------------------')
                    text = ''
            if(flag == 8):
                flag = 0
                break
        # get the outline of the post
        file.close()
    for g in posts[lastpart+1:]:
        url = g.url
        try:
            if("files/" in url):
                g.setOutline("由于网页不支持打开，请到该站点查看")
                continue
            driver.get(url)
            outline = driver.find_element(By.XPATH, "//div[@class=\"wp_articlecontent\"]")
            outline = outline.text[:200]
            g.setOutline(outline)
        except selenium.common.exceptions.NoSuchElementException:
            g.setOutline("由于网页不支持打开，请到该站点查看")
        count += 1
    lastpart = count
    file3 = open("./result.md","a")
    for o in posts:
        file3.write("[")
        file3.write(o.title)
        file3.write("](")
        file3.write(o.url)
        file3.write(")\n")
        file3.write(o.outline+"……")
        file3.write("\n\n")
    file3.close()
    driver.get("https://mp.weixin.qq.com")
    try:
        cookies1 = login()
    finally:
        writeafile = driver.find_elements(By.XPATH, "//div[@class=\"new-creation__menu-title\"]")
        writeafile[0].click()
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        time.sleep(10)
        opentag = driver.find_element(By.XPATH, "//li[@id=\"js_editor_insertlink\"]")
        opentag.click()
        time.sleep(5)
        opentag = driver.find_elements(By.XPATH, "//button[@class=\"weui-desktop-btn weui-desktop-btn_default\"]")
        opentag[0].click()
        inputtag = driver.find_elements(By.XPATH, "//input[@class=\"weui-desktop-form__input\"]")
        inputtag[1].send_keys("青春二工大")
        searchtag = driver.find_elements(By.XPATH, "//button[@class=\"weui-desktop-icon-btn weui-desktop-search__btn\"]")
        searchtag[0].click()
        time.sleep(5)
        selecttag = driver.find_elements(By.XPATH, "//li[@class=\"inner_link_account_item\"]")
        selecttag[0].click()
        list = driver.requests
        url = ""
        for i in list:
            if("mp.weixin.qq.com" in i.url):
                if("cgi-bin/appmsgpublish?sub=list&search_field=null" in i.url):
                    if(not ('&query=&fakeid=&' in i.url)):
                        url = i.url
                        break
        del driver.requests
        driver.get(url)
        htmls = driver.page_source
        text = ''
        flag = 0
        for i in htmls:
            text += i
            if( '"title\\\\\":\\\\' in text):
                k += 1
                text = ''
                flag = 1
                posts.append(Post())
            if(flag == 1):
                if('\\\\\"' in text):
                    text = text.replace('"','')
                    text = text.replace('\\\\','')
                    text = text.replace('"','')
                    print(text)
                    posts[k].setTitle(title=text)
                    flag = 2
                    text = ''
            if(flag == 2):
                if('"link\\\\\":\\\\' in text):
                    text = ''
                    flag = 3
            if(flag == 3):
                if('\\\\\"' in text):
                    text = text.replace('"','')
                    text = text.replace('\\\\','')
                    text = text.replace('"','')
                    print(text)
                    posts[k].setUrl(url=text)
                    flag = 4
                    text = ''
            if(flag == 4):
                flag = 0
        driver.close()
        file3 = open("./result.md","a")
        for g in posts[lastpart+1:]:
            url = g.url
            try:
                if("files/" in url):
                    g.setOutline("由于网页不支持打开，请到该站点查看")
                    continue
                driver.get(url)
                outline = driver.find_element(By.XPATH, "//div[@class=\"wp_articlecontent\"]")
                outline = outline.text[:200]
                g.setOutline(outline)
            except selenium.common.exceptions.NoSuchElementException:
                g.setOutline("由于网页不支持打开，请到该站点查看")
        file3.write("## 青春二工大\n\n")
        for o in posts[lastpart+1:]:
            file3.write("[")
            file3.write(o.title)
            file3.write("](")
            file3.write(o.url)
            file3.write(")\n")
            file3.write(o.outline+"……")
            file3.write("\n\n")
        file3.close()
def login():
    cookies1 = ''
    needthings = ["name", "value", "domain", "path", "expiry", "secure", "httpOnly", "sameSite", "priority", "sameParty", "sourceScheme", "sourcePort", "sourcePriority", "isSameSite", "isSameParty", "isSecure", "isHttpOnly", "isHostOnly", "isSession", "isPersistent", "isExpired", "isSecureContext", "isFirstPartyOnly", "sameSiteStatus", "samePartyStatus", "priorityValue", "sourcePriorityValue", "sameSiteValue", "samePartyValue", "priorityValue", "sourcePriorityValue", "sameSiteValue", "samePartyValue", "domain"]
    try:
        cookies = pickle.load(open("taobao_cookies.pkl", "rb"))
        for cookie in cookies: 
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            for thing in needthings:
                if(thing in cookie):
                    value = cookie.get(thing)
                    cookies1 += thing
                    cookies1 += "="
                    cookies1 += str(value)
                    cookies1 += "; "
            driver.add_cookie(cookie)
        driver.refresh()
        writeafile = driver.find_elements(By.XPATH, "//div[@class=\"new-creation__menu-title\"]")
        if writeafile[0] == '':
            MakeError()
    except FileNotFoundError:
        LoginTag = driver.find_element(By.XPATH, "//a[@class=\"login__type__container__select-type\"]")    
        LoginTag.click()
        UserNameTag = driver.find_element(By.XPATH, "//input[@name=\"account\"]")
        UserNameTag.send_keys(settings["weixinUsername"])
        PasswordTag = driver.find_element(By.XPATH, "//input[@name=\"password\"]")
        PasswordTag.send_keys(settings["weixinPassword"])
        LoginTag = driver.find_element(By.XPATH, "//a[@class=\"btn_login\"]")
        LoginTag.click()
        time.sleep(60)
        cookie = driver.get_cookies()
        pickle.dump(cookie, open('taobao_cookies.pkl','wb'))
        driver.refresh()
        writeafile = driver.find_elements(By.XPATH, "//div[@class=\"new-creation__menu-title\"]")
        if writeafile[0] == '':
                MakeError()
        cookies = pickle.load(open("taobao_cookies.pkl", "rb"))
        for cookie in cookies: 
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            for thing in needthings:
                if(thing in cookie):
                    value = cookie.get(thing)
                    cookies1 += thing
                    cookies1 += "="
                    cookies1 += str(value)
                    cookies1 += "; "
            driver.add_cookie(cookie)
    except Exception:
        driver.delete_all_cookies()
        LoginTag = driver.find_element(By.XPATH, "//a[@class=\"login__type__container__select-type\"]")    
        LoginTag.click()
        UserNameTag = driver.find_element(By.XPATH, "//input[@name=\"account\"]")
        UserNameTag.send_keys(settings["weixinUsername"])
        PasswordTag = driver.find_element(By.XPATH, "//input[@name=\"password\"]")
        PasswordTag.send_keys(settings["weixinPassword"])
        LoginTag = driver.find_element(By.XPATH, "//a[@class=\"btn_login\"]")
        LoginTag.click()
        time.sleep(60)
        cookie = driver.get_cookies()
        pickle.dump(cookie, open('taobao_cookies.pkl','wb'))
        driver.refresh()
        writeafile = driver.find_elements(By.XPATH, "//div[@class=\"new-creation__menu-title\"]")
        if writeafile[0] == '':
                MakeError()
        cookies = pickle.load(open("taobao_cookies.pkl", "rb"))
        for cookie in cookies: 
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            for thing in needthings:
                if(thing in cookie):
                    value = cookie.get(thing)
                    cookies1 += thing
                    cookies1 += "="
                    cookies1 += str(value)
                    cookies1 += "; "
            driver.add_cookie(cookie)
    return cookies1
if __name__ == "__main__" :
    get()
