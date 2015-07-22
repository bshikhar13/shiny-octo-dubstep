<?php



?>
<!DOCTYPE html>
<html>
<head>
	<title>Mario</title>
</head>
<body>
	<form action="assets/process.php" method="POST">
	<label>Number of records to process : </label>
	<input type="text" name="limit">
	<br><br><br>
	<input type="checkbox" name="smsussd" value="1"> SMS-USSD Filter
	<br>
	<input type="checkbox" name="io" value="1">Incoming/Outgoing Filter
	<br>
	<input type="checkbox" name="hg" value="1">Home Group Filter
	<br>
	<input type="checkbox" name="gprs" value="1">GPRS Filter
	<br>
	<input type="checkbox" name="imeiimsi" value="1">IMEI vs IMSI Filter
	<br>
	<br>
	<input type="submit" value="Submit">
	</form>
</body>
</html>
