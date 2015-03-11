/**
 * Created by Administrator on 2015/01/27.
 */
var url = require('url');
var crypto = require('crypto');
var http = require('http');
var querystring = require('querystring');
var fs = require('fs');

var aliyunRDS = require('./aliyunRDS');

var keyID = 'ICfKMQhyhyotR07W';
var secretKey = 'cObYq5CD1ppf1zzzhw0iyEaszEMaG9';
var instanceId = 'rdsmnbjvrqvqyb3';
var aliyun = new aliyunRDS(keyID,secretKey);


aliyun.setDBInstanceId(instanceId);
aliyun.getDescribeAccounts(function(err,res){
console.log('========1: describeAccounts============');
		var info = JSON.stringify(res);
		console.log(info);
});
aliyun.getDescribeResourceUsage(function(err,res){
console.log('========2: describe Usage============');
		console.log(res);
});
aliyun.getDescribeDBInstanceAttribute(function(err,res){
console.log('========3: describe attrubute============');
		var info = JSON.stringify(res);
		console.log(info);
		
});
aliyun.getDescribeBackupPolicy(function(err,res){
console.log('========4: describe backup policy============');
		var info = JSON.stringify(res);
		console.log(info);
		
});

var key = 'MySQL_NetworkTraffic';
//var StartTime = new Date().toISOString();
//var EndTime = new Date().toISOString();
//var StartTime = '2014-01-28T07:00:00Z';
//var EndTime = '2014-01-28T08:00:00Z';
var StartTime = '2014-01-11T15:00Z';
var EndTime = '2014-01-20T15:00Z';
aliyun.getDescribeDBInstancePerformance(key, StartTime, EndTime, function(err,res){
console.log('========5: describe performance============');
		if(err) {
			console.log(err);
		}{

		var info = JSON.stringify(res);
			console.log(info);
		
		}
});

aliyun.getDescribeBackups(StartTime, EndTime, function(err,res){
console.log('========6: describe Backups============');
		if(err) {
			console.log(err);
		}{
		var info = JSON.stringify(res);
			console.log(info);
		
		}
});

