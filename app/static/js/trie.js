;(function(exports){
    var Trie = function(arg){
        if (arg == 'i'){
            this.case_insensitive = true;
        }
        this.root = new Node(null);
    };

    var Node = function(ch){
        this.children = {};
        this.ch = ch;
    };

    /**
     * stores val in node where characters of key end
     */
    Trie.prototype.add = function (key, val){
        if (this.case_insensitive = true){
            key = key.toLowerCase();
        }
        currentNode = this.root;
        for (var i = 0; i < key.length; i++){
            if (currentNode.children.hasOwnProperty(key[i])){
                currentNode = currentNode.children[key[i]];
            } else {
                newNode = new Node(key[i]);
                currentNode.children[key[i]] = newNode;
                currentNode = newNode;
            }
        }
        currentNode.storage = val;
    }

    /**
     * returns all strings prefixed by passed string
     */
    Trie.prototype.startsWith = function(prefix) {
        if (this.case_insensitive){
            prefix = prefix.toLowerCase();
        }
        var currentNode = this.find(prefix)
        //find is returning null
        if (currentNode === null){ return []; }
        return this.findStoredBelow(currentNode);
    }

    /*
     * grabs node where passed string ends, returns null if
     * no added string contains str and a prefix
     */
    Trie.prototype.find = function(str){
        var currentNode = this.root;
        for (var i = 0; i < str.length; i++){
            if (currentNode.children.hasOwnProperty(str[i])){
                currentNode = currentNode.children[str[i]];
            } else {
                //if we don't have a child for the next letter exit
                return null;
            }
        }
        return currentNode;
    }

    /**
     * returns all values below a given node
     */
    Trie.prototype.findStoredBelow = function(node) {
        var values = [];
        if (node.hasOwnProperty('storage')){
            values.push(node['storage']);
        }
        for (var ch in node.children){
            values = values.concat(this.findStoredBelow(node.children[ch]));
        }
        return values;
    }

    exports.Trie = Trie;
}(this));
