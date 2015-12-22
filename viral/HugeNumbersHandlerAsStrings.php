<?php 

/**
* 
*/
class HugeNumbersHandlerAsStrings
{
	
	function __construct()
	{
		
	}

	public function add2Numbers($numStr1, $numStr2)
	{
		$loopLength = (strlen($numStr1)>strlen($numStr2))? strlen($numStr1) : strlen($numStr2);
		$remainder = 0;
		$resultStr = str_repeat(' ', $loopLength);

		for ($i=$loopLength-1 ; $i>=0 ; $i--) {
			$numStr1Digit = (isset($numStr1[$i]))? intval($numStr1[$i]) : 0;
			$numStr2Digit = (isset($numStr2[$i]))? intval($numStr2[$i]) : 0;

			$tempRes = $numStr1Digit + $numStr2Digit + $remainder;
			
			if ($tempRes > 9) {
				$remainder = 1;
				$tempRes -= 10;
			} else {
				$remainder = 0;
			}

			$resultStr[$i] = $tempRes;
		}

		if ($remainder === 1) {
			$resultStr = '1'.$resultStr;
		}

		return $resultStr;
	}

	public function multiply2Numbers($numStr1, $numStr2)
	{
		$intVal = intVal($numStr2);
		$sum = '';
		for ($i=0 ; $i<$intVal ; $i++) {
			$sum = $this->add2Numbers($numStr1, $sum);
		}

		return $sum;
	}
}

$ob = new HugeNumbersHandlerAsStrings();
$rs = $ob->multiply2Numbers('4', '4');
var_dump($rs);