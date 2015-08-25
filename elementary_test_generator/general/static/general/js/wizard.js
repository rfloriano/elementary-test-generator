$(document).ready(function(){
    var VARS_PATTERN = new RegExp('{{(.*)}}');

    $('.step .before').on('click', function(e){
        e.preventDefault();
        var current = $('.wizard .step:visible');
        current.hide();
        var prev = current.prev();
        prev.show();
    });

    $('.step .after').on('click', function(e){
        e.preventDefault();
        var current = $('.wizard .step:visible');
        current.hide();
        var next = current.next();
        next.show();
    });

    $('#id_question_template').on('blur', function(e) {
        var val = $(e.currentTarget).val();
        val = VARS_PATTERN.exec(val)[0];
        var labels = $("label[for='id_question_property'], label[for='id_answer_property']");
        labels.each(function(i, e){
            $(e).text($(e).text().replace('{{ property }}', val));
        });
    });
});
