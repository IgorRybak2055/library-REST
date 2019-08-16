$(function () {
    var $b_name = $('#b_name');
    var $b_author = $('#b_author');
    var $b_genre = $('#b_genre');
    var $b_lang = $('#b_lang');

    $.ajax({
        type: 'GET',
        url:'http://127.0.0.1:8000/book/' + $('#b_id').val(),
        success: function(data) {
            let div = document.querySelector('.container')
            data.data.book_info.forEach((info) => {
                $b_name.val(info.book_name),
                $b_author.val(info.author),
                $b_genre.val(info.genre),
                $b_lang.val(info.language)
            });
        }
    });


    $('#save-changes').on('click', function () {
        var book = {
            book_name: $b_name.val(),
            author: $b_author.val(),
            genre: $b_genre.val(),
            language: $b_lang.val()
        };

        $.ajax({
            type: 'PUT',
            url: 'http://127.0.0.1:8000/book/'+ $('#b_id').val(),
            data: book,
            success: function () {
                console.log('change ', book)
            }
        });
    });
});
