/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";
import { Notebook } from "@web/core/notebook/notebook";
import { Pager } from "@web/core/pager/pager";
import { useService } from "@web/core/utils/hooks";

class NotebookPage extends Component {
    static template = "default.NotebookPage"
    
    static components = {
        registry,
        Notebook,
        Pager
    }

    setup() {
        this.orm = useService("orm");
        console.log("JS Notebook Page is running..............")
        this.state = useState({ allServices: [] });
        this.rpc = useService("rpc");

        this.handleclickevent();
    }

    // async handleclickevent() {
    //     console.log("fetchSevices");
    //     const allSevices = new Promise(async (resolve) => {
    //         const result = await this.orm.call('add.services', 'get_services');
    //         resolve(result); 
    //         }
    //     );
        
    //     console.log(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,allSevices", allSevices);
    //     this.state.allSevices = allSevices;
    // } 

    async handleclickevent() {
        console.log("fetchServices");
    
        const allServices = await this.rpc("/default/models/add.services/get_services",{
            model: 'add.services',
            method: 'get_services',
            args: []
        })
    
        console.log("All Services:", allServices);
        this.state.allSevices = allServices;
    }
    
}
console.log("Hello call js Page !");
NotebookPage.template = "default.NotebookPage";

registry.category("actions").add("default.NotebookPage", NotebookPage);