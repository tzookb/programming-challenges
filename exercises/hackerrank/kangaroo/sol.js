function doTheyMeet(x1, v1, x2, v2) {
	var res = (x1-x2)/(v2-v1);
	if ( !Number.isInteger(res))
		return false;
	if (res < 0)
		return false;
	return true;
}