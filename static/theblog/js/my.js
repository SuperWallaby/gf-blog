function changeImg(base) {
    var val = $("input[name=face]:checked").val()
    $('.comment_img_viewer--change').attr('src', base + val + ".png");
}