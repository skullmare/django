let btn_modal_del_event = document.querySelectorAll('.btn_modal_del_event')
    btn_modal_del_event.forEach(function (btn) {
        btn.addEventListener('click', function () {
            document.querySelector('#hidd_del_event_id').value = btn.getAttribute('event_id')
        })
    })
    let btn_modal_update_event = document.querySelectorAll('.btn_modal_update_event')
    btn_modal_update_event.forEach(function (btn) {
        btn.addEventListener('click', function () {
            fetch(`/api/events/?format=json&id=${btn.getAttribute('event_id')}`)
                .then((response) => response.json())
                .then((response) => fill_fields_model(response))
        })
        function fill_fields_model(events) {
            events.forEach(function (event) {
                [...document.querySelector('.form_update')].forEach(i => {
                    Object.keys(event).forEach(key => {
                        if (i.id.includes(key)) {
                            i.value = event[key]
                        }
                    })
                })
            })
        }
    })