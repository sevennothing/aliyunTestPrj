'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Ess20140828DeleteScalingRuleRequest(RestApi):
	def __init__(self,domain='ess.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.ScalingRuleId = None

	def getapiname(self):
		return 'ess.aliyuncs.com.DeleteScalingRule.2014-08-28'
