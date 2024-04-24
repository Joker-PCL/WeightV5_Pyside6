// สร้างหน้าข้อมูลการชั่งน้ำหนัก ipc
class WeighingIpc {
  constructor(role, containerId, options) {
    this.role = role;
    this.main_container = document.getElementById(containerId);
    this.container = document.createElement("main");
    this.setupTable = options.setupTable;

    this.remarksTableId = options.remarks.id;
    this.remarksTitle = options.remarks.title;
    this.remarksHeaders = options.remarks.headers;

    this.listsMenu = new CreateViewWeighingMenu("weighingIpcList");
    this.viewWeighingMenu = this.listsMenu.container;
    this.listsMenuInput = this.listsMenu.input;
    this.main_container.appendChild(this.viewWeighingMenu);

    // สร้างรายการ autocomplete รายการผลิต 10 เม็ด
    const dataList = [
      "เครื่องตอก T11 (LOT. ปัจจุบัน)",
      "เครื่องตอก T17 (LOT. ปัจจุบัน)",
      "40474_DOMPERDONE_T17_IPC_29/03/2024",
      "40473_DOMPERDONE_T17_IPC_26/03/2024",
    ];

    $(this.listsMenuInput)
      .autocomplete({
        source: dataList,
        autoFocus: false,
        minLength: 0,
        open: function (event, ui) {
          var widget = $(this).autocomplete("widget");
          widget.attr("id", `${containerId}_widget`);
        },
        select: function (event, ui) {
          const value = ui.item.value;
          console.log(value);
          this.loadWeighingData(datatest);
        }.bind(this),
      })
      .focus(function () {
        $(this).data("ui-autocomplete").search($(this).val());
      });

    // สร้างฟอร์มสำหรับบันทึกข้อมูล Remarks
    if (
      this.role === role_definition.Admin ||
      this.role === role_definition.Superuser
    ) {
      $(document).ready(
        function () {
          this.formRemarks = new FormRemarksModal(`${this.containerId}_form`);
        }.bind(this)
      );
    }
  }

  // โหลดข้อมูลการชั่งน้ำหนัก
  loadWeighingData() {
    loadingPage("show");

    setTimeout(
      function () {
        loadingPage("hide");
        SwalMiniAlert.fire({ title: "อัพเดทข้อมูลเรียบร้อยแล้ว" });

        this.render(datatestIpc);
      }.bind(this),
      2500
    );
  }

  // จบการผลิต
  endOfProduction() {
    loadingEdit("show");
    setTimeout(
      function () {
        loadingEdit("hide");
        SwalAlert.fire({
          text: "จัดเก็บเอกสารการผลิตเรียบร้อยแล้ว",
        }).then(this.loadWeighingData.bind(this));
      }.bind(this),
      2500
    );
  }

  // ลงชื่อตรวจสอบการตั้งค่า
  signInToCheckTheSettings() {
    loadingEdit("show");
    setTimeout(
      function () {
        loadingEdit("hide");
        SwalAlert.fire({
          text: "ลงชื่อตรวจสอบการตั้งค่าเรียบร้อยแล้ว",
        }).then(this.loadWeighingData.bind(this));
      }.bind(this),
      2500
    );
  }

  // บันทึกข้อมูล Remarks
  onSubmitFormRemarks(form) {
    loadingEdit("show");

    setTimeout(
      function () {
        loadingEdit("hide");
        SwalMiniAlert.fire({ title: "อัพเดทข้อมูลเรียบร้อยแล้ว" });
        this.formRemarks.modal.hide();

        const formData = form.elements;
        const dataRow = [
          formData.timestamp.value,
          formData.issues.value,
          formData.cause.value,
          formData.resolves.value,
          formData.notes.value,
          "จักรทิพย์",
          "Admin",
        ];
        var node;
        if (formData.rowIndex.value) {
          node = this.remarksTable
            .row(formData.rowIndex.value)
            .data(dataRow)
            .draw(false)
            .node();
        } else {
          node = this.remarksTable.row.add(dataRow).draw().node();
        }

        $(node).hide();
        $(node).fadeIn(1500);
        form.reset();
      }.bind(this),
      2500
    );
  }

  // แสดงผลข้อมูลการชั่งน้ำหนัก
  render(data) {
    this.settingDetail = data.settingDetail;
    this.productName = this.settingDetail.productName;
    this.lot = this.settingDetail.lot;
    this.balanceID = this.settingDetail.balanceID;
    this.tabletID = this.settingDetail.tabletID;
    this.numberPunches = this.settingDetail.numberPunches;
    this.numberTablets = this.settingDetail.numberTablets;
    this.meanWeight = this.settingDetail.meanWeight;
    this.percentWeightVariation = this.settingDetail.percentWeightVariation;
    this.meanWeightAvgMin = this.settingDetail.meanWeightAvgMin;
    this.meanWeightAvgMax = this.settingDetail.meanWeightAvgMax;
    this.meanWeightInhouseMin = this.settingDetail.meanWeightInhouseMin;
    this.meanWeightInhouseMax = this.settingDetail.meanWeightInhouseMax;
    this.meanWeightRegMin = this.settingDetail.meanWeightRegMin;
    this.meanWeightRegMax = this.settingDetail.meanWeightRegMax;
    this.prepared = this.settingDetail.prepared;
    this.approved = this.settingDetail.approved;
    this.finished = this.settingDetail.finished;
    this.finishTime = this.settingDetail.finishTime;

    this.weighingData = data.weighing.dataset;
    this.remarksData = data.remarks.dataset;

    if (this.container.innerHTML != "") {
      $(this.container).hide();
      this.container.innerHTML = "";
    }

    this.renderSettingsDetailsIpc();
    this.renderWeightTable();
    this.renderRemarksTable();
    this.main_container.appendChild(this.container);

    // เพิ่ม event ปุ่มอัพเดทข้อมูล
    $(this.buttonUpdate).click(this.loadWeighingData.bind(this));

    // เพิ่ม event ปุ่มจบการผลิต
    $(this.buttonFinished).click(() => {
      SwalPopup.fire({
        title: "ยืนยันการจัดเก็บเอกสาร",
        text: "คุณต้องการจบการผลิตและจัดเก็บเอกสารใช่หรือไม่?",
        icon: "warning",
        confirmButtonText: "ยืนยัน, จบการผลิต",
      }).then((res) => {
        if (res.isConfirmed) {
          this.endOfProduction();
        }
      });
    });

    // เพิ่ม event ปุ่มลงชื่อตรวจสอบการตั้งค่า
    $(this.buttonApproved).click(this.signInToCheckTheSettings.bind(this));

    // เพิ่ม event ปุ่มลงบันทึกข้อมูล remarks
    $(this.container).fadeIn(1500);

    // เพิ่ม event ปุ่มลงบันทึกข้อมูล remarks
    $(this.addRemarksButton).click(() => {
      this.formRemarks.createForm();
    });

    // เพิ่ม event ปุ่มลงบันทึกข้อมูล remarks
    if (
      this.role === role_definition.Admin ||
      this.role === role_definition.Superuser
    ) {
      $(document).ready(() => {
        $(this.remarks_tbody).on(
          "click",
          "tr",
          function (e) {
            const row = e.currentTarget._DT_RowIndex;
            const data = this.remarksTable.row(row).data();
            this.formRemarks.createForm({ rowIndex: row, dataRow: data });
          }.bind(this)
        );

        const form = this.formRemarks.form;
        $(form).submit(
          function (e) {
            e.preventDefault();
            this.onSubmitFormRemarks(form);
          }.bind(this)
        );
      });
    }
  }

  weightOutOfRange(weight) {
    if (weight < this.meanWeightRegMin)
      return "weight-outOfRange-regulation-min";
    else if (weight > this.meanWeightRegMax) {
      return "weight-outOfRange-regulation-max";
    } else if (weight < this.meanWeightInhouseMin) {
      return "weight-outOfRange-inHouse-min";
    } else if (weight > this.meanWeightInhouseMax) {
      return "weight-outOfRange-inHouse-max";
    } else {
      return;
    }
  }

  // สร้างข้อมูลการตั้งค่าน้ำหนัก ipc
  renderSettingsDetailsIpc() {
    const container = document.createElement("div");
    const detail_container = document.createElement("div");
    container.classList.add("detail");
    const settings_container = document.createElement("div");
    settings_container.classList.add("detail-settings");
    settings_container.id = "weight_detail_ipc"; // Set id
    settings_container.style.width = "100%";

    const title = document.createElement("p");
    title.classList.add("detail-title");
    title.innerHTML = "รายละเอียดการตั้งค่า";
    settings_container.appendChild(title);

    // เพิ่มปุ่มอัพเดทข้อมูล
    const buttonEl = document.createElement("div");
    buttonEl.classList.add("detail-buttons-group");
    this.buttonUpdate = document.createElement("button");
    this.buttonUpdate.id = "button_update_ipc";
    this.buttonUpdate.classList.add("btn", "btn-secondary", "button-update");
    this.buttonUpdate.textContent = "อัพเดทข้อมูล";
    buttonEl.appendChild(this.buttonUpdate);

    // เพิ่มปุ่มจบการผลิต
    if (
      this.role === role_definition.Admin ||
      this.role === role_definition.Superuser
    ) {
      this.buttonFinished = document.createElement("button");
      this.buttonFinished.id = "button_finished_ipc";
      this.buttonFinished.classList.add("btn", "btn-danger", "button-finished");
      this.buttonFinished.textContent = "จบการผลิต";
      buttonEl.appendChild(this.buttonFinished);
    }
    settings_container.appendChild(buttonEl);

    const details = document.createElement("div");
    const details_ul = document.createElement("ul");

    const productName_li = document.createElement("li");
    productName_li.textContent = `ชื่อยา ${this.productName}`;
    details_ul.appendChild(productName_li);

    const lot_li = document.createElement("li");
    lot_li.textContent = `เลขที่ผลิต ${this.lot}`;
    details_ul.appendChild(lot_li);

    const balanceID_li = document.createElement("li");
    balanceID_li.textContent = `เครื่องชั่งหมายเลข ${this.balanceID}`;
    details_ul.appendChild(balanceID_li);

    const tabletID_li = document.createElement("li");
    tabletID_li.textContent = `เครื่องตอก ${this.tabletID}`;
    details_ul.appendChild(tabletID_li);

    const numberPunches_li = document.createElement("li");
    numberPunches_li.textContent = `จำนวนสาก ${this.numberPunches} สาก`;
    details_ul.appendChild(numberPunches_li);

    const numberTablets_li = document.createElement("li");
    numberTablets_li.textContent = `จำนวนเม็ดที่ต้องชั่ง ${this.numberTablets} เม็ด`;
    details_ul.appendChild(numberTablets_li);

    const meanWeight_li = document.createElement("li");
    meanWeight_li.textContent = `น้ำหนักตอก/เม็ด ${this.meanWeight} กรัม`;
    details_ul.appendChild(meanWeight_li);

    const percentWeightVariation_li = document.createElement("li");
    percentWeightVariation_li.textContent = `% ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ ${this.percentWeightVariation}`;
    details_ul.appendChild(percentWeightVariation_li);

    const meanWeightRange_li = document.createElement("li");
    meanWeightRange_li.textContent = `ช่วงน้ำหนักเฉลี่ยที่ยอมรับ ${this.meanWeightAvgMin} - ${this.meanWeightAvgMax} กรัม`;
    details_ul.appendChild(meanWeightRange_li);

    const meanWeightInhouse_li = document.createElement("li");
    meanWeightInhouse_li.textContent = `ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ ${this.meanWeightInhouseMin} - ${this.meanWeightInhouseMax} กรัม`;
    details_ul.appendChild(meanWeightInhouse_li);

    const meanWeightRegRange_li = document.createElement("li");
    meanWeightRegRange_li.textContent = `ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ ${this.meanWeightRegMin} - ${this.meanWeightRegMax} กรัม`;
    details_ul.appendChild(meanWeightRegRange_li);

    const prepared_approved_li = document.createElement("li");
    prepared_approved_li.classList.add("fw-bold");
    const prepared = `ตั้งค่าน้ำหนักโดย ${this.prepared}`;
    const approved =
      this.approved === "xxxxx" ? "" : `ตรวจสอบการตั้งค่าโดย ${this.approved}`;
    prepared_approved_li.textContent = `${prepared} ${approved}`;
    details_ul.appendChild(prepared_approved_li);

    if (this.finished !== "xxxxx") {
      const finished_li = document.createElement("li");
      finished_li.classList.add("fw-bold");
      finished_li.textContent = `จบการผลิตโดย ${this.finished} วันที่ ${this.finishTime}`;
      details_ul.appendChild(finished_li);
    }

    details.appendChild(details_ul);
    settings_container.appendChild(details);
    detail_container.appendChild(settings_container);
    container.appendChild(detail_container);

    // Method, ปุ่มลงชื่อตรวจสอบการตั้งค่า
    if (this.role === role_definition.Admin) {
      if (this.approved === "xxxxx") {
        const approved_button_div = document.createElement("div");
        approved_button_div.classList.add("d-flex", "justify-content-center");
        this.buttonApproved = document.createElement("button");
        this.buttonApproved.id = "button_approved_ipc";
        this.buttonApproved.classList.add(
          "btn",
          "btn-success",
          "button-approved"
        );
        this.buttonApproved.textContent = "ลงชื่อตรวจสอบการตั้งค่า";
        approved_button_div.appendChild(this.buttonApproved);
        settings_container.appendChild(approved_button_div);
      }
    }

    const summary_container = this.renderWeightSummary();
    container.appendChild(summary_container);

    this.container.appendChild(container);
  }

  // สร้างสรุปข้อมูลการชั่งน้ำหนัก ipc
  renderWeightSummary() {
    let weights = [];
    Object.entries(this.weighingData).forEach(([datetime, rowData]) => {
      Object.entries(rowData.weights).forEach(([timestamp, data]) => {
        if (
          data.weight >= this.meanWeightRegMin &&
          data.weight <= this.meanWeightRegMax
        ) {
          weights.push(parseFloat(data.weight));
        }
      });
    });

    const weight_min = Math.min(...weights); // หาค่าน้ำหนักต่ำสุดที่อยู่ในช่วง
    const weight_max = Math.max(...weights); // หาค่าน้ำหนักสูงสุดที่อยู่ในช่วง
    const weight_average = weights.reduce((a, b) => a + b, 0) / weights.length; // หาค่าเฉลี่ยน้ำหนัก

    const container = document.createElement("div");
    const summary_container = document.createElement("div");
    summary_container.classList.add("weight-summary");

    const weight_summaryEl = document.createElement("div");
    const weight_summary_title = document.createElement("p");
    weight_summary_title.textContent = "สรุปข้อมูลการชั่งน้ำหนักทั้งหมด";
    weight_summaryEl.appendChild(weight_summary_title);

    const weight_summary_group = document.createElement("div");
    weight_summary_group.classList.add("summary-group");

    const weight_minEl = document.createElement("p");
    weight_minEl.classList.add("summary-min");
    weight_minEl.textContent = `ต่ำสุด ${weight_min.toFixed(3)} กรัม`;
    weight_summary_group.appendChild(weight_minEl);

    const weight_maxEl = document.createElement("p");
    weight_maxEl.classList.add("summary-max");
    weight_maxEl.textContent = `สูงสุด ${weight_max.toFixed(3)} กรัม`;
    weight_summary_group.appendChild(weight_maxEl);

    const weight_averageEl = document.createElement("p");
    weight_averageEl.classList.add("summary-average");
    weight_averageEl.textContent = `เฉลี่ย ${weight_average.toFixed(3)} กรัม`;
    weight_summary_group.appendChild(weight_averageEl);

    weight_summaryEl.appendChild(weight_summary_group);

    summary_container.appendChild(weight_summaryEl);
    container.appendChild(summary_container);

    return container;
  }

  // สร้างตารางข้อมูลการชั่งน้ำหนัก ipc
  createTable(tableID, [datetime, rowData]) {
    const tableCreator = new CreateTable(tableID); // Create table instance
    const table = tableCreator.table; // Get the created table element

    // Create table header
    const thead = document.createElement("thead");
    const title_headerRow = document.createElement("tr");
    const title_headerCell = document.createElement("th");
    title_headerCell.setAttribute("colspan", "2");
    title_headerCell.textContent = "ตารางข้อมูลน้ำหนักยา";
    title_headerRow.appendChild(title_headerCell);

    const date_headerRow = document.createElement("tr");
    const date_headerCell = document.createElement("th");
    date_headerCell.setAttribute("colspan", "2");
    date_headerCell.textContent = datetime;
    date_headerRow.appendChild(date_headerCell);

    const headerRow = document.createElement("tr");
    const headerCell1 = document.createElement("th");
    headerCell1.textContent = "เวลา";
    const headerCell2 = document.createElement("th");
    headerCell2.textContent = "น้ำหนัก (กรัม)";
    headerRow.appendChild(headerCell1);
    headerRow.appendChild(headerCell2);

    thead.appendChild(title_headerRow);
    thead.appendChild(date_headerRow);
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body
    const tbody = document.createElement("tbody");
    let weights_cache = [];

    Object.entries(rowData.weights).forEach(([timestamp, data]) => {
      const row = document.createElement("tr");
      const time_cell = document.createElement("td");
      time_cell.textContent = data.timestamp;
      const weight_cell = document.createElement("td");
      const weight_div = document.createElement("div");
      weight_div.classList.add(
        "data-control-ipc",
        this.weightOutOfRange(data.weight)
      );
      weight_div.textContent = data.weight;
      row.appendChild(time_cell);
      weight_cell.appendChild(weight_div);
      row.appendChild(weight_cell);
      tbody.appendChild(row);

      weights_cache.push(data.weight);
    });

    table.appendChild(tbody);

    const footer = document.createElement("tfoot");
    const average_row = document.createElement("tr");
    const average_title = document.createElement("td");
    average_title.textContent = "น้ำหนักเฉลี่ยที่ได้ (g)";
    const average_cell = document.createElement("td");
    const average_div = document.createElement("div");
    average_div.classList.add("data-control-ipc");
    const average =
      weights_cache.reduce((a, b) => parseFloat(a) + parseFloat(b)) /
      weights_cache.length;
    if (average < this.meanWeightAvgMin) {
      average_div.classList.add("weight-outOfRange-average-min");
    } else if (average > this.meanWeightAvgMax) {
      average_div.classList.add("weight-outOfRange-average-max");
    }
    average_div.textContent = average.toFixed(3);
    average_row.appendChild(average_title);
    average_cell.appendChild(average_div);
    average_row.appendChild(average_cell);
    footer.appendChild(average_row);

    const weightVariationTitle_row = document.createElement("tr");
    const weightVariationTitle_cell = document.createElement("td");
    weightVariationTitle_cell.setAttribute("colspan", "2");
    weightVariationTitle_cell.textContent = "ช่วงน้ำหนักเบี่ยงเบน";
    weightVariationTitle_row.appendChild(weightVariationTitle_cell);

    const weightVariation_row = document.createElement("tr");
    const weightVariationMin_cell = document.createElement("td");
    const weightVariationMin_div = document.createElement("div");
    const weightVariationMin = Math.min(...weights_cache).toFixed(3);
    weightVariationMin_div.classList.add(
      "data-control-ipc",
      this.weightOutOfRange(weightVariationMin)
    );
    weightVariationMin_div.textContent = weightVariationMin;
    const weightVariationMax_cell = document.createElement("td");
    const weightVariationMax_div = document.createElement("div");
    const weightVariationMax = Math.min(...weights_cache).toFixed(3);
    weightVariationMax_div.classList.add(
      "data-control-ipc",
      this.weightOutOfRange(weightVariationMax)
    );
    weightVariationMax_div.textContent = weightVariationMax;
    footer.appendChild(weightVariationTitle_row);
    weightVariationMin_cell.appendChild(weightVariationMin_div);
    weightVariationMax_cell.appendChild(weightVariationMax_div);
    weightVariation_row.appendChild(weightVariationMin_cell);
    weightVariation_row.appendChild(weightVariationMax_cell);
    footer.appendChild(weightVariation_row);

    const numberTablet_row = document.createElement("tr");
    const numberTabletTitle_cell = document.createElement("td");
    numberTabletTitle_cell.textContent = "จำนวน (เม็ด)";
    const numberTablet_cell = document.createElement("td");
    numberTablet_cell.textContent = weights_cache.length;
    numberTablet_row.appendChild(numberTabletTitle_cell);
    numberTablet_row.appendChild(numberTablet_cell);
    footer.appendChild(numberTablet_row);

    const characteristics_row = document.createElement("tr");
    const characteristicsTitle_cell = document.createElement("td");
    characteristicsTitle_cell.textContent = "ลักษณะเม็ด";
    const characteristics_cell = document.createElement("td");
    const characteristics_div = document.createElement("div");
    characteristics_div.classList.add(
      "data-control-ipc",
      "characteristics-control"
    );
    characteristics_div.textContent = rowData.characteristics;
    characteristics_div.setAttribute("data-content", rowData.characteristics);

    characteristics_row.appendChild(characteristicsTitle_cell);
    characteristics_cell.appendChild(characteristics_div);
    characteristics_row.appendChild(characteristics_cell);
    footer.appendChild(characteristics_row);

    const operator_row = document.createElement("tr");
    const operatorTitle_cell = document.createElement("td");
    operatorTitle_cell.textContent = "ผู้บันทึกข้อมูล";
    const operator_cell = document.createElement("td");
    operator_cell.textContent = rowData.operator;
    operator_row.appendChild(operatorTitle_cell);
    operator_row.appendChild(operator_cell);
    footer.appendChild(operator_row);

    const type_row = document.createElement("tr");
    const type_cell = document.createElement("td");
    type_cell.setAttribute("colspan", "2");
    const type_div = document.createElement("div");
    type_div.classList.add("data-control-ipc", "type-control");
    type_div.textContent = rowData.type;
    type_div.setAttribute("data-content", rowData.type);
    type_cell.appendChild(type_div);
    type_row.appendChild(type_cell);
    footer.appendChild(type_row);

    table.appendChild(footer);

    // Append table to container
    return table;
  }

  renderWeightTable() {
    const container = document.createElement("div");
    container.classList.add("container-slide");

    const weighingData = Object.entries(this.weighingData);

    const total_slide = weighingData.length;
    const totalPages = parseInt(total_slide / 2);

    for (let index = 0; index < total_slide; index++) {
      const table_container = document.createElement("div");
      table_container.classList.add("slide");

      if (index == 0) {
        table_container.classList.add("active");
        const tableId = `table${index}`;
        const table1 = this.createTable(tableId, weighingData[index]);
        table_container.appendChild(table1);
      }

      index += 1;
      if (index <= total_slide) {
        const tableId = `table${index}`;
        const table2 = this.createTable(tableId, weighingData[index]);
        table_container.appendChild(table2);
      }

      container.appendChild(table_container);
    }

    const slide_controls = document.createElement("div");
    slide_controls.classList.add("slide-controls");
    const slide_control_buttons = document.createElement("div");
    slide_control_buttons.classList.add("slide-control-buttons");
    const slide_control_prev = document.createElement("button");
    slide_control_prev.classList.add("slide-control-prev");
    slide_control_prev.textContent = "ก่อนหน้า";
    const slide_control_next = document.createElement("button");
    slide_control_next.classList.add("slide-control-next");
    slide_control_next.textContent = "ถัดไป";
    slide_control_buttons.appendChild(slide_control_prev);
    slide_control_buttons.appendChild(slide_control_next);
    slide_controls.appendChild(slide_control_buttons);

    const page_info = document.createElement("div");
    page_info.classList.add("page-info");
    const page_info_text = document.createElement("a");
    page_info_text.textContent = `หน้า 1 จาก ${totalPages} หน้า`;
    page_info.appendChild(page_info_text);
    slide_controls.appendChild(page_info);

    container.appendChild(slide_controls);

    this.container.appendChild(container);

    let currentPage = 1;
    $(document).ready(function () {
      const weighing_slide = $(".container-slide>.slide");
      const totalSlides = weighing_slide.length; // นับจำนวนสไลด์ทั้งหมด
      let currentPage = 1;

      function updateActiveSlide() {
        weighing_slide.removeClass("active");
        $(weighing_slide[currentPage - 1]).addClass("active");
      }

      $(slide_control_prev).on("click", function () {
        currentPage = currentPage === 1 ? totalSlides : currentPage - 1;
        page_info_text.textContent = `หน้า ${currentPage} จาก ${totalSlides} หน้า`;
        updateActiveSlide();
      });

      $(slide_control_next).on("click", function () {
        currentPage = currentPage === totalSlides ? 1 : currentPage + 1;
        page_info_text.textContent = `หน้า ${currentPage} จาก ${totalSlides} หน้า`;
        updateActiveSlide();
      });
    });
  }

  // สร้างตาราง Remarks
  renderRemarksTable() {
    const tableCreator = new CreateTable(this.remarksTableId); // Create table instance
    const table = tableCreator.table; // Get the created table element
    table.classList.add("remarks-table", "cell-border");

    // Create table header
    const thead = document.createElement("thead");
    const title_headerRow = document.createElement("tr");
    const headerRow = document.createElement("tr");
    this.remarksHeaders.forEach((header, index) => {
      if (index == 0) {
        const timestamp = document.createElement("th");
        timestamp.setAttribute("rowspan", "2");
        timestamp.textContent = Object.values(header)[0];

        const title = document.createElement("th");
        title.classList.add("table-title");
        title.setAttribute("colspan", "6");
        title.textContent = this.remarksTitle;

        title_headerRow.appendChild(timestamp);
        title_headerRow.appendChild(title);
        headerRow.appendChild(title_headerRow);
      } else {
        const th = document.createElement("th");
        th.textContent = Object.values(header)[0];
        headerRow.appendChild(th);
      }
    });

    thead.appendChild(title_headerRow);
    thead.appendChild(headerRow);

    // เพิ่มข้อมูล remarks
    if (
      this.role === role_definition.Admin ||
      this.role === role_definition.Superuser
    ) {
      this.addRemarksButton = document.createElement("button");
      this.addRemarksButton.classList.add("add-remarks-button");
      this.addRemarksButton.textContent = "เพิ่มข้อมูล";
      thead.appendChild(this.addRemarksButton);
    }

    table.appendChild(thead);

    // Create table body
    this.remarks_tbody = document.createElement("tbody");

    Object.entries(this.remarksData).forEach(([timestamp, rowData]) => {
      const row = document.createElement("tr");

      this.remarksHeaders.forEach((header) => {
        const key = Object.keys(header)[0];
        const cell = document.createElement("td");
        const data = rowData[key];

        // timestamp
        if (key === "timestamp") {
          cell.textContent = timestamp;
        } else {
          cell.textContent = data || "";
        }
        row.appendChild(cell);
      });

      this.remarks_tbody.appendChild(row);
    });

    table.appendChild(this.remarks_tbody);

    // Append table to container
    this.container.appendChild(table);

    // สร้างตาราง DataTable
    const tableID = this.remarksTableId;
    $(document).ready(
      function () {
        $(`#${tableID}`).DataTable().destroy();
        this.remarksTable = $(`#${tableID}`).DataTable(setupTable);
      }.bind(this)
    );
  }
}
