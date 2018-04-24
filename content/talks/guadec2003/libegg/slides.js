function open_presentation(uri) {
    window.open(uri, 'presentation',
		'location=no,menubar=no,toolbar=no,' +
		'directories=no,status=no,scrollbars=yes');
    return false;
}

var last_window_height = -1;
function resize_handler() {
    /* if window height hasn't changed, do nothing */
    if (window.innerHeight == last_window_height) {
	return;
    }
    last_window_height = window.innerHeight;

    /* replace style rules */
    var screen_style_el = document.getElementById('screen-style');
    if (!screen_style_el) return;

    /* create a text node with font size related to window size */
    var fontsize = window.innerHeight / 30;
    var textnode = document.createTextNode('html, body { font-size: ' + fontsize + 'px; }');

    screen_style_el.replaceChild(textnode,
				 screen_style_el.firstChild);
}
window.onresize = resize_handler;
resize_handler();

function keypress_handler(e) {
    if (e.charCode == e.DOM_VK_SPACE) {
	var link_els = document.getElementsByTagName('link');
	for (var i = link_els.length-1; i >= 0; i--) {
            var el = link_els[i];

            if (el.getAttribute('rel') == 'next') {
		window.location.href = el.getAttribute('href');
		e.preventDefault();
		break;
            }
	}
    }
}
document.addEventListener("keypress", keypress_handler, false);
