// ดึงข้อมูลชีตทั้งหมดที่อยู่ในฐานข้อมูล สร้าง dropdown list
function getProductionLists10s(jwtToken) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return { result: verifyToken };
  } else {
    let folderId10s = globalVariables().folderId10s;
    let folder10s = DriveApp.getFolderById(folderId10s);
    let contents10s = folder10s.getFiles();
    let sheetLists10s = [];

    const fileType = "application/vnd.google-apps.spreadsheet";
    if (verifyToken.userData.role != "Operator") {
      while (contents10s.hasNext()) {
        let file = contents10s.next();
        if (file.getMimeType() === fileType) {
          const tablet_name = file.getName().toUpperCase();
          const tablet_url_10s = file.getUrl();
          sheetLists10s.push({
            name: tablet_name,
            url: tablet_url_10s,
          });
        }
      }
    }

    // จัดเรียงข้อมูลตามวันที่
    sheetLists10s = sheetLists10s.sort((item1, item2) => {
      const date1Parts = item1.name.split("_").pop().split("/");
      const date2Parts = item2.name.split("_").pop().split("/");
      const date1 = new Date(
        `${date1Parts[2]}-${date1Parts[1]}-${date1Parts[0]}`
      );
      const date2 = new Date(
        `${date2Parts[2]}-${date2Parts[1]}-${date2Parts[0]}`
      );
      return date1 - date2;
    });

    let ssMain = SpreadsheetApp.getActiveSpreadsheet();
    let shTabetList = ssMain.getSheetByName(globalVariables().shTabetList);

    let lists = shTabetList.getDataRange().getDisplayValues().slice(1);
    lists.reverse().forEach((data) => {
      const tablet_name = data[0].toUpperCase();
      const tablet_url_10s = data[3];
      sheetLists10s.push({
        name: `เครื่องตอก ${tablet_name} (LOT. ปัจจุบัน)`,
        url: tablet_url_10s,
      });
    });

    return { result: verifyToken, productionLists: sheetLists10s };
  }
}

// ดึงข้อมูลจากชีตปัจจุบัน จาก url ของชีต 10 เม็ด
function getWeighingData10s({ url, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return verifyToken.message;
  } else {
    // const url = "https://docs.google.com/spreadsheets/d/1XySGAC8aaywquHFKwr_zBBDpOgj99CF15UHe3P3kYF8/edit?usp=sharing"
    const spreadsheet = SpreadsheetApp.openByUrl(url); // เข้าถึง Spreadsheet
    const data_setting = spreadsheet
      .getSheetByName(globalVariables().shSetWeight) // เข้าถึง sheet ตั้งค่าน้ำหนักยา
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

    const data_weighing = spreadsheet
      .getSheetByName(globalVariables().shWeight10s) // เข้าถึง sheet ชั่งน้ำหนัก
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(2); // ตัดข้อมูลส่วนหัวทิ้ง

    const data_remarks = spreadsheet
      .getSheetByName(globalVariables().shRemarks) // เข้าถึง sheet remarks
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

    // สร้างข้อมูลการตั้งค่าน้ำหนักยา
    const settingDetail = {
      productName: data_setting[0][1], // ชื่อยา
      lot: data_setting[1][1], // เลขที่ผลิต
      balanceID: data_setting[2][1], // เครื่องชั่ง
      tabletID: data_setting[3][1], // เครื่องตอก
      meanWeight: data_setting[4][1], // น้ำหนักตามทฤษฎี
      percentWeightVariation: data_setting[5][1], // เปอร์เซ็นเบี่ยงเบน
      meanWeightMin: data_setting[6][1], // ช่วงน้ำหนัก 10 เม็ด(Min.)
      meanWeightMax: data_setting[7][1], // ช่วงน้ำหนัก 10 เม็ด(Max.)
      meanWeightRegMin: data_setting[8][1], // ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
      meanWeightRegMax: data_setting[9][1], // ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
      thicknessMin: data_setting[10][1], // ค่าความหนา(Min.)
      thicknessMax: data_setting[11][1], // ค่าความหนา(Max.)
      prepared: data_setting[12][1], // ตั้งค่าน้ำหนักโดย
      approved: data_setting[13][1], // ตรวจสอบการตั้งค่าโดย
      finished: data_setting[14][1], // จบการผลิตโดย
      finishTime: data_setting[15][1], // จบการผลิตเวลา
    };

    // สร้างข้อมูลน้ำหนักยา
    let weighingData = [];
    data_weighing.forEach((row) => {
      const rowData = {
        timestamp: row[0],
        type: row[1],
        weight1: row[2],
        weight2: row[3],
        characteristics: row[4],
        operator: row[5],
        inspector: row[6],
        thickness: [],
      };

      // ข้อมูลความหนา
      for (let i = 0; i < 10; i++) {
        rowData.thickness.push(row[7 + i]);
      }

      // นำข้อมูลการชั่งแต่ล่ะครั้งไปเก็บใน dataObj
      weighingData.push(rowData);
    });

    // สร้างข้อมูลการ remarks
    let remarksData = [];
    data_remarks.forEach((row) => {
      const rowData = {
        timestamp: row[0],
        issues: row[1],
        cause: row[2],
        resolve: row[3],
        notes: row[4],
        recorder: row[5],
        role: row[6],
      };

      // นำข้อมูลการชั่งแต่ล่ะครั้งไปเก็บใน dataObj
      remarksData.push(rowData);
    });

    // เก็บข้อมูลการชั่งน้ำหนักทั้งหมด
    const dataset = {
      settingDetail: settingDetail,
      weighingData: weighingData.reverse(),
      remarksData: remarksData.reverse(),
    };

    return { result: verifyToken, dataset: dataset };
  }
}

// ลงชื่อผู้ตรวจสอบการตั้งค่า
function signInToCheckTheSettings10s({ url, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return verifyToken.message;
  } else {
    const spreadsheet = SpreadsheetApp.openByUrl(url);
    const sheet = spreadsheet.getSheetByName(globalVariables().shSetWeight); // เข้าถึง sheet ตั้งค่าน้ำหนักยา
    const data_setting = sheet
      .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
      .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
      .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

    // ลงชื่อผู้ตรวจสอบการตั้งค่า
    sheet
      .getRange(globalVariables().approvedRange10s)
      .setValue(verifyToken.userData.nameTH);

    // สร้างข้อมูลการตั้งค่าน้ำหนักยา
    const settingDetail = {
      productName: data_setting[0][1], // ชื่อยา
      lot: data_setting[1][1], // เลขที่ผลิต
      tabletID: data_setting[3][1], // เครื่องตอก
    };

    // บันทึกการปฏิบัติงาน
    const details = `ระบบเครื่องชั่ง 10 เม็ด\
                    \nชื่อยา ${settingDetail.productName}\
                    \nเลขที่ผลิต ${settingDetail.lot}\
                    \nเครื่องตอก ${settingDetail.tabletID}`;

    recordAuditTrailData({
      list: "ลงชื่อตรวจสอบการตั้งค่า",
      details: details,
      username: verifyToken.userData.nameTH,
      role: verifyToken.userData.role,
    });

    const timestamp = new Date().toLocaleString("en-GB", {
      timeZone: "Asia/Bangkok",
    });
    const approval_msg = `🌈ระบบเครื่องชั่ง 10 เม็ด\n
                        \n🔰ชื่อยา ${settingDetail.productName}\
                        \n🔰เลขที่ผลิต ${settingDetail.lot}\
                        \n🔰เครื่องตอก ${settingDetail.tabletID}\n
                        \n⪼ ตรวจสอบการตั้งค่าโดย\
                        \n⪼ คุณ ${verifyToken.userData.nameTH}\
                        \n⪼ ${timestamp}`;

    sendLineNotify(approval_msg, globalVariables().approval_token);
    return { result: verifyToken };
  }
}

// ลงชื่อผู้ตรวจสอบ
function signInToCheckTheWeighingData({ url, jwtToken }) {
  const verifyToken = validateToken(jwtToken);

  if (verifyToken.message != "success") {
    return verifyToken.message;
  } else {
    const spreadsheet = SpreadsheetApp.openByUrl(url);
    const sheet = spreadsheet.getSheetByName(globalVariables().shWeight10s);
    const row = sheet.getLastRow();
    sheet
      .getRange(row, globalVariables().inspectorCol)
      .setValue(verifyToken.userData.nameTH);

    return { result: verifyToken, inspectorName: verifyToken.userData.nameTH };
  }
}

// สิ้นสุดการผลิต
function endJob_10s(url, username) {
  let spreadsheet = SpreadsheetApp.openByUrl(url);
  let today = new Date().toLocaleString("en-GB", { timeZone: "Asia/Bangkok" });
  let date = today.split(",")[0];

  let shSetWeight = spreadsheet.getSheetByName(globalVariables().shSetWeight);
  let tabletID = shSetWeight.getRange("A2").getDisplayValue();
  let productName = shSetWeight.getRange("A4").getDisplayValue();
  let lot = shSetWeight.getRange("A5").getDisplayValue();

  // Set number format
  let shData = spreadsheet.getSheetByName(globalVariables().shWeight10s);
  shData.getRange("C5:E").setNumberFormat("0.000");
  shData.getRange("J5:S").setNumberFormat("0.00");

  // บันทึกคนที่กด ENDJOB
  shSetWeight
    .getRange(globalVariables().checkEndjobRange10s)
    .setValue("จบการผลิตโดย " + username + " วันที่ " + today);

  // บันทึกการปฏิบัติงาน
  let detail = `ระบบเครื่องชั่ง: 10 เม็ด\
                \nชื่อยา: ${productName}\
                \nเลขที่ผลิต: ${lot}\
                \nเครื่องตอก: ${tabletID}`;

  audit_trail("จบการผลิต", detail, username);

  // จัดเก็บข้อมูลไปยังโฟล์เดอร์
  let folder = DriveApp.getFolderById(globalVariables().folderId10s);
  let newSh = spreadsheet.copy(`${lot}_${productName}_${tabletID}_${date}`);
  let shID = newSh.getId(); // get newSheetID
  let file = DriveApp.getFileById(shID);

  folder.addFile(file); // ย้ายไฟล์ไปยังแฟ้มเก็บข้อมูล

  // ลบชีตที่ไม่ใช่ชีตหลักออก
  let shName = spreadsheet.getSheets();
  for (i = 0; i < shName.length; i++) {
    let sh = shName[i].getName();
    if (sh == "WEIGHT" || sh == "กราฟ" || sh == "Remark" || sh == "Setting") {
      continue;
    } else {
      spreadsheet.deleteSheet(shName[i]);
    }
  }

  spreadsheet
    .getSheetByName(globalVariables().shWeight10s)
    .getRange("A5:S")
    .clearContent();
  spreadsheet
    .getSheetByName(globalVariables().shRemarks)
    .getRange("A3:F")
    .clearContent();
  spreadsheet
    .getSheetByName(globalVariables().shSetWeight)
    .getRange("A3:A16")
    .setValue("xxxxx");

  return getCurrentData_10s(url);
}
