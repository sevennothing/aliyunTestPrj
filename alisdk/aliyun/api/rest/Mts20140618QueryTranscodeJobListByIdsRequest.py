'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Mts20140618QueryTranscodeJobListByIdsRequest(RestApi):
	def __init__(self,domain='mts.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.MediaIds = None

	def getapiname(self):
		return 'mts.aliyuncs.com.QueryTranscodeJobListByIds.2014-06-18'
