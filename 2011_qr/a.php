<?php

$fin = fopen($_SERVER['argv'][1], 'r');
$fout = fopen($$_SERVER['argv'][1].'.out', 'w+');

$cases = fgets($fin);
$case = 0;
while (!feof($fin)) {
	$case++; $in = fgets($fin);
	if ($case > $cases) break;
	$in = preg_replace('~^\d+ ~', '', $in);
	$out = solve(parse($in));
	$res = sprintf("Case #%d: %d\n", $case, $out);
	fputs($fout, $res);
	echo "$res";
}


function parse($in) {
	$in = preg_split('~ (?=[OB])~', $in);
	$out = array('B' => array(), 'O' => array());
	$s = array('B' => 1, 'O' => 1);
	foreach ($in as &$i) {
		$i = explode(' ', $i);
		$ns = (int)$i[1];
		$i[1] = abs($s[$i[0]] - $ns) + 1;
		$s[$i[0]] = $ns;
	}
	return $in;
}

function solve($in) {
	$currR = 'B'; $currT = 0; $sum = 0;
	foreach ($in as $i) {
		$r = $i[0];
		$t = $i[1];
		if ($r == $currR) {
			$currT += $t;
		} else {
			$sum += $currT;
			$currR = $r;
			if ($t <= $currT) {
				$currT = 1;
			} else {
				$currT = $t - $currT;
			}
		}
	}
	$sum += $currT;
	
	return $sum;
}
