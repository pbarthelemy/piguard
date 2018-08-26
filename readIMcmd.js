const util = require('util');
var http = require('http');
const { parse } = require('querystring');

http.createServer(function (request, response) {

   response.writeHead(200, {'Content-Type': 'text/plain'});
   collectRequestData(request, result => {
            console.log(result);
		var cmd = result.text
console.log('command is' + cmd );
   response.end('{"text": " ${result.text}"}');
            //res.end(`Parsed data belonging to ${result.fname}`);
	});
 
}).listen(8080);


console.log('Server started');
 
function collectRequestData(request, callback) {
        let body = '';
        request.on('data', chunk => {
            body += chunk.toString();
        });
        request.on('end', () => {
            callback(parse(body));
        });
 }
