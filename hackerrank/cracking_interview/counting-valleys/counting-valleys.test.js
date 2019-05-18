import countingValleys from './counting-valleys';

const DONT_CARE = '';

describe('Testing Counting Valleys', () => {

  it('it should have a single valley', () => {
    expect(countingValleys(DONT_CARE, 'DDUUUUDD')).toBe(1);
  });
  
  it('it should have no valleys', () => {
    expect(countingValleys(DONT_CARE, 'UDUUDD')).toBe(0);
  });
  
  it('it should have no valleys', () => {
    expect(countingValleys(DONT_CARE, 'UDDDUDUU')).toBe(1);
  });
  
  it('it should have no valleys', () => {
    expect(countingValleys(DONT_CARE, 'DUDDUU')).toBe(2);
  });

});