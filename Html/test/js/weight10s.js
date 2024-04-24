// สร้างกราฟเปอร์เซ็นต์น้ำหนักยา parameter(container, น้ำหนักตามทฤษฎี 10 เม็ด, ข้อมูลการชั่งน้ำหนัก)
class CreateChart {
  constructor(container, meanWeight, dataSource) {
    this.container = container;
    this.id = container.id;
    this.meanWeight = meanWeight;
    this.dataSource = dataSource;

    this.createChart();
  }

  createChart() {
    const dataPoints = Object.entries(this.dataSource).map(
      ([timestamp, rowData]) => {
        const weights_cache = [rowData["weight1"], rowData["weight2"]];
        const average =
          weights_cache.reduce((a, b) => parseFloat(a) + parseFloat(b)) /
          weights_cache.length;
        const percent = (average / this.meanWeight) * 100;
        return { y: parseFloat(percent), label: timestamp };
      }
    );

    $(document).ready(function () {
      const chart = new CanvasJS.Chart(`chart_10s`, {
        animationEnabled: true,
        animationDuration: 2000,
        zoomEnabled: true,
        // exportEnabled: true,
        title: {
          text: "Control Chart (%)",
          fontSize: 22,
        },
        toolTip: {
          shared: "true",
          cornerRadius: 5,
        },
        axisX: {
          labelMaxWidth: 60,
          labelWrap: true, // change it to false
          labelAngle: 0,
          labelTextAlign: "center",
          labelAutoFit: false,
          labelFontSize: 11,
        },
        axisY: {
          labelFontSize: 12,
        },
        data: [
          {
            yValueFormatString: "#.000 เปอร์เซนต์",
            type: "spline",
            color: "#3e95cd",
            showInLegend: true,
            name: "เครื่องตอก T15",
            markerSize: 8,
            markerBorderColor: "red",
            dataPoints: dataPoints,
          },
        ],
      });
      chart.render();
    });
  }
}

// สร้างหน้าข้อมูลการชั่งน้ำหนัก 10 เม็ด parameter(ไอดี container, ข้อมูลการชั่งน้ำหนักและข้อมูลอื่นๆ)
class Weighing10s {
  constructor(role, containerId, options) {
    this.role = role;
    this.containerId = containerId;
    this.main_container = document.getElementById(this.containerId);
    this.container = document.createElement("main");
    this.setupTable = options.setupTable;
    this.weighingTableId = options.weighing.weighingID;
    this.weighingTitle = options.weighing.weigtingTitle;
    this.weighingHeaders = options.weighing.weigtingHeaders;

    this.thicknessTableId = options.weighing.thicknessID;
    this.thicknessTitle = options.weighing.thicknessTitle;
    this.thicknessHeaders = options.weighing.thicknessHeaders;

    this.remarksTableId = options.remarks.id;
    this.remarksTitle = options.remarks.title;
    this.remarksHeaders = options.remarks.headers;

    this.listsMenu = new CreateViewWeighingMenu("weighing10sList");
    this.viewWeighingMenu = this.listsMenu.container;
    this.listsMenuInput = this.listsMenu.input;
    this.main_container.appendChild(this.viewWeighingMenu);

    this.productionLists = {};  // รายการผลิตทั้งหมด
    this.currentListname = "";  // รายการผลิตที่เลือก
    this.url = ""; // url ไฟล์

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

  searchUrl(currentListname) {
    const result = Object.entries(this.productionLists).find(
      ([_listName, url]) => {
        return _listName == currentListname;
      }
    );

    if (result) {
      return result[1];
    } else {
      return null;
    }
  }

  createProductionLists(productionLists) {
    // สร้างรายการ autocomplete รายการผลิต 10 เม็ด
    this.productionLists = productionLists;

    const dataSource = [];

    Object.entries(this.productionLists).forEach(([name, url]) => {
      dataSource.push(name);
    });

    $(this.listsMenuInput)
      .autocomplete({
        source: dataSource.reverse(),
        autoFocus: false,
        minLength: 0,
        open: function (event, ui) {
          var widget = $(this).autocomplete("widget");
          // widget.attr("id", `${this.containerId}_widget`);
        },
        select: function (event, ui) {
          this.currentListname = ui.item.value;
          this.loadWeighingData();
        }.bind(this),
      })
      .focus(function () {
        $(this).data("ui-autocomplete").search($(this).val());
      });
  }

  // โหลดข้อมูลการชั่งน้ำหนัก
  loadWeighingData() {
    loadingPage("show");
    this.url = this.searchUrl(this.currentListname);

    setTimeout(
      function () {
        loadingPage("hide");
        SwalMiniAlert.fire({ title: "อัพเดทข้อมูลเรียบร้อยแล้ว" });
        this.render(dataUpdate);
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

  // ลงชื่อตรวจสอบข้อมูลการชั่งน้ำหนัก
  signInToCheckTheWeighingData() {
    loadingEdit("show");
    setTimeout(
      function () {
        const firstRow = this.weighingTable.row(0);
        const rowData = firstRow.data();
        rowData[8] = "ยิ่งลักษณ์"; // ลงชื่อผู้ตรวจสอบ
        loadingEdit("hide");

        if (!rowData[8]) {
          SwalMiniAlert.fire({ title: "ลงชื่อผู้ตรวจสอบเรียบร้อยแล้ว" });
          const node = this.weighingTable
            .row(0)
            .data(rowData)
            .draw(false)
            .node();

          $(node).hide();
          $(node).fadeIn(1500);
        } else {
          SwalAlert.fire({
            icon: "error",
            title: "แจ้งเตือนการดำเนินการ",
            text: "มีการลงชื่อตรวจสอบข้อมูลการชั่งน้ำหนักแล้ว",
          });
        }
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
          role_definition.Admin,
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

  // แสดงหน้าชั่งน้ำหนัก
  render(data) {
    this.settingDetail = data.settingDetail;
    this.productName = this.settingDetail.productName;
    this.lot = this.settingDetail.lot;
    this.balanceID = this.settingDetail.balanceID;
    this.tabletID = this.settingDetail.tabletID;
    this.meanWeight = this.settingDetail.meanWeight;
    this.percentWeightVariation = this.settingDetail.percentWeightVariation;
    this.meanWeightMin = this.settingDetail.meanWeightMin;
    this.meanWeightMax = this.settingDetail.meanWeightMax;
    this.meanWeightRegMin = this.settingDetail.meanWeightRegMin;
    this.meanWeightRegMax = this.settingDetail.meanWeightRegMax;
    this.thicknessMin = this.settingDetail.thicknessMin;
    this.thicknessMax = this.settingDetail.thicknessMax;
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

    this.renderSettingsDetails10s();
    this.renderChart();
    this.renderWeightTable();
    this.container.appendChild(document.createElement("hr"));
    this.renderThicknessTable();
    this.container.appendChild(document.createElement("hr"));
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

    // เพิ่ม event ปุ่มลงชื่อผู้ตรวจสอบ
    $(this.addCheckerButton).click(() => {
      SwalPopup.fire({
        title: "ลงชื่อตรวจสอบข้อูล",
        text: "ตรวจสอบความถูกต้องของข้อมูลการชั่งน้ำหนักเรียบร้อยแล้ว",
        icon: "warning",
        confirmButtonText: "ยืนยัน",
      }).then((res) => {
        if (res.isConfirmed) {
          this.signInToCheckTheWeighingData();
        }
      });
    });

    // เพิ่ม event ปุ่มลงบันทึกข้อมูล remarks
    $(this.addRemarksButton).click(() => {
      this.formRemarks.createForm();
    });

    $(this.container).fadeIn(1500);

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

  // เทียบข้อมูลน้ำหนักกับเกณฑ์การผลิต
  weightOutOfRange(weight) {
    if (weight < this.meanWeightRegMin)
      return "weight-outOfRange-regulation-min";
    else if (weight > this.meanWeightRegMax) {
      return "weight-outOfRange-regulation-max";
    } else if (weight < this.meanWeightMin) {
      return "weight-outOfRange-inHouse-min";
    } else if (weight > this.meanWeightMax) {
      return "weight-outOfRange-inHouse-max";
    } else {
      return;
    }
  }

  // สร้างข้อมูลการตั้งค่าน้ำหนัก 10 เม็ด
  renderSettingsDetails10s() {
    const container = document.createElement("div");
    const detail_container = document.createElement("div");
    container.classList.add("detail");
    const settings_container = document.createElement("div");
    settings_container.classList.add("detail-settings");
    settings_container.id = "weight_detail_10s"; // Set id
    settings_container.style.width = "100%";

    const title = document.createElement("p");
    title.classList.add("detail-title");
    title.innerHTML = "รายละเอียดการตั้งค่า";
    settings_container.appendChild(title);

    // Method, ปุ่มอัพเดทข้อมูล
    const buttonEl = document.createElement("div");
    buttonEl.classList.add("detail-buttons-group");
    this.buttonUpdate = document.createElement("button");
    this.buttonUpdate.id = "button_update_10s";
    this.buttonUpdate.classList.add("btn", "btn-secondary", "button-update");
    this.buttonUpdate.textContent = "อัพเดทข้อมูล";
    buttonEl.appendChild(this.buttonUpdate);

    // Method, ปุ่มจบการผลิต
    if (
      this.role === role_definition.Admin ||
      this.role === role_definition.Superuser
    ) {
      if (this.prepared != "xxxxx" && this.approved != "xxxxx") {
        this.buttonFinished = document.createElement("button");
        this.buttonFinished.id = "button_finished_10s";
        this.buttonFinished.classList.add(
          "btn",
          "btn-danger",
          "button-finished"
        );
        this.buttonFinished.textContent = "จบการผลิต";
        buttonEl.appendChild(this.buttonFinished);
      }
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

    const meanWeight_li = document.createElement("li");
    meanWeight_li.textContent = `น้ำหนักตามทฤษฎี 10 เม็ด ${parseFloat(
      this.meanWeight
    ).toFixed(3)} กรัม`;
    details_ul.appendChild(meanWeight_li);

    const percentWeightVariation_li = document.createElement("li");
    percentWeightVariation_li.textContent = `% ช่วงน้ำหนักเบี่ยงเบนที่ยอมรับ ${parseFloat(
      this.percentWeightVariation
    ).toFixed(2)}`;
    details_ul.appendChild(percentWeightVariation_li);

    const meanWeightRange_li = document.createElement("li");
    meanWeightRange_li.textContent = `ช่วงน้ำหนัก 10 เม็ด ${parseFloat(
      this.meanWeightMin
    ).toFixed(3)} - ${parseFloat(this.meanWeightMax).toFixed(3)} กรัม`;
    details_ul.appendChild(meanWeightRange_li);

    const meanWeightRegRange_li = document.createElement("li");
    meanWeightRegRange_li.textContent = `ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ ${parseFloat(
      this.meanWeightRegMin
    ).toFixed(3)} - ${parseFloat(this.meanWeightRegMax).toFixed(3)} กรัม`;
    details_ul.appendChild(meanWeightRegRange_li);

    const thicknessRange_li = document.createElement("li");
    thicknessRange_li.textContent = `ค่าความหนา(Thickness) ${parseFloat(
      this.thicknessMin
    ).toFixed(2)} - ${parseFloat(this.thicknessMax).toFixed(2)} มิลลิเมตร(mm)`;
    details_ul.appendChild(thicknessRange_li);

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
        this.buttonApproved.id = "button_approved_10s";
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

  // สร้างกราฟ เปอร์เซ็นต์น้ำหนักเฉลี่ย
  renderChart() {
    const chart_container = document.createElement("div");
    chart_container.classList.add("chart-container");
    const chart_title = document.createElement("p");
    chart_title.classList.add("chart-title");
    chart_title.textContent = "เปอร์เซ็นต์น้ำหนักเฉลี่ย";
    chart_container.appendChild(chart_title);
    const chartEl = document.createElement("div");
    chartEl.classList.add("chart-div");
    chartEl.id = "chart_10s";
    chart_container.appendChild(chartEl);
    this.container.appendChild(chart_container);
    const chartCreator = new CreateChart(
      chart_container,
      this.meanWeight,
      this.weighingData
    );
    this.container.appendChild(chart_container);
  }

  // สร้างสรุปข้อมูลการชั่งน้ำหนักและความหนา 10 เม็ด
  renderWeightSummary() {
    let weights = [];
    let thickness = [];
    Object.entries(this.weighingData).forEach(([timestamp, rowData]) => {
      // ดึงค่าน้ำหนัก 10 เม็ด ครั้งที่ 1 ที่อยู่ในช่วง
      if (
        rowData.weight1 >= this.meanWeightRegMin &&
        rowData.weight1 <= this.meanWeightRegMax
      ) {
        weights.push(parseFloat(rowData.weight1));
      }

      // ดึงค่าน้ำหนัก 10 เม็ด ครั้งที่ 2 ที่อยู่ในช่วง
      if (
        rowData.weight2 >= this.meanWeightRegMin &&
        rowData.weight2 <= this.meanWeightRegMax
      ) {
        weights.push(parseFloat(rowData.weight2));
      }

      // ดึงค่าความหนาที่อยู่ในช่วง
      Object.entries(rowData.thickness).forEach(([key, tiknessVal]) => {
        if (
          tiknessVal >= this.thicknessMin &&
          tiknessVal <= this.thicknessMax
        ) {
          thickness.push(parseFloat(tiknessVal));
        }
      });
    });

    const weight_min = Math.min(...weights); // หาค่าน้ำหนักต่ำสุดที่อยู่ในช่วง
    const weight_max = Math.max(...weights); // หาค่าน้ำหนักสูงสุดที่อยู่ในช่วง
    const weight_average = weights.reduce((a, b) => a + b, 0) / weights.length; // หาค่าเฉลี่ยน้ำหนัก

    const thickness_min = Math.min(...thickness); // หาค่าความหนาต่ำสุดที่อยู่ในช่วง
    const thickness_max = Math.max(...thickness); // หาค่าความหนาสูงสุดที่อยู่ในช่วง
    const thickness_average =
      thickness.reduce((a, b) => a + b, 0) / thickness.length; // หาค่าเฉลี่ยความหนา

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

    // สรุปข้อมูลความหนาเม็ดยา
    const thickness_summaryEl = document.createElement("div");
    const thickness_summary_title = document.createElement("p");
    thickness_summary_title.textContent = "สรุปข้อมูลความหนาทั้งหมด";
    thickness_summaryEl.appendChild(thickness_summary_title);

    const thickness_summary_group = document.createElement("div");
    thickness_summary_group.classList.add("summary-group");

    const thickness_minEl = document.createElement("p");
    thickness_minEl.classList.add("summary-min");
    thickness_minEl.textContent = `ต่ำสุด ${thickness_min.toFixed(2)} mm.`;
    thickness_summary_group.appendChild(thickness_minEl);

    const thickness_maxEl = document.createElement("p");
    thickness_maxEl.classList.add("summary-max");
    thickness_maxEl.textContent = `สูงสุด ${thickness_max.toFixed(2)} mm.`;
    thickness_summary_group.appendChild(thickness_maxEl);

    const thickness_averageEl = document.createElement("p");
    thickness_averageEl.classList.add("summary-average");
    thickness_averageEl.textContent = `เฉลี่ย ${thickness_average.toFixed(
      2
    )} mm.`;
    thickness_summary_group.appendChild(thickness_averageEl);

    weight_summaryEl.appendChild(weight_summary_group);
    thickness_summaryEl.appendChild(thickness_summary_group);

    summary_container.appendChild(weight_summaryEl);
    summary_container.appendChild(thickness_summaryEl);
    container.appendChild(summary_container);

    return container;
  }

  // สร้างตารางข้อมูลการชั่งน้ำหนัก 10 เม็ด
  renderWeightTable() {
    const tableCreator = new CreateTable(this.weighingTableId); // Create table instance
    const table = tableCreator.table; // Get the created table element

    // Create table header
    const thead = document.createElement("thead");
    const title_headerRow = document.createElement("tr");
    const headerRow = document.createElement("tr");

    this.weighingHeaders.forEach((header, index) => {
      if (index == 0) {
        const timestamp = document.createElement("th");
        timestamp.setAttribute("rowspan", "2");
        timestamp.textContent = Object.values(header)[0];

        const title = document.createElement("th");
        title.classList.add("table-title");
        title.setAttribute("colspan", "8");
        title.textContent = this.weighingTitle;

        title_headerRow.appendChild(timestamp);
        title_headerRow.appendChild(title);
      } else {
        const th = document.createElement("th");
        th.textContent = Object.values(header)[0];
        headerRow.appendChild(th);
      }
    });

    thead.appendChild(title_headerRow);
    thead.appendChild(headerRow);

    // เพิ่มปุ่มลงชื่อตรวจสอบข้อมูลน้ำหนักยา
    thead.classList.add("weight10s-checker");
    if (
      this.role === role_definition.Admin ||
      this.role === role_definition.Superuser ||
      this.role === role_definition.Inspector
    ) {
      this.addCheckerButton = document.createElement("button");
      this.addCheckerButton.classList.add("add-checker-button");
      this.addCheckerButton.textContent = "ลงชื่อตรวจสอบ";
      thead.appendChild(this.addCheckerButton);
    }

    table.appendChild(thead);

    // Create table body
    const tbody = document.createElement("tbody");

    Object.entries(this.weighingData).forEach(([timestamp, rowData]) => {
      const row = document.createElement("tr");
      let weights_cache = [];
      this.weighingHeaders.forEach((header) => {
        const key = Object.keys(header)[0];
        const cell = document.createElement("td");
        const data = rowData[key];

        // timestamp
        if (key === "timestamp") {
          const div = document.createElement("div");
          div.classList.add("data-control-10s", "time-control");
          div.textContent = timestamp;
          cell.appendChild(div);
        } else if (key === "type") {
          const div = document.createElement("div");
          div.classList.add("data-control-10s", "type-control");
          div.setAttribute("data-content", data);
          div.textContent = data || "";
          cell.appendChild(div);
        } else if (key === "weight1") {
          const div = document.createElement("div");
          const weight_val = parseFloat(data).toFixed(3) || "";
          weights_cache.push(weight_val);
          div.classList.add(
            "data-control-10s",
            "weight-control",
            this.weightOutOfRange(weight_val)
          );
          div.textContent = weight_val;
          cell.appendChild(div);
        } else if (key === "weight2") {
          const div = document.createElement("div");
          const weight_val = parseFloat(data).toFixed(3) || "";
          weights_cache.push(weight_val);
          div.classList.add(
            "data-control-10s",
            "weight-control",
            this.weightOutOfRange(weight_val)
          );
          div.textContent = weight_val;
          cell.appendChild(div);
        } else if (key === "average") {
          const div = document.createElement("div");
          const average =
            weights_cache.reduce((a, b) => parseFloat(a) + parseFloat(b)) /
            weights_cache.length;
          const average_val = parseFloat(average).toFixed(3) || "";
          div.classList.add(
            "data-control-10s",
            "average-control",
            this.weightOutOfRange(average_val)
          );
          div.textContent = average_val;
          cell.appendChild(div);
        } else if (key === "percent") {
          const div = document.createElement("div");
          div.classList.add("data-control-10s");
          const average =
            weights_cache.reduce((a, b) => parseFloat(a) + parseFloat(b)) /
            weights_cache.length;
          const percent = (average / this.meanWeight) * 100;
          div.textContent = parseFloat(percent).toFixed(2) || "";
          const span = document.createElement("span");
          span.textContent = "%";
          div.appendChild(span);
          cell.appendChild(div);
        } else if (key === "characteristics") {
          const div = document.createElement("div");
          div.classList.add("data-control-10s", "characteristics-control");
          div.setAttribute("data-content", data);
          div.textContent = data;
          cell.appendChild(div);
        } else {
          cell.textContent = data || "";
        }
        row.appendChild(cell);
      });

      tbody.appendChild(row);
    });

    table.appendChild(tbody);

    // Append table to container
    this.container.appendChild(table);

    // สร้างตาราง DataTable
    const tableID = this.weighingTableId;
    $(document).ready(
      function () {
        $(`#${tableID}`).DataTable().destroy();
        this.weighingTable = $(`#${tableID}`).DataTable(setupTable);
      }.bind(this)
    );
  }

  // สร้างตารางบันทึกค่าความหนา 10 เม็ด
  renderThicknessTable() {
    // Create table element
    const tableCreator = new CreateTable(this.thicknessTableId); // Create table instance
    const table = tableCreator.table; // Get the created table element

    // Create table header
    const thead = document.createElement("thead");
    const title_headerRow1 = document.createElement("tr");
    const title_headerRow2 = document.createElement("tr");
    const headerRow = document.createElement("tr");

    this.thicknessHeaders.forEach((header, index) => {
      if (index == 0) {
        const timestamp = document.createElement("th");
        timestamp.setAttribute("rowspan", "3");
        timestamp.textContent = Object.values(header)[0];

        const title1 = document.createElement("th");
        title1.classList.add("table-title");
        title1.setAttribute("colspan", "10");
        title1.textContent = this.thicknessTitle;

        const title2 = document.createElement("th");
        title2.setAttribute("colspan", "10");
        title2.textContent = `ค่าความหนา(Thickness) ${this.thicknessMin} - ${this.thicknessMax} มิลลิเมตร(mm)`;

        title_headerRow1.appendChild(timestamp);
        title_headerRow1.appendChild(title1);
        title_headerRow2.appendChild(title2);
      } else {
        const th = document.createElement("th");
        th.textContent = Object.values(header)[0];
        headerRow.appendChild(th);
      }
    });

    thead.appendChild(title_headerRow1);
    thead.appendChild(title_headerRow2);
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body
    const tbody = document.createElement("tbody");

    Object.entries(this.weighingData).forEach(([timestamp, rowData]) => {
      const row = document.createElement("tr");

      let thicknessValues = [];
      this.thicknessHeaders.forEach((header) => {
        const key = Object.keys(header)[0];
        const cell = document.createElement("td");
        const data = rowData.thickness[key];

        // timestamp
        const div = document.createElement("div");
        if (key === "timestamp") {
          div.classList.add("data-control-10s", "time-control");
          div.textContent = timestamp;
          cell.appendChild(div);
        } else {
          if (data !== "-") {
            thicknessValues.push(parseFloat(data).toFixed(2));
          }

          div.classList.add("data-control-10s", "thickness-control");
          div.textContent = data == "-" ? data : parseFloat(data).toFixed(2);
          cell.appendChild(div);
        }
        row.appendChild(cell);
      });

      let min = Math.min(...thicknessValues);
      let max = Math.max(...thicknessValues);
      let isMin = false;
      let isMax = false;

      // เน้นค่า min และ max ในตาราง
      let lastIndex = 0;
      row.querySelectorAll("td .thickness-control").forEach((cell, index) => {
        const value = parseFloat(cell.textContent);
        // หา cell ไม่ได้อยู่ในช่วง
        if (value < this.thicknessMin) {
          cell.classList.add("thickness-outOfRange-min");
          thicknessValues.splice(index - lastIndex, 1);
          lastIndex += 1;
        } else if (value > this.thicknessMax) {
          cell.classList.add("thickness-outOfRange-max");
          thicknessValues.splice(index - lastIndex, 1);
          lastIndex += 1;
        }
      });

      min = Math.min(...thicknessValues);
      max = Math.max(...thicknessValues);

      row.querySelectorAll("td .thickness-control").forEach((cell) => {
        const value = parseFloat(cell.textContent);
        // หา cell ที่มีค่าตรงกับ min
        if (value === min && !isMin) {
          isMin = true;
          cell.classList.add("thickness-min");
        }
        // หา cell ที่มีค่าตรงกับ max
        if (value === max && !isMax) {
          isMax = true;
          cell.classList.add("thickness-max");
        }
      });

      tbody.appendChild(row);
    });

    table.appendChild(tbody);

    // Append table to container
    this.container.appendChild(table);

    // สร้างตาราง DataTable
    const tableID = this.thicknessTableId;
    $(document).ready(function () {
      $(`#${tableID}`).DataTable().destroy();
      const table = $(`#${tableID}`).DataTable({
        ...setupTable,
        searching: false,
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
