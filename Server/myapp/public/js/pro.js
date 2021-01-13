$(function(){
	$(".proList li").on('mouseenter',function(){
		var html="";
		
		$(this).css('border','1px solid #000').append(html);
		$(".quick").on('click',function(){
			$(".mask").show();
			$(".proDets").show();
		});
		$(".btns .cart").click(function(){
			if($(".categ p").hasClass("on")){
				$(".proDets").hide();
				$(".mask").hide();
			}
		});
	});
	$(".proList li").on('mouseleave',function(){
		$(this).find("p").remove();
		$(this).css('border','1px solid #fff');
	});

	$(".next").click(function(){
		$(".two").show();
		$(".one").hide();
		$(".forCon ul li").eq(1).addClass("on").siblings("li").removeClass("on");
	});
})
