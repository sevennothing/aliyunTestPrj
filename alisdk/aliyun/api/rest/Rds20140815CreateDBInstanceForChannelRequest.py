'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Rds20140815CreateDBInstanceForChannelRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.AccountName = None
		self.AccountPassword = None
		self.ClientToken = None
		self.DBInstanceClass = None
		self.DBInstanceDescription = None
		self.DBInstanceNetType = None
		self.DBInstanceStorage = None
		self.Engine = None
		self.EngineVersion = None
		self.PayType = None
		self.RegionId = None
		self.SecurityIPList = None

	def getapiname(self):
		return 'rds.aliyuncs.com.CreateDBInstanceForChannel.2014-08-15'
