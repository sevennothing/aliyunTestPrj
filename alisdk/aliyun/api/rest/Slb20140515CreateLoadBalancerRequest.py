'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Slb20140515CreateLoadBalancerRequest(RestApi):
	def __init__(self,domain='slb.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.AddressType = None
		self.Bandwidth = None
		self.ClientToken = None
		self.InternetChargeType = None
		self.LoadBalancerName = None
		self.RegionId = None

	def getapiname(self):
		return 'slb.aliyuncs.com.CreateLoadBalancer.2014-05-15'
