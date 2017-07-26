# -*- coding: utf-8 -*-

import pingpp
import os

'''
    优惠券模板接口
'''
# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')


# app_id 支持全局配置
pingpp.app_id = app_id
try:
    params = {
        "name": "25OFF",
        "type": 1,
        "percent_off": 25,
        "amount_available": 10000,
        "max_circulation": 1000,
        "amount_off": 10,
        "metadata": {
        },
    }
    # 创建优惠券模板
    new_coupon = pingpp.CouponTemplate.create(app=app_id, **params)
    print(new_coupon)

    # 获取优惠券模板列表
    coupon_templ_list = pingpp.CouponTemplate.list()
    print(coupon_templ_list)

    # 查询优惠券模板
    retr_coupon_templ = pingpp.CouponTemplate.retrieve("100116111111111100011101")
    print(retr_coupon_templ)

    # 更新优惠券模板
    update_coupon_tpl_params = {
        'metadata': {
            'key': 'value'
        }
    }
    update_coupon_templ = pingpp.CouponTemplate.update("100116111111111100011101", **update_coupon_tpl_params)
    print(update_coupon_templ)

    # 删除优惠券模板
    delete_coupon_templ = pingpp.CouponTemplate.delete("100116111111111100011102")
    print delete_coupon_templ

    # 批量创建优惠券
    create_params = {
        "users": [
            "test_user_001",
            "test_user_002"
        ]
    }
    batch_create_coupons = pingpp.CouponTemplate.create_coupons(app=app_id, coupon_tmpl="100116111111111100011101", **create_params)
    print(batch_create_coupons)

    # 查询模板下的优惠券
    tmpl_coupon_list = pingpp.CouponTemplate.retrieve_coupons(coupon_tmpl="100116111111111100011101")
    print(tmpl_coupon_list)
except Exception as e:
    print(e.http_body)
