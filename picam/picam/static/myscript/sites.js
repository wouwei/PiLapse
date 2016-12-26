

//functions 
function SetScreenshotSize() {
    Jumbosize = $("#Screenshot").width();
    JumboPadding = parseInt($("#Screenshot").css('padding-right').replace('px','')) + parseInt($("#Screenshot").css('padding-left').replace('px',''));
    console.log($("#Screenshot").css('padding-right'), JumboPadding,Jumbosize);
    $("#Screenshot-image").width(Jumbosize - JumboPadding);

}

SetScreenshotSize();