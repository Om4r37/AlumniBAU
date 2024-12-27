window.addEventListener('click', (e) => {
	var element = document.querySelector('.toastui-editor-tabs .tab-item[aria-label="URL"]');
	if (element) {
		element.click();
	}
	if(document.querySelector('[aria-label="File"]')) {
		document.querySelector('[aria-label="File"]').style.display = "none"
	}
});