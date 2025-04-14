/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";

class SaleWidget extends Component {
    static template = "default.SaleWidget"
    
    static components = {
        registry
    }

    setup() {
        console.log("Sale Widget Start...........")
        
    }

    onSubmit() {
        const form = document.getElementById("myForm");
        if (form) {
            form.submit();
        } else {
            console.error("Form with ID 'myForm' not found.");
        }
    }
 
}
console.log("Hello call js Sale !");
SaleWidget.template = "default.SaleWidget";

registry.category("actions").add("default.SaleWidget", SaleWidget);