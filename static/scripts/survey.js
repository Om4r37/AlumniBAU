function employment(){
    var select = document.getElementById("does_work");
    var value = select.options[select.selectedIndex].value;
    var field_names = ["sector", "place", "address", "date", "title", "phone"];
    var reason_field = document.getElementsByName("reason")[0];
    var reason_label = document.getElementsByTagName("label")[12];
    if (value == 0){
        reason_label.style.display = "none";
        reason_field.style.display = "none";
        reason_label.required = false;
        reason_field.required = false;
        for (var i = 0; i < field_names.length; i++){
            var field = document.getElementsByName(field_names[i])[0];
            field.style.display = "none";
            field.required = false;
            document.getElementsByTagName("label")[13 + i].style.display = "none";
        }
    } else if (value == 1){
        reason_label.style.display = "none";
        reason_field.style.display = "none";
        reason_label.required = false;
        reason_field.required = false;
        for (var i = 0; i < field_names.length; i++){
            var field = document.getElementsByName(field_names[i])[0];
            field.style.display = "block";
            field.required = true;
            document.getElementsByTagName("label")[13 + i].style.display = "block";
        }
    } else if (value == 2){
        reason_label.style.display = "block";
        reason_field.style.display = "block";
        reason_label.required = true;
        reason_field.required = true;
        for (var i = 0; i < field_names.length; i++){
            var field = document.getElementsByName(field_names[i])[0];
            field.style.display = "none";
            field.required = false;
            document.getElementsByTagName("label")[13 + i].style.display = "none";
        }
    }
}
employment();

class Accordion {
    constructor(el) {
        this.el = el;
        this.summary = el.querySelector('summary');
        this.content = el.querySelector('form');
        this.animation = null;
        this.isClosing = false;
        this.isExpanding = false;
        this.summary.addEventListener('click', (e) => this.onClick(e));
    }
    onClick(e) {
        e.preventDefault();
        this.el.style.overflow = 'hidden';
        if (this.isClosing || !this.el.open) {
            this.open();
        } else if (this.isExpanding || this.el.open) {
            this.shrink();
        }
    }
    shrink() {
        this.isClosing = true;
        const startHeight = `${this.el.offsetHeight}px`;
        const endHeight = `${this.summary.offsetHeight}px`;
        if (this.animation) {
            this.animation.cancel();
        }
        this.animation = this.el.animate({
            height: [startHeight, endHeight]
        }, {
            duration: 300,
            easing: 'ease-out'
        });
        this.animation.onfinish = () => this.onAnimationFinish(false);
        this.animation.oncancel = () => this.isClosing = false;
    }
    open() {
        this.el.style.height = `${this.el.offsetHeight}px`;
        this.el.open = true;
        window.requestAnimationFrame(() => this.expand());
    }
    expand() {
        this.isExpanding = true;
        const startHeight = `${this.el.offsetHeight}px`;
        const endHeight = `${this.summary.offsetHeight + this.content.offsetHeight}px`;
        if (this.animation) {
            this.animation.cancel();
        }
        this.animation = this.el.animate({
            height: [startHeight, endHeight]
        }, {
            duration: 300,
            easing: 'ease-out'
        });
        this.animation.onfinish = () => this.onAnimationFinish(true);
        this.animation.oncancel = () => this.isExpanding = false;
    }
    onAnimationFinish(open) {
        this.el.open = open;
        this.animation = null;
        this.isClosing = false;
        this.isExpanding = false;
        this.el.style.height = this.el.style.overflow = '';
    }
}
document.querySelectorAll('details').forEach((el) => {
    new Accordion(el);
});