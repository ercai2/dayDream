setInterval("leftTimer(2019,12,22,9,00,00)",1000);

function leftTimer(year,month,day,hour,minute,second){
  var leftTime = (new Date(year,month-1,day,hour,minute,second)) - (new Date()); // 计算剩余的毫秒数
  var days = parseInt(leftTime / 1000 / 60 / 60 / 24 , 10);                      // 计算剩余的天数
  var hours = parseInt(leftTime / 1000 / 60 / 60 % 24 , 10);                     // 计算剩余的小时
  var minutes = parseInt(leftTime / 1000 / 60 % 60, 10);                         // 计算剩余的分钟
  var seconds = parseInt(leftTime / 1000 % 60, 10);                              // 计算剩余的秒数

  hours = checkTime(hours);
  minutes = checkTime(minutes);
  seconds = checkTime(seconds);

  document.getElementById("timer").innerHTML = days+" 天 " + hours+" 小时 " + minutes+" 分 "+seconds+" 秒 ";
  document.getElementById("loadingDiv").style.display="none";
}

function checkTime(i){
 if(i<10)
 {
  i = "0" + i;
 }
 return i;
}
