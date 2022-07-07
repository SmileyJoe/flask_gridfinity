var stl_viewer = null;

document.addEventListener("DOMContentLoaded", function(event) {
    stl_viewer=new StlViewer(
            document.getElementById("stl-container"),
            {models:[]}
        );
});

function load(path, name) {
    stl_viewer.clean()
    stl_viewer.add_model({id:1, filename:path})
    document.getElementsByClassName("dropdown-action")[0].innerHTML = name

    var download = document.getElementsByClassName("download")[0]
    download.href = path
    download.style.display = "block"
}