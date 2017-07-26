# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  接入退款流程参考开发者中心：https://www.pingxx.com/docs/server ，文档可筛选后端语言和接入渠道。
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import os
import time

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')
# 用户充值接口示例

'''
    time_expire 订单失效时间，用 Unix 时间戳表示。时间范围在订单创建后的 5 分钟到 1 天，默认为 1 天，创建时间以 Ping++ 服务器时间为准。 微信对该参数的有效值限制为 2 小时内；银联对该参数的有效值限制为 1 小时内。
    metadata,extra 参照charge中的参数
'''
params = {
  "app": app_id,
  "uid": "15800973612",
  "merchant_order_no": "88888888888",
  "channel":"wx",
  "amount": "30",
  "client_ip": "127.0.0.1",
  "currency": "cny",
  "subject": "test1",
  "body": "test1body1",
  "description": "test1-description",
  "time_expire": "1479266356"
}

# 创建 recharge
try:
    recharge = pingpp.Recharge.create(**params)
    print(">> create recharge ", recharge)
except Exception as e:
    print e.http_body