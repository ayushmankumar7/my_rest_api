$.getJSON('http://127.0.0.1:8000/classmates/', function(data) {
    console.log(data);
       
       
        var div = document.getElementById("test");
        div.innerHTML = data[2].firstname + " " +data[2].lastname + "\n Roll No. :" +data[2].roll ;
        

});