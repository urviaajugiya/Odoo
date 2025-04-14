// /** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState} from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class TermCondition extends Component {
    static template = "default.TermCondition"
    
    static components = {
        registry,
    }

    setup() {
        this.orm = useService("orm");
        console.log("Term Condition Start...........")  
        this.state = useState({
            allTerm: [],  
        });

        // this.fetchAllTerm();
        this.handleclickevent();
    }
    
    // async fetchAllTerm() {
    //     console.log("fetchAllTerm")
    //     const allTerm = await this.orm.call("term.condition", "get_term");
    //     console.log("::::::::::::::::::::::::::::::allTerm",allTerm)
    //     this.state.allTerm = allTerm; 
    // }

    // handleclickevent(){
    //     console.log("fetchAllTerm")
    //     const allTerm = this.orm.call('term.condition', 'get_term');
    //     console.log("::::::::::::::::::::::::::::::allTerm",allTerm)
    //     this.state.allTerm = allTerm; 
    // }
    
    async handleclickevent() {
        console.log("fetchAllTerm");
        const allTerm = new Promise(async (resolve) => {
                const result = await this.orm.call('term.condition', 'get_term');
                resolve(result); 
            }
        );

        console.log("::::::::::::::::::::::::::::::allTerm", allTerm);
        this.state.allTerm = allTerm;
        } 
    }

console.log("Term Condition---------------!");
TermCondition.template = "default.TermCondition";

registry.category("actions").add("default.TermCondition", TermCondition);