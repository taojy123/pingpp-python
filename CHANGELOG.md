# 2.2.0
- 增加:
    - 子商户接口
    - 子商户渠道参数配置接口
    - 结算账号接口
    - 分润接口
    - 分润结算接口
    - 分润结算明细接口
- 修改
    - 企业清算明细新增user_fee_total user_fee_recharge user_fee_balance_transfer
    - 企业交易明细接口去除 fee 和 user_fee 字段,新增method、order_no、transaction_no source_url字段,查询列表新增 method order_no transaction_no asset_account 参数
    - 订单创建uid改为选填 order创建新增receipt_app、service_app、royalty_users字段.返回对象新增available_methods receipt_app service_app
    - user对象新增type,related_app,settle_accounts字段.查询user对象列表新增type查询参数.

# 2.1.0
- 增加:
    - 企业付款SDK更新接口  
    - 请求认证接口接口  
    - 报关接口接口  
    - 批量退款接口  
    - 订单创建更新查询删除支付接口  
    - 用户充值接口接口  
    - 企业清算账户交易明细接口  
    - 用户接口  
    - 余额转账接口  
    - 优惠券及优惠券模板接口  
    - 企业清算账户额度统计,批量提现确认创建查询接口  
- 修改
    - 请求签名方法更新

# 2.0.12
- 增加：  
    - customs 报关接口

# 2.0.11
- 修复：  
    - python2 报错信息无法解析的问题

# 2.0.10
- 增加：  
    - 添加设置私钥内容方式
- 修复：  
    - python3 不兼容问题

# 2.0.9
- 修复：  
    - python3 不兼容问题

# 2.0.8
- 更改：  
    - 增加请求签名

# 2.0.7
- 更改：  
    - wxpub auth 获取 code 时的参数固定顺序

# 2.0.6
- 更改：  
    - wxpub auth 获取 code 时的 bug

# 2.0.5
- 增加：  
    - 增加微信企业付款

# 2.0.4
- 更改：  
    - 更改在 python3.4 中 pip install 出错的问题

# 2.0.3
- 增加：  
    - 新增 event 查询，新增京东手机网页支付

# 2.0.1
- 增加：  
    - 新增微信红包

# 2.0.0
- 更改：  
    - 添加新渠道：百付宝、百付宝WAP、微信公众号支付
