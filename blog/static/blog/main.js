
function blog_sum(x, y) {
    jQuery.get('/add/?x=10&y=20').done(function(response) {
        console.log(response);
    });
}
