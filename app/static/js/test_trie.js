var assert = require("assert");
var Trie = require("./trie").Trie;
describe('Trie', function(){
    beforeEach(function(){
        trie = new Trie();
    });

    it('it should be able to run test file', function(){
        assert.equal(1,1);
    })

    it('should be creatable', function(){
        assert(trie);
    });

    it('should have a root with a null character', function(){
        assert.equal(trie.root.ch, null);
    });

    describe('#add', function(){
        it('should have add method', function(){
            assert(trie.add);
        });
        
        it('should be able to add hello', function() {
            var word = 'hello';
            var val = 'myval';
            trie.add(word, val);
            var result = getVal(word);
            assert.equal(result, val);
        });

        /**
         * Move to Trie
         */
        var getVal = function (key){
            var node = trie.root;
            for (var i = 0; i < key.length; i++){
                if (node.children.hasOwnProperty(key[i])){
                    node = node.children[key[i]];
                } else {
                    break;
                }
            }
            return node.storage;
        }

        it('should be able to add several words', function(){
            var words = ['hello', 'how', 'are', 'you'];
            var vals = [1, 2, 3, 4];
            for (var i = 0; i < words.length; i++){
                trie.add(words[i], vals[i]);
            }
            for (var i = 0; i < words.length; i++){
                var result = getVal(words[i]);
                assert.equal(result, vals[i]);
            }
        });
    });

    describe('#startsWith', function(){
        it('should have a startsWith', function() {
            assert(trie.startsWith);
        });

        it('should give correct value when one word is added', function() {
            trie.add('hello', 10);
            assert.equal(trie.startsWith('he')[0], 10);
        });

        it('should return the correct value for all substrings of a key', function(){
            var str = "hello";
            var val = 10;
            trie.add(str, val);
            for (var i = 1; i < str.length; i++){
                assert.equal(trie.startsWith(str.substring(0, i))[0], val);
            }
        });

        it('should return several correct values', function(){
            var kv = {
                'abba': 1,
                'abbc': 3,
                'abbb': 5,
                'blaaaarg': 10
            };
            var goodVals = [1, 3, 5];
            var badVals = [10];
            for (var key in kv){
                trie.add(key, kv[key]);
            }
            results = trie.startsWith('ab');
            assert(results.indexOf(1) > -1);
            for (var i = 0; i < goodVals.length; i++){
                assert(results.indexOf(goodVals[i]) > -1);
            }
            for (var i = 0; i < badVals.length; i++){
                assert(results.indexOf(badVals[i]) === -1);
            }
        });
    });
})
