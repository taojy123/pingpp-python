# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
  子商户渠道设置接口示例
'''
import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->企业设置->开发设置-> Secret Key
api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = api_key
# app_id 支持全局配置
pingpp.app_id = app_id


try:
    # 创建子商户渠道参数
    params = {
        "banned_msg": None,
        "channel": "alipay",
        "description": "Your description",
        "params": {
            "alipay_account": "Your alipay Account",
            "alipay_app_id": "Your Alipay App ID",
            "alipay_app_public_key": "-----BEGIN PUBLIC KEY-----\nMIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgHoOhsk4g\/6sIK5KB5V9Vvim\/tFb\nCNuJ2zVhBjp377rnWIlf0ogfW7AHW5lyPl8rwVshFdk1F1eFk4Hk9s25tp8klbJl\nkJ3\/DxZIqBc7i9j\/h75Lx\/0nKqsLophYGBGWxJGl1RgwXlbw+mXJdpXbSNxAifIv\nqNqEZwwAS7C\/rmn1AgMBAAE=\n-----END PUBLIC KEY-----",
            "alipay_app_public_key_rsa2": None,
            "alipay_mer_app_private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgHoOhsk4g\/6sIK5KB5V9Vvim\/tFbCNuJ2zVhBjp377rnWIlf0ogf\nW7AHW5lyPl8rwVshFdk1F1eFk4Hk9s25tp8klbJlkJ3\/DxZIqBc7i9j\/h75Lx\/0n\nKqsLophYGBGWxJGl1RgwXlbw+mXJdpXbSNxAifIvqNqEZwwAS7C\/rmn1AgMBAAEC\ngYBuV5mUaaoyXovA5J4Mj95DNj0hKMpOJkds70TBMNIhxqlsr5rVgnvSHCS8COLI\nCPdpGfT1gyCR9+kNQd+4xg6IeqDpL3CqIgtZi+qRGpVJgXW1x\/oZYzzpqD4Q0\/4U\nUmOp6Mo9bDPnYKSVgReWWNtCdKncWvBE4gbYadHXYva6FQJBALfW1SPWzA2i7fQu\ncG89pPkBQOMG\/pd8JyeBgEHOv2\/nBN9zqir\/zMMFd+EbI00A1goy1pu4IVvt+GFG\nq\/\/5ZE8CQQCp93SxpFjbB49s5F+Lvs0PR08IzfxY9eoCrd9xt4hXqmksUYcodBtu",
            "alipay_mer_app_private_key_rsa2": None,
            "alipay_pid": "alipay_pid",
            "alipay_refund_nopwd": False,
            "alipay_security_key": "alipay_security_key",
            "alipay_sign_type": "rsa",
            "alipay_version": 1,
            "fee_rate": 80
        }
    }
    channel = pingpp.Channel.create(app=pingpp.app_id, sub_app_id='app_1Gqj58ynP0mHeX1q', **params)
    print('create sub_app channel:', channel)

    # 更新子商户渠道参数
    updateParams = {
        'description': 'Your Channel description',
        'params': {
            "alipay_account": "Your alipay Account",
            "alipay_app_id": "Your Alipay App ID",
            "alipay_app_public_key": "-----BEGIN PUBLIC KEY-----\nMIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgHoOhsk4g\/6sIK5KB5V9Vvim\/tFb\nCNuJ2zVhBjp377rnWIlf0ogfW7AHW5lyPl8rwVshFdk1F1eFk4Hk9s25tp8klbJl\nkJ3\/DxZIqBc7i9j\/h75Lx\/0nKqsLophYGBGWxJGl1RgwXlbw+mXJdpXbSNxAifIv\nqNqEZwwAS7C\/rmn1AgMBAAE=\n-----END PUBLIC KEY-----",
            "alipay_app_public_key_rsa2": None,
            "alipay_mer_app_private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgHoOhsk4g\/6sIK5KB5V9Vvim\/tFbCNuJ2zVhBjp377rnWIlf0ogf\nW7AHW5lyPl8rwVshFdk1F1eFk4Hk9s25tp8klbJlkJ3\/DxZIqBc7i9j\/h75Lx\/0n\nKqsLophYGBGWxJGl1RgwXlbw+mXJdpXbSNxAifIvqNqEZwwAS7C\/rmn1AgMBAAEC\ngYBuV5mUaaoyXovA5J4Mj95DNj0hKMpOJkds70TBMNIhxqlsr5rVgnvSHCS8COLI\nCPdpGfT1gyCR9+kNQd+4xg6IeqDpL3CqIgtZi+qRGpVJgXW1x\/oZYzzpqD4Q0\/4U\nUmOp6Mo9bDPnYKSVgReWWNtCdKncWvBE4gbYadHXYva6FQJBALfW1SPWzA2i7fQu\ncG89pPkBQOMG\/pd8JyeBgEHOv2\/nBN9zqir\/zMMFd+EbI00A1goy1pu4IVvt+GFG\nq\/\/5ZE8CQQCp93SxpFjbB49s5F+Lvs0PR08IzfxY9eoCrd9xt4hXqmksUYcodBtu",
            "alipay_mer_app_private_key_rsa2": None,
            "alipay_pid": "alipay_pid",
            "alipay_refund_nopwd": False,
            "alipay_security_key": "alipay_security_key",
            "alipay_sign_type": "rsa",
            "alipay_version": 1,
            "fee_rate": 80
        },
        'banned': False,
    }
    channel = pingpp.Channel.update(app=pingpp.app_id, sub_app_id='app_1Gqj58ynP0mHeX1q', channel='alipay',
                                    **updateParams)
    print('update sub_app channel :', channel)

    # 查询子商户渠道参数
    channel_list = pingpp.Channel.retrieve(app=pingpp.app_id, sub_app_id='app_1Gqj58ynP0mHeX1q', channel='alipay')
    print('retrieve sub_app channel list:', channel_list)

    # 删除子商户渠道参数
    channel_del = pingpp.Channel.delete(app=pingpp.app_id, sub_app_id='app_1Gqj58ynP0mHeX1q', channel='alipay')
    print('delete sub_app channel:', channel_del)

except Exception as e:
    print(e.http_body)
