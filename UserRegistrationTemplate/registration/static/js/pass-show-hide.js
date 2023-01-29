const passfield= document.querySelector(".form .field input[type='password']");
let togglebtn = document.querySelector(".form .field i");

console.log(togglebtn);
togglebtn.onclick= ()=>{
    if(passfield.type == "password")
    {
        passfield.type = "text";
        togglebtn.classList.add("active");
    }
    else
    {
        passfield.type= "password";
        togglebtn.classList.remove("active")
    }
}