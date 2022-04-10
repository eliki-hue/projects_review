console.log('hellow js')

//get all the stars

const one= document.getElementById('first')
const two= document.getElementById('two')
const three= document.getElementById('three')
const four= document.getElementById('four')
const five= document.getElementById('five')

const arr= [one, two, three, four, five]

const handleselect = (Selection)=>{
    switch(Selection){
        case 'first':{
            one.classList.add('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }

        case 'two':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }

        case 'three':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }

        case 'four':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.remove('checked')
            return
        }

        case 'five':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            return
        }
    }
}

arr.forEach(item=> item.addEventListener('mouseover',(event)=>{
    handleselect(event.target.id)
}))