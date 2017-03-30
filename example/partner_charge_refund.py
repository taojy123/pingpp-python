# -*- coding: utf-8 -*-

import pingpp
import os
import time

api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

# 设置 API Key
pingpp.api_key = api_key
pingpp.verify_ssl_certs = False


'''
  设置请求签名密钥，密钥对需要你自己用 openssl 工具生成，如何生成可以参考帮助中心：https://help.pingxx.com/article/123161；
  生成密钥后，需要在代码中设置请求签名的私钥(rsa_private_key.pem)；
'''
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

# 创建charge refund对象
try:
    params = dict(
        description='订单描述'
    )
    charge_refund = pingpp.PartnerChargeRefund.create('ch_8yfHq5jH4Oy5n5KKKSbDibbT', **params)
    print(charge_refund.to_str())  # // 输出 Ping++ 返回的charge refund对象 charge refund
except Exception as e:
    print(e.http_body)

# 查询 charge refund 对象
try:
    charge_refund_info = pingpp.PartnerChargeRefund.retrieve('ch_iTyrvHrzjjrLuXvnXDKW94aH','re_8yfHq5jH4Oy5n5KKKSbDibbT')
    print(charge_refund_info.to_str())
except Exception as e:
    print(e.http_body)
