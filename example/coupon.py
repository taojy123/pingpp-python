# -*- coding: utf-8 -*-

import pingpp
import os

'''
优惠券接口
'''
# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_live_vjfr90jj1q985KuPO84iP8KO'
app_id = 'app_LibTW1n1SOq9Pin1'
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

# app_id 支持全局配置
pingpp.app_id = app_id


params = {
    "coupon_template": "300116082415452100000700",
    "metadata": {
        "key": "value"
    }
}

try:
    # 创建优惠券
    new_coupon = pingpp.Coupon.create(user="user_test_001", **params)
    print(new_coupon)

    # 查询
    retr_coupon = pingpp.Coupon.retrieve("coupon_id_001", user="user_test_001")
    print(retr_coupon)

    # 获取列表
    coupon_list = pingpp.Coupon.list(user="user_test_001")
    print(coupon_list)

    # 删除优惠券
    delete_coupon = pingpp.Coupon.delete("coupon_id_001", user="user_test_001")
    print(delete_coupon)

    # 更新优惠券
    update_params = {
        "metadata": {
            "key": "value"
        }
    }
    update_coupon = pingpp.Coupon.update("coupon_id_001", user="user_test_001", **update_params)
    print(update_coupon)
except Exception as e:
    print(e.http_body)
