'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class DdReservedUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.mark = None
		self.option = None
		self.seller_memo = None
		self.store_id = None

	def getapiname(self):
		return 'taobao.dd.reserved.update'
