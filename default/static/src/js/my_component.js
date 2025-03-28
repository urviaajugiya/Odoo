/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";

class MyComponent extends Component {
    setup() {
        this.state = useState({ value: 1 });
    }
    
    increment() {
        this.state.value++;
    }
}
console.log("Hello call js---------------!");
MyComponent.template = "default.MyComponent";

registry.category("actions").add("default.MyComponent", MyComponent);