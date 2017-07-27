# Ping++ Python SDK for Partners

## 安装
1. 先安装依赖
    - requests
    - pycrypto

2. 执行 `python setup.py install` 进行安装

## 使用
1. 导入

    ``` python
    import pingpp
    ```
2. 设置 API Key

    ``` python
    pingpp.api_key = 'Ping++ 分配的 Key' # partner_xxxxxxxxxxxxx
    ```
3. 设置私钥用于签名

    ``` python
    pingpp.private_key_path = '你的 PEM 格式私钥文件路径'
    ```
4. 调用接口创建 charge

    ``` python
    pingpp.PartnerCharge.create(
        order_no='20161102000002',
        channel='alipay_wap',
        amount=100,  # 支付金额, 人民币单位：分
        currency='cny',
        client_ip='127.0.0.1',
        subject='订单商品',
        body='订单内容',
        time_expire=int(time.time()) + 3600,  # 过期时间
        description='订单描述',
        extra=dict(success_url='http://127.0.0.1/success')
    )
    ```
    - 示例见 `example/partner_charge.py`
    - `extra` 字段的说明请查看 [API 文档](https://www.pingxx.com/api#支付渠道-extra-参数说明)
