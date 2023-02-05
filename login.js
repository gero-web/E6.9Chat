
function login(){

    let login = prompt('Ваш логин?');
    let pass = prompt('Ваш пароль?');
    let data = {
        "username": login,
        "password": pass
    }
   
    let prom = fetch(" http://127.0.0.1:8000/auth/jwt/create/", {
        "method": 'POST',
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
          },
         body: JSON.stringify(data)
    },)
    prom.then(rep=> {
        if(rep.status.toString() == "401")
            throw "Unauthorized";
        return rep.json();
    }).then(data => {
        console.log(data);
        sessionStorage.setItem("username", login);
        sessionStorage.setItem("Authorization", data["access"]);
        location.reload();
    }).catch((d)=>{
        console.error(d);
    });
}