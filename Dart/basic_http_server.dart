// This is basic http server, which will listen on predefined port (8080 in this case) and will send text response 'Basic http answer'.
// 
// $ dart2native basic_http_server.dart
// 
import 'dart:io';

Future main() async {
  
  var server = await HttpServer.bind(
    InternetAddress.loopbackIPv4,
    8080,
  );
  
  print('Listening on localhost:${server.port}');

  
  await for (HttpRequest request in server) {
    request.response.write('Basic http answer');
    await request.response.close();
  }
  
}
