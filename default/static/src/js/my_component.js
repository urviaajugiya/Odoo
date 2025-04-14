/** @odoo-module **/
import { registry } from "@web/core/registry";
import { ActionSwiper } from "@web/core/action_swiper/action_swiper";
import { Component, useState } from "@odoo/owl";
import { CheckBox } from "@web/core/checkbox/checkbox";
import { Dropdown } from "@web/core/dropdown/dropdown";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { Notebook } from "@web/core/notebook/notebook";
import { Pager } from "@web/core/pager/pager";
import { SelectMenu } from "@web/core/select_menu/select_menu";

class MyComponent extends Component {
    static components = {
        ActionSwiper,
        CheckBox,
        Dropdown,
        DropdownItem,
        Notebook,
        Pager,
        SelectMenu
    }
    
    setup() {
        this.pagerProps = this.env.config.pagerProps
            ? useState(this.env.config.pagerProps)
            : undefined;
        this.state = useState({ value: 5 });
        console.log("Component is being set up");
        this.state.message = "Odoo is awesome!";
    }
    // useEffect
    get pages() {
        return [
          {
            Component: MyComponent,
            title: "Page 1",
            props: {
              title: "My First Page",
              text: "This page is not visible",
          },
          },
          {
            Component: MyComponent,
            id: "page_2",
            title: "Page 2",
            props: {
              title: "My second page",
              text: "You're at the right place!",
            },
          },
        ]
      }
    
    changeMessage() {
        this.state.message = "Message Changed!";
    }
    
    increment() {
        this.state.value++;
    }

    onRightSwipe() {
        if (this.swiper) {
            console.log("Swiper exists:", this.swiper);
            this.swiper.slideNext(); 
        } else {
            console.error("Swiper not initialized");
        }
    }

    onLeftSwipe() {
        if (this.swiper) {
            console.log("Swiper exists:", this.swiper);
            this.swiper.slidePrev();
        } else {
            console.error("Swiper not initialized");
        }
    }

    onValueChange(event) {
        this.state.isChecked = event.target.checked; 
        console.log('Checkbox changed to:', this.state.isChecked);
    }

    get choices() {
    return [
        {
          value: "value_1",
          label: "First value"
        }
    ]
  }
  get groups() {
    return [
      {
          label: "Group A",
          choices: [
              {
                value: "value_2",
                label: "Second value"
              },
              {
                value: "value_3",
                label: "Third value"
              }
          ]
      },
      {
          label: "Group B",
          choices: [
              {
                value: "value_4",
                label: "Fourth value"
              }
          ]
      }
    ]
  }
}
console.log("Hello call js---------------!");
MyComponent.template = "default.MyComponent";

registry.category("actions").add("default.MyComponent", MyComponent);