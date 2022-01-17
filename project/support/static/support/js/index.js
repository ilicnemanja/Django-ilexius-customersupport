const phoneInputField = document.querySelector("#phone");
const phoneInput = window.intlTelInput(phoneInputField, {
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});

function logout_confirmation(event) {
    const choice = window.confirm("Are you sure you want to logout?")
    if (choice == false) {
        event.preventDefault();
        return false
    }
}

function delete_confirmation(event) {
    const choice = window.confirm("Are you sure you want to delete this customer issue?")
    if (choice == false) {
        event.preventDefault();
        return false
    }
}

var logic = function(currentDateTime) {

    day = moment(currentDateTime.date).day()
    if ([1, 2, 3, 4, 5].includes(day)) {
        $('#datetimepicker1').data("DateTimePicker").enabledHours([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    } else if (day == 6) {
        $('#datetimepicker1').data("DateTimePicker").enabledHours([8, 9, 10, 11, 12])
    } else {
        $('#datetimepicker1').data("DateTimePicker").enabledHours([])
    }
};

$(function() {
    $('#datetimepicker1').datetimepicker({
        format: 'YYYY-MM-DD HH:mm',
        toolbarPlacement: 'top',
        showClear: true,
        minDate: new Date(),
        showClose: true,
        sideBySide: true,
        daysOfWeekDisabled: [0],
        stepping: 30,
    }).on("dp.change", logic);
});

var logic = function(currentDateTime) {
    day = moment(currentDateTime.date).day()
    if ([1, 2, 3, 4, 5].includes(day)) {
        $('#datetimepicker1').data("DateTimePicker").enabledHours([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    } else if (day == 6) {
        $('#datetimepicker1').data("DateTimePicker").enabledHours([8, 9, 10, 11, 12])
    } else {
        $('#datetimepicker1').data("DateTimePicker").enabledHours([])
    }
    $('#datetimepicker1').data("DateTimePicker").daysOfWeekDisabled([0])
};