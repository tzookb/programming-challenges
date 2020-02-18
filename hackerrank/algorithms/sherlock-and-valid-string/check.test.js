import isValid from './sol';

describe('sherlock and valid string', () => {
  it('aabb', () => {
    expect(isValid('aabb')).toBe('YES')
  });
  it('aabbc', () => {
    expect(isValid('aabbc')).toBe('YES')
  });
  it('aabbcd', () => {
    expect(isValid('aabbcd')).toBe('NO')
  });
  it('aabcd', () => {
    expect(isValid('aabcd')).toBe('YES')
  });
  it('aaabbcc', () => {
    expect(isValid('aaabbcc')).toBe('YES')
  });
  it('aaabbbc', () => {
    expect(isValid('aaabbbc')).toBe('YES')
  });
  it('aaaabbcc', () => {
    expect(isValid('aaaabbcc')).toBe('NO')
  });
  it('short or equal to 3', () => {
    expect(isValid('abc')).toBe('YES')
    expect(isValid('ab')).toBe('YES')
    expect(isValid('a')).toBe('YES')
    expect(isValid('')).toBe('YES')
  });
});