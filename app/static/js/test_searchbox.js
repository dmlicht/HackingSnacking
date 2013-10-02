var assert = require("assert");
var searchbox = require("./searchbox");
describe('Searchbox', function(){
    beforeEach(function(){
    });

    it('it should be able to run test file', function(){
        assert.equal(1,1);
    })

    describe('#unionLists', function(){
        it('should give good output for good input digits', function(){
            var input = [[1,2,4,5], [2,7,0,6], [2,7,-3,10]]
            var expected = [-3, 0, 1, 2, 4, 5, 6, 7, 10];
            var result = searchbox.unionLists(input);
            assert.equal(expected.length, result.length);
            for (var ii in expected){
                assert(result.indexOf(expected[ii]) != -1);
            }
        });
    });
});
 
