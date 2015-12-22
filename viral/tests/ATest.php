<?php

require (__DIR__.'/../MinInBothArr.php');

class ATest extends PHPUnit_Framework_TestCase {

	public function testGere($value='')
	{
		$a = [1,4,4,3,2];
		$b = [12312312,3333,55,1212,13123];
		$res = solution($a, $b);
		$this->assertEquals(-1, $res);
	}



	
}