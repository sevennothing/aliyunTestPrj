'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class UmpMbbGetbycodeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.code = None

	def getapiname(self):
		return 'taobao.ump.mbb.getbycode'
