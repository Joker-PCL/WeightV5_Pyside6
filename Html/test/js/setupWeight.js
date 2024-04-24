class CreateForm {
  constructor(role, containerId, settingLists) {
    this.role = role;
    this.containerId = containerId;
    this.container = document.getElementById(this.containerId);
    this.productLists = settingLists.productLists;
    this.tabletLists = settingLists.tabletLists;
    this.balanceLists = settingLists.balanceLists;
  }

  // ค้นหาข้อมูลการตั้งค่าจากรายชื่อยา
  searchProduct(product) {
    const results = Object.entries(this.productLists).find(
      ([_product, setting]) => {
        return _product.toUpperCase() == product.toUpperCase();
      }
    );

    if (results) {
      const [res_product, res_setting] = results;
      console.log(res_product, res_setting);
      const [formGroup10s, formGroupIpc] = $(this.container).find(
        ".form-group"
      );

      Object.entries(res_setting.weight_control_10s).forEach(([key, value]) => {
        const inputEl = $(formGroup10s).find(
          `.input-group>input[name="${key}"]`
        );
        inputEl.val(value.replace("%", ""));
      });

      Object.entries(res_setting.weight_control_ipc).forEach(([key, value]) => {
        const inputEl = $(formGroupIpc).find(
          `.input-group>input[name="${key}"]`
        );
        inputEl.val(value.replace("%", ""));
      });
    } else {
      $(this.container).find(".form-group").find(".input-group>input").val("");
    }
  }

  // สร้างรายการจากชื่อยา
  createDropdownProductList(element, dataSettings) {
    if (dataSettings) {
      this.productLists = dataSettings;
    }

    let datasource = [];
    Object.entries(this.productLists).forEach(([product, setting]) => {
      datasource.push(product.toUpperCase());
    });

    // สร้าง dropdown lists
    $(element)
      .autocomplete({
        source: datasource,
        autoFocus: false,
        minLength: 0,
        open: function (event, ui) {
          var widget = $(this).autocomplete("widget");
          // widget.attr("id", `${this.containerId}_widget`);
        },
        select: function (event, ui) {
          const value = ui.item.value;
          console.log(value);
          this.searchProduct(value);
        }.bind(this),
      })
      .focus(function () {
        $(this).data("ui-autocomplete").search($(this).val());
      });

    $(element).keyup((event) => {
      this.searchProduct(event.target.value);
    });
  }

  // บันทึกการตั้งค่าน้ำหนักยา
  setupFormOnSubmit() {
    loadingEdit("show");
    setTimeout(function () {
      SwalAlert.fire({
        text: "ตั้งค่าน้ำหนักยาเรียบร้อยแล้ว",
      });
      loadingEdit("hide");
    }, 2500);
  }

  // บันทึกการเพิ่ม, แก้ไขฐานข้อมูลตั้งค่าน้ำหนักยา
  editFormOnSubmit(form) {
    loadingEdit("show");
    setTimeout(function () {
      SwalAlert.fire({
        text: "เพิ่ม, แก้ไขฐานข้อมูลน้ำหนักยาเรียบร้อยแล้ว",
      });
      loadingEdit("hide");
      form.reset();
    }, 2500);
  }

  // สร้าง tag input รับข้อมูล
  createInputOuterBorder({ id, placeholder, type }) {
    const container = document.createElement("div");
    container.classList.add("input-outer-border");

    var input;
    if (type === "select") {
      input = document.createElement("select");
      input.classList.add("form-select");
      input.required = true;
      const options = document.createElement("option");
      options.value = "";
      options.innerText = placeholder;
      // options.selected = true;
      input.appendChild(options);
    } else {
      input = document.createElement("input");
      input.classList.add("form-control");
      input.required = true;
      input.type = "text";
      input.placeholder = placeholder;
    }

    input.name = id;
    container.appendChild(input);
    return container;
  }

  // สร้าง tag input รับข้อมูล
  createInput({ id, type, options, unit }) {
    const container = document.createElement("div");
    container.classList.add("input-group");

    const input = document.createElement("input");
    input.className = "form-control";
    input.type = type;
    input.name = id;
    input.required = true;
    Object.entries(options).forEach(([option, value]) => {
      input.setAttribute(option, value);
    });
    container.appendChild(input);

    const span = document.createElement("span");
    span.className = "input-group-text";
    span.textContent = unit;
    container.appendChild(span);

    return container;
  }

  // สร้าง tag input รับข้อมูล
  createInputGroup({ label, input1, input2 }) {
    const container = document.createElement("div");
    container.className = "input-group-row";
    const _label = document.createElement("a");
    _label.className = "input-group-label";
    _label.textContent = label;

    const input_group = document.createElement("div");
    input_group.className = "group-row";
    const _input1 = this.createInput(input1);
    const _input2 = this.createInput(input2);
    container.appendChild(_label);
    input_group.appendChild(_input1);
    input_group.appendChild(_input2);
    container.appendChild(input_group);
    return container;
  }

  // สร้างฟอร์มการตั้งค่าน้ำหนัก 10 เม็ด
  createForm10s({ formType }) {
    const container = document.createElement("div");
    container.className = "form-main-group";
    const weight10s_main_group = document.createElement("div");
    weight10s_main_group.className = "form-header-group";
    const weight10s_title = document.createElement("p");
    weight10s_title.className = "form-title";
    weight10s_title.textContent = "ตั้งค่าน้ำหนักยา 10 เม็ด";
    weight10s_main_group.appendChild(weight10s_title);

    // หมายเลขเครื่องชั่ง
    if (formType == "setup") {
      const balanceID10s = this.createInputOuterBorder({
        id: "balanceId10s",
        placeholder: "หมายเลขเครื่องชั่ง...",
        type: "select",
      });
      weight10s_main_group.appendChild(balanceID10s);

      const balanceID = $(balanceID10s)[0].firstChild;
      this.balanceLists.forEach((balance) => {
        const options = document.createElement("option");
        options.value = balance;
        options.innerText = balance;
        balanceID.appendChild(options);
      });
    }

    container.appendChild(weight10s_main_group);

    const weight10s_group = document.createElement("div");
    weight10s_group.className = "form-group";

    // น้ำหนักทางทฤษฎี 10 เม็ด
    const meanWeight10s = this.createInputGroup({
      label: "น้ำหนักทางทฤษฎี 10 เม็ด",
      input1: {
        id: "meanWeight10s",
        type: "number",
        unit: "กรัม",
        options: { placeholder: "น้ำหนัก..." },
      },
      input2: {
        id: "percentWeightVariation10s",
        type: "number",
        unit: "%",
        options: { placeholder: "% นน..." },
      },
    });
    weight10s_group.appendChild(meanWeight10s);

    // ช่วงน้ำหนัก 10 เม็ด Min-Max
    const meanWeight10sInhouse = this.createInputGroup({
      label: "ช่วงน้ำหนัก 10 เม็ด Min-Max",
      input1: {
        id: "meanWeight10sMin",
        type: "number",
        unit: "กรัม",
        options: { placeholder: "ต่ำสุด..." },
      },
      input2: {
        id: "meanWeight10sMax",
        type: "number",
        unit: "กรัม",
        options: { placeholder: "สูงสุด..." },
      },
    });
    weight10s_group.appendChild(meanWeight10sInhouse);

    // เกณฑ์การยอมรับทะเบียน Min-Max
    const meanWeightReg10s = this.createInputGroup({
      label: "เกณฑ์การยอมรับทะเบียน Min-Max",
      input1: {
        id: "meanWeightReg10sMin",
        type: "number",
        unit: "กรัม",
        options: { placeholder: "ต่ำสุด..." },
      },
      input2: {
        id: "meanWeightReg10sMax",
        type: "number",
        unit: "กรัม",
        options: { placeholder: "สูงสุด..." },
      },
    });
    weight10s_group.appendChild(meanWeightReg10s);

    // ความหนาของเม็ดยา Min-Max
    const thickness10s = this.createInputGroup({
      label: "ความหนาของเม็ดยา Min-Max",
      input1: {
        id: "thickness10sMin",
        type: "number",
        unit: "mm.",
        options: { placeholder: "ต่ำสุด..." },
      },
      input2: {
        id: "thickness10sMax",
        type: "number",
        unit: "mm.",
        options: { placeholder: "สูงสุด..." },
      },
    });
    weight10s_group.appendChild(thickness10s);

    container.appendChild(weight10s_group);

    return container;
  }

  // สร้างฟอร์มการตั้งค่าน้ำหนัก ipc
  createFormIpc({ formType }) {
    const container = document.createElement("div");
    container.className = "form-main-group";
    const weight10s_main_group = document.createElement("div");
    weight10s_main_group.className = "form-header-group";
    const weight10s_title = document.createElement("p");
    weight10s_title.className = "form-title";
    weight10s_title.textContent = "ตั้งค่าน้ำหนักยา IPC";
    weight10s_main_group.appendChild(weight10s_title);

    // หมายเลขเครื่องชั่ง
    if (formType == "setup") {
      const balanceID10s = this.createInputOuterBorder({
        id: "balanceIdIpc",
        placeholder: "หมายเลขเครื่องชั่ง...",
        type: "select",
      });
      weight10s_main_group.appendChild(balanceID10s);

      const balanceID = $(balanceID10s)[0].firstChild;
      this.balanceLists.forEach((balance) => {
        const options = document.createElement("option");
        options.value = balance;
        options.innerText = balance;
        balanceID.appendChild(options);
      });
    }

    container.appendChild(weight10s_main_group);

    const weightIpc_group = document.createElement("div");
    weightIpc_group.className = "form-group";

    // จำนวนเม็ดที่ต้องชั่ง,จำนวนสาก
    if (formType == "setup") {
      const numberTabletAndPunches = this.createInputGroup({
        label: "จำนวนเม็ดที่ต้องชั่ง,จำนวนสาก",
        input1: {
          id: "numberTablets",
          type: "number",
          unit: "เม็ด",
          options: { placeholder: "จำนวนสาก..." },
        },
        input2: {
          id: "numberPunches",
          type: "number",
          unit: "สาก",
          options: { placeholder: "จำนวนสาก..." },
        },
      });
      weightIpc_group.appendChild(numberTabletAndPunches);
    }

    // น้ำหนักตอก/เม็ด
    const meanWeightIpcInhouse = this.createInputGroup({
      label: "น้ำหนักตอก/เม็ด",
      input1: {
        id: "meanWeightIpc",
        type: "number",
        unit: "กรัม",
        options: { placeholder: "น้ำหนัก..." },
      },
      input2: {
        id: "percentWeightIpc",
        type: "number",
        unit: "%",
        options: { placeholder: "% นน." },
      },
    });
    weightIpc_group.appendChild(meanWeightIpcInhouse);
    
    // ค่าน้ำหนักเฉลี่ยที่ยอมรับ Min-Max
    const meanWeightAverageIpc = this.createInputGroup({
      label: "ค่าน้ำหนักเฉลี่ยที่ยอมรับ Min-Max",
      input1: {
        id: "meanWeightAverageIpcMin",
        type: "number",
        unit: "กรัม",
        options: { placeholder: "ต่ำสุด..." },
      },
      input2: {
        id: "meanWeightAverageIpcMax",
        type: "number",
        unit: "กรัม",
        options: { placeholder: "สูงสุด." },
      },
    });
    weightIpc_group.appendChild(meanWeightAverageIpc);

    // ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ Min-Max
    const meanWeightVariationIpc = this.createInputGroup({
      label: "ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ Min-Max",
      input1: {
        id: "meanWeightVariationIpcMin",
        type: "number",
        unit: "mm.",
        options: { placeholder: "ต่ำสุด..." },
      },
      input2: {
        id: "meanWeightVariationIpcMax",
        type: "number",
        unit: "mm.",
        options: { placeholder: "สูงสุด." },
      },
    });
    weightIpc_group.appendChild(meanWeightVariationIpc);

    // เกณฑ์การยอมรับทะเบียน Min-Max
    const meanWeightRegIpc = this.createInputGroup({
      label: "เกณฑ์การยอมรับทะเบียน Min-Max",
      input1: {
        id: "meanWeightRegIpcMin",
        type: "number",
        unit: "mm.",
        options: { placeholder: "ต่ำสุด..." },
      },
      input2: {
        id: "meanWeightRegIpcMax",
        type: "number",
        unit: "mm.",
        options: { placeholder: "สูงสุด." },
      },
    });
    weightIpc_group.appendChild(meanWeightRegIpc);

    container.appendChild(weightIpc_group);

    return container;
  }

  // สร้างฟอร์มการตั้งค่าน้ำหนักยาของเครื่องตอก
  createSetupForm() {
    const form = document.createElement("form");
    const search_group = document.createElement("div");
    search_group.classList.add("form-search-group");

    // รายชื่อยา
    const productName = this.createInputOuterBorder({
      id: "productName",
      placeholder: "พิมพ์ชื่อยา...",
      type: "input",
    });
    search_group.appendChild(productName);

    // เลขที่ผลิต
    const lot = this.createInputOuterBorder({
      id: "lot",
      placeholder: "เลขที่ผลิต...",
      type: "input",
    });
    search_group.appendChild(lot);

    // หมายเลขเครื่องตอก
    const tabletID = this.createInputOuterBorder({
      id: "tabletID",
      placeholder: "เครื่องตอก...",
      type: "select",
    });

    // เพิ่มรายชื่อเครื่องตอกจากข้อมูลในระบบ
    const tabletID_El = $(tabletID)[0].firstChild;
    Object.keys(this.tabletLists).forEach((tablet) => {
      const options = document.createElement("option");
      options.value = tablet;
      options.innerText = `เครื่องตอก ${tablet}`;
      tabletID_El.appendChild(options);
    });

    search_group.appendChild(tabletID);
    form.appendChild(search_group);

    const weight10sForm = this.createForm10s({ formType: "setup" });
    const weightIpcForm = this.createFormIpc({ formType: "setup" });
    form.appendChild(weight10sForm);
    form.appendChild(document.createElement("hr"));
    form.appendChild(weightIpcForm);

    const containerSubmitForm = document.createElement("div");
    containerSubmitForm.className = "form-submit-group";
    const submitForm = document.createElement("button");
    submitForm.className = "btn btn-success";
    submitForm.type = "submit";
    submitForm.textContent = "บันทึกข้อมูล";
    containerSubmitForm.appendChild(submitForm);

    const resetForm = document.createElement("button");
    resetForm.className = "btn btn-danger";
    resetForm.type = "reset";
    resetForm.textContent = "ยกเลิก";
    containerSubmitForm.appendChild(resetForm);
    form.appendChild(containerSubmitForm);
    this.container.appendChild(form);

    $(form).submit((event) => {
      event.preventDefault();
      this.setupFormOnSubmit(form);
    });

    this.searchProductsEl = $(productName)[0].firstChild;
    this.createDropdownProductList(this.searchProductsEl);
  }
  
  // สร้างฟอร์มแก้ไขฐานข้อมูลน้ำหนักยา
  createEditForm() {
    const form = document.createElement("form");
    const search_group = document.createElement("div");
    search_group.classList.add("form-search-group");

    // รายชื่อยา
    const productName = this.createInputOuterBorder({
      id: "productName",
      placeholder: "พิมพ์ชื่อยา...",
      type: "input",
    });
    search_group.appendChild(productName);
    form.appendChild(search_group);

    const weight10sForm = this.createForm10s({ formType: "edit" });
    const weightIpcForm = this.createFormIpc({ formType: "edit" });
    form.appendChild(weight10sForm);
    form.appendChild(document.createElement("hr"));
    form.appendChild(weightIpcForm);

    const containerSubmitForm = document.createElement("div");
    containerSubmitForm.className = "form-submit-group";
    const submitForm = document.createElement("button");
    submitForm.className = "btn btn-success";
    submitForm.type = "submit";
    submitForm.textContent = "บันทึกข้อมูล";
    containerSubmitForm.appendChild(submitForm);

    const resetForm = document.createElement("button");
    resetForm.className = "btn btn-danger";
    resetForm.type = "reset";
    resetForm.textContent = "ยกเลิก";
    containerSubmitForm.appendChild(resetForm);
    form.appendChild(containerSubmitForm);
    this.container.appendChild(form);

    $(form).submit((event) => {
      event.preventDefault();
      this.editFormOnSubmit(form);
    });

    this.searchProductsEl = $(productName)[0].firstChild;
    this.createDropdownProductList(this.searchProductsEl);
  }
}
