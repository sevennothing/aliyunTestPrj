'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class FenxiaoProductQuantityUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.product_id = None
		self.properties = None
		self.quantity = None
		self.type = None

	def getapiname(self):
		return 'taobao.fenxiao.product.quantity.update'
