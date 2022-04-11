console.log('hellow js')

//get all the stars

const one= document.getElementById('first')
const two= document.getElementById('two')
const three= document.getElementById('three')
const four= document.getElementById('four')
const five= document.getElementById('five')
const six= document.getElementById('six')
const seven= document.getElementById('seven')
const eight= document.getElementById('eight')
const nine= document.getElementById('nine')
const ten= document.getElementById('ten')

const form =document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(form)
console.log(confirmBox)
console.log(csrf)

const arr= [one, two, three, four, five, six, seven, eight, nine, ten]

// const handleselect = (size)=>{
//     const children = form.children
//     for(let i=0; i < children.length; i++){
//         if(i <= size){
//             children[i].classList.add('checked')

//         }else {
//             children[i].classList.remove('checked')
                                   
//         }
//     }

const handleselect = (Selection)=>{
    switch(Selection){
        case 'first':{
            one.classList.add('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            six.classList.remove('checked')
            seven.classList.remove('checked')
            eight.classList.remove('checked')
            nine.classList.remove('checked')
            ten.classList.remove('checked')
           
            return
        }

        case 'two':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            six.classList.remove('checked')
            seven.classList.remove('checked')
            eight.classList.remove('checked')
            nine.classList.remove('checked')
            ten.classList.remove('checked')
            return
        }

        case 'three':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            six.classList.remove('checked')
            seven.classList.remove('checked')
            eight.classList.remove('checked')
            nine.classList.remove('checked')
            ten.classList.remove('checked')
            return
        }

        case 'four':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.remove('checked')
            six.classList.remove('checked')
            seven.classList.remove('checked')
            eight.classList.remove('checked')
            nine.classList.remove('checked')
            ten.classList.remove('checked')
            return
        }

        case 'five':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            six.classList.remove('checked')
            seven.classList.remove('checked')
            eight.classList.remove('checked')
            nine.classList.remove('checked')
            ten.classList.remove('checked')
            return
        }

        case 'six':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            six.classList.add('checked')
            seven.classList.remove('checked')
            eight.classList.remove('checked')
            nine.classList.remove('checked')
            ten.classList.remove('checked')
           
            return
        }

        case 'seven':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            six.classList.add('checked')
            seven.classList.add('checked')
            eight.classList.remove('checked')
            nine.classList.remove('checked')
            ten.classList.remove('checked')
           
            return
        }
        case 'eight':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            six.classList.add('checked')
            seven.classList.add('checked')
            eight.classList.add('checked')
            nine.classList.remove('checked')
            ten.classList.remove('checked')
           
            return
        }

        case 'nine':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            six.classList.add('checked')
            seven.classList.add('checked')
            eight.classList.add('checked')
            nine.classList.add('checked')
            ten.classList.remove('checked')
           
            return
        }
        case 'ten':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            six.classList.add('checked')
            seven.classList.add('checked')
            eight.classList.add('checked')
            nine.classList.add('checked')
            ten.classList.add('checked')
           
            return
        }
    }
}
const getNumericvalue= (stringValue)=>{
    let NumericValue;
    if (stringValue ==='first'){
        NumericValue =1
    }
    else if(stringValue ==='two'){
        NumericValue =2
    }
    else if(stringValue ==='three'){
        NumericValue =3
    }
    else if(stringValue ==='four'){
        NumericValue =4
    }
    else if(stringValue ==='five'){
        NumericValue =5
    }
    else if(stringValue ==='six'){
        NumericValue =6
    }
    else if(stringValue ==='seven'){
        NumericValue =7
    }
    else if(stringValue ==='eight'){
        NumericValue =8
    }
    else if(stringValue ==='nine'){
        NumericValue =9
    }
    else if(stringValue ==='ten'){
        NumericValue =10
    }
    else {
        NumericValue =0
    }

    return NumericValue
}
arr.forEach(item=> item.addEventListener('mouseover',(event)=>{
    handleselect(event.target.id)
}))

arr.forEach(item=> item.addEventListener('mouseover',(event)=>{
    const val = (event.target.id)
    
    form.addEventListener('submit', e=>{
        e.preventDefault()
        const id = e.target.id
        const val_num = getNumericvalue(val)
        
        $.ajax({
            type:'POST',
            url:'/rate/',
            data:{
                'csrfmiddlewaretoken':csrf[0].value,
                'project_id':id,
                'val_num':val_num,

            },
            success:function(response){
                console.log(response)
                confirmBox.innerHTML='<h3>Successfuly rated</h3>'
            },
            error:function(error){
                consolee.log(error)
                confirmBox.innerHTML ='<h1>ups... something went wrong</h1>'
            }

        })
    })
    

    
}))


    // $(document).ready(function(){
    //     $('form').submit(function(event){
    //       event.preventDefault()
    //       form = $("form")
      
    //         $.ajax({
    //             type:'POST',
    //             url:'/rate/',
    //             data:{
    //                 'csrfmiddlewaretoken':csrf[0].value,
    //                 'project_id':id,
    //                 'val_num':val_num,

    //             },
    //             success:function(response){
    //                 console.log(response)
    //                 confirmBox.innerHTML='<h1>Successfuly rated with ${response.score}</h1>'
    //             },
    //             error:function(error){
    //                 consolee.log(error)
    //                 confirmBox.innerHTML ='<h1>ups... something went wrong</h1>'
    //             }
    //         }) // End of document ready function
    //      })
    //     })
