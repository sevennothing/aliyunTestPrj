'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class SpContentUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.schema_name = None
		self.site_key = None
		self.tags = None
		self.value = None

	def getapiname(self):
		return 'taobao.sp.content.update'
