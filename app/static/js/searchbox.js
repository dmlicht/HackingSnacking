// We need to:
//      * store the json data
//      * get all stored json elements from try
//      *

window.onload = function(){
    var xhReq = new XMLHttpRequest();
    xhReq.open("GET", "/_deal_data", false);
    xhReq.send(null);
    var serverResponse = xhReq.responseText;
    var deals = getDealList(serverResponse);
    trie = buildTrie(deals);
    populateDealsList(deals);
};

/**
 * takes raw string input containing json of a list of deals
 * returns list of deal objects
 */
function getDealList(dealsString){
    var dealsJSON = JSON.parse(dealsString);
    var deals = new Array();
    for (var dealName in dealsJSON){
        deals.push(JSON.parse(dealsJSON[dealName])); 
    }
    return deals;
}

/**
 * takes list of deal objects and returns a trie
 * mapping names of a deal to deal objects
 */
function buildTrie(deals){
    var trie = new this.Trie();
    for (var ii in deals){
        trie.add(deals[ii]['name'], deals[ii]);
    }
    return trie;
}

function filterList(){
	var query = getQuery();
    //should trie be non-global? How can I restructure?
    clearElementChildren('deals');
    populateDealsList(trie.startsWith(query));
}

function clearElementChildren(nodeID){
    var node = document.getElementById(nodeID);
    while (node.hasChildNodes()) {
        node.removeChild(node.lastChild);
    }
}

function getQuery(){
	return document.getElementById("search-field").value;
}

/** adds passed deals to dom */
var populateDealsList = function(deals) {
    for (var dealName in deals){
        var deal = deals[dealName];
        add_deal(
            deal['name'], 
            deal['yelp_score'],
            deal['num_reviews'],
            deal['deal_url'],
            deal['yelp_url']
        );
    }
}

function add_deal(name, score, nreviews, grouponUrl, yelpUrl){
  var article = document.createElement('article');
  article.className += "deal";

  var div = document.createElement('div');
  div.className += "deal-content";

  var nameLink = document.createElement('a');
  nameLink.href = grouponUrl;

  var h1 = document.createElement('h1');
  h1.innerText = name;

  nameLink.appendChild(h1);

  var pscore = document.createElement('p');
  var scoreLink = document.createElement('a');
  scoreLink.href = yelpUrl;
  scoreLink.innerText = score + " out of " + nreviews + " on yelp!";
  pscore.appendChild(scoreLink);

  article.appendChild(div);
  div.appendChild(nameLink);
  div.appendChild(pscore);

  var deals = document.getElementById('deals');
  deals.appendChild(article);
  return article;
}
