'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class FenxiaoOrderConfirmPaidRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.confirm_remark = None
		self.purchase_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.order.confirm.paid'
