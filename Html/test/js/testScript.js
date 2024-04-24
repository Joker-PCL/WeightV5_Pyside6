const role_definition = {
  Admin: "Admin",
  Superuser: "Superuser",
  Inspector: "Inspector",
  Operator: "Operator",
};

const role = "Admin";

// สร้างรายการเมนู Sidebar parameters(สิทธิ์การใช้งาน)
$(document).ready(function () {
  const sidebar_body = document.getElementById("sidebar_body");
  const menu_lists = new CreateSidebarMenu(role);
  sidebar_body.appendChild(menu_lists.lists);

  const sidebar_menu = new bootstrap.Offcanvas("#sidebar_menu");
  // ซ่อนและแสดงหน้า
  $(".page-menu").on("click", function () {
    sidebar_menu.hide();
    const currentPage = $(this).attr("data-toggle");
    $(".pages>.page").each(function () {
      const page = $(this).attr("data-toggle");
      if (currentPage === page) {
        $(this).fadeIn(500);
        $(this).addClass("active");
        window.scrollTo(0, 0);
      } else {
        $(this).removeClass("active");
        $(this).hide();
      }
    });
  });
});

// สร้างหน้าชั่งน้ำหนัก 10 เม็ด(สิทธิ์การใช้งาน)
$(document).ready(function () {
  // Create an instance of Table10s
  const weight10s = new Weighing10s(role, "container10s", {
    setupTable: setupTable,

    // ข้อมูลการชั่งน้ำหนัก 10 เม็ด
    weighing: {
      weighingID: "weight_10s",
      weigtingTitle: "ตารางบันทึกบันทึกค่าน้ำหนัก 10 เม็ด 2 ครั้งทุก 30 นาที",
      weigtingHeaders: [
        { timestamp: "วันที่,เวลา" },
        { type: "TYPE" },
        { weight1: "ครั้งที่ 1" },
        { weight2: "ครั้งที่ 2" },
        { average: "นน.เฉลี่ย" },
        { percent: "%นน.เฉลี่ย" },
        { characteristics: "ลักษณะเม็ด" },
        { operator: "ผู้ปฏิบัติ" },
        { inspector: "ผู้ตรวจสอบ" },
      ],

      thicknessID: "thickness_10s",
      thicknessTitle: "ตารางบันทึกค่าความหนาของเม็ดยา ทุก 2 ชั่วโมง",
      thicknessHeaders: [
        { timestamp: "วันที่,เวลา" },
        { thickness1: "1" },
        { thickness2: "2" },
        { thickness3: "3" },
        { thickness4: "4" },
        { thickness5: "5" },
        { thickness6: "6" },
        { thickness7: "7" },
        { thickness8: "8" },
        { thickness9: "9" },
        { thickness10: "10" },
      ],
    },

    // Remarks
    remarks: {
      id: "remarks_weight_10s",
      title: "Remarks",
      headers: [
        { timestamp: "วันที่/เวลา" },
        { issues: "เหตุการที่เกิดการเปลี่ยนแปลง" },
        { cause: "สาเหตุ" },
        { resolve: "การแก้ไข" },
        { notes: "หมายเหตุ" },
        { recorder: "ผู้บันทึก" },
        { role: "สิทธิ์" },
      ],
    },
  });

  weight10s.createProductionLists(productionLists.sheetLists10s);
});

// สร้างหน้าชั่งน้ำหนัก ipc(สิทธิ์การใช้งาน)
$(document).ready(function () {
  // Create an instance of ipc
  const weightIpc = new WeighingIpc(role, "containerIpc", {
    setupTable: setupTable,

    // ข้อมูลการชั่งน้ำหนัก 10 เม็ด
    weighing: {
      weighingID: "weight_ipc",
    },

    // Remarks
    remarks: {
      id: "remarks_weight_ipc",
      title: "Remarks",
      headers: [
        { timestamp: "วันที่/เวลา" },
        { issues: "เหตุการที่เกิดการเปลี่ยนแปลง" },
        { cause: "สาเหตุ" },
        { resolve: "การแก้ไข" },
        { notes: "หมายเหตุ" },
        { recorder: "ผู้บันทึก" },
        { role: "สิทธิ์" },
      ],
    },
  });
});

// ตั้งค่าน้ำหนักยาของเครื่องตอก, แก้ไขฐานข้อมูลน้ำหนักยา
$(document).ready(function () {
  const form_weighing_setup = new CreateForm(role, "weighing_setup", dataSettings);
  form_weighing_setup.createSetupForm();
  // form_weighing_setup.updateLists(form_weighing_setup.searchProductsEl, dataSettings);

  const form_weighing_database = new CreateForm(role, "weighing_database", dataSettings);
  form_weighing_database.createEditForm();
  // form_weighing_database.updateLists(form_weighing_database.searchProductsEl, dataSettings);

  const form_userData = new CreateUserDataForm("user_edit", dataSettings.userLists).createFormUserData();
});

$(document).ready(function () {
  const dataLogging = new CreateDataLogging("data_logging", {
    setupTable: setupTable,
    title: "บันทึกการปฎิบัติงาน",
    tableId: "dataLoggingTable",
    headers: {
      datetime: "วันที่/เวลา",
      list: "รายการ",
      details: "รายละเอียด",
      recorder: "ผู้บันทึก",
      role: "สิทธิ์การเข้าถึง",
    },
  });

  dataLogging.render(dataLog);
});
