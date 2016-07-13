var bleno = require('bleno');

var BlenoPrimaryService = bleno.PrimaryService;

var EchoName = require('./ble_name');
var EchoPdf = require('./ble_pdf');
var EchoTxt = require('./ble_txt');

process.env['BLENO_DEVICE_NAME'] = 'EcoTicketBeta';

bleno.on('stateChange', function(state) {
	console.log('on -> stateChange: ' + state);

	if (state === 'poweredOn') {
		bleno.startAdvertising('EcoTicket', ['6d95c7ae-468f-11e6-beb8-9e71128cae77']);
	} else {
		bleno.stopAdvertising();
	}
});

bleno.on('advertisingStart', function(error) {
	console.log('on -> advertisingStart: ' + (error ? 'error ' + error : 'success'));

    if (!error) {
	    bleno.setServices([
	      new BlenoPrimaryService({
	        uuid: '6d95c7ae-468f-11e6-beb8-9e71128cae77',
	        characteristics: [
				new EchoName(),
				new EchoPdf(),
				new EchoTxt()
	        ]
	      })
        ]);
    }
});

bleno.on('accept', function(clientAddress) {
	console.log('on -> accept: ' + clientAddress);
});

bleno.on('disconnect', function(clientAddress) {
	console.log('on -> disconnect: ' + clientAddress);
	process.exit();
});
