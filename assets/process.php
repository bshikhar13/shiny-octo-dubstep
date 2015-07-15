<?php

$limit = $_POST['limit'];

$smsussd = $_POST['smsussd'];
$io = $_POST['io'];
$hg = $_POST['hg'];
$gprs = $_POST['gprs'];
$imeiimsi = $_POST['imeiimsi'];

if (!isset($smsussd)){
	$smsussd = 0;
}

if (!isset($io)){
	$io = 0;
}

if (!isset($hg)){
	$hg = 0;
}

if (!isset($gprs)){
	$gprs = 0;
}

if (!isset($imeiimsi)){
	$imeiimsi = 0;
}

//echo $smsussd.$io.$hg.$gprs.$imeiimsi;

$tmp =  exec("python master.py $limit $smsussd $io $hg $gprs $imeiimsi",$output);
//var_dump($output) ;

$a = $output[0];
$b = $output[1];
$c = $output[2];
$d = $output[3];
$e = $output[4];
$f = $output[5];

$efficiency = (1-($f/$a))*100; 





?>

<!DOCTYPE html>
<html>
<head>
	<title>mario</title>



</head>
<body>

<script type='text/javascript' src="raphel.js"></script>
<script type='text/javascript' src="http://underscorejs.org/underscore-min.js"></script>
<script type='text/javascript' src="sequence-diagram-min.js"></script>

 <pre id="uml" style="display: none;">

Master Data->SMS_USSD Filter:<?php echo $a; ?> 
SMS_USSD Filter->Incoming/Outgoing Filter:<?php echo $b; ?> 
Incoming/Outgoing Filter->Home_Group Filter:<?php echo $c; ?> 
Home_Group Filter->GPRS_FILTER:<?php echo $d; ?> 
GPRS_FILTER->IMEI vs IMSI Filter:<?php echo $e; ?> 
IMEI vs IMSI Filter->Filtered:<?php echo $f; ?> 
Note right of Filtered: Suspicious IMSIs=<?php echo $f;?> 
Note left of Master Data: Unique IMSIs=<?php echo $a; ?> 
Note right of Filtered: Efficiency=<?php echo $efficiency ; ?> 

</pre>
Total Unique Sims : <?php echo $a; ?>

<svg width="100" height="100">
	<div id="diagram">
		
	</div>
</svg>

<script>



  var diagram = Diagram.parse(document.getElementById('uml').innerText);
  diagram.drawSVG("diagram", {theme: 'simple'});

</script>

</body>

</html>