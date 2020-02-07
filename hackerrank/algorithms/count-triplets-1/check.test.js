import countTriplets from './sol';

describe('countTriplets', () => {

  it('it should have a single valley', () => {
    const res = countTriplets(
      [1, 5, 5, 25, 125],
      5
    )
    expect(res).toBe(4);
  });

  it('it should have a single valley', () => {
    const res = countTriplets(
      [1, 1, 3, 3, 9],
      3
    )
    expect(res).toBe(4);
  });

  // it('only ones', () => {
  //   const res = countTriplets(
  //     [1, 1, 1, 1],
  //     1
  //   )
  //   expect(res).toBe(4);
  // });

});