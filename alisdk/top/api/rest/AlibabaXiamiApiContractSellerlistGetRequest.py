'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class AlibabaXiamiApiContractSellerlistGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.limit = None
		self.page = None
		self.time_end = None
		self.time_start = None

	def getapiname(self):
		return 'alibaba.xiami.api.contract.sellerlist.get'
