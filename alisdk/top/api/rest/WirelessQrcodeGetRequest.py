'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class WirelessQrcodeGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.height = None
		self.nick = None
		self.urlparam = None
		self.width = None

	def getapiname(self):
		return 'taobao.wireless.qrcode.get'
