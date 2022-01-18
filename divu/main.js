function login(){
    var username= document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username=="divu" && password=="divu"){
        window.location.href="welcome.html";
    }
    else{
        if (document.getElementById("Check").textContent == ''){
            var user= document.getElementById("Check");
            user.textContent+="Wrong  Username or Password";
        }
    }
}
function toggle(){
    var a= document.getElementById("password");
    if (a.type == "password"){
        a.type = "text";
    }
    else{
        a.type="password";
    }
}