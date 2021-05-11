const comment_box = document.getElementById('comments');

const addComment = (nickname, author_picture_url, content)=>{
    let single_comment = document.createElement('div');
    comment_box.appendChild(single_comment);
    
    let author_space = document.createElement('div');
    author_space.innerText = nickname;

    let img = document.createElement('img');
    img.src = author_picture_url;

    let comment_content = document.createElement('div');
    comment_content.innerText = content;

    single_comment.appendChild(author_space);
    single_comment.appendChild(img);
    single_comment.appendChild(comment_content);

}

const likes_box = document.getElementById('likes');
const dislikes_box = document.getElementById('dislikes');

function updateRating(likes, dislikes){
    likes_box.innerText = likes;
    dislikes_box.innerText = dislikes;
}


//#################   Ajax   ################

const csrf_name = 'csrfmiddlewaretoken'
const rating_csrf_token = document.getElementsByName(csrf_name)[0].value;

function send_request(url, data){
    const fd = new FormData();
    fd.append(csrf_name, rating_csrf_token);
    fd.append(data[0], data[1]);

    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'text/plain',
        data: fd,
        success: function(response){
            let likes = response['rating']['likes'];
            let dislikes = response['rating']['dislikes'];
            updateRating(likes, dislikes);
        },
        error: function(error){
            console.log(error);
        },
        cache: false,
        contentType: false,
        processData: false,
    })
}




//###########  add to save playlist ajax, copy link  ###################

const share_button = document.getElementById('share');
const save_button = document.getElementById('watch-later');

share_button.addEventListener('click', e=>{
    
    const el = document.createElement('textarea');
    el.value = window.location.href;
    el.setAttribute('readonly', '');
    el.style.position = 'absolute';
    el.style.left = '-9999px';
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    
}, false);

save_button.addEventListener('click', e=>{
    
    const fd = new FormData();
    fd.append(csrf_name, rating_csrf_token);
    fd.append('cos', 'cos');

    $.ajax({
        type: 'POST',
        url: 'playlist_update',
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


}, false);






//###########  Rating ajax  ###################

const rating_button_like = document.getElementById('rating-like');
const rating_button_dislike = document.getElementById('rating-dislike');


rating_button_like.addEventListener('click', e=>{
    send_request('', ['rating', 'like']);
}, false);

rating_button_dislike.addEventListener('click', e=>{
    send_request('', ['rating', 'dislike']);
}, false);


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
            author = response['added_comment']['author'];
            author_picture_url = response['added_comment']['picture'];

            content = response['added_comment']['content'];
            addComment(author, author_picture_url, content);
        },
        error: error=>{
            console.log(error);
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})