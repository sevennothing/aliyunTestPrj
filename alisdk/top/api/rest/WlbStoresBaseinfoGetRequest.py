'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class WlbStoresBaseinfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.type = None

	def getapiname(self):
		return 'taobao.wlb.stores.baseinfo.get'
