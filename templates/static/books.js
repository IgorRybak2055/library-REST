$(function () {
    $.ajax({
        type: 'GET',
        url:'http://127.0.0.1:8000/free_books',
        success: function(data) {
            let table = document.querySelector('.table')
            data.data.free_books.forEach((book) => {
                table.innerHTML += `<tr>
                                        <td>${book.author}</td>
                                        <td>${book.genre}</td>
                                        <td>${book.book_name}</td>
                                        <td><a href="edit_book/${book.id}">Редактировать</a></td>
                                    </tr>`
            });
        }
    });

    var $b_name = $('#name');
    var $b_author = $('#author');
    var $b_genre = $('#genre');
    var $b_lang = $('#lang');

    $('#add-book').on('click', function () {
        var book = {
            book_name: $b_name.val(),
            author: $b_author.val(),
            genre: $b_genre.val(),
            language: $b_lang.val()
        };

        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/free_books',
            data: book,
            success: function (data) {
                console.log(data.data.status)
            }
        });

        $b_name.val(''),
        $b_author.val(''),
        $b_genre.val(''),
        $b_lang.val('')
    });

});
