var bleno = require('bleno');

var uuid = require('uuid');

var BlenoPrimaryService = bleno.PrimaryService;

var EchoName = require('./ble_name');
var EchoPdf = require('./ble_pdf');
var EchoTxt = require('./ble_txt');

fs = require('fs');

var chunkingStreams = require('chunking-streams');
var SizeChunker = chunkingStreams.SizeChunker

var name = fs.readFileSync('./parsed/name_tmp.txt', 'utf8');
var characs = [new EchoName(name)];

/*var pdf = fs.readFileSync('./parsed/pdf_tmp.txt', 'utf8');
pdf = pdf.match(/[\s\S]{1,20}/g) || [];
var i = 0;
var len = pdf.length;
while (i < len) {
	characs.push(new EchoPdf(pdf[i], uuid.v1()));
	i = i + 1;
}*/
var input = fs.createReadStream('./parsed/pdf_tmp.txt'),
    chunker = new SizeChunker({
        chunkSize: 20
    });
 
chunker.on('data', function(chunk) {
    characs.push(new EchoPdf(chunk.data, uuid.v1()));
});

input.pipe(chunker); 

var txt = fs.readFileSync('./parsed/txt_tmp.txt', 'utf8');
txt = txt.match(/[\s\S]{1,20}/g) || [];
var i = 0;
var len = txt.length;
while (i < len) {
	characs.push(new EchoTxt(txt[i], uuid.v1()));
	i = i + 1;
}

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
	        characteristics: characs
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
