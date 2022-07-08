function tag_clicked(tag, tags_current){
    var checkbox = document.getElementById(tag)
    var tags = []

    // if there are tags, turn them into an array
    if(tags_current){
        tags = tags_current.split(',')
    }

    if(checkbox.checked){
        // if the box is checked, add the tag
        tags.push(tag)
    } else {
        // if the box is not checked, we need to remove the tag
        // get the index
        var tag_index = tags.indexOf(tag)
        if( tag_index > -1){
            // if the index exists, remove it and update the list to remoce holes
            tags.splice(tag_index, 1)
        }
    }

    if(tags.length > 0){
        // if there are tags, turn them into a csv and load the page
        window.location.href = '/?tags='+tags.join(',');
    } else {
        // if there are no tags, just load the page showing everything
        window.location.href = '/';
    }
}