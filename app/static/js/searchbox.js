function filterList(){
	var query = getQuery();
  return null;
}

function get_query(){
	return document.getElementById("search-field").value;
}


var populate_deals_list = function(deals_json) {

}

function add_deal(name, score, nreviews, groupon_url, yelp_url){
  article = document.createElement('article');

  h1 = document.createElement('h1');
  h1.innerText = name;

  pscore = document.createElement('p')
  pscore.innerText = "recieved " + score + " averaged from " + nreviews + " reviews!"

  pgroupon_url = document.createElement('p')
  pgroupon_url.innerText = groupon_url

  pyelp_url  = document.createElement('p')
  pyelp_url.innerText = yelp_url

  article.appendChild(h1);
  article.appendChild(pscore)
  article.appendChild(pgroupon_url)
  article.appendChild(pyelp_url)

  deals = document.getElementById('deals');
  deals.appendChild(article);
  return article;
}