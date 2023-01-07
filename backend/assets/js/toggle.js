$(function(){

  let scrollPosition;
  $('#toggle').click(function(){

      if ($(this).hasClass('open')){
        scrollPosition = $(window).scrollTop();

        //ハンバーガーボタンの切り替え
        $(this).addClass('close');
        $(this).removeClass('open');

        //グローバルメニューの表示
        $('#global-menu').addClass('show')

        /*ウィンドウの高さを取得してグローバルメニュー、nav-barに適用*/
        let h = $(window).height();
        $('.global-menu').height(h);

        //bodyの高さをスクロール位置で固定
        $('body').addClass('fixed').css({'top': -scrollPosition});
      }else{
        //ハンバーガーボタンの切り替え
        $(this).addClass('open');
        $(this).removeClass('close');

        //グローバルメニューの非表示
        $('#global-menu').removeClass('show')

        $('body').removeClass('fixed').css({'top': 0});
		    window.scrollTo( 0 , scrollPosition );
      }
  });
});
