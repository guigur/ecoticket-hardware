var util = require('util');

var bleno = require('bleno');

var buff = "";

fs = require('fs');
fs.readFile('./parsed/pdf_tmp.txt', 'utf8', function (err,data) {
	if (err) {
		return console.log(err);
	}
	buff = Buffer(data);
});

var BlenoCharacteristic = bleno.Characteristic;

var EchoCharacteristic = function() {
	EchoCharacteristic.super_.call(this, {
		uuid: '186a1c44-468f-11e6-beb8-9e71128cae77',
	    properties: ['read'],
		value: buff
	});

	this._value = buff;
	this._updateValueCallback = null;
};

util.inherits(EchoCharacteristic, BlenoCharacteristic);

EchoCharacteristic.prototype.onReadRequest = function(offset, callback) {
	callback(this.RESULT_SUCCESS, buff);
};

module.exports = EchoCharacteristic;
