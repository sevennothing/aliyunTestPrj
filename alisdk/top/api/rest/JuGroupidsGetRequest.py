'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class JuGroupidsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.page_no = None
		self.page_size = None
		self.terminal_type = None

	def getapiname(self):
		return 'taobao.ju.groupids.get'
