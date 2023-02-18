let man = document.getElementById('man')
let women = document.getElementById('women')
let child = document.getElementById('child')

let os_man = document.querySelector('.osnov-man')
let os_women = document.querySelector('.osnov-women')
let os_child = document.querySelector('.osnov-child')



let clothes_man = document.getElementById('clothes_man')
let clothes_women = document.getElementById('clothes_women')
let clothes_child = document.getElementById('clothes_child')

let osnov_clothes_man = document.querySelector('.osnov-clothes-man')
let osnov_clothes_women = document.querySelector('.osnov-clothes-women')
let osnov_clothes_child = document.querySelector('.osnov-clothes-child')

let shoes_man = document.getElementById('shoes_man')
let wrapper_shoes_man = document.querySelector('.osnov-shoes-man')


shoes_man.onmousemove = function(){
   shoes_man.append(wrapper_shoes_man)
    document.querySelector('.osnov-shoes-man').style.display = 'block'
}


shoes_man.onmouseleave = function(){
    
    document.querySelector('.osnov-shoes-man').style.display = 'none'
}




clothes_man.onmousemove = function(){
    
    clothes_man.append(osnov_clothes_man)
    document.querySelector('.osnov-clothes-man').style.display = 'block'
}

clothes_man.onmouseleave = function(){
    
    document.querySelector('.osnov-clothes-man').style.display = 'none'
}



osnov_clothes_man.onmousemove = function(){
    
    document.querySelector('.osnov-clothes-man').style.display = 'block'
}



man.onmousemove = function(){
    document.querySelector('.osnov-man').style.display = 'block'
    document.querySelector('.osnov-women').style.display = 'none'
    document.querySelector('.osnov-child').style.display = 'none'
}

os_man.onmouseleave = function(){
    document.querySelector('.osnov-man').style.display = 'none'
    
}



women.onmousemove = function(){
    document.querySelector('.osnov-women').style.display = 'block'
    document.querySelector('.osnov-child').style.display = 'none'
    document.querySelector('.osnov-man').style.display = 'none'
}

os_women.onmouseleave = function(){
    document.querySelector('.osnov-women').style.display = 'none'
}




child.onmousemove = function(){
    document.querySelector('.osnov-women').style.display = 'none'
    document.querySelector('.osnov-child').style.display = 'block'
    document.querySelector('.osnov-man').style.display = 'none'
}

os_child.onmouseleave = function(){
    document.querySelector('.osnov-child').style.display = 'none'
}

