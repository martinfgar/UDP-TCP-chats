<?php
error_reporting(E_ALL);

echo "<h2>TCP/IP Connection</h2>\n";

/* Get the port for the WWW service. */
$service_port = 10000;

/* Get the IP address for the target host. */
$address = '10.10.17.191';

/* Create a TCP/IP socket. */
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n";
} else {
    echo "OK.\n";
}

echo "Attempting to connect to '$address' on port '$service_port'...";
$result = socket_connect($socket, $address, $service_port);
if ($result === false) {
    echo "socket_connect() failed.\nReason: ($result) " . socket_strerror(socket_last_error($socket)) . "\n";
} else {
    echo "OK.\n";
}

if ($out = socket_read($socket, 2048)) {
    echo $out;
}
while (true){
    $in = readline("Introduce mensaje: ");
    socket_write($socket, $in, strlen($in));
    if ($in == 'quit'){
        break;
    }
    echo "Reading response:\n\n";
    if ($out = socket_read($socket, 2048)) {
        echo $out;
    }
   
}


echo "Closing socket...";
socket_close($socket);
echo "OK.\n\n";
?>