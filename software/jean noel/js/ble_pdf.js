var util = require('util');

var bleno = require('bleno');

var buff = "";

var BlenoCharacteristic = bleno.Characteristic;

var EchoCharacteristic = function(data, i) {
	EchoCharacteristic.super_.call(this, {
		uuid: i,
	    properties: ['read'],
		value: new Buffer(data)
	});

	this._value = buff;
	this._updateValueCallback = null;
};

util.inherits(EchoCharacteristic, BlenoCharacteristic);

EchoCharacteristic.prototype.onReadRequest = function(offset, callback) {
	callback(this.RESULT_SUCCESS, buff);
};

module.exports = EchoCharacteristic;
