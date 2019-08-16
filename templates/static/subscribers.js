$(function () {
    $.ajax({
        type: 'GET',
        url:'http://127.0.0.1:8000/users_books/' + $('#user_id').val(),
        success: function(data) {
            let table = document.querySelector('.table')
            let add_select = document.querySelector('.combo-box')
            data.data.users_books.forEach((book) => {
                table.innerHTML += `<tr>
                                        <td>${book.author}</td>
                                        <td>${book.genre}</td>
                                        <td><a href="../edit_book/${book.id}">${book.book_name}</a></td>
                                        <td><button id="free_book" value="${book.id}">Free</button></td>
                                    </tr>`
            });

            document.addEventListener('click', (e) => {
                if (e.target.id === 'free_book') {
                    var book = {
                    book_id: $('#free_book').val()
                };

                    $.ajax({
                    type: 'PUT',
                    url: 'http://127.0.0.1:8000/users_books/'+$('#free_book').val(),
                    data: book,
                    success: function (data) {
                        console.log(data.data.status)
                    }
                });
                }
            })



            data.data.free_books.forEach((book) => {
                add_select.innerHTML += `<option name="mast">${book.book_name}</option>`
            });
        }
    });


    var $b_name = $('#b_name');

    $('#add-book').on('click', function () {
        var book = {
            book_name: $b_name.val(),
        };

        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/users_books/'+ $('#user_id').val(),
            data: book,
            success: function () {
                console.log('add ', book)
            }
        });
    });
});
