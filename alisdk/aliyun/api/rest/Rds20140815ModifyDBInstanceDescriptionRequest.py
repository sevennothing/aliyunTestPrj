'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Rds20140815ModifyDBInstanceDescriptionRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.DBInstanceDescription = None
		self.DBInstanceId = None

	def getapiname(self):
		return 'rds.aliyuncs.com.ModifyDBInstanceDescription.2014-08-15'
