$('#login-button').click(function (event) {
    let userName = document.getElementById("userName").value;
    let pwd = document.getElementById("pwd").value;
    if (userName == "孙思佳" && pwd == "happybirthday") {
        $('#h').text("生日快乐");
        event.preventDefault();
        $('form').fadeOut(500);
        $('.wrapper').addClass('form-success');
        setTimeout(function () {
            location.href = "BirthdayCake.html";
        }, 4000);
    } else {
        alert("用户名或密码不正确！,我不会告诉你用户是:孙思佳，密码是:happybirthday");
    }
});
