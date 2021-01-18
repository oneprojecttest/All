$(function(){
	
	$(".gotop a").hover(function(){
		var aa=$(this).hasClass("dh");
		if(aa==true){
			$(this).find("dt").hide().siblings("dd").fadeIn().parents("a").siblings("p").show().animate({left:"-110px"});
		}else{
			$(this).find("dt").hide().siblings("dd").fadeIn().parents("a").siblings("p").hide().animate({left:"-130px"});
		}
	},function(){
		$(this).find("dt").fadeIn().siblings("dd").hide().parents("a").siblings("p").hide();
	});
	
	$(window).scroll(function(){
		var wh=$(window).scrollTop();
		if(wh>100){
			$(".toptop").fadeIn();
		}else{
			$(".toptop").fadeOut();
		}
		$(".toptop").click(function(){
			$(window).scrollTop(0);
		});
	});
	

