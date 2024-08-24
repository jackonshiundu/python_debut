==============MT DJANGO NOTES================
1. When you creatign log in and logout you dont nned to create logic for this django provides you this as long as you just provide the tamplete to be redirected to however when you creating the register you will just need to process the logic but but .
2.Django Signals-this is a mechanism that that allows executing of accode in response to event without tightly coupling the code to the action itself
SIGNAL DISPATCHER- is a component handles the process of diapatching asignals when certain events occur. Notifies when something acctually happens. 
3.Django views--views are essential components that handle the logic for processing user requests and returning responses.
=>Function-Based Views (FBVs): Traditional view functions that handle HTTP requests.
=>Class-Based Views (CBVs): Object-oriented views that provide more structure and reusable components.
   ->ListView(can be used along class based views)Shows a list of multiple items from a model
   ->Detailview(can be used along class based views)Shows detailed information for a single item from a model.