# -*- coding: utf-8 -*-
import pingpp
import os

'''
    企业清算账户接口
'''
# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

# 获取指定清算信息
try:
    # 获取清算信息明细 示例
    retr_at = pingpp.AssetTransaction.retrieve(app=app_id, id="310016111615002600000301")
    print("retrieve asset transaction", retr_at)

    # 获取列表
    at_list = pingpp.AssetTransaction.list(app=app_id)
    print("retrieve asset transaction list", at_list)

except Exception as e:
    print(e.http_body)
