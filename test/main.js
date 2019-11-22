$.getJSON('http://127.0.0.1:8000/classmates/', function(data) {
    console.log(data);
       
       
        var div = document.getElementById("test");
        div.innerHTML = data[0].firstname + " " +data[0].lastname + "\n Roll No. :" +data[0].roll ;

});