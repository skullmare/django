let btns = document.querySelectorAll('.selSeat');
    let params = new URLSearchParams(document.location.search);
    let event_id = params.get('id');
    let btnPay = document.querySelector('.pay');
    let sel_seats = []
    btns.forEach(function (btn) {
        btn.addEventListener('change', function () {
            let seat_id = btn.getAttribute('seat_id')
            if (btn.checked) {
                sel_seats.push(seat_id)
            }
            else {
                let index = sel_seats.indexOf(seat_id)
                console.log(index)
                sel_seats.splice(index, 1)
            }
            console.log(sel_seats)
            if (sel_seats.length == 0) {
                document.querySelector('.div_btn_modal_pay').innerHTML = ''
            }
            else {
                document.querySelector('.div_btn_modal_pay').innerHTML = ''
                let dbmp = document.querySelector('.div_btn_modal_pay')
                let template = document.querySelector('#btn_modal_pay').content.cloneNode(true);
                dbmp.appendChild(template)
            }
        })
    })
    btnPay.addEventListener('click', function () {
        const formdata = new FormData();
        formdata.append('sel_seats', sel_seats);
        formdata.append('event_id', event_id);
        formdata.append('email', document.querySelector('#email').value);
        const requestOptions = {
            method: "POST",
            body: formdata
        };
        fetch(`pay`, requestOptions)
            .then((response) => {
                if (response.status >= 200 && response.status < 300) {
                    alert('Бронирование произведено успешно')
                    location.replace(document.URL);
                } else {
                    alert('Бронирование отклонено')
                    location.replace(document.URL);
                }
            })
        
    })