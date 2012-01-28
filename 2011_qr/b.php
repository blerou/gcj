<?php

$inputFile = $_SERVER['argv'][1];
$outputFile = $inputFile.'.out';

$fin = fopen($inputFile, 'r');
$fout = fopen($outputFile, 'w+');

$cases = fgets($fin);
$case = 0;
while (!feof($fin)) {
	$case++; $in = fgets($fin);
	if ($case > $cases) break;
	list($combs, $opps, $inv) = parse($in);
	$out = solve($combs, $opps, $inv);
	$res = sprintf("Case #%d: %s\n", $case, format($out));
	fputs($fout, $res);
	echo "$res";
}


function parse($in) {
	$in = explode(' ', $in);
	$numComb = (int)$in[0];
	$combs = array_slice($in, 1, $numComb);
	$in = array_slice($in, ($numComb+1));
	$numOpp = (int)$in[0];
	$opps = array_slice($in, 1, $numOpp);
	$in = array_slice($in, ($numOpp+1));
	$numInv = (int)$in[0];
	$inv = array();
	for ($i = 0; $i < $numInv; ++$i)
		$inv[] = $in[1]{$i};
		
	return array($combs, $opps, $inv);
}

function solve($comb, $opp, $inv) {
	$out = array();
	foreach ($inv as $m) {
		array_unshift($out, $m);
		$out = apply_comb($out, $comb);
		$out = apply_opp($out, $opp);
	}
	return $out;
}

function apply_comb($out, $combs) {
	foreach ($combs as $comb) {
		$new  = substr($comb, 2, 1);
		$comb = substr($comb, 0, 2);
		$a = $comb == $out[0].$out[1];
		$b = $comb == $out[1].$out[0];
		if ($a || $b) {
			array_shift($out);
			array_shift($out);
			array_unshift($out, $new);
		}
	}
	return $out;
}

function apply_opp($out, $opps) {
	foreach ($opps as $opp) {
		$a = $opp{0}; $b = $opp{1};
		if (in_array($a, $out) && in_array($b, $out)) {
			$out = array();
		}
	}
	return $out;
}

function format($in) {
	$out = ']';
	foreach ($in as $i) {
		$out = ', '.$i.$out;
	}
	return '['.ltrim($out, ' ,');
}
