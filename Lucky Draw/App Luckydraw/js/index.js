//抽奖人员名单
var allPerson = ["KH:Phạm Văn Hải, SĐT:964133556, Code:Luxury-CG0998 ;KH:Phạm Quang Thịnh, SĐT:1638108075, Code:Luxury-SN0997 ;KH:Phạm Quang Thịnh, SĐT:1638108075, Code:Luxury-FL0996 ;KH:Mầu Văn Giang, SĐT:1663498407, Code:Luxury-TN0995 ;KH:Mầu Văn Giang, SĐT:1663498407, Code:Luxury-YT0994 ;KH:Bùi Thị Ly, SĐT:0123 456 789, Code:Luxury-MK0992 ;KH:Bùi Thị Ly, SĐT:0123 456 789, Code:Luxury-LJ0991 ;KH:Đào Thu Thủy, SĐT:0127 2118 852, Code:Luxury-LF0990 ;KH:Nguyễn Tuyết Nhung, SĐT:0163 142 1525, Code:Luxury-QA0989 ;KH:Nguyễn Tuyết Nhung, SĐT:0163 142 1525, Code:Luxury-QG0988 ;KH:Đào Quỳnh Trang, SĐT:0166 3498 404, Code:Luxury-XK0987 ;KH:Phạm Lan Hương, SĐT:0156 789 1235, Code:Luxury-WZ0986 ;KH:Phạm Lan Hương, SĐT:0156 789 1235, Code:Luxury-UV0985 ;"];
//领导人员名单
var leaderArr = [""];
//未中奖人员名单
var remainPerson = allPerson.toString().split(";");
//中奖人员名单
var luckyMan = [];
var timer;//定时器
var times = 1;//抽奖次数,如果不是第一次，不加粗显示领导姓名
$(function () {
    iconAnimation();
    //开始抽奖
    $("#btnStart").on("click", function () {
        //判断是开始还是结束
        if ($("#btnStart").text() === "Bắt đầu") {
            if (!$("#txtNum").val()) {
                showDialog("Vui lòng nhập số người chiến thắng");
                return false;
            }
            if ($("#txtNum").val() > 49) {
                showDialog("Có thể nhập tối đa 49 người mỗi lần");
                return false;
            }
            if ($("#txtNum").val() > remainPerson.length) {
                showDialog("Số lượng rút thăm hiện tại lớn hơn tổng số giải thưởng<br>số giải thưởng：<b>" + $("#txtNum").val() + "</b>Số lượng rút thăm：<b>" + remainPerson.length + "</b>人");
                return false;
            }
            $("#result").fadeOut();
            //显示动画框，隐藏中奖框
            $("#luckyDrawing").show().next().addClass("hide");
            move();
            $("#btnStart").text("Dừng");
            $("#bgLuckyDrawEnd").removeClass("bg");
        }
        else {
            $("#btnStart").text("Bắt đầu");//设置按钮文本为开始
            var luckyDrawNum = $("#txtNum").val();
            startLuckDraw();//抽奖开始

            $("#luckyDrawing").fadeOut();
            clearInterval(timer);//停止输入框动画展示
            $("#luckyDrawing").val(luckyMan[luckyMan.length - 1]);//输入框显示最后一个中奖名字
            $("#result").fadeIn().find("div").removeClass().addClass("p" + luckyDrawNum);//隐藏输入框，显示中奖框
            $("#bgLuckyDrawEnd").addClass("bg");//添加中奖背景光辉
            $("#txtNum").attr("placeholder", "Nhập số người chiến thắng(" + remainPerson.length + ")");
        }
    });

    $("#btnReset").on("click", function () {
        //确认重置对话框
        var confirmReset = false;
        showConfirm("Xác nhận đặt lại?", function () {
            //熏置未中奖人员名单
            remainPerson = allPerson.toString().split(";");
            //中奖人数框置空
            $("#txtNum").val("").attr("placeholder", "Vui lòng nhập số người chiến thắng");
            $("#showName").val("");
            //隐藏中奖名单,然后显示抽奖框
            $("#result").fadeOut();//.prev().fadeIn()
            $("#bgLuckyDrawEnd").removeClass("bg");//移除背景光辉
            times++;
            console.log(times);

        });
    });
});

//抽奖主程序
function startLuckDraw() {
    //抽奖人数
    var luckyDrawNum = $("#txtNum").val();
    if (luckyDrawNum > remainPerson.length) {
        alert("Số lần rút ra nhiều hơn số lượng giải thưởng!");
        return false;
    }
    //随机中奖人
    var randomPerson = getRandomArrayElements(remainPerson, luckyDrawNum);
    var tempHtml = "";
    $.each(randomPerson, function (i, person) {
        if (leaderArr.indexOf(person) > -1 && times == 1) {
            tempHtml += "<span><b>" + person + "</b></span>";
        }
        else {
            tempHtml += "<span>" + person + "</span>";
        }
    });
    $("#result>div").html(tempHtml);
    //剩余人数剔除已中奖名单
    remainPerson = remainPerson.delete(randomPerson);
    //中奖人员
    luckyMan = luckyMan.concat(randomPerson);
    //设置抽奖人数框数字为空
    $("#txtNum").val("");
}

//参考这篇文章：http://www.html-js.com/article/JS-rookie-rookie-learned-to-fly-in-a-moving-frame-beating-figures
//跳动的数字
function move() {
    var $showName = $("#showName"); //显示内容的input的ID
    var interTime = 30;//设置间隔时间
    timer = setInterval(function () {
        var i = GetRandomNum(0, remainPerson.length);
        $showName.val(remainPerson[i]);//输入框赋值
    }, interTime);
}

//顶上的小图标，随机动画
function iconAnimation() {
    var interTime = 200;//设置间隔时间
    var $icon = $("#iconDiv>span");
    var arrAnimatoin = ["bounce", "flash", "pulse", "rubberBand", "shake", "swing", "wobble", "tada"];
    var timer2 = setInterval(function () {
        var i = GetRandomNum(0, $icon.length);
        var j = GetRandomNum(0, arrAnimatoin.length);
        //console.log("i:" + i + ",j:" + j);
        $($icon[i]).removeClass().stop().addClass("animated " + arrAnimatoin[j]);//输入框赋值
    }, interTime);

}
