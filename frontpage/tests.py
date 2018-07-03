# from django.test import TestCase

# # Create your tests here.
# <!doctype html>
# <html lang="en">
#     <head>
#         <meta charset="utf-8">
#         {% load staticfiles %}
#         <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#         <meta name="description" content="">
#         <meta name="author" content="">

    
#         <title></title>
#         <script
#             src="https://code.jquery.com/jquery-3.3.1.min.js"
#             integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
#             crossorigin="anonymous"></script>
#         <script
#             src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"
#             integrity="sha256-VazP97ZCwtekAsvgPBSUwPFKdrwD3unUfSGVYrahUqU="
#             crossorigin="anonymous"></script>
        
#         <!--script src="{% static 'frontpage/js/jquery-3.3.1.min.js' %}"></script-->
#         <!-- Bootstrap core CSS -->
#         <!--link href="{% static 'frontpage/css/jquery-ui.min.css' %}" rel="stylesheet"-->
#         <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.css" >
#         <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">

#         <!-- 3rd party JS       -->
#         <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
#         <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>        
#         <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.min.js"></script>  
#         <script src="https://cdnjs.cloudflare.com/ajax/libs/waypoints/4.0.1/jquery.waypoints.min.js"></script>
#         <script src="https://cdnjs.cloudflare.com/ajax/libs/waypoints/4.0.1/shortcuts/infinite.min.js"></script>
#         <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-notify/0.2.0/js/bootstrap-notify.min.js"></script>

#         <!-- Custom styles for this template -->
#         <link href="{% static 'frontpage/css/dashboard.css' %}" rel="stylesheet">
#       <style>@media print {#ghostery-purple-box {display:none !important}}</style>
#     </head>
#     <body>
#         <nav class="navbar navbar-expand-lg navbar-dark fixed-top" style="background-color: rgb(55, 55, 110);" >
#             <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
#                     <span class="navbar-toggler-icon"></span>
#             </button>
#             <div class="collapse navbar-collapse justify-content-between" id="navbarSupportedContent">
#                 <div>
#                     <ul class="navbar-nav mr-auto">
#                         <li class="nav-item active">
#                             <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
#                         </li>
#                         <li class="nav-item active">
#                             <a class="nav-link" href="/api/">API</a>
#                         </li>
#                         <li class="nav-item active">
#                             <a class="nav-link disabled" href="#">Subscription</a>
#                         </li>
#                         <li class="nav-item active">
#                                 <a class="nav-link disabled" href="#" disabled>Profile</a>
#                         </li>
#                         <li class="nav-item active">
#                             <a class="nav-link disabled" href="#">Sign out</a>
#                         </li>
#                     </ul>
#                 </div>
#                 <div>
#                     <form class="form-inline my-2 my-lg-0";>
#                         {% comment %} <input class="form-control mr-sm-2" id="search_bar" type="search" placeholder="Search" aria-label="Search" oninput="filter()"> {% endcomment %}
#                         <div class="input-group">
#                             <input id="search_bar" class="form-control mr-sm-2" type="search" placeholder="Name, symbol, or ID" oninput="filter()" autocomplete=off>
#                             <!--datalist id="results" class="display_results">
#                             </datalist-->
#                         </div>
#                         <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Search</button>
#                     </form>
#                 </div>
#             </div>
#         </nav>
#         <!--{% include "frontpage/chat.html" %}-->
        
#         {% block content %}
#         {% endblock %}

#         <!--primary scripts; populate navbar and searchbar auto complete-->
#         <script id="nav_scripts">
#             // call CoinViewSet filter method
#             function filter() {
#                 var filter_token = document.getElementById("search_bar").value;
#                 var searchURL = 'http://' + window.location.host + "/api/coins/?search=" + filter_token
            
#                 var xmlHttp = new XMLHttpRequest();
#                 xmlHttp.onreadystatechange = function() {
#                     if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
#                         var data = JSON.parse(this.responseText);
#                         populate_options(data.results);
#                     }
#                 };
#                 xmlHttp.open("GET", searchURL, true);
#                 xmlHttp.send(null);
#             }

#             // callback function for filter function accepts array of coin model objects
#             function populate_options(arr) {
#                 var displayOptions = "";
#                 var i;
#                 var source = [];
#                 var base_url = 'http://' + window.location.host + "/";
#                 var iter_count = Math.min(arr.length, 20);
#                 for (i=0; i < iter_count; i++) {
#                     var slug = arr[i].slug;
#                     var url = base_url + slug;
#                     var label = arr[i].name  +' / '+ arr[i].symbol +' / '+ arr[i].id;
#                     source.push({value: url, label:label})
#                     //displayOptions+= '<option label="' + arr[i].name  +' / '+ arr[i].symbol +' / '+ arr[i].id + '">' + '</option>';
#                 }

#                 // ajax auto complete function
#                 $(function () {
#                     $( "#search_bar" ).autocomplete({
#                         source: source,
#                         position: {
#                             my: "top+5%",
#                             //collision: "none"
#                         },
#                         select:function( event, ui ) { 
#                             window.location.href = ui.item.value;
#                             event.preventDefault();
#                         },
#                         focus: function(event, ui){
#                             event.preventDefault();
#                             var display_string = ui.item.label.split(" / ");
#                             $("#search_bar").val(display_string[0]);                
#                         }
#                     });
#                 });
#                 //document.getElementById("results").innerHTML = displayOptions;
#             }
#         </script>

#         <!--collection of js helper functions-->
#         <script id="helper_functions">
#             function parse_subscriptions(response) {
#                 var response = JSON.parse(response);
#                 // data we are interested in is stored in response.results
#                 var subscription_json = response.results;
#                 return subscription_json;
#             }

#             function raise_update_alert(name, price) {
#                 msg = 'Update received - <strong>' + name +  '</strong>' + ': ' + price;
#                 var notify = $.notify(msg, {
#                     placement: {
#                         from: "bottom"
#                     },
#                     animate: {
#                         enter: 'animated fadeInRight',
#                         exit: 'animated fadeOutRight',
#                     },
#                 });
#             }

#             // take user subscriptions list and iteratively open socket connection to server
#             function create_socket_connections(subscriptions) {
#                 // iterate subscription objects and create new socket connections
#                 for (var i=0; i < subscriptions.length; i++) {
#                     // extract slug from results[index].coin
#                     var slug = subscriptions[i].coin;
#                     // refer to coins.routing.py for socket endpoint construction
#                     var socket_url = 'ws://' + window.location.host + '/ws/coin/' + slug + '/';
#                     console.log(socket_url);
#                     // create websocket connection for every subscription
#                     var socket = new WebSocket(socket_url);
#                     socket.onmessage = function(e){
#                         // extract data from coin_json = {"type":"", "content":json_data}
#                         var data = JSON.parse(e.data);
#                         var content = JSON.parse(data.content);
#                         var price = content.price;
#                         // log price for debugging
#                         console.log(price);
#                         // raise alerts on every message received
        
#                         raise_update_alert(content.name, content.price);
#                     };
#                 }
#             }

#             // get which currency the user is subscribed to, then callback
#             function get_subscriptions(callback) {
#                 var subscription_XMLHttp = new XMLHttpRequest();
#                 // get host url
#                 var URL_root = window.location.host;
#                 // URL_root is now in this form: example.org:8000
#                 var subscription_URL = 'http://' + URL_root + '/api/subscription/'
#                 subscription_XMLHttp.onreadystatechange = function() {
#                     // check if request is accepted
#                     if (subscription_XMLHttp.readyState==4 && this.status==200) {
#                         var subscriptions = parse_subscriptions(this.responseText);
#                         var ws_connect = callback;
#                         ws_connect(subscriptions);
#                     }
#                 }
#                 subscription_XMLHttp.open('GET', subscription_URL, true);
#                 subscription_XMLHttp.send(null);
#             }
#         </script>

#         <script>
#             function init_subscriptions_ws_feed() {
#                 /*
#                 1) get which currency the user is subscribed to
#                     - send GET request to /api/subscription/
#                     - parse response -> acquire currency slugs
#                 2) open ws connections for each currency with matching slugs */
#                 var callback = create_socket_connections; // step 1
#                 get_subscriptions(callback); //step 2
#             }
#             // call 
#             init_subscriptions_ws_feed();
#         </script>
        
#     <!-- Bootstrap core JavaScript
#     ================================================== -->
#     <!-- Placed at the end of the document so the pages load faster -->
#     {% comment %} <script src="{% static 'frontpage/js/jquery-3.3.1.min.js' %}"></script> {% endcomment %}
#     {% comment %} <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script> {% endcomment %}
#     {% comment %} <script>window.jQuery || document.write('<script src="../../js/jquery-slim.min.js"><\/script>')</script> {% endcomment %}
#     {% comment %} <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script> {% endcomment %}
#     <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->

#     </body>
# </html>