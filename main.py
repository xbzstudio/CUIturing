'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG
'''
import json,os
have_settings=os.path.isfile(".//settings.ini")
setting=open(".//settings.ini")
if(not(have_settings)):
    setting.write("")
import turingAPI
import urllib3
cookie=input("cookie:")
print("Logging...")
user=turingAPI.icodeUser(cookie)
print("Login is successfully.")
if(not(user.checkLogin())):
    print("cookie is invalid")
    exit(1)
print("小图灵控制台版登陆成功，请输入功能编号")
'''
while(True):
    num=int(input())
    if(num)
    '''