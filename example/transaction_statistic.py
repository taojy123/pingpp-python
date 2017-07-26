# -*- coding: utf-8 -*-

import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_live_vjfr90jj1q985KuPO84iP8KO'
app_id = 'app_LibTW1n1SOq9Pin1'

pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

'''
  设置请求签名密钥，密钥对需要你自己用 openssl 工具生成，如何生成可以参考帮助中心：https://help.pingxx.com/article/123161；
  生成密钥后，需要在代码中设置请求签名的私钥(rsa_private_key.pem)；
  然后登录 [Dashboard](https://dashboard.pingxx.com)->点击右上角公司名称->开发信息->商户公钥（用于商户身份验证）
  将你的公钥复制粘贴进去并且保存->先启用 Test 模式进行测试->测试通过后启用 Live 模式
'''
# 设置私钥内容方式1：通过路径读取签名私钥
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

# app_id 支持全局配置
pingpp.app_id = app_id

# Statistics
try:
    statistics = pingpp.Statistics.retrieve(app=app_id)
    print(statistics)
except Exception as e:
    print(e.http_body)
