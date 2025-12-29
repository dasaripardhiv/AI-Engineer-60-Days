async function send(){
    let input=document.getElementById("input");
    let msg=input.value.trim();
    if(msg==="") return;

    add(msg,"user");
    input.value="";

    let res=await fetch("http://127.0.0.1:8000/chat",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({message:msg})
    });

    let data=await res.json();
    add(data.reply,"bot");
}

function add(text,type){
    let box=document.getElementById("chat-area");
    let p=document.createElement("p");

    p.className=type;
    p.innerText=text;

    box.appendChild(p);
    box.scrollTop=box.scrollHeight;
}
