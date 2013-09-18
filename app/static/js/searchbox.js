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
 * mapping names and tags of deal objects to deals
 */
function buildTrie(deals){
    var trie = new this.Trie('i'); //i for case insensitive. Borrowed from regex flag
    tagsDict = createTagToDealListDictionary(deals)
    for (var ii in deals){
        trie.add(deals[ii]['name'], [deals[ii]]);
    }
    for (var ii in tagsDict){
        trie.add(ii, tagsDict[ii]);
    }
    return trie;
}

/**
 * takes a list of deals and returns a dictionionary
 * mapping each element of the set of tags associated with deals
 * to the list of all deals matching the tag
 */
function createTagToDealListDictionary(deals){
    var catDict = new Object();
    for (var ii in deals){
        var categories = deals[ii]['categories'];
        for (var jj in categories){
            if (!catDict.hasOwnProperty(categories[jj])){
                catDict[categories[jj]] = new Array();
            }
            catDict[categories[jj]].push(deals[ii]);
        }
    }
    return catDict;
}


function filterList(){
	var query = getQuery();
    //NOTE: should trie be non-global? How can I restructure?
    clearElementChildren('deals');
    var listOfLists = trie.startsWith(query);
    populateDealsList(unionLists(listOfLists));
}

/**
 * returns the union of a list of lists
 * iterates through each list and checks against
 * a dictionary of seen elements, all elements
 * are then pushed into a list and returned
 */
function unionLists(lists){
    var unique = new Object();
    var uniqueArray = new Array();
    for (var ii in lists){
        for (var jj in lists[ii]){
            var name = lists[ii][jj]['name'];
            //Note: refactor for better implementation than name
            if (!unique.hasOwnProperty(name)){
                unique[name] = lists[ii][jj];
                console.log(name);
            }
        }
    }
    for (var seen in unique){
        uniqueArray.push(unique[seen]);
    }
    return uniqueArray;
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
            deal['categories'],
            deal['deal_url'],
            deal['yelp_url']
        );
    }
}

function add_deal(name, score, nreviews, categories, grouponUrl, yelpUrl){
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

  var cats = document.createElement('ul');
  for (var i = 0; i < categories.length; i++){
    var el = document.createElement('li');
    el.innerText = categories[i];
    cats.appendChild(el)
  }
  div.appendChild(cats);

  var deals = document.getElementById('deals');
  deals.appendChild(article);
  return article;
}
