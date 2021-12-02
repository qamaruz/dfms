
// object to represent data
var sensorData = {date:    '',
           cm: 0,
            inches:     0,
            time:'',
            sensorDate:'',
            firstLevel:0,
            secondLevel:0,
            thirdLevel:0,
            arduinoid:''};

// initialiser
sensorData.init = function(date,cm,inches,time,sensorDate,firstLevel,secondLevel,thirdLevel,arduinoid){

        this.date = date;
        this.cm =cm;
        this.inches=inches;
        this.time=time;
        this.sensorDate= sensorDate;
        this.firstLevel = firstLevel;
        this.secondLevel = secondLevel;
        this.thirdLevel = thirdLevel;
        this.arduinoid = arduinoid;
   
}


function AppViewModel() {
    var self = this;    

    self.Query = ko.observable('');
    self.DataList = ko.observableArray([]);//show all data
 
    
    /*self.saveData = function(){
        console.log("save!");
        if (self.feedList.lenght() > 0)
        console.log(self.feedList()[0].image);
        self.feedList()[0].image.push("images/lindsay.jpg");
        console.log(self.feedList()[0].image);

    }*/
    
   
   
  /*self.searchResults = ko.computed(function(){
       var q= self.Query();
       return self.users().filter(function(i){
           return i.name.toLowerCase().indexOf(q) >=0;
       });
   });*/
   
  // Function to remove book used in simple data-binding
  /*self.removeBook = function(feed) { console.log("remove"); self.feedList.remove(user) };*/
  
  
  self.ajaxTestVM = function(){
    $.post("http://api.clickatell.com/http/sendmsg?user=qamaruz&password=ZGJGbIRcdgadBg&api_id=3621525&to=6738643939&text=ajaxtest",function(json_data, status){
        console.log(status,xhr);
        console.log(json_data);
    //alert("foo: " + json_data.data+ "\nStatus: " + status);
    });
    };

	
	self.debug = function(item) {
        console.log("Debug");
        $.post("/v_0_1/getSensorData/", function(json_data, status){
            //console.log(json_data);
            
         new_data1 = Object.create(sensorData);
        //date,cm,inches,time,sensorDate,firstLevel,secondLevel,thirdLevel
        new_data1.init(json_data[0][0], json_data[0][1], json_data[0][2],json_data[0][3],json_data[0][4],json_data[0][5],json_data[0][6],json_data[0][7],json_data[0][8]);
        self.DataList.unshift(new_data1);
        console.log("Data Added!");
        });
        //self.DataList.pop();
        
	 /* for(i in self.users()){
         //console.log(self.users()[i].name);
         $.post("http://localhost/fashLink/postTest/",ko.toJSON({name:self.users()[i].name}),function(json_data, status){
        console.log(json_data)
    //alert("foo: " + json_data.data+ "\nStatus: " + status);
    });
         
      }*/
	  
    };
    
    self.send = function(item) {
        console.log("sendEmai");
        $.post("/v_0_1/sendEmail", function(json_data, status){
            console.log(json_data);
            
         
        });
        
	  
    };

    
    self.remove = function(item) {
        
        self.DataList.pop();
    }
    /*self.getSensorData = ko.computed (function(){$.post("/v_0_1/getSensorData/", function(json_data, status){
        console.log(json_data);
       });
  });*/
    
  // function to load books from the reading list
  self.initViewModel = ko.computed (function(){$.post("/v_0_1/getData/", function(json_data, status){
        
    //alert("foo: " + json_data.data+ "\nStatus: " + status);
      //var tmpList = []
      for (i in json_data){
        //console.log(json_data)
        new_data = Object.create(sensorData);
        //date,cm,inches,time,sensorDate,firstLevel,secondLevel,thirdLevel
        new_data.init(json_data[i][0], json_data[i][1], json_data[i][2],json_data[i][3],json_data[i][4],json_data[i][5],json_data[i][6],json_data[i][7],json_data[i][8]);
        self.DataList.push(new_data);
         
      }

      });
  });
  

      (function () {
   self.initViewModel();
  })();

  
  //console.log(self.DataList());
}

 
$().ready(function(){
  ko.applyBindings(new AppViewModel()); 
});