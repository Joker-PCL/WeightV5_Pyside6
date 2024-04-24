// จัดเรียงข้อมูล DataTable ตามวันที่มากไปน้อย
$(document).ready(function () {
  DataTable.datetime("DD/MM/YYYY, HH:mm:ss");
});

// สร้างรายการเมนู Sidebar parameters(สิทธิ์การใช้งาน)
class CreateSidebarMenu {
  constructor(role) {
    this.role = role;
    this.lists = document.createElement("ul");
    this.lists.classList.add("navbar-nav");
    this.createMenu();
  }

  createMenu() {
    const page1_menu = document.createElement("li");
    page1_menu.setAttribute("data-toggle", "home_page");
    page1_menu.classList.add("nav-item", "page-menu");
    const page1_title = document.createElement("a");
    page1_title.classList.add("nav-link");
    page1_title.textContent = "หน้าหลัก";
    page1_menu.appendChild(page1_title);

    const page2_menu = document.createElement("li");
    page2_menu.setAttribute("data-toggle", "weight_10s_page");
    page2_menu.classList.add("nav-item", "page-menu");
    const page2_title = document.createElement("a");
    page2_title.classList.add("nav-link");
    page2_title.textContent = "ตารางข้อมูลน้ำหนักยา 10 เม็ด";
    page2_menu.appendChild(page2_title);

    const page3_menu = document.createElement("li");
    page3_menu.setAttribute("data-toggle", "weight_ipc_page");
    page3_menu.classList.add("nav-item", "page-menu");
    const page3_title = document.createElement("a");
    page3_title.classList.add("nav-link");
    page3_title.textContent = "ตารางข้อมูลน้ำหนักยา IPC";
    page3_menu.appendChild(page3_title);

    const page4_menu = document.createElement("li");
    page4_menu.setAttribute("data-toggle", "weighing_setup_page");
    page4_menu.classList.add("nav-item", "page-menu");
    const page4_title = document.createElement("a");
    page4_title.classList.add("nav-link");
    page4_title.textContent = "ตั้งค่าน้ำหนักยาของเครื่องตอก";
    page4_menu.appendChild(page4_title);

    const page5_menu = document.createElement("li");
    page5_menu.setAttribute("data-toggle", "weighing_database_page");
    page5_menu.classList.add("nav-item", "page-menu");
    const page5_title = document.createElement("a");
    page5_title.classList.add("nav-link");
    page5_title.textContent = "แก้ไขฐานข้อมูลน้ำหนักยา";
    page5_menu.appendChild(page5_title);

    const page6_menu = document.createElement("li");
    page6_menu.setAttribute("data-toggle", "user_database_page");
    page6_menu.classList.add("nav-item", "page-menu");
    const page6_title = document.createElement("a");
    page6_title.classList.add("nav-link");
    page6_title.textContent = "แก้ไขรายชื่อผู้ปฏิบัติงาน";
    page6_menu.appendChild(page6_title);

    const page7_menu = document.createElement("li");
    page7_menu.setAttribute("data-toggle", "data_logging_page");
    page7_menu.classList.add("nav-item", "page-menu");
    const page7_title = document.createElement("a");
    page7_title.classList.add("nav-link");
    page7_title.textContent = "บันทึกการปฏิบัติงาน";
    page7_menu.appendChild(page7_title);

    const pages_menu = [
      page1_menu,
      page2_menu,
      page3_menu,
      page4_menu,
      page5_menu,
      page6_menu,
      page7_menu,
    ];

    switch (this.role) {
      case "Admin":
        break;
      case "Superuser":
        pages_menu.splice(4);
        break;
      case "Operator":
        pages_menu.splice(3);
        break;
      case "Inspector":
        pages_menu.splice(3);
        pages_menu.push(page7_menu);
        break;
      default:
        pages_menu.splice(1);
        break;
    }

    pages_menu.forEach((page) => {
      this.lists.appendChild(page);
    });
  }
}

// สร้าง dropdown lists จากรายการผลิตทั้งหมด parameters(ไอดี element)
class CreateViewWeighingMenu {
  constructor(id) {
    this.id = id;
    this.container = document.createElement("div");
    this.container.id = id;
    this.container.classList.add("weighing-lists");
    this.createMenu();
  }

  createMenu() {
    const container_group = document.createElement("div");
    container_group.classList.add("input-group", "justify-content-center");

    // Method
    this.input = document.createElement("input");
    this.input.classList.add("form-control", "view-menu-input");
    this.input.type = "text";
    this.input.placeholder = "กรอกข้อมูล...";
    this.input.autocomplete = "off";
    container_group.appendChild(this.input);

    const clear_btn = document.createElement("button");
    clear_btn.type = "button";
    clear_btn.classList.add("view-menu-clear", "btn", "btn-danger");
    container_group.appendChild(clear_btn);

    const openFile = document.createElement("button");
    openFile.type = "button";
    openFile.classList.add("view-menu-file", "btn", "btn-success");
    openFile.textContent = "PDF";
    container_group.appendChild(openFile);

    this.container.appendChild(container_group);

    $(clear_btn).on(
      "click",
      function () {
        this.input.value = "";
      }.bind(this)
    );
  }
}

// สร้างแม่แบบตาราง
class CreateTable {
  constructor(id) {
    this.table = document.createElement("table");
    this.table.id = id; // Set table id
    this.table.style.width = "100%";
    // this.table.classList.add('cell-border');
  }
}

// สร้างแม่แบบฟอร์มบันทึก remarks
class FormRemarksModal {
  constructor(id) {
    this.body = document.body;
    this.id = id;
    this.modal = document.createElement("div");
    this.modal.id = id;
    this.modal.classList.add("remarks-modal", "modal", "fade");
    this.modal.setAttribute("tabindex", "-1");
    this.modal.setAttribute("data-bs-backdrop", "static");
    this.modal.setAttribute("aria-hidden", "true");

    this.modalDialog = document.createElement("div");
    this.modalDialog.classList.add("modal-dialog", "modal-dialog-centered");

    this.modalContent = document.createElement("div");
    this.modalContent.classList.add("modal-content");
    this.modal.appendChild(this.modalDialog);

    this.title = document.createElement("p");
    this.title.classList.add("modal-title");
    this.title.textContent = "Remarks";
    this.modalContent.appendChild(this.title);
    this.modalDialog.appendChild(this.modalContent);
    this.form = document.createElement("form");

    this.body.appendChild(this.modal);

    this.modal = new bootstrap.Modal(document.getElementById(id));
  }

  createInput({ label, tagName, options }) {
    const container = document.createElement("div");
    this.label = document.createElement("label");
    this.label.textContent = label;
    container.appendChild(this.label);

    this.input = document.createElement(tagName);
    this.input.classList.add("form-control");

    Object.entries(options).forEach(([option, value]) => {
      this.input[option] = value;
    });

    container.appendChild(this.input);

    return container;
  }

  createForm({ rowIndex = undefined, dataRow = [] } = {}) {
    var timestamp = "",
      issues = "",
      cause = "",
      resolves = "",
      notes = "";
    if (dataRow.length > 0) {
      [timestamp, issues, cause, resolves, notes] = dataRow;
    }

    this.form.innerHTML = "";
    this.rowIndex = document.createElement("input");
    this.rowIndex.type = "hidden";
    this.rowIndex.name = "rowIndex";
    this.rowIndex.value = rowIndex != undefined ? rowIndex : "";
    this.form.appendChild(this.rowIndex);

    this.timestamp = this.createInput({
      label: "วันที่, เวลา",
      tagName: "input",
      options: {
        placeholder: "วัน/เดือน/ปี, เวลา",
        name: "timestamp",
        readOnly: true,
        required: true,
        value:
          timestamp ||
          new Date().toLocaleString("en-GB", {
            timeZone: "Asia/Jakarta",
          }),
      },
    });
    this.form.appendChild(this.timestamp);

    this.issues = this.createInput({
      label: "ปัญหาที่พบ",
      tagName: "textarea",
      options: {
        value: issues || "",
        placeholder: "ระบุปัญหาที่พบ...",
        name: "issues",
        rows: "10",
        readOnly: issues.indexOf("[แจ้งเตือนจากระบบ]") == -1 ? false : true,
        required: true,
      },
    });
    this.form.appendChild(this.issues);

    this.cause = this.createInput({
      label: "สาเหตุ",
      tagName: "textarea",
      options: {
        value: cause || "",
        placeholder: "ระบุสาเหตุที่เกิด...",
        name: "cause",
        rows: "5",
        required: true,
      },
    });
    this.form.appendChild(this.cause);

    this.resolves = this.createInput({
      label: "การแก้ไข",
      tagName: "textarea",
      options: {
        value: resolves || "",
        placeholder: "ระบุการแก้ไข...",
        name: "resolves",
        rows: "5",
        required: true,
      },
    });
    this.form.appendChild(this.resolves);

    this.notes = this.createInput({
      label: "หมายเหตุ",
      tagName: "textarea",
      options: {
        value: notes || "",
        placeholder: "หมายเหตุ...",
        name: "notes",
        rows: "5",
      },
    });
    this.form.appendChild(this.notes);

    const containerSubmitForm = document.createElement("div");
    containerSubmitForm.className = "form-submit-group";
    this.submitForm = document.createElement("button");
    this.submitForm.className = "btn btn-success";
    this.submitForm.type = "submit";
    this.submitForm.textContent = "บันทึกข้อมูล";
    containerSubmitForm.appendChild(this.submitForm);

    this.resetForm = document.createElement("button");
    this.resetForm.className = "btn btn-danger";
    this.resetForm.type = "reset";
    this.resetForm.textContent = "ยกเลิก";
    containerSubmitForm.appendChild(this.resetForm);
    $(this.resetForm).click(() => {
      this.modal.hide();
    });
    this.form.appendChild(containerSubmitForm);

    this.modalContent.appendChild(this.form);
    this.modal.show();
  }
}
