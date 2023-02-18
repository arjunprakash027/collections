//document.getElementById("count-el").innerText = 5

let welcome = document.getElementById("welcome")
welcome.innerText = "Hello,"
welcome.innerText += "User!"

let entries = "previous entries:"
let countEL = document.getElementById("count-el")
let saveEL = document.getElementById("save-el")
console.log(countEL)

let count = 0
function increment(){
    count = count + 1
    countEL.innerText = count
}

function decrement(){
    count = count - 1
    countEL.innerText = count
}

function save(){
    entries += count + " - "
    saveEL.innerText = entries
}

countEL.innerText = count



