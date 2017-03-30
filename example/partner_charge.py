# -*- coding: utf-8 -*-

import pingpp
import os
import time

api_key = 'partner_2381239714787349712987'

# 设置 API Key
pingpp.api_key = api_key


'''
  设置请求签名密钥，密钥对需要你自己用 openssl 工具生成，如何生成可以参考帮助中心：https://help.pingxx.com/article/123161；
  生成密钥后，需要在代码中设置请求签名的私钥(rsa_private_key.pem)；
'''
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

# 创建charge对象
try:
    charge = pingpp.PartnerCharge.create(
        order_no='20161102000002',
        channel='alipay_pc_direct',
        amount=100,  # 支付金额, 人民币单位：分
        currency='cny',
        client_ip='127.0.0.1',
        subject='订单商品',
        body='订单内容',
        time_expire=int(time.time()) + 3600,  # 过期时间
        description='订单描述',
        extra=dict(success_url='http://127.0.0.1/success')
    )
    print(charge.to_str())  # // 输出 Ping++ 返回的charge对象 charge
except Exception as e:
    print(e.http_body)

# 查询charge对象
try:
    charge_info = pingpp.PartnerCharge.retrieve(charge.id)
    print(charge_info.to_str())
except Exception as e:
    print(e)
