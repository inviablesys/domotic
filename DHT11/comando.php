 <?php

  $th=shell_exec ('/home/pi/DHT11/dht11_adafruit.sh 11 4');

  echo $th;

 $temperatura = substr ($th,5,4);
 echo $temperatura;
 echo '
<br>';
 $humedad = substr ($th,21,4);
 echo $humedad;
 echo '</br>';

  ?>
