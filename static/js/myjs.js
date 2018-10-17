
var expanded  = false;
var tile = $('.strips__strip');
var tileLink = $('.strips__strip > .strip__content');
var tileText = tileLink.find('.strip__inner-text');
var stripClose = $('.strip__close');

var setOL = document.getElementById('leftOne');
var setOR = document.getElementById('rightOne');
function Sopacity (){
        setOL.style.opacity = 0.2;
        setOR.style.opacity = 0.2;
       
      setOL.addEventListener('mouseover',function(){
        if(!expanded){
          setOL.style.opacity = 0.7;
          // console.log(expanded);
        }
      })
      setOR.addEventListener('mouseover',function(){
        if(!expanded){
          setOR.style.opacity = 0.7;
          // console.log(expanded);
        }
      })
      setOL.addEventListener('mouseleave',function(){
          if(!expanded){
          setOL.style.opacity = 0.2;    
          }
      })
      setOR.addEventListener('mouseleave',function(){
        if(!expanded){
        setOR.style.opacity = 0.2;    
        }
    })

      
}

var check = false;
function checkFunc(){
  check = true;
}
var Expand = (function() {
  
   expanded  = false;

  var open = function() {
      
    var tile = $(this).parent();

      if (!expanded) {
        tile.addClass('strips__strip--expanded');
        setOL.style.opacity = 1;
        setOR.style.opacity = 1;
        // add delay to inner text
        
        tileText.css('transition', 'all .5s .3s cubic-bezier(0.23, 1, 0.32, 1)');
        stripClose.addClass('strip__close--show');
        stripClose.css('transition', 'all .6s 1s cubic-bezier(0.23, 1, 0.32, 1)');
        expanded = true;
        setTimeout('checkFunc()',100);
      } 
    };
  
  var close = function() {
    if (expanded) {
      tile.removeClass('strips__strip--expanded');
      // remove delay from inner text
      
      tileText.css('transition', 'all 0.15s 0 cubic-bezier(0.23, 1, 0.32, 1)');
      stripClose.removeClass('strip__close--show');
      stripClose.css('transition', 'all 0.2s 0s cubic-bezier(0.23, 1, 0.32, 1)')
      expanded = false;
      check = false;
      Sopacity();
    }
  }

    var bindActions = function() {
      tileLink.on('click', open);
      stripClose.on('click', close);
    };

    var init = function() {
      bindActions();
    };

    return {
      init: init
    };
    
  }());

Expand.init();

window.addEventListener('scroll',function(){
  if (expanded && check==true) {
    tile.removeClass('strips__strip--expanded');
    // remove delay from inner text
    tileText.css('transition', 'all 0.15s 0 cubic-bezier(0.23, 1, 0.32, 1)');
    stripClose.removeClass('strip__close--show');
    stripClose.css('transition', 'all 0.2s 0s cubic-bezier(0.23, 1, 0.32, 1)')
    expanded = false;
    check = false;
    Sopacity();
  }

})
window.onload = function(){
  if (!expanded)
  {
    // console.log(expanded);
     Sopacity();
}
}