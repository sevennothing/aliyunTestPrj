'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class SpContentPublishRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.schema_name = None
		self.site_key = None
		self.tags = None
		self.value = None

	def getapiname(self):
		return 'taobao.sp.content.publish'
