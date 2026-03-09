$("#upload").click(function() {
    let file = $("#fileInput")[0].files[0]
    let form = new FormData()
    form.append("file", file)

    $.ajax({

        url: "/transactions/upload",
        type: "POST",
        data: form,
        contentType: false,
        processData: false,

        success: function() {
            alert("Upload complete");
            // Redirect user to dashboard.html file
            window.location.href = "dashboard.html";
        }

    })
})
