'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Ess20140828CreateScalingRuleRequest(RestApi):
	def __init__(self,domain='ess.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.AdjustmentType = None
		self.AdjustmentValue = None
		self.Cooldown = None
		self.ScalingGroupId = None
		self.ScalingRuleName = None

	def getapiname(self):
		return 'ess.aliyuncs.com.CreateScalingRule.2014-08-28'
