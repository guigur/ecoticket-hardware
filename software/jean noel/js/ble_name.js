var util = require('util');

var bleno = require('bleno');

var buff = "";

var BlenoCharacteristic = bleno.Characteristic;

var EchoCharacteristic = function(data) {
	EchoCharacteristic.super_.call(this, {
		uuid: '186a18ca-468f-11e6-beb8-9e71128cae77',
	    properties: ['read'],
		value: new Buffer(data)
	});

	this._value = new Buffer(0);
	this._updateValueCallback = null;
};

util.inherits(EchoCharacteristic, BlenoCharacteristic);

EchoCharacteristic.prototype.onReadRequest = function(offset, callback) {
	callback(this.RESULT_SUCCESS, buff);
};

module.exports = EchoCharacteristic;
