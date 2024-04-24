// ดึงข้อมูลจากชีตปัจจุบัน จาก url ของชีต 10 เม็ด
function getCurrentData_10s() {
  const url = "https://docs.google.com/spreadsheets/d/1XySGAC8aaywquHFKwr_zBBDpOgj99CF15UHe3P3kYF8/edit?usp=sharing"
  const spreadsheet = SpreadsheetApp.openByUrl(url); // เข้าถึง Spreadsheet
  const data_weighing = spreadsheet.getSheetByName(globalVariables().shWeight10s) // เข้าถึง sheet ชั่งน้ำหนัก
    .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
    .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
    .slice(2); // ตัดข้อมูลส่วนหัวทิ้ง

  const data_setting = spreadsheet.getSheetByName(globalVariables().shSetWeight)  // เข้าถึง sheet ตั้งค่าน้ำหนักยา
    .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
    .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
    .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

  const data_remarks = spreadsheet.getSheetByName(globalVariables().shRemarks)  // เข้าถึง sheet remarks
    .getDataRange() // ดึงข้อมูลทั้งหมดที่อยู่ใน sheet
    .getDisplayValues() // ดึงข้อมูลแบบที่แสดงผลบนหน้าจอ
    .slice(1); // ตัดข้อมูลส่วนหัวทิ้ง

  // สร้างข้อมูลน้ำหนักยา
  let weighingData = {};
  data_weighing.forEach((row) => {
    const timestamp = row[0];
    const rowData = {
      type: row[1],
      weight1: row[2],
      weight2: row[3],
      characteristics: row[6],
      operator: row[7],
      inspector: row[8],
      thickness: {}
    };

    // ข้อมูลความหนา
    for (let i = 0; i < 10; i++) {
      rowData.thickness[`thickness${i + 1}`] = row[9 + i];
    }

    // นำข้อมูลการชั่งแต่ล่ะครั้งไปเก็บใน dataObj
    weighingData[timestamp] = rowData;
  });

  // สร้างข้อมูลการตั้งค่าน้ำหนักยา
  const settingData = {
    "productName": data_setting[0][1],  // ชื่อยา
    "lot": data_setting[1][1],  // เลขที่ผลิต
    "balanceID": data_setting[2][1],  // เครื่องชั่ง
    "tabletID": data_setting[3][1], // เครื่องตอก
    "meanWeight": data_setting[4][1], // น้ำหนักตามทฤษฎี 
    "percentWeightVariation": data_setting[5][1], // เปอร์เซ็นเบี่ยงเบน
    "meanWeightMin": data_setting[6][1],  // ช่วงน้ำหนัก 10 เม็ด(Min.)
    "meanWeightMax": data_setting[7][1],  // ช่วงน้ำหนัก 10 เม็ด(Max.)
    "meanWeightRegMin": data_setting[8][1],  // ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Min.)
    "meanWeightRegMax": data_setting[9][1],  // ช่วงน้ำหนักเบี่ยงเบนที่กฎหมายยอมรับ (Max.)
    "thicknessMin": data_setting[10][1],  // ค่าความหนา(Min.)
    "thicknessMax": data_setting[11][1],  // ค่าความหนา(Max.)
    "prepared": data_setting[12][1],  // ตั้งค่าน้ำหนักโดย
    "approved": data_setting[13][1],  // ตรวจสอบการตั้งค่าโดย
    "finished": data_setting[14][1],  // จบการผลิตโดย
    "finishTime": data_setting[15][1],  // จบการผลิตเวลา
  };

// สร้างข้อมูลการ remarks
  let remarksData = {};
  data_remarks.forEach((row) => {
    const timestamp = row[0];
    const rowData = {
      incident: row[1],
      cause: row[2],
      resolve: row[3],
      notes: row[4],
      recorder: row[5],
      role: row[6]
    };

    // นำข้อมูลการชั่งแต่ล่ะครั้งไปเก็บใน dataObj
    remarksData[timestamp] = rowData;
  });

  // เก็บข้อมูลการชั่งน้ำหนักทั้งหมด
  const data = {
    "weighingData": weighingData,
    "settingData": settingData,
    "remarksData": remarksData
  };

  console.log(data.remarksData);
};

// ลงชื่อผู้ตรวจสอบการตั้งค่า
function setting_addChecker_10s(url, username, detail) {
  let ss = SpreadsheetApp.openByUrl(url);
  let sheet = ss.getSheetByName(globalVariables().shSetWeight);

  sheet.getRange(globalVariables().checkSetupRange10s).setValue(username);

  // บันทึกการปฏิบัติงาน
  let auditTrial_msg = `ระบบเครื่องชั่ง ${detail.type}\
                      \n${detail.product}\
                      \n${detail.lot}\
                      \n${detail.tabletID}`;

  audit_trail("ลงชื่อตรวจสอบการตั้งค่า", auditTrial_msg, username);

  const timeStamp = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Jakarta' });
  const approval_msg = `🌈ระบบเครื่องชั่ง ${detail.type}
    \n🔰${detail.tabletID}\
    \n🔰${detail.lot}\
    \n🔰${detail.product}
    \n⪼ ตรวจสอบการตั้งค่าโดย\
    \n⪼ คุณ ${username}\
    \n⪼ ${timeStamp}`;

  sendLineNotify(approval_msg, globalVariables().approval_token);
}

// บันทึกลัษณะของเม็ดยา
function recodeCharacteristics(url, date_time, value) {
  let ss = SpreadsheetApp.openByUrl(url);
  let sheet = ss.getSheetByName(globalVariables().shWeight10s);
  let data = sheet.getDataRange().getDisplayValues();

  for (let i = 4; i < data.length; i++) {
    if (data[i][0] == date_time) {
      sheet.getRange(i + 1, 7).setValue(value);
      return;
    };
  };
}

// บันทึกค่าความหนาของเม็ดยา
function recordThickness(form) {
  let ss = SpreadsheetApp.openByUrl(form.thickness_url);
  let sheet = ss.getSheetByName(globalVariables().shWeight10s);
  let data = sheet.getDataRange().getDisplayValues();

  let dataList = [
    form.thickness1,
    form.thickness2,
    form.thickness3,
    form.thickness4,
    form.thickness5,
    form.thickness6,
    form.thickness7,
    form.thickness8,
    form.thickness9,
    form.thickness10
  ];

  for (let i = 4; i < data.length; i++) {
    if (data[i][0] == form.thickness_timestamp) {
      sheet.getRange(i + 1, 10, 1, 10).setValues([dataList]);
      return { date_time: form.thickness_timestamp, dataList };
    };
  };
}

// ลงชื่อผู้ตรวจสอบ
function addChecker(url, username) {
  let ss = SpreadsheetApp.openByUrl(url);
  let sheet = ss.getSheetByName(globalVariables().shWeight10s);

  sheet.getRange(sheet.getLastRow(), 9).setValue(username);
}

// สิ้นสุดการผลิต
function endJob_10s(url, username) {
  let ss = SpreadsheetApp.openByUrl(url);
  let today = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Jakarta' });
  let date = today.split(",")[0];

  let shSetWeight = ss.getSheetByName(globalVariables().shSetWeight);
  let tabletID = shSetWeight.getRange('A2').getDisplayValue();
  let productName = shSetWeight.getRange('A4').getDisplayValue();
  let lot = shSetWeight.getRange('A5').getDisplayValue();

  // Set number format
  let shData = ss.getSheetByName(globalVariables().shWeight10s);
  shData.getRange('C5:E').setNumberFormat('0.000');
  shData.getRange('J5:S').setNumberFormat('0.00');

  // บันทึกคนที่กด ENDJOB
  shSetWeight.getRange(globalVariables().checkEndjobRange10s).setValue("จบการผลิตโดย " + username + " วันที่ " + today);

  // บันทึกการปฏิบัติงาน
  let detail = `ระบบเครื่องชั่ง: 10 เม็ด\
                \nชื่อยา: ${productName}\
                \nเลขที่ผลิต: ${lot}\
                \nเครื่องตอก: ${tabletID}`;

  audit_trail("จบการผลิต", detail, username);

  // จัดเก็บข้อมูลไปยังโฟล์เดอร์
  let folder = DriveApp.getFolderById(globalVariables().folderId10s);
  let newSh = ss.copy(`${lot}_${productName}_${tabletID}_${date}`);
  let shID = newSh.getId(); // get newSheetID
  let file = DriveApp.getFileById(shID);

  folder.addFile(file); // ย้ายไฟล์ไปยังแฟ้มเก็บข้อมูล

  // ลบชีตที่ไม่ใช่ชีตหลักออก
  let shName = ss.getSheets();
  for (i = 0; i < shName.length; i++) {
    let sh = shName[i].getName();
    if (sh == "WEIGHT" || sh == "กราฟ" || sh == "Remark" || sh == "Setting") {
      continue;
    } else {
      ss.deleteSheet(shName[i]);
    }
  };

  ss.getSheetByName(globalVariables().shWeight10s).getRange("A5:S").clearContent();
  ss.getSheetByName(globalVariables().shRemarks).getRange("A3:F").clearContent();
  ss.getSheetByName(globalVariables().shSetWeight).getRange("A3:A16").setValue("xxxxx");

  return getCurrentData_10s(url);
};



