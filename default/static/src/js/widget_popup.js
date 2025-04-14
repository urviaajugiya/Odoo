/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";

class Popup extends Component {
    static template = "default.popup"
    
    static components = {
        registry
    }
    setup() {
        console.log("Popup Widget Start...........")
    }
    // constructor(){
    //     super(...arguments);
    //     this.state = useState({
    //         name: '',
    //         email: '',
    //         isVisible: true,
    //     });
    // }
    submitForm(event) {
        event.preventDefault();  // Prevent the default form submission
        console.log('Term & Condition Apply');
        alert('Term & Condition Apply');
        // console.log('Name:', this.state.name);
        // console.log('Email:', this.state.email);
    }
    
    hidePopup(event) {
        event.cancelable;
        // this.trigger('close');  // Triggering the 'close' event to close the popup
        // this.state.isVisible = false;
        alert('Action canceled!');
    }
}

console.log("Hello call js---------------!");
Popup.template = "default.Popup";

registry.category("actions").add("default.Popup", Popup);