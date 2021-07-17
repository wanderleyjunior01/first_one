// // Ajax do form 
// function ajax_request(){
//     let xmlhttp = new XMLHttpRequest();
//     xmlhttp.onreadystatechange = function(){
//         if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
//             var att_list = document.getElementsByClassName("table");
//             att_list.innerHTML = xmlhttp.responseText;
//         }
//     }
//     xmlhttp.open("GET", "att_list", true);
//     ajax.reload
//     xmlhttp.send();
// }

// Ajax add data
if(document.querySelector(".form2")){
    let form = document.querySelector(".form2");
    function sendForm(event)
    {
        event.preventDefault();
        let data = new FormData(form);
        let ajax = new XMLHttpRequest();
        let token = document.querySelectorAll("input")[0].value
        ajax.open("POST", form.action);
        ajax.setRequestHeader("X-CSRFToken", token)
        ajax.onreadystatechange = function()
        {
            if(ajax.status === 200 && ajax.readyState === 4){
            }
        }
        ajax.send(data);
        form.reset();

    }
    form.addEventListener("submit",sendForm,false)
};


// Ajax delete data
$(document).on("click", ".btnDel", function(){
    $(this).parents("tr").remove();
    var id = $(this).attr("id");
    var string = id;
    $.post("delete", {string: string})
    });

// Ajax autoreload page when add new student
$(document).ready(function() {
    function RefreshTable() {
        $(".table").load(location.href + " .table");
    }
    $("#submit").on("click", RefreshTable);
});

//Open modal with data as values by id



// QUery modal
$(document).on("click", ".btnEdit", function ()
{   
    let student_data = {}
    student_data["id"] = $(this).attr("id");
    student_data["name"] = $(this).attr("name");
    student_data["subject"] = $(this).attr("subject");
    student_data["fee"] = $(this).attr("fee");
    console.log(student_data)

    $(".modal-body #modalForm-name").val( student_data["name"] );
    $(".modal-body #modalForm-subject-selected").html( student_data["subject"] );
    $(".modal-body #modalForm-fee").val( student_data["fee"] );
    $(".modal-footer").attr('id', student_data["id"]);
});

// Ajax edit form
$(document).on("click", ".d-flex", function()
{   
    let id = $(this).attr("id")
    let name = $("#modalForm-name").val()
    let subject = $("#modalForm-subject").val()
    let fee = $("#modalForm-fee").val()
    $.post("edit", {id:id, name:name, subject:subject, fee:fee})
}
);

$(document).ready(function() {
    function RefreshTableByModal() {
        $(".table").load(location.href + " .table");
    }
    $("#btnUpdate").on("click", RefreshTableByModal);
});
