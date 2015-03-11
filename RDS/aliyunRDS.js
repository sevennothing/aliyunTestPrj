/**
 * Created by Administrator on 2015/01/27.
 */
var url = require('url');
var crypto = require('crypto');
var http = require('http');
var querystring = require('querystring');
var fs = require('fs');
//var errMessage = require('../../module/error_message');

var aliyunAction = {
	DescribeResourceUsage: 'DescribeResourceUsage',
 DescribeDBInstancePerformance:'DescribeDBInstancePerformance',
DescribeAccounts:'DescribeAccounts',
DescribeBackups :'DescribeBackups',
DescribeBackupPolicy : 'DescribeBackupPolicy',
DescribeDBInstanceAttribute : 'DescribeDBInstanceAttribute'


};


var calAuthorization = function (options,sigStr, secret,callback) {
	var dictSigStr = {};
	var keys = Object.keys(sigStr).sort();

	var uriNew = {};
 for(var i=0,n=keys.length,key; i< n; ++i){
 	key=keys[i];
	dictSigStr[key] = sigStr[key];
 }

 for(var i=0,n=keys.length,key; i< n; ++i){
 	key=keys[i];
	if(key === 'StartTime' || key === 'EndTime') continue;
	uriNew[key] = sigStr[key];
 }

 uriNew = querystring.stringify(uriNew); 
 uriNew += '&' + 'StartTime=' + sigStr.StartTime + '&' + 'EndTime=' + sigStr.EndTime; 
 //console.log(sigStr);
 //console.log(dictSigStr);

	var uri = querystring.stringify(dictSigStr); 

  var crypStr = options.method + '&' + encodeURIComponent(options.path) + '&' + encodeURIComponent(uri);

	//console.log(crypStr);
	var useSecret = secret + '&';
  var signature = crypto.createHmac('sha1', useSecret).update(crypStr).digest().toString('base64');
  //console.log(signature);
	//signature = signature.replace('=','%3d');
	signature = encodeURIComponent(signature);	
	callback(null,options.path + '?' + uri +'&'+'Signature=' + signature);
};

function aliyunRDS(keyID,secretkey){
	this.name = 'aliyun RDS';
	this.keyID = keyID;
	this.secretkey = secretkey;
	this.aliyunHost = 'rds.aliyuncs.com';

}

aliyunRDS.prototype.Init = function(keyID,secretkey){
	this.keyID = keyID;
	this.secretkey = secretkey;
}

aliyunRDS.prototype.setDBInstanceId = function(instanceId){
	this.DBInstanceId = instanceId;

};

aliyunRDS.prototype.core = function(code, specParam,callback){
	var action = '';
	var method = 'GET';
	var path = '/';
	var format = 'Format=JSON';
	var sigStr ={};
  var commSigStr= {
		Action:'',
		Format:"JSON",
		AccesskeyId:this.keyID,
    SignatureMethod:'HMAC-SHA1',
		SignatureVersion: "1.0",
		SignatureNonce :Math.ceil(Math.random()*100000000000000),
		Timestamp:new Date().toISOString(),
		Version:'2014-08-15'
	};
	var keys =  Object.keys(commSigStr);
	for(var i=0; i< keys.length; i++){
		var key = keys[i];
		sigStr[key] = commSigStr[key];
	}

	action = aliyunAction[code];
	method = 'GET';
	path = '/';
	switch(code){
		case 'DescribeDBInstanceAttribute':
			break;
		case 'DescribeAccounts':
			break;
		case 'DescribeBackupPolicy':
			break;
	  case 'DescribeBackups':
			sigStr.StartTime = specParam.StartTime;
			sigStr.EndTime = specParam.EndTime;
			break;
		case 'DescribeResourceUsage':
	    action = aliyunAction[code];
	    method = 'GET';
	    path = '/';
			break;
		case 'DescribeDBInstancePerformance':
			sigStr.Key = specParam.Key;
			sigStr.StartTime = specParam.StartTime;
			sigStr.EndTime = specParam.EndTime;
			break;
	
	}
	sigStr.Action = action;
	sigStr.DBInstanceId = this.DBInstanceId;

  var options = {
    host: this.aliyunHost,
    path: path,
    method: method,
    headers: {
      'Cache-Control': 'no-cache',
      'Content-Encoding': 'utf-8',
      'Date': new Date().toUTCString()
    }
  };

	calAuthorization(options,sigStr, this.secretkey, function(err, uri){
			//options.path = encodeURIComponent(uri);	
			options.path = uri;	
			//console.log(options.path)
			var req = http.request(options, function (res) {
				var result = '';
				res.setEncoding('utf8');
				res.on('data', function (chunk) {
					//console.log('BODY: ' + chunk);
					result += chunk;
					});
				res.on('end',function(){
					//console.log(result)
					var resJson = JSON.parse(result);
					callback(null,resJson);				
					});

				});
			req.on('error', function (e) {
				console.log(e.message);
				callback(e,null);
				});
			req.end();


	});
}

aliyunRDS.prototype.getDescribeDBInstanceAttribute = function(callback){
	this.core('DescribeDBInstanceAttribute','',function(err,res){
		//console.log(res);
		callback(null,res);
	});
}

aliyunRDS.prototype.getDescribeAccounts = function(callback){
	this.core('DescribeAccounts','',function(err,res){
		//console.log(res);
		callback(null,res);
	});
}

aliyunRDS.prototype.getDescribeBackupPolicy = function(callback){
	this.core('DescribeBackupPolicy','',function(err,res){
		//console.log(res);
		callback(null,res);
	});
}

aliyunRDS.prototype.getDescribeBackups = function(StartTime,EndTime,callback){

	var specParam = {};
	specParam.StartTime = StartTime;
	specParam.EndTime = EndTime;
	this.core('DescribeBackups',specParam,function(err,res){
		//console.log(res);
		callback(null,res);
	});
}
aliyunRDS.prototype.getDescribeResourceUsage = function(callback){
	this.core('DescribeResourceUsage','',function(err,res){
		//console.log(res);
		callback(null,res);
	});
}

aliyunRDS.prototype.getDescribeDBInstancePerformance = function(Key,StartTime,EndTime,callback){
	//check param
	if(arguments.length !== 4){
		var msg = 'describeDBInstancePerformance Interface erro: parma erro';
		//console.log(msg);
		throw new Error(msg);
		//return callback(msg,null);
	}
	var specParam = {};
	specParam.Key = Key;
	specParam.StartTime = StartTime;
	specParam.EndTime = EndTime;
	this.core('DescribeDBInstancePerformance',specParam,function(err,res){
		//console.log(res);
		callback(null,res);
									
	});
}

module.exports = exports = aliyunRDS;
