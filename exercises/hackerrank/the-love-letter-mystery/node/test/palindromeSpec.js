// let expect = require("chai").expect;
let palindrome = require("./../palindrome");
let assert = require('assert');

describe("Api Responder", function() {

	describe("removeMiddleChar()", function() {
		it("handle odd string", function() {
			let res = palindrome.removeMiddleChar('12Ads');
			assert.equal(res, '12ds');
		});
		it("handle even string", function() {
			let res = palindrome.removeMiddleChar('12ds');
			assert.equal(res, '12ds');
		});
	});

	describe("getPalindromeSteps()", function() {
		it("handle already palindrome", function() {
			let res = palindrome.getPalindromeSteps('aba');
			assert.equal(res, 0);
		});
		it("handle one step palindrome even string", function() {
			let res = palindrome.getPalindromeSteps('ab');
			assert.equal(res, 1);
		});

		it("handle one step palindrome odd string", function() {
			let res = palindrome.getPalindromeSteps('acb');
			assert.equal(res, 1);
		});

		it("handle several steps palindrome", function() {
			let res = palindrome.getPalindromeSteps('acf');
			assert.equal(res, 5);
		});

		it("handle several steps palindrome with several change points", function() {
			let res = palindrome.getPalindromeSteps('abcdf');
			assert.equal(res, 7);
		});
	});

	describe("getCharCode()", function() {
		it("get code of a", function() {
			assert.equal(palindrome.getCharCode('a'), 97);
			assert.equal(palindrome.getCharCode('A'), 65);
			assert.equal(palindrome.getCharCode('z'), 122);
			assert.equal(palindrome.getCharCode('Z'), 90);
		});
	});

});