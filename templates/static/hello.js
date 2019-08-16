$(function (){
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000',
        success: function (data) {
            let table = document.querySelector('.table')
            data.data.users.forEach((el) => {
                table.innerHTML += `<tr>
                                        <td><a href="subscriptions/${el.id}">${el.first_name}</a></td>
                                        <td>${el.last_name}</td>
                                        <td>${el.address}</td>
                                        <td>${el.phone}</td>       
                                   </tr>`
            });
        }
    });

    var $f_name = $('#first_name');
    var $l_name = $('#last_name');
    var $address = $('#address');
    var $phone = $('#phone');

    $('#add-user').on('click', function () {
        var user = {
            first_name: $f_name.val(),
            last_name: $l_name.val(),
            address: $address.val(),
            phone: $phone.val()
        };

        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000',
            data: user,
            success: function (data) {
                console.log(data.data.status)
            }
        });

        $f_name.val(''),
        $l_name.val(''),
        $address.val(''),
        $phone.val('')
    });

});

