const addComment = (nickname, content)=>{
    console.log(nickname + ' ' + content);
}


//#################   Ajax   ################

const csrf_name = 'csrfmiddlewaretoken'

//###########  Rating ajax  ###################

const rating_form = document.getElementById('rating-form');
const rating_csrf_token = document.getElementsByName(csrf_name)[0].value;

const rating_button_like = document.getElementById('rating-like');
const rating_button_dislike = document.getElementById('rating-dislike');

let rating_data;

rating_button_like.addEventListener('click', e=>{
    rating_data = 'like';
}, false);

rating_button_dislike.addEventListener('click', e=>{
    rating_data = 'dislike';
}, false);

rating_form.addEventListener('submit', e=>{
    e.preventDefault();

    const fd = new FormData();
    fd.append(csrf_name, rating_csrf_token)
    fd.append('rating', rating_data)

    $.ajax({
        type: 'POST',
        url: '',
        enctype: 'text/plain',
        data: fd,
        success: function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error);
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})

//###########  Comment ajax  ###################

const comment_form = document.getElementById('comment-form');
const comment_field = document.getElementById('comment-field');
const comment_csrf_token = document.getElementsByName(csrf_name)[1].value;

comment_form.addEventListener('submit', e=>{
    e.preventDefault()

    const fd = new FormData();
    fd.append(csrf_name, comment_csrf_token);
    fd.append("content", comment_field.value);


    $.ajax({
        type: 'POST',
        url: '',
        enctype: 'text/plain',
        data: fd,
        success: response=>{
            console.log(response);
            author = response['added_comment']['author'];
            content = response['added_comment']['content'];
            addComment(author, content);
        },
        error: error=>{
            console.log(error);
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})