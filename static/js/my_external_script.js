function bookTable(event){

    if (event.target.getAttribute('fill') == 'green') {

            $('#MyForm').toggle(500);
            $('#tablenumber').attr("value",event.target.id);
            $('#choosendate').attr("value",$('#datepicker').val());
    }

}

